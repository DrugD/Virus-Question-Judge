/* ============================================================
   Scientific-Question Judge SPA — main controller
   ============================================================ */

const API = "";
const $  = (sel, root = document) => root.querySelector(sel);
const $$ = (sel, root = document) => Array.from(root.querySelectorAll(sel));

document.getElementById("api-host").textContent = location.host;
document.getElementById("run-stamp").textContent = new Date().toLocaleString();

const state = {
  dataFile: null,        // File | Blob (zipped folder)
  dataLabel: "",
  goldFile: null,
  candidateFile: null,   // optional AgentOutput JSON for judge-only mode
  candidateJson: null,   // parsed candidate
  uploadId: null,
  manifest: null,
  agents: [],
  selectedAgents: new Set(),
  runId: null,
  evtSource: null,
  rows: {},
  streams: {},           // agent_id -> { thinking: "", question: "" }
};

/* ============ ROUTING ============ */

/**
 * Reset everything that belongs to a single "new eval" session: uploaded
 * files, parsed manifests, selected agents, in-flight SSE, and the UI bits
 * that show their values. Triggered every time the user enters the
 * view-new route so clicking "新评测" really does open a fresh window
 * instead of inheriting cached state from the previous run.
 */
function resetNewEvalView() {
  // tear down any live progress stream
  if (state.evtSource) {
    try { state.evtSource.close(); } catch {}
    state.evtSource = null;
  }
  // reset session state (keep agents catalog + judge config — those are global)
  state.dataFile = null;
  state.dataLabel = "";
  state.goldFile = null;
  state.candidateFile = null;
  state.candidateJson = null;
  state.uploadId = null;
  state.questionSetId = null;
  state.manifest = null;
  state.selectedAgents = new Set();
  state.runId = null;
  state.rows = {};
  state.streams = {};

  // reset UI: dropzones
  ["data-name", "gold-name", "candidate-name"].forEach(id => {
    const el = document.getElementById(id); if (el) el.textContent = "";
  });
  ["dz-data", "dz-gold", "dz-candidate"].forEach(id => {
    const el = document.getElementById(id); if (el) el.classList.remove("set");
  });
  ["data-input", "data-folder-input", "gold-input", "candidate-input"].forEach(id => {
    const el = document.getElementById(id); if (el) el.value = "";
  });

  // reset UI: form bits
  const qset = document.getElementById("qset-id"); if (qset) qset.value = "";
  const banner = document.getElementById("judge-only-banner"); if (banner) banner.hidden = true;
  const grid = document.getElementById("agent-grid");
  if (grid) grid.querySelectorAll(".agent-card.checked").forEach(c => c.classList.remove("checked"));

  // reset UI: status pills back to idle
  ["step-upload", "step-agents", "step-progress", "step-results"].forEach(id => {
    const card = document.getElementById(id);
    const pill = card?.querySelector(".status-pill");
    if (pill) {
      pill.dataset.status = "idle";
      const defaults = {
        "step-upload": "未上传",
        "step-agents": "等上传通过",
        "step-progress": "未启动",
        "step-results": "等待运行",
      };
      pill.textContent = defaults[id] || "idle";
    }
  });

  // reset UI: validation + progress + results panels
  ["validation-errors", "validation-warnings", "progress-timeline",
   "agent-streams", "event-log", "elements-grid"].forEach(id => {
    const el = document.getElementById(id); if (el) el.innerHTML = "";
  });
  const lbBody = document.querySelector("#leaderboard-table tbody");
  if (lbBody) lbBody.innerHTML = "";

  const uploadBtn = document.getElementById("upload-btn"); if (uploadBtn) uploadBtn.disabled = true;
  const startBtn = document.getElementById("start-run"); if (startBtn) {
    startBtn.disabled = true;
    startBtn.textContent = "开始评测 →";
  }
  const uploadText = document.getElementById("upload-text"); if (uploadText) uploadText.textContent = "";
  document.querySelector("#step-agents .action-row")?.style.removeProperty("display");
  if (grid) grid.style.removeProperty("display");
}

function route() {
  const hash = location.hash.replace(/^#/, "") || "/";
  const isHistory = hash.startsWith("/history");
  const m = hash.match(/^\/run\/([^/]+)\/([^/]+)$/);
  // Tear down any live-detail SSE when leaving the detail view (or
  // re-entering with a different run id). loadRunDetail() also does this
  // defensively, but doing it here too keeps the home/history views clean.
  if (!m && state.detailEvtSource) {
    try { state.detailEvtSource.close(); } catch {}
    state.detailEvtSource = null;
  }
  $$(".view").forEach(v => v.classList.remove("active"));
  $$(".nav-link").forEach(a => a.classList.remove("active"));
  if (m) {
    $(".view-detail").classList.add("active");
    $$(".nav-link").filter(a => a.dataset.route === "/history")[0]?.classList.add("active");
    loadRunDetail(m[1], m[2]);
  } else if (isHistory) {
    $(".view-history").classList.add("active");
    $$(".nav-link").filter(a => a.dataset.route === "/history")[0]?.classList.add("active");
    loadHistory();
  } else {
    // Fresh "new eval" window every time the user lands on /.
    resetNewEvalView();
    $(".view-new").classList.add("active");
    $$(".nav-link").filter(a => a.dataset.route === "/")[0]?.classList.add("active");
    refreshHistoryCount();
  }
}
window.addEventListener("hashchange", route);
$$(".nav-link").forEach(a => a.addEventListener("click", e => {
  e.preventDefault();
  location.hash = a.dataset.route;
}));

/* ============ STEP 1 — dual upload ============ */

setupDataDropzone();
setupGoldDropzone();
setupCandidateDropzone();
$$("button[data-pick]").forEach(b => b.addEventListener("click", e => {
  e.preventDefault();
  document.getElementById(b.dataset.pick).click();
}));
$("#upload-btn").addEventListener("click", uploadBoth);

// candidate format toggles
document.getElementById("show-candidate-format")?.addEventListener("click", e => {
  e.preventDefault();
  const det = document.getElementById("candidate-format");
  det.hidden = false;
  det.open = true;
  det.scrollIntoView({ behavior: "smooth", block: "center" });
});
document.getElementById("dl-candidate-template")?.addEventListener("click", e => {
  e.preventDefault();
  const tmpl = {
    agent_id: "user_uploaded_candidate",
    workspace_id: "user_uploaded",
    questions: [{
      rank: 1,
      question: "Does <X> drive <Y> in this dataset?",
      rationale: "Two-to-four sentences citing specific files / fields ...",
      data_support: ["data/foo.csv"],
      expected_test: "How this is answerable from the data",
      scope_keywords: ["3-8", "short", "keywords"],
    }],
  };
  _download("candidate_template.json", JSON.stringify(tmpl, null, 2), "application/json");
});
document.getElementById("cancel-judge-only")?.addEventListener("click", () => {
  state.candidateFile = null;
  state.candidateJson = null;
  document.getElementById("candidate-name").textContent = "";
  document.getElementById("dz-candidate").classList.remove("set");
  document.getElementById("judge-only-banner").hidden = true;
  document.getElementById("agent-grid").style.display = "";
  document.querySelector("#step-agents .action-row").style.display = "";
  $("#start-run").textContent = "开始评测 →";
  refreshUploadButton();
  updateAgentStepStatus();
});

function setupDataDropzone() {
  const dz = $("#dz-data");
  const zipInput = $("#data-input");
  const folderInput = $("#data-folder-input");
  const name = $("#data-name");

  zipInput.addEventListener("change", e => {
    const f = e.target.files?.[0];
    if (!f) return;
    state.dataFile = f;
    state.dataLabel = `${f.name} · ${prettyBytes(f.size)} (zip)`;
    name.textContent = state.dataLabel;
    dz.classList.add("set"); refreshUploadButton();
  });

  folderInput.addEventListener("change", async e => {
    const files = Array.from(e.target.files || []);
    if (!files.length) return;
    name.textContent = `打包文件夹 (${files.length} 个文件) …`;
    const blob = await zipFolder(files);
    state.dataFile = new File([blob], "uploaded_folder.zip", { type: "application/zip" });
    state.dataLabel = `📁 ${files[0].webkitRelativePath?.split("/")[0] || "folder"} · ${files.length} files · ${prettyBytes(blob.size)} (zipped)`;
    name.textContent = state.dataLabel;
    dz.classList.add("set"); refreshUploadButton();
  });

  ["dragenter", "dragover"].forEach(ev =>
    dz.addEventListener(ev, e => { e.preventDefault(); dz.classList.add("over"); }));
  ["dragleave", "drop"].forEach(ev =>
    dz.addEventListener(ev, e => { e.preventDefault(); dz.classList.remove("over"); }));
  dz.addEventListener("drop", async e => {
    const items = Array.from(e.dataTransfer?.items || []);
    const files = Array.from(e.dataTransfer?.files || []);
    // detect folder drop via DataTransferItem.webkitGetAsEntry
    const entries = items
      .map(it => (it.kind === "file" && it.webkitGetAsEntry) ? it.webkitGetAsEntry() : null)
      .filter(Boolean);
    const hasDir = entries.some(en => en.isDirectory);
    if (hasDir) {
      name.textContent = "正在读取文件夹 …";
      const collected = [];
      for (const en of entries) await walkEntry(en, "", collected);
      const blob = await zipFolderEntries(collected);
      state.dataFile = new File([blob], "uploaded_folder.zip", { type: "application/zip" });
      state.dataLabel = `📁 ${entries[0].name} · ${collected.length} files · ${prettyBytes(blob.size)} (zipped)`;
      name.textContent = state.dataLabel;
      dz.classList.add("set"); refreshUploadButton();
      return;
    }
    if (files.length) {
      const f = files.find(x => /\.zip$/i.test(x.name)) || files[0];
      state.dataFile = f;
      state.dataLabel = `${f.name} · ${prettyBytes(f.size)}`;
      name.textContent = state.dataLabel;
      dz.classList.add("set"); refreshUploadButton();
    }
  });
}

async function walkEntry(entry, prefix, out) {
  return new Promise(resolve => {
    if (entry.isFile) {
      entry.file(file => {
        out.push({ relPath: prefix + entry.name, file });
        resolve();
      });
    } else if (entry.isDirectory) {
      const reader = entry.createReader();
      const all = [];
      const readBatch = () => reader.readEntries(async ents => {
        if (!ents.length) {
          for (const e of all) await walkEntry(e, prefix + entry.name + "/", out);
          resolve();
        } else {
          all.push(...ents);
          readBatch();
        }
      });
      readBatch();
    } else resolve();
  });
}

async function zipFolder(filelist) {
  const zip = new JSZip();
  for (const f of filelist) {
    const rel = f.webkitRelativePath || f.name;
    zip.file(rel, f);
  }
  return await zip.generateAsync({ type: "blob", compression: "DEFLATE", compressionOptions: { level: 6 } });
}
async function zipFolderEntries(entries) {
  const zip = new JSZip();
  for (const { relPath, file } of entries) zip.file(relPath, file);
  return await zip.generateAsync({ type: "blob", compression: "DEFLATE", compressionOptions: { level: 6 } });
}

function setupGoldDropzone() {
  const dz = $("#dz-gold");
  const input = $("#gold-input");
  const name = $("#gold-name");
  function commit(f) {
    if (!f) return;
    state.goldFile = f;
    name.textContent = `${f.name} · ${prettyBytes(f.size)}`;
    dz.classList.add("set"); refreshUploadButton();
  }
  input.addEventListener("change", e => commit(e.target.files?.[0]));
  ["dragenter","dragover"].forEach(ev => dz.addEventListener(ev, e => { e.preventDefault(); dz.classList.add("over"); }));
  ["dragleave","drop"].forEach(ev => dz.addEventListener(ev, e => { e.preventDefault(); dz.classList.remove("over"); }));
  dz.addEventListener("drop", e => {
    const f = e.dataTransfer?.files?.[0];
    if (f) commit(f);
  });
}

function setupCandidateDropzone() {
  const dz = $("#dz-candidate");
  const input = $("#candidate-input");
  const name = $("#candidate-name");
  async function commit(f) {
    if (!f) return;
    let parsed;
    try {
      parsed = JSON.parse(await f.text());
    } catch (e) {
      alert("候选 JSON 解析失败: " + e.message);
      return;
    }
    if (!parsed?.questions || !Array.isArray(parsed.questions)) {
      alert("候选 JSON 必须包含 questions: [...] 数组");
      return;
    }
    state.candidateFile = f;
    state.candidateJson = parsed;
    name.textContent = `${f.name} · ${prettyBytes(f.size)} · ${parsed.questions.length} 个候选`;
    dz.classList.add("set");
    refreshUploadButton();
  }
  input.addEventListener("change", e => commit(e.target.files?.[0]));
  ["dragenter","dragover"].forEach(ev => dz.addEventListener(ev, e => { e.preventDefault(); dz.classList.add("over"); }));
  ["dragleave","drop"].forEach(ev => dz.addEventListener(ev, e => { e.preventDefault(); dz.classList.remove("over"); }));
  dz.addEventListener("drop", e => {
    const f = e.dataTransfer?.files?.[0];
    if (f) commit(f);
  });
}

function refreshUploadButton() {
  $("#upload-btn").disabled = !(state.dataFile && state.goldFile);
}

async function uploadBoth() {
  if (!state.dataFile || !state.goldFile) return;
  const qsetRaw = ($("#qset-id")?.value || "").trim();
  if (qsetRaw && !/^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$/.test(qsetRaw)) {
    alert("题集 id 仅允许字母/数字/.-_，且必须以字母或数字开头，最长 64 字符。");
    return;
  }
  setStatus("step-upload", "running", "上传 + 校验中…");
  $("#upload-btn").disabled = true;
  $("#upload-progress").hidden = false;
  $("#upload-text").textContent = `${state.dataLabel}  +  ${state.goldFile.name}` + (qsetRaw ? `  ·  题集 ${qsetRaw}` : "  ·  自动 ts_<unix>");

  const fd = new FormData();
  fd.append("file", state.dataFile);
  fd.append("gold", state.goldFile);
  if (qsetRaw) fd.append("question_set_id", qsetRaw);

  const xhr = new XMLHttpRequest();
  xhr.open("POST", `${API}/api/uploads`);
  xhr.upload.onprogress = e => {
    if (e.lengthComputable) $("#upload-bar").style.width = `${(e.loaded / e.total) * 95}%`;
  };
  xhr.onload = () => {
    $("#upload-bar").style.width = "100%";
    let r;
    try { r = JSON.parse(xhr.responseText); }
    catch { r = { ok: false, errors: ["non-JSON response"] }; }
    renderManifest(r, xhr.status);
  };
  xhr.onerror = () => renderManifest({ ok: false, errors: ["network error"] }, 0);
  xhr.send(fd);
}

function renderManifest(m, httpStatus) {
  state.uploadId = m.upload_id || null;
  state.questionSetId = m.question_set_id || null;
  state.manifest = m;
  const okRoot = m.ok && httpStatus < 400;
  $("#validation-report").hidden = false;
  if (state.questionSetId && $("#qset-id")) {
    // reflect server-normalised id back to the input (covers auto ts_<unix>)
    $("#qset-id").value = state.questionSetId;
  }

  // ---- data side ----
  const ds = $("#data-summary");
  const tree = $("#data-tree");
  ds.innerHTML = ""; tree.innerHTML = "";
  const dataObj = m.data || {};
  if (dataObj && Object.keys(dataObj).length) {
    ds.innerHTML = `
      <div class="row"><span class="k">file count</span><code>${dataObj.file_count ?? "-"}</code></div>
      <div class="row"><span class="k">total size</span><code>${prettyBytes(dataObj.total_size_bytes ?? 0)}</code></div>
      ${dataObj.truncated ? `<div class="row"><span class="k">truncated</span><code>yes</code></div>` : ""}
      <div class="ext-hist">
        ${Object.entries(dataObj.extension_histogram || {})
            .map(([k,v]) => `<span class="pill">${escapeHtml(k)} · ${v}</span>`).join("")}
      </div>`;
    for (const f of (dataObj.files || []).slice(0, 60)) {
      const extra =
        f.sample.columns ? `${f.sample.columns.length} cols`
        : f.sample.sequence_count ? `${f.sample.sequence_count} seqs`
        : f.sample.line_count ? `${f.sample.line_count} lines`
        : f.sample.top_keys ? `${f.sample.top_keys.length} keys`
        : "";
      tree.insertAdjacentHTML("beforeend", `
        <div class="ft-row">
          <span class="name">${escapeHtml(f.path)}</span>
          <span class="extra">${extra}</span>
          <span class="size">${prettyBytes(f.size_bytes)}</span>
        </div>`);
    }
  }

  // ---- gold side ----
  const gs = $("#gold-summary"); const gl = $("#gold-list");
  gs.innerHTML = ""; gl.innerHTML = "";
  const g = m.gold || {};
  if (g && Object.keys(g).length) {
    gs.innerHTML = `
      <div class="row"><span class="k">total</span><code>${g.total_count ?? "-"}</code></div>
      <div class="row"><span class="k">primary</span><code>${g.primary_count ?? 0}</code></div>
      <div class="row"><span class="k">secondary</span><code>${g.secondary_count ?? 0}</code></div>`;
    for (const q of (g.questions_preview || [])) {
      gl.insertAdjacentHTML("beforeend", `
        <div class="gq-card">
          <div class="hd">
            <span class="gid">${escapeHtml(q.id || "")}</span>
            <span class="cent ${q.centrality || "secondary"}">${escapeHtml(q.centrality || "")}</span>
            <span class="qtype">${escapeHtml(q.type || "")}</span>
          </div>
          <div class="q">${escapeHtml(q.question || "")}</div>
          <div class="req">${q.required_elements_count ?? 0} required elements</div>
        </div>`);
    }
  }

  $("#validation-errors").innerHTML = (m.errors || []).map(e => `<li>${escapeHtml(e)}</li>`).join("");
  $("#validation-warnings").innerHTML = ((m.data?.warnings) || []).concat(g.warnings || [])
      .map(w => `<li>${escapeHtml(w)}</li>`).join("");

  if (okRoot) {
    setStatus("step-upload", "ok", "校验通过");
    enableAgentSelection();
  } else {
    setStatus("step-upload", "bad", `失败 · stage=${m.stage || "?"}`);
    $("#upload-btn").disabled = false;
  }
}

/* ============ judge info + rubric definitions ============ */

(async () => {
  try {
    const r = await fetch(`${API}/api/judge_info`).then(r => r.json());
    state.judgeInfo = r;
    state.judgeId = r.default_id || r.model;
    const sel = $("#judge-model-select");
    if (sel) {
      const opts = (r.options && r.options.length)
        ? r.options
        : [{ id: r.model, label: r.model, model: r.model, provider: r.provider, description: "" }];
      sel.innerHTML = opts.map(o => `<option value="${escapeHtml(o.id)}">${escapeHtml(o.label || o.model)}</option>`).join("");
      sel.value = state.judgeId;
      const refresh = () => {
        const o = opts.find(x => x.id === sel.value) || opts[0];
        state.judgeId = o.id;
        $("#judge-provider").textContent = o.provider || r.provider || "-";
        $("#judge-desc").textContent = o.description || "";
      };
      sel.addEventListener("change", refresh);
      refresh();
    }
    $("#judge-baseurl").textContent = r.base_url || "(default)";
    $("#judge-threshold").textContent = String(r.threshold ?? 0.6);
    $("#rubric-threshold").textContent = String(r.threshold ?? 0.6);
    setStatus("step-judge", "ok", "已加载");
  } catch {
    setStatus("step-judge", "bad", "加载失败");
  }
  try {
    const spec = await fetch(`${API}/api/rubric_definitions`).then(r => r.json());
    state.rubricSpec = spec;
    renderRubricSpec(spec);
  } catch (e) {
    $("#rubric-spec").innerHTML = `<div class="muted">加载评测标准失败: ${escapeHtml(String(e))}</div>`;
  }
})();

function renderRubricSpec(spec) {
  const root = $("#rubric-spec");
  if (!root) return;
  const cards = Object.keys(spec.weights || {}).map(dim => {
    const w = spec.weights[dim];
    const label = (spec.dimension_labels || {})[dim] || dim;
    const def   = (spec.dimension_defs   || {})[dim] || "";
    const anchors = (spec.dimension_anchors || {})[dim] || [];
    return `
      <div class="rubric-card" data-dim="${dim}">
        <div class="rd-hd">
          <span class="name">${escapeHtml(label)}</span>
          <span class="weight">w = ${w.toFixed(2)}</span>
          <code class="muted" style="margin-left:auto;font-size:11px;">${dim}</code>
        </div>
        <div class="rd-def">${escapeHtml(def)}</div>
        <div class="rd-anchors">
          ${anchors.map(a => `
            <div class="rd-anchor"><span class="s s-${a.score}">${a.score}</span><span class="txt">${escapeHtml(a.anchor)}</span></div>
          `).join("")}
        </div>
      </div>`;
  }).join("");
  root.innerHTML = cards;
}

/* ============ STEP 2 — agents ============ */

const FAMILY_COLOR = {
  "OpenAI":          "rgba(108,193,255,1)",
  "Anthropic":       "rgba(154,123,255,1)",
  "Google":          "rgba(95,208,114,1)",
  "Alibaba":         "rgba(240,180,64,1)",
  "DeepSeek":        "rgba(239,93,97,1)",
  "Z.AI":            "rgba(192,132,252,1)",
  "Shanghai AILab":  "rgba(255,143,69,1)",
};

async function loadAgents() {
  const r = await fetch(`${API}/api/agents`).then(r => r.json());
  state.agents = r.agents || [];
  const grid = $("#agent-grid");
  grid.innerHTML = "";
  for (const a of state.agents) {
    const c = FAMILY_COLOR[a.family] || "rgba(140,150,170,.8)";
    const card = document.createElement("label");
    card.className = "agent-card";
    card.dataset.agent = a.id;
    card.style.setProperty("--family-color", c);
    card.innerHTML = `
      <input type="checkbox" />
      <div class="name">${escapeHtml(a.label)}</div>
      <div class="desc">${escapeHtml(a.desc || "")}</div>
      <div class="agent-meta">
        <span class="family-pill" style="background:${c}22;color:${c};border:1px solid ${c}55;">
          ${escapeHtml(a.family || "")}
        </span>
        <span class="muted" style="font-size:10.5px;">${escapeHtml(a.kind || "")}</span>
      </div>
      <div class="checkmark"></div>`;
    card.addEventListener("click", e => { e.preventDefault(); toggleAgent(a.id, card); });
    grid.appendChild(card);
  }
}
loadAgents();

$("#select-all").addEventListener("click", () => {
  state.selectedAgents = new Set(state.agents.map(a => a.id));
  $$("#agent-grid .agent-card").forEach(c => c.classList.add("checked"));
  updateAgentStepStatus();
});
$("#select-none").addEventListener("click", () => {
  state.selectedAgents.clear();
  $$("#agent-grid .agent-card").forEach(c => c.classList.remove("checked"));
  updateAgentStepStatus();
});

function toggleAgent(id, card) {
  if (state.selectedAgents.has(id)) {
    state.selectedAgents.delete(id);
    card.classList.remove("checked");
  } else {
    state.selectedAgents.add(id);
    card.classList.add("checked");
  }
  updateAgentStepStatus();
}

function enableAgentSelection() {
  // judge-only mode: candidate uploaded → hide agent grid, swap CTA label
  if (state.candidateJson) {
    setStatus("step-agents", "ok", "判官直评模式");
    document.getElementById("judge-only-banner").hidden = false;
    document.getElementById("agent-grid").style.display = "none";
    document.querySelector("#step-agents .action-row").style.display = "";
    $("#start-run").textContent = "提交直评 →";
    $("#start-run").disabled = false;
    return;
  }
  document.getElementById("judge-only-banner").hidden = true;
  document.getElementById("agent-grid").style.display = "";
  $("#start-run").textContent = "开始评测 →";
  setStatus("step-agents", "running", "选择 agent");
  // pre-check the cheap & fast agents from the curated set
  $$("#agent-grid .agent-card").forEach(c => {
    const id = c.dataset.agent;
    const cheapDefaults = ["claude-haiku-4-5", "gemini-2.5-flash", "glm-4.6"];
    if (cheapDefaults.includes(id) && !state.selectedAgents.has(id)) {
      state.selectedAgents.add(id);
      c.classList.add("checked");
    }
  });
  updateAgentStepStatus();
}

function updateAgentStepStatus() {
  if (state.candidateJson) {
    $("#start-run").disabled = !state.uploadId;
    setStatus("step-agents", "ok", "判官直评模式");
    return;
  }
  const n = state.selectedAgents.size;
  if (n) setStatus("step-agents", "ok", `${n} 个 agent 已选`);
  else   setStatus("step-agents", "running", "选择 agent");
  $("#start-run").disabled = !(state.uploadId && state.manifest?.ok && n > 0);
}

/* ============ STEP 4 — run + SSE ============ */

$("#start-run").addEventListener("click", startRun);

async function startRun() {
  if (!state.uploadId) return;
  $("#start-run").disabled = true;
  setStatus("step-progress", "running", "排队中");
  $("#progress-timeline").innerHTML = "";
  $("#agent-streams").innerHTML = "";
  $("#event-log").textContent = "";
  state.rows = {}; state.streams = {};

  // Clear last run's result panes so the user sees a clean "等待数据" state
  // instead of leftover leaderboard/charts from a previous evaluation.
  // (History on disk is untouched — only the in-page render is reset.)
  const lbBody = document.querySelector("#leaderboard-table tbody");
  if (lbBody) lbBody.innerHTML = "";
  ["elements-grid", "question-grid"].forEach(id => {
    const el = document.getElementById(id); if (el) el.innerHTML = "";
  });
  if (window.Charts?.destroyAll) window.Charts.destroyAll();

  const judgeOnly = !!state.candidateJson;
  const agentsToShow = judgeOnly
    ? [state.candidateJson.agent_id || "user_uploaded_candidate"]
    : [...state.selectedAgents];
  for (const a of agentsToShow) {
    state.rows[a] = { phase: "queued", t0: null, agentTime: 0, judgeTime: 0, scores: null };
    state.streams[a] = { thinking: "", question: "" };
    renderTimelineRow(a);
    renderStreamCard(a);
  }

  const body = judgeOnly
    ? { upload_id: state.uploadId, agents: [], judge_only: true, candidate: state.candidateJson, judge_id: state.judgeId }
    : { upload_id: state.uploadId, agents: [...state.selectedAgents], judge_id: state.judgeId };

  let r;
  try {
    const resp = await fetch(`${API}/api/runs`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    });
    r = await resp.json();
    if (!resp.ok) throw new Error(r.detail || `HTTP ${resp.status}`);
  } catch (e) {
    setStatus("step-progress", "bad", "启动失败");
    alert("启动失败: " + e.message);
    $("#start-run").disabled = false;
    return;
  }

  state.runId = r.run_id;
  setStatus("step-progress", "running", judgeOnly ? "直评中" : "运行中");
  setStatus("step-results", "running", "等待数据");
  attachSSE(state.uploadId, state.runId);
}

function attachSSE(uploadId, runId) {
  const url = `${API}/api/runs/${uploadId}/${runId}/events`;
  const es = new EventSource(url);
  state.evtSource = es;
  ["run_started","agent_started","agent_streaming","agent_finished","agent_failed",
   "judge_started","judge_finished","run_finished","run_failed","end"].forEach(k => {
    es.addEventListener(k, e => {
      try { onEvent(JSON.parse(e.data)); } catch {}
      if (k === "run_finished" || k === "run_failed" || k === "end") es.close();
    });
  });
  es.onerror = () => { /* tolerate transient drops */ };
}

function logEvent(ev) {
  const log = $("#event-log");
  const t = new Date(ev.ts * 1000).toLocaleTimeString();
  log.textContent += `[${t}] ${ev.kind} ${JSON.stringify(stripHeavy(ev))}\n`;
  log.scrollTop = log.scrollHeight;
}
function stripHeavy(ev) {
  const { ts, kind, scores, weights, candidate, agent_questions, covered_required_elements, missing_required_elements, rationale, delta, ...rest } = ev;
  if (delta) rest._streamed = `${delta.length}c`;
  return rest;
}

function onEvent(ev) {
  logEvent(ev);
  const a = ev.agent_id;
  switch (ev.kind) {
    case "agent_started":
      state.rows[a] = { ...(state.rows[a] || {}), phase: "running", t0: ev.ts };
      renderTimelineRow(a);
      break;
    case "agent_streaming":
      if (!state.streams[a]) { state.streams[a] = { thinking: "", question: "" }; renderStreamCard(a); }
      state.streams[a].thinking += ev.delta || "";
      // try to extract a streaming preview of the question
      const m = state.streams[a].thinking.match(/"question"\s*:\s*"([^"\\]*(?:\\.[^"\\]*)*)/);
      if (m) state.streams[a].question = m[1].replace(/\\"/g, '"').replace(/\\n/g, " ");
      updateStreamCard(a);
      break;
    case "agent_finished":
      state.rows[a].phase = "judging";
      state.rows[a].agentTime = ev.wall_time_s;
      state.streams[a].question = ev.agent_questions?.questions?.[0]?.question || state.streams[a].question;
      renderTimelineRow(a);
      updateStreamCard(a);
      break;
    case "agent_failed":
      state.rows[a].phase = "failed";
      state.rows[a].error = ev.error;
      state.streams[a].error = ev.error;
      renderTimelineRow(a);
      updateStreamCard(a);
      break;
    case "judge_started":
      state.rows[a].judgeStart = ev.ts;
      renderTimelineRow(a);
      break;
    case "judge_finished":
      state.rows[a].phase = "done";
      state.rows[a].judgeTime = ev.judge_wall_time_s;
      state.rows[a].scores = ev;
      renderTimelineRow(a);
      maybeRenderResults();
      break;
    case "run_finished":
      setStatus("step-progress", "ok", "完成");
      setStatus("step-results", "ok", "已生成");
      maybeRenderResults();
      refreshHistoryCount();
      break;
    case "run_failed":
      setStatus("step-progress", "bad", "失败");
      break;
  }
}

function renderTimelineRow(a) {
  const row = state.rows[a];
  let el = document.querySelector(`.tl-row[data-agent="${a}"]`);
  if (!el) {
    el = document.createElement("div");
    el.className = "tl-row";
    el.dataset.agent = a;
    el.innerHTML = `
      <div class="agent">${a}</div>
      <div class="bars"></div>
      <div class="total"></div>`;
    $("#progress-timeline").appendChild(el);
  }
  el.dataset.status = row.phase;
  const aT = row.agentTime || (row.phase === "running" ? (Date.now()/1000 - (row.t0 || Date.now()/1000)) : 0);
  const jT = row.judgeTime || (row.phase === "judging" ? Math.max(0, Date.now()/1000 - (row.judgeStart || 0)) : 0);
  const total = aT + jT || 1;
  const bars = el.querySelector(".bars");
  bars.innerHTML = `
    <div class="seg agent-seg ${row.phase === 'running' ? 'running' : ''}" style="width: ${(aT / total) * 60}%"></div>
    <div class="seg judge-seg ${row.phase === 'judging' ? 'running' : ''}" style="width: ${(jT / total) * 40}%"></div>
    <span class="pill ${row.phase}">${labelOf(row.phase)}</span>`;
  el.querySelector(".total").textContent =
    row.phase === "done"  ? `agent ${aT.toFixed(1)}s · judge ${jT.toFixed(1)}s` :
    row.phase === "failed"? "failed" :
    `${(aT + jT).toFixed(0)}s`;
}
function labelOf(p) {
  return ({ queued: "queued", running: "agent running", judging: "judging", done: "done", failed: "failed" })[p] || p;
}
setInterval(() => {
  Object.keys(state.rows || {}).forEach(a => {
    if (["running","judging"].includes(state.rows[a].phase)) renderTimelineRow(a);
  });
}, 1000);

/* live agent stream cards */

function renderStreamCard(agentId) {
  const wrap = $("#agent-streams");
  if (document.querySelector(`.agent-stream-card[data-agent="${agentId}"]`)) return;
  const el = document.createElement("div");
  el.className = "agent-stream-card";
  el.dataset.agent = agentId;
  el.innerHTML = `
    <div class="hd">
      <span class="name">${agentId}</span>
      <span class="meta" data-status>(thinking…)</span>
      <button class="ghost toggle" type="button">折叠</button>
    </div>
    <div class="question-banner" hidden>
      <div class="label">候选 question (live)</div>
      <div class="text"></div>
    </div>
    <div class="body" data-body>(等待 token…)</div>`;
  el.querySelector(".toggle").addEventListener("click", () => {
    el.classList.toggle("collapsed");
    el.querySelector(".toggle").textContent = el.classList.contains("collapsed") ? "展开" : "折叠";
  });
  wrap.appendChild(el);
}
function updateStreamCard(agentId) {
  const el = document.querySelector(`.agent-stream-card[data-agent="${agentId}"]`);
  if (!el) return;
  const s = state.streams[agentId] || {};
  const body = el.querySelector("[data-body]");
  body.textContent = s.thinking || "(等待 token…)";
  body.scrollTop = body.scrollHeight;
  // question banner
  const banner = el.querySelector(".question-banner");
  if (s.question) {
    banner.hidden = false;
    banner.querySelector(".text").textContent = s.question;
  }
  // status meta
  const st = el.querySelector("[data-status]");
  if (s.error) st.textContent = `❌ ${s.error}`;
  else if (state.rows[agentId]?.phase === "done") st.textContent = "✓ done";
  else if (state.rows[agentId]?.phase === "judging") st.textContent = "judging…";
  else st.textContent = `(${(s.thinking || "").length} chars)`;
}

/* ============ STEP 5 — results ============ */

$$(".result-tabs .tab").forEach(t =>
  t.addEventListener("click", () => {
    const grp = t.parentElement;
    $$(".tab", grp).forEach(x => x.classList.remove("active"));
    const pane = grp.parentElement;
    $$(".tab-pane", pane).forEach(p => p.classList.remove("active"));
    t.classList.add("active");
    pane.querySelector(`.tab-pane[data-tab="${t.dataset.tab}"]`).classList.add("active");
    Charts.relayoutAll();
  }));

function maybeRenderResults() {
  const rows = Object.entries(state.rows)
    .filter(([_, r]) => r.scores)
    .map(([id, r]) => ({ ...r.scores, agent_id: id, agent_wall_time_s: r.agentTime, judge_wall_time_s: r.judgeTime }));
  if (rows.length === 0) return;
  // Rank by Pass@5 descending — that's the headline agent-level metric now.
  rows.sort((a, b) => (b.pass_at_5_value ?? b.pass_at_k_value ?? -1) - (a.pass_at_5_value ?? a.pass_at_k_value ?? -1));
  renderLeaderboard($("#leaderboard-table tbody"), rows);
  renderQuestions($("#question-grid"), rows);
  renderElements($("#elements-grid"), rows);
  Charts.renderAll(rows.filter(r => r.ok !== false && r.composite_score != null), "radar-canvas", "bars-canvas", "timing-canvas");
}

function renderLeaderboard(tb, rows) {
  // Each agent renders as 1 main row + 1 sub-row that spans all columns and
  // contains a flat 5-question grid. Avg Composite / Avg Raw are agent-level
  // aggregates over the 5 candidates. Per-candidate Composite/Raw/Pass live
  // INSIDE the sub-row (Item 3 of the user's request).
  tb.innerHTML = rows.map((r, i) => {
    if (r.ok === false) {
      const err = escapeHtml(r.error || "failed");
      return `
        <tr class="failed-row">
          <td class="rank">#${i+1}</td>
          <td>${escapeHtml(r.agent_id)}</td>
          <td colspan="5" class="muted" style="color:var(--bad);">✗ ${err}</td>
          <td>${(r.agent_wall_time_s || 0).toFixed(1)}s</td>
          <td>${(r.judge_wall_time_s || 0).toFixed(1)}s</td>
        </tr>`;
    }
    const p1Val = r.pass_at_1_value ?? (r.pass_at_1 ? 1.0 : 0.0);
    const p5Val = r.pass_at_5_value ?? r.pass_at_k_value ?? 0;
    const p1Cls = p1Val >= 1 ? "pass-true" : "pass-false";
    const p5Cls = p5Val > 0 ? "pass-true" : "pass-false";
    const fh = r.first_hit_rank;
    const ph = r.primary_hit_count ?? 0;
    const sh = r.secondary_hit_count ?? 0;
    const np = r.pass_count ?? 0;
    const k = r.candidate_count ?? 5;
    const avgComp = r.avg_composite ?? _computeAvg(r.all_candidate_scores, "composite_score");
    const avgRaw  = r.avg_raw       ?? _computeAvg(r.all_candidate_scores, "composite_score_raw");
    const hitParts = [];
    hitParts.push(fh != null ? `first@rank ${fh}` : `<span class="muted">no hit</span>`);
    hitParts.push(`<span class="primary-tag">${ph}P</span>+<span class="secondary-tag">${sh}S</span>`);
    hitParts.push(`<span class="muted">${np}/${k}</span>`);

    const all = (r.all_candidate_scores || []).slice().sort((a, b) => a.rank - b.rank);
    const winner = r.best_candidate_rank;

    const subRow = all.length ? `
      <tr class="candidate-sub-row">
        <td colspan="9">
          <div class="leaderboard-candidates">
            ${all.map(c => _leaderboardCandidate(c, c.rank === winner)).join("")}
          </div>
        </td>
      </tr>` : "";

    return `
      <tr class="agent-row">
        <td class="rank">#${i+1}</td>
        <td>${escapeHtml(r.agent_id)}</td>
        <td class="pk-cell"><span class="pk-pill ${p1Cls}">${(p1Val * 100).toFixed(0)}%</span></td>
        <td class="pk-cell"><span class="pk-pill ${p5Cls}">${(p5Val * 100).toFixed(1)}%</span></td>
        <td class="num">${avgComp.toFixed(3)}</td>
        <td class="num">${avgRaw.toFixed(2)}</td>
        <td class="hit-detail-cell">${hitParts.join(" · ")}</td>
        <td class="num">${(r.agent_wall_time_s || 0).toFixed(1)}s</td>
        <td class="num">${(r.judge_wall_time_s || 0).toFixed(1)}s</td>
      </tr>
      ${subRow}`;
  }).join("");
}

function _computeAvg(arr, key) {
  if (!arr || !arr.length) return 0;
  const vals = arr.map(c => c[key]).filter(v => v != null);
  if (!vals.length) return 0;
  return vals.reduce((a, b) => a + b, 0) / vals.length;
}

function _leaderboardCandidate(c, isWinner) {
  // Compact per-question card shown inside the sub-row: rank pill | question
  // (truncated, hover to see full) | Composite | Raw | Pass | Matched GQ | Centrality.
  const passed = !!c.passed;
  const passCls = passed ? "pass-true" : "pass-false";
  const qFull = c.question || "";
  return `
    <div class="lb-cand ${isWinner ? 'winner' : ''}" title="${escapeHtml(qFull)}">
      <span class="lb-rank">rank ${c.rank}${isWinner ? ' · winner' : ''}</span>
      <span class="lb-q">${escapeHtml(qFull)}</span>
      <span class="lb-metric"><span class="k">Comp</span><span class="v">${(c.composite_score ?? 0).toFixed(3)}</span></span>
      <span class="lb-metric"><span class="k">Raw</span><span class="v">${(c.composite_score_raw ?? 0).toFixed(2)}</span></span>
      <span class="lb-pass ${passCls}">${passed ? '✓ pass' : '✗ fail'}</span>
      <span class="lb-match"><code>${escapeHtml(c.matched_gold_id || "-")}</code> <span class="cent ${c.matched_centrality}">${escapeHtml(c.matched_centrality || "-")}</span></span>
    </div>`;
}

function _scoreBadges(r) {
  // Agent-level summary badges only. Composite / Raw / Pass / Matched GQ are
  // per-question metrics — they live inside each candidate mini-card below,
  // not here.
  if (r.ok === false) {
    return `
      <div class="score-badges">
        <span class="sb pass-false"><span class="k">Status</span><span class="v">✗ failed</span></span>
      </div>`;
  }
  const p1Val = r.pass_at_1_value ?? (r.pass_at_1 ? 1.0 : 0.0);
  const p5Val = r.pass_at_5_value ?? r.pass_at_k_value ?? 0;
  const np = r.pass_count ?? 0;
  const k = r.candidate_count ?? 5;
  const fh = r.first_hit_rank;
  const ph = r.primary_hit_count ?? 0;
  const sh = r.secondary_hit_count ?? 0;
  const p1Cls = p1Val >= 1 ? "pass-true" : "pass-false";
  const p5Cls = p5Val > 0 ? "pass-true" : "pass-false";
  const hits = (fh != null || ph + sh > 0)
    ? `<span class="sb"><span class="k">Hits</span><span class="v">${fh != null ? `first@${fh}` : '—'} · ${ph}P + ${sh}S · ${np}/${k}</span></span>`
    : "";
  return `
    <div class="score-badges">
      <span class="sb ${p1Cls}"><span class="k">Pass@1</span><span class="v">${(p1Val * 100).toFixed(0)}%</span></span>
      <span class="sb ${p5Cls}"><span class="k">Pass@5</span><span class="v">${(p5Val * 100).toFixed(1)}%</span></span>
      ${hits}
    </div>`;
}

function renderQuestions(grid, rows) {
  const dims = ["match_strength", "required_elements_coverage", "acceptability", "data_grounding"];
  const dimLabels = state.rubricSpec?.dimension_labels || {};
  grid.innerHTML = rows.map(r => {
    if (r.ok === false) {
      return `
        <div class="question-card failed-card">
          <h4>${escapeHtml(r.agent_id)}</h4>
          ${_scoreBadges(r)}
          <div class="muted" style="font-size:11.5px;">agent did not produce a parseable response</div>
          <pre class="failure-trace">${escapeHtml(r.error || "(no error message recorded)")}</pre>
        </div>`;
    }

    // Per-agent header (Pass@1 / Pass@5 / hits) + the 5 candidates each with
    // their OWN Composite / Raw / Pass / Matched GQ / Centrality + reasoning.
    const all = (r.all_candidate_scores || []).slice().sort((a, b) => a.rank - b.rank);

    return `
      <div class="question-card">
        <h4>${escapeHtml(r.agent_id)} <span class="muted" style="font-size:11px;font-weight:400;">${all.length} candidates</span></h4>
        ${_scoreBadges(r)}
        <div class="all-candidates-body" style="margin-top:14px;">
          ${all.map(c => _renderCandidateBlock(c, r, dims, dimLabels)).join("")}
        </div>
      </div>`;
  }).join("");
}

function _renderCandidateBlock(c, agentRow, dims, dimLabels) {
  // Per-question rendering: each candidate gets its own Composite / Raw /
  // Pass / Matched GQ / Centrality + per-dim scores + reasoning. Each of
  // the 5 candidates was judged independently, so per-dim reasoning is
  // available for all of them (not just the winner).
  const sc = c.scores || {};
  const passed = !!c.passed;
  const passCls = passed ? "pass-true" : "pass-false";
  const isWinner = c.rank === agentRow.best_candidate_rank;

  // Per-candidate reasoning. Fall back to the agent-level (winner-only)
  // reasoning ONLY for the winner — old runs (pre per-candidate persistence)
  // didn't save per-candidate reasoning, so non-winners legitimately have
  // none and we surface that explicitly rather than silently showing "—".
  const hasOwnReasoning = !!c.per_dimension_reasoning
    && Object.values(c.per_dimension_reasoning).some(v => v && String(v).trim());
  const perDim = hasOwnReasoning
    ? c.per_dimension_reasoning
    : (isWinner && agentRow.per_dimension_reasoning) || {};
  const closestAcceptable = c.closest_acceptable_variant
    || (isWinner ? agentRow.closest_acceptable_variant : null);
  const closestUnacceptable = c.closest_unacceptable_variant
    || (isWinner ? agentRow.closest_unacceptable_variant : null);
  const rationale = c.rationale
    || (isWinner ? agentRow.rationale : null);
  const reasoningMissing = !hasOwnReasoning && !isWinner;

  const reasoningBlock = dims.map(d => {
    const score = sc[d] ?? 0;
    const label = dimLabels[d] || d;
    const reason = perDim[d] || "—";
    return `
      <div class="dim-row">
        <span class="score s-${score}">${score}</span>
        <span class="label">${escapeHtml(label)}<br><code class="muted" style="font-size:10.5px;">${d}</code></span>
        <span class="reason">${escapeHtml(reason)}</span>
      </div>`;
  }).join("");

  const variantBlocks = `
    ${closestAcceptable ? `
      <div class="variant acceptable">
        <div class="lbl">closest acceptable variant</div>
        <div class="text">${escapeHtml(closestAcceptable)}</div>
      </div>` : ""}
    ${closestUnacceptable ? `
      <div class="variant unacceptable">
        <div class="lbl">closest UNACCEPTABLE variant</div>
        <div class="text">${escapeHtml(closestUnacceptable)}</div>
      </div>` : ""}`;

  const matchedGold = c.matched_gold_question
    || (isWinner ? agentRow.matched_gold_question : null);

  return `
    <div class="candidate-block ${isWinner ? 'winner' : ''}">
      <div class="cand-head">
        <span class="rank-pill">rank ${c.rank}${isWinner ? ' · winner' : ''}</span>
        <span class="cand-pass ${passCls}">${passed ? '✓ pass' : '✗ fail'}</span>
        <span class="cand-metric"><span class="k">Composite</span><span class="v">${(c.composite_score ?? 0).toFixed(3)}</span></span>
        <span class="cand-metric"><span class="k">Raw</span><span class="v">${(c.composite_score_raw ?? 0).toFixed(2)} / 5</span></span>
        <span class="cand-metric"><span class="k">Matched</span><span class="v"><code>${escapeHtml(c.matched_gold_id || "-")}</code> <span class="cent ${c.matched_centrality}">${escapeHtml(c.matched_centrality || "-")}</span></span></span>
      </div>
      <p class="q">${escapeHtml(c.question || "")}</p>
      ${matchedGold ? `<div class="muted" style="font-size:11px;margin:-4px 0 6px;">matched gold: ${escapeHtml(matchedGold)}</div>` : ""}
      <div class="judge-detail">
        <h5>per-dimension reasoning${reasoningMissing ? ' <span class="muted" style="font-weight:400;font-size:10.5px;">(旧版本评测未存储非冠军 candidate 的理由 · 重新评测可填充)</span>' : ''}</h5>
        ${reasoningBlock}
        ${variantBlocks}
        ${rationale ? `
          <div class="muted" style="font-size:11px;margin-top:6px;">overall rationale</div>
          <div class="reason" style="font-size:12px;color:#cfd6e3;line-height:1.5;">${escapeHtml(rationale)}</div>` : ""}
      </div>
    </div>`;
}

function renderElements(grid, rows) {
  grid.innerHTML = rows.map(r => {
    const failed = r.ok === false || r.matched_gold_id == null;
    if (failed) {
      return `
        <div class="question-card failed-card">
          <h4>${escapeHtml(r.agent_id)}</h4>
          ${_scoreBadges(r)}
          <div class="muted" style="font-size:11.5px;">required-elements not evaluable: agent did not match a gold question</div>
        </div>`;
    }
    return `
      <div class="question-card">
        <h4>${escapeHtml(r.agent_id)} · <code>${escapeHtml(r.matched_gold_id || "-")}</code></h4>
        ${_scoreBadges(r)}
        <div class="muted" style="margin-top:6px;">covered (${(r.covered_required_elements||[]).length})</div>
        <div class="meta">
          ${(r.covered_required_elements || []).map(e =>
            `<span class="chip" style="background:rgba(95,208,114,.15);color:var(--good);border-color:rgba(95,208,114,.35);">${escapeHtml(e)}</span>`).join('') || '<span class="muted">—</span>'}
        </div>
        <div class="muted" style="margin-top:10px;">missing (${(r.missing_required_elements||[]).length})</div>
        <div class="meta">
          ${(r.missing_required_elements || []).map(e =>
            `<span class="chip" style="background:rgba(239,93,97,.12);color:var(--bad);border-color:rgba(239,93,97,.35);">${escapeHtml(e)}</span>`).join('') || '<span class="muted">—</span>'}
        </div>
      </div>`;
  }).join("");
}

/* ============ Recent + History ============ */

async function refreshHistoryCount() {
  try {
    const r = await fetch(`${API}/api/runs`).then(r => r.json());
    $("#nav-history-count").textContent = (r.runs || []).length;
  } catch { /* tolerate transient drops */ }
}

async function loadHistory() {
  // Always pull both shapes — runs (flat) for the table view, sets (grouped)
  // for the default grouped view.
  const [runsR, setsR] = await Promise.all([
    fetch(`${API}/api/runs`).then(r => r.json()).catch(() => ({ runs: [] })),
    fetch(`${API}/api/question_sets`).then(r => r.json()).catch(() => ({ question_sets: [] })),
  ]);
  const runs = runsR.runs || [];
  const sets = setsR.question_sets || [];
  $("#nav-history-count").textContent = runs.length;

  const grouped = $("#history-grouped");
  const tbl = $("#history-table");
  const groupToggle = $("#history-group-toggle");
  const showGrouped = groupToggle ? groupToggle.checked : true;
  grouped.hidden = !showGrouped;
  tbl.hidden = showGrouped;

  // ---- grouped view ----
  if (sets.length === 0) {
    grouped.innerHTML = `<div class="muted" style="padding:14px;">尚未运行任何评测。</div>`;
  } else {
    grouped.innerHTML = sets.map(g => {
      const totalRuns = g.run_count || 0;
      const best = g.best_composite;
      const bestCls = best == null ? "" : (best >= 0.6 ? "" : "fail");
      const bestStr = best == null ? "—" : best.toFixed(3);
      const bestAgent = g.best_agent ? ` · ${escapeHtml(g.best_agent)}` : "";
      const last = new Date((g.last_seen || 0) * 1000).toLocaleString();
      const runsHtml = (g.uploads || []).flatMap(u =>
        (u.runs || []).map(r => {
          const composite = r.top_composite;
          const compositeStr = composite == null ? "—" : composite.toFixed(3);
          const cls = composite == null ? "" : (composite >= 0.6 ? "pass-true" : "pass-false");
          const agents = (r.agents || []).map(a => `<span class="pill">${escapeHtml(a)}</span>`).join("");
          const ts = new Date((r.created_at || 0) * 1000).toLocaleString();
          const isLive = r.status === "queued" || r.status === "running";
          const isAbandoned = r.status === "abandoned";
          let statusCell, rowCls;
          if (r.finished) {
            statusCell = `<span class="status">✓ 完成</span>`;
            rowCls = "";
          } else if (isLive) {
            statusCell = `<span class="status running"><span class="dot"></span>${escapeHtml(r.status)} · 点击查看进度 →</span>`;
            rowCls = "running";
          } else if (isAbandoned) {
            statusCell = `<span class="status abandoned">⚠ 已中断（server 重启） · 查看 →</span>`;
            rowCls = "abandoned";
          } else {
            statusCell = `<span class="status">${escapeHtml(r.status || "—")}</span>`;
            rowCls = "";
          }
          // Render as a real anchor — native navigation means clicks always work,
          // regardless of any other listener / propagation issues.
          return `
            <a class="qrun-row ${rowCls}" href="#/run/${u.upload_id}/${r.run_id}">
              <span class="ts">${ts}</span>
              <span><code style="font-size:11px;">${escapeHtml(r.run_id)}</code></span>
              <span class="agents">${agents || '<span class="muted">—</span>'}</span>
              <span class="composite ${cls}">${compositeStr}</span>
              ${statusCell}
            </a>`;
        })
      ).join("");
      return `
        <div class="qset-group">
          <div class="qset-hd">
            <span class="qsid">${escapeHtml(g.question_set_id)}</span>
            <span class="meta">最近：${last} · ${totalRuns} 次 run · ${(g.uploads || []).length} 次 upload</span>
            <span class="best ${bestCls}">best <span class="v">${bestStr}</span>${bestAgent}</span>
          </div>
          <div class="qset-runs">${runsHtml || '<div class="muted" style="padding:10px 16px;">该题集下还没有 run。</div>'}</div>
        </div>`;
    }).join("");
    // No JS click handlers here — the rows are real <a> anchors.
  }

  // ---- flat table view (toggle off) ----
  const enriched = await Promise.all(runs.map(async row => {
    try {
      const d = await fetch(`${API}/api/runs/${row.upload_id}/${row.run_id}`).then(r => r.json());
      const lb = d.leaderboard || {};
      return { ...row, agents: (lb.rows || []).map(x => x.agent_id), top: (lb.rows || [])[0] };
    } catch { return { ...row, agents: [], top: null }; }
  }));
  const tb = $("#history-table tbody");
  tb.innerHTML = enriched.map(e => {
    const compStr = (e.top && e.top.composite_score != null) ? e.top.composite_score.toFixed(3) : "—";
    const isLive = e.status === "queued" || e.status === "running";
    const isAbandoned = e.status === "abandoned";
    let statusCell, rowCls, linkLabel;
    if (e.finished) {
      statusCell = `<span class="pass-true">✓ 完成</span>`;
      rowCls = ""; linkLabel = "查看 →";
    } else if (isLive) {
      statusCell = `<span class="status running"><span class="dot"></span>${escapeHtml(e.status)}</span>`;
      rowCls = "running"; linkLabel = "查看进度 →";
    } else if (isAbandoned) {
      statusCell = `<span class="status abandoned">⚠ 已中断</span>`;
      rowCls = "abandoned"; linkLabel = "查看 →";
    } else {
      statusCell = `<span class="status">${escapeHtml(e.status || "—")}</span>`;
      rowCls = ""; linkLabel = "查看 →";
    }
    const href = `#/run/${e.upload_id}/${e.run_id}`;
    return `
    <tr data-href="${href}" class="${rowCls}">
      <td>${new Date((e.created_at || 0) * 1000).toLocaleString()}</td>
      <td><code>${escapeHtml(e.question_set_id || "—")}</code></td>
      <td><code>${escapeHtml(e.upload_id)}</code></td>
      <td><code>${escapeHtml(e.run_id)}</code></td>
      <td><span class="agents">${(e.agents || []).map(a => `<span class="pill">${escapeHtml(a)}</span>`).join("")}</span></td>
      <td class="composite">${compStr}</td>
      <td>${statusCell}</td>
      <td><a class="link" href="${href}">${linkLabel}</a></td>
    </tr>`;
  }).join("");
  // Native <a> handles the action-column click; this listener is for clicks
  // anywhere else on the row (timestamps, agent pills, etc.).
  $$("#history-table tbody tr").forEach(tr =>
    tr.addEventListener("click", (ev) => {
      // Don't double-trigger when the user clicks the inner anchor.
      if (ev.target.closest("a")) return;
      const href = tr.dataset.href;
      if (href) location.hash = href.replace(/^#/, "");
    }));
}

document.getElementById("history-group-toggle")?.addEventListener("change", loadHistory);

$("#clear-history-btn")?.addEventListener("click", async () => {
  if (!confirm("将永久删除所有上传记录与评测结果。此操作不可撤销，确认继续？")) return;
  const btn = $("#clear-history-btn");
  btn.disabled = true; btn.textContent = "清空中…";
  try {
    const r = await fetch(`${API}/api/runs`, { method: "DELETE" }).then(r => r.json());
    btn.textContent = `已删除 ${r.removed || 0} 个上传`;
    setTimeout(() => { btn.textContent = "清空全部历史"; btn.disabled = false; }, 1800);
    await loadHistory();
    refreshHistoryCount();
  } catch (e) {
    btn.textContent = "清空失败";
    setTimeout(() => { btn.textContent = "清空全部历史"; btn.disabled = false; }, 1800);
  }
});

async function loadRunDetail(uploadId, runId) {
  // Close any prior live-detail SSE before re-entering this view.
  if (state.detailEvtSource) { try { state.detailEvtSource.close(); } catch {} state.detailEvtSource = null; }
  state.detailLiveAgents = {};

  $("#detail-title").textContent = `${runId}`;
  $("#detail-meta").innerHTML = `<span class="muted">loading…</span>`;
  for (const id of ["export-csv-btn", "export-json-btn", "export-md-btn"]) {
    const b = document.getElementById(id);
    if (b) b.disabled = true;
  }
  state.detailRows = null;
  state.detailMeta = null;
  try {
    await _renderDetailFromServer(uploadId, runId);
    // If this run is still alive on the server, attach SSE so the user
    // can watch live progress instead of staring at a blank screen.
    const status = state.detailMeta?.status;
    const live = status === "queued" || status === "running";
    if (live) _attachDetailSSE(uploadId, runId);
  } catch (e) {
    $("#detail-meta").innerHTML = `<span class="muted">加载失败: ${escapeHtml(String(e))}</span>`;
  }
}

async function _renderDetailFromServer(uploadId, runId) {
  const d = await fetch(`${API}/api/runs/${uploadId}/${runId}`).then(r => r.json());
  const lb = d.leaderboard || { rows: [] };
  let rows = (lb.rows || []).slice();
  rows.sort((a, b) => (b.pass_at_5_value ?? b.pass_at_k_value ?? -1) - (a.pass_at_5_value ?? a.pass_at_k_value ?? -1));
  state.detailRows = rows;
  state.detailMeta = {
    uploadId, runId,
    qsetId: d.question_set_id,
    judge: lb.judge_model,
    provider: lb.judge_provider,
    status: d.status,
  };

  const okCount = rows.filter(r => r.ok !== false && r.composite_score != null).length;
  const failCount = rows.length - okCount;
  const live = d.status === "queued" || d.status === "running";
  const abandoned = !live && !rows.length && d.status !== "finished";
  const statusBadge = live
    ? `<span class="pill running" style="margin-left:8px;">● ${escapeHtml(d.status)}</span>`
    : (d.status === "failed"
        ? `<span class="pill" style="margin-left:8px;background:#3a1414;color:#ff8b8b;">✗ failed</span>`
        : abandoned
          ? `<span class="pill" style="margin-left:8px;background:#3a2c14;color:#ffc86c;">⚠ 已中断（server 重启 / 任务未完成）</span>`
          : `<span class="pill" style="margin-left:8px;background:#0d2a17;color:#73e3a4;">✓ done</span>`);
  $("#detail-meta").innerHTML = `
    <span class="muted">题集</span> · <code>${escapeHtml(d.question_set_id || "—")}</code>
    <span class="muted" style="margin-left:14px">upload</span> · <code>${escapeHtml(uploadId)}</code>
    <span class="muted" style="margin-left:14px">judge</span> · <code>${escapeHtml(lb.judge_model || "?")} (${escapeHtml(lb.judge_provider || "?")})</code>
    <span class="muted" style="margin-left:14px">agents</span> · <code>${rows.length}</code> (<span class="pass-true">${okCount} ok</span>${failCount ? ` · <span class="pass-false">${failCount} failed</span>` : ""})
    <span class="muted" style="margin-left:14px">events</span> · <code>${(d.events || []).length}</code>
    ${statusBadge}`;

  // Live progress strip — visible only while the run is still going. We
  // synthesize per-agent phase from the event stream so the user sees
  // queued → running → judging → done/failed without having to refresh.
  const stripHost = $("#detail-live-strip");
  if (stripHost) {
    if (live) {
      _ingestEventsToLiveAgents(d.events || []);
      stripHost.hidden = false;
      stripHost.innerHTML = _renderLiveStrip();
    } else {
      stripHost.hidden = true;
      stripHost.innerHTML = "";
    }
  }

  if (rows.length) {
    renderLeaderboard($("#detail-leaderboard tbody"), rows);
    renderQuestions($("#detail-questions"), rows);
    renderElements($("#detail-elements"), rows);
    Charts.renderRadar(rows.filter(r => r.ok !== false && r.composite_score != null), "detail-radar");
  } else if (live) {
    $("#detail-leaderboard tbody").innerHTML = `<tr><td colspan="9" class="muted" style="text-align:center;padding:18px;">运行中，尚无 leaderboard 数据。看 ↑ 上方进度。</td></tr>`;
    $("#detail-questions").innerHTML = `<div class="muted" style="padding:18px;">运行中…</div>`;
    $("#detail-elements").innerHTML = `<div class="muted" style="padding:18px;">运行中…</div>`;
  } else if (abandoned) {
    const msg = `这个 run 没有产出 leaderboard.json —— 多半是 server 重启时被中断了 (status=${escapeHtml(d.status || "?")})。事件日志里可能还有部分历史，但无法继续。`;
    $("#detail-leaderboard tbody").innerHTML = `<tr><td colspan="9" class="muted" style="text-align:center;padding:18px;">${msg}</td></tr>`;
    $("#detail-questions").innerHTML = `<div class="muted" style="padding:18px;">${msg}</div>`;
    $("#detail-elements").innerHTML = `<div class="muted" style="padding:18px;">${msg}</div>`;
  } else {
    $("#detail-leaderboard tbody").innerHTML = `<tr><td colspan="9" class="muted" style="text-align:center;padding:18px;">没有结果。</td></tr>`;
    $("#detail-questions").innerHTML = "";
    $("#detail-elements").innerHTML = "";
  }

  $("#detail-events").textContent = (d.events || [])
    .map(ev => `[${new Date(ev.ts*1000).toLocaleTimeString()}] ${ev.kind} ${JSON.stringify(stripHeavy(ev))}`)
    .join("\n");

  for (const id of ["export-csv-btn", "export-json-btn", "export-md-btn"]) {
    const b = document.getElementById(id);
    if (b) b.disabled = !rows.length;
  }
}

function _ingestEventsToLiveAgents(events) {
  const m = state.detailLiveAgents || {};
  for (const ev of events) {
    const a = ev.agent_id;
    if (!a) continue;
    if (!m[a]) m[a] = { agent_id: a, phase: "queued", t0: null, agentTime: null, judgeTime: null, error: null };
    switch (ev.kind) {
      case "agent_started":   m[a].phase = "running"; m[a].t0 = ev.ts; break;
      case "agent_finished":  m[a].phase = "judging"; m[a].agentTime = ev.wall_time_s ?? null; break;
      case "agent_failed":    m[a].phase = "failed"; m[a].error = ev.error || "unknown error"; break;
      case "judge_started":   if (m[a].phase !== "failed") m[a].phase = "judging"; break;
      case "judge_finished":  if (m[a].phase !== "failed") { m[a].phase = "done"; m[a].judgeTime = ev.judge_wall_time_s ?? null; } break;
    }
  }
  state.detailLiveAgents = m;
}

function _renderLiveStrip() {
  const m = state.detailLiveAgents || {};
  const items = Object.values(m);
  if (!items.length) {
    return `<div class="muted" style="padding:14px;">等待 agent 启动…</div>`;
  }
  const phaseLabel = {
    queued: "队列中",
    running: "agent 运行中",
    judging: "判官评分中",
    done: "✓ 完成",
    failed: "✗ 失败",
  };
  return `
    <div class="live-strip-grid">
      ${items.map(it => `
        <div class="live-strip-row" data-phase="${it.phase}">
          <span class="agent-name"><code>${escapeHtml(it.agent_id)}</code></span>
          <span class="phase-pill">${phaseLabel[it.phase] || it.phase}</span>
          <span class="muted timing">
            ${it.agentTime != null ? `agent ${it.agentTime.toFixed(1)}s` : ""}
            ${it.judgeTime != null ? ` · judge ${it.judgeTime.toFixed(1)}s` : ""}
          </span>
          ${it.error ? `<span class="err-snip" title="${escapeHtml(it.error)}">${escapeHtml(it.error.slice(0, 80))}${it.error.length > 80 ? "…" : ""}</span>` : ""}
        </div>`).join("")}
    </div>`;
}

function _attachDetailSSE(uploadId, runId) {
  const url = `${API}/api/runs/${uploadId}/${runId}/events`;
  const es = new EventSource(url);
  state.detailEvtSource = es;
  let pending = false;
  const refresh = async () => {
    if (pending) return;
    pending = true;
    try { await _renderDetailFromServer(uploadId, runId); } catch {}
    pending = false;
  };
  ["agent_started","agent_finished","agent_failed",
   "judge_started","judge_finished",
   "run_finished","run_failed","end"].forEach(k => {
    es.addEventListener(k, async (e) => {
      // Update the in-memory live map first so the strip re-renders quickly,
      // then refetch the full state for any persisted leaderboard rows.
      try {
        const obj = JSON.parse(e.data);
        _ingestEventsToLiveAgents([{ ...obj, kind: k }]);
        const stripHost = $("#detail-live-strip");
        if (stripHost && !stripHost.hidden) stripHost.innerHTML = _renderLiveStrip();
      } catch {}
      await refresh();
      if (k === "run_finished" || k === "run_failed" || k === "end") {
        try { es.close(); } catch {}
        state.detailEvtSource = null;
      }
    });
  });
  es.onerror = () => { /* tolerate transient drops; SSE auto-reconnects */ };
}

/* ============ export helpers (run detail) ============ */

function _csvCell(v) {
  if (v == null) return "";
  let s = String(v);
  if (Array.isArray(v)) s = v.join("|");
  if (typeof v === "object" && !Array.isArray(v)) s = JSON.stringify(v);
  if (/[",\n\r]/.test(s)) s = `"${s.replace(/"/g, '""')}"`;
  return s;
}

function _runCsv(rows, meta) {
  // One row per CANDIDATE (since Composite / Raw / matched_gold belong to the
  // question, not the agent). Agent-level Pass@1 / Pass@5 are repeated on
  // every row so users can pivot in Excel either way.
  const headers = [
    "agent_rank", "agent_id",
    "agent_pass_at_1", "agent_pass_at_1_pct",
    "agent_pass_at_5_value", "agent_pass_at_5_pct",
    "agent_pass_count", "agent_candidate_count",
    "agent_first_hit_rank",
    "agent_primary_hit_count", "agent_secondary_hit_count",
    "agent_wall_time_s", "agent_judge_wall_time_s",
    "agent_error",
    // per-candidate (per-question) metrics:
    "candidate_rank", "candidate_question",
    "composite_score", "composite_score_raw", "passed",
    "matched_gold_id", "matched_centrality",
    "match_strength", "required_elements_coverage", "acceptability", "data_grounding",
    "is_winner",
  ];
  const lines = [headers.map(_csvCell).join(",")];
  rows.forEach((r, i) => {
    if (r.ok === false) {
      lines.push([
        i + 1, r.agent_id,
        "", "", "", "", "", "", "", "", "",
        "", "", r.error,
        "", "", "", "", "", "", "",
        "", "", "", "", "",
      ].map(_csvCell).join(","));
      return;
    }
    const p1 = r.pass_at_1 ? 1 : 0;
    const p1Pct = ((r.pass_at_1_value ?? p1) * 100).toFixed(1);
    const p5Val = r.pass_at_5_value ?? r.pass_at_k_value ?? 0;
    const all = r.all_candidate_scores || [];
    const winner = r.best_candidate_rank;
    all.forEach(c => {
      lines.push([
        i + 1, r.agent_id,
        p1, p1Pct,
        p5Val.toFixed(4), (p5Val * 100).toFixed(1),
        r.pass_count, r.candidate_count,
        r.first_hit_rank,
        r.primary_hit_count, r.secondary_hit_count,
        r.agent_wall_time_s, r.judge_wall_time_s,
        "",
        c.rank, c.question,
        c.composite_score, c.composite_score_raw, c.passed,
        c.matched_gold_id, c.matched_centrality,
        c.scores?.match_strength, c.scores?.required_elements_coverage,
        c.scores?.acceptability, c.scores?.data_grounding,
        (c.rank === winner) ? "true" : "false",
      ].map(_csvCell).join(","));
    });
  });
  return "﻿" + lines.join("\r\n");
}

function _runMarkdown(rows, meta) {
  const head = [
    `# 评测详情 · ${meta.runId}`,
    "",
    `- 题集 \`${meta.qsetId || "—"}\``,
    `- Upload \`${meta.uploadId}\``,
    `- Judge: \`${meta.judge || "?"}\` (${meta.provider || "?"})`,
    "",
    "## Leaderboard (agent-level: Pass@1 + Pass@5)",
    "",
    "| Rank | Agent | Pass@1 | Pass@5 | first hit | P/S | Agent t | Judge t |",
    "|---:|:--|:--:|:--:|:--:|:--:|--:|--:|",
  ];
  rows.forEach((r, i) => {
    if (r.ok === false) {
      head.push(`| ${i+1} | ${r.agent_id} | — | — | — | — | ${(r.agent_wall_time_s||0).toFixed(1)}s | ${(r.judge_wall_time_s||0).toFixed(1)}s |`);
      return;
    }
    const p1 = (r.pass_at_1_value ?? (r.pass_at_1 ? 1 : 0)) * 100;
    const p5 = (r.pass_at_5_value ?? r.pass_at_k_value ?? 0) * 100;
    const fh = r.first_hit_rank != null ? `rank ${r.first_hit_rank}` : "—";
    const ps = `${r.primary_hit_count ?? 0}P+${r.secondary_hit_count ?? 0}S`;
    head.push(`| ${i+1} | ${r.agent_id} | ${p1.toFixed(0)}% | ${p5.toFixed(1)}% | ${fh} | ${ps} | ${(r.agent_wall_time_s||0).toFixed(1)}s | ${(r.judge_wall_time_s||0).toFixed(1)}s |`);
  });

  head.push("", "## Per-question detail (Composite / Raw / Pass are per-candidate)", "");
  rows.forEach(r => {
    head.push(`### ${r.agent_id}`);
    if (r.ok === false) {
      head.push("");
      head.push(`> ✗ failed: ${r.error || "(no error message)"}`);
      head.push("");
      return;
    }
    const winner = r.best_candidate_rank;
    head.push("");
    head.push("| Rank | Pass | Composite | Raw /5 | Matched GQ | Centrality | Question |");
    head.push("|---:|:--:|--:|--:|:--|:--|:--|");
    (r.all_candidate_scores || []).forEach(c => {
      const star = c.rank === winner ? " ⭐" : "";
      head.push(`| ${c.rank}${star} | ${c.passed ? "✓" : "✗"} | ${(c.composite_score ?? 0).toFixed(3)} | ${(c.composite_score_raw ?? 0).toFixed(2)} | ${c.matched_gold_id || "-"} | ${c.matched_centrality || "-"} | ${(c.question || "").replace(/\|/g, "\\|")} |`);
    });
    if (r.rationale) {
      head.push("");
      head.push(`**Winner rationale**: ${r.rationale}`);
    }
    head.push("");
  });
  return head.join("\n");
}

function _download(name, content, mime) {
  const blob = new Blob([content], { type: mime });
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url; a.download = name;
  document.body.appendChild(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(url), 4000);
}

document.getElementById("export-csv-btn")?.addEventListener("click", () => {
  if (!state.detailRows) return;
  const m = state.detailMeta;
  _download(`${m.qsetId || "run"}__${m.runId}.csv`, _runCsv(state.detailRows, m), "text/csv;charset=utf-8");
});
document.getElementById("export-json-btn")?.addEventListener("click", async () => {
  if (!state.detailMeta) return;
  const m = state.detailMeta;
  try {
    const d = await fetch(`${API}/api/runs/${m.uploadId}/${m.runId}`).then(r => r.json());
    _download(`${m.qsetId || "run"}__${m.runId}.json`, JSON.stringify(d, null, 2), "application/json");
  } catch (e) { alert(`下载失败: ${e}`); }
});
document.getElementById("export-md-btn")?.addEventListener("click", async () => {
  if (!state.detailRows) return;
  const md = _runMarkdown(state.detailRows, state.detailMeta);
  try {
    await navigator.clipboard.writeText(md);
    const btn = document.getElementById("export-md-btn");
    const old = btn.textContent;
    btn.textContent = "✓ 已复制";
    setTimeout(() => { btn.textContent = old; }, 1500);
  } catch {
    _download(`${state.detailMeta.qsetId || "run"}__${state.detailMeta.runId}.md`, md, "text/markdown;charset=utf-8");
  }
});

/* ============ Tooltip floater ============ */

const tt = $("#tooltip");
document.addEventListener("mouseover", e => {
  const t = e.target.closest("[data-tip]");
  if (!t) return;
  tt.textContent = t.dataset.tip;
  tt.hidden = false;
  positionTip(e);
});
document.addEventListener("mousemove", e => {
  if (tt.hidden) return;
  positionTip(e);
});
document.addEventListener("mouseout", e => {
  if (e.target.closest("[data-tip]")) tt.hidden = true;
});
function positionTip(e) {
  const pad = 14;
  let x = e.clientX + pad, y = e.clientY + pad;
  const r = tt.getBoundingClientRect();
  if (x + r.width > innerWidth - 8) x = e.clientX - r.width - pad;
  if (y + r.height > innerHeight - 8) y = e.clientY - r.height - pad;
  tt.style.left = `${x}px`; tt.style.top = `${y}px`;
}

/* ============ utils ============ */

function setStatus(stepId, status, label) {
  const pill = document.querySelector(`#${stepId} .status-pill`);
  if (!pill) return;
  pill.dataset.status = status;
  if (label) pill.textContent = label;
}
function prettyBytes(n) {
  if (!n) return "0 B";
  const units = ["B","KB","MB","GB"];
  let i = 0; while (n >= 1024 && i < units.length - 1) { n /= 1024; i++; }
  return `${n.toFixed(n < 10 ? 1 : 0)} ${units[i]}`;
}
function escapeHtml(s) {
  return (s || "").replace(/[&<>"']/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]));
}

route();
