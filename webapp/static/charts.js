/* Charts module — adapted to gold-rubric 2-dimension (semantic_alignment + acceptability) result schema.
   Exposes:
     Charts.renderAll(rows, radarId, barsId, timingId)
     Charts.renderRadar(rows, canvasId)
     Charts.relayoutAll()
*/

window.Charts = (function () {
  const CHART_CACHE = {}; // canvasId -> Chart instance

  const PALETTE = [
    { fill: "rgba(108,193,255,0.20)", stroke: "rgba(108,193,255,1)" },
    { fill: "rgba(154,123,255,0.18)", stroke: "rgba(154,123,255,1)" },
    { fill: "rgba(95,208,114,0.18)",  stroke: "rgba(95,208,114,1)"  },
    { fill: "rgba(240,180,64,0.18)",  stroke: "rgba(240,180,64,1)"  },
    { fill: "rgba(239,93,97,0.18)",   stroke: "rgba(239,93,97,1)"   },
    { fill: "rgba(192,132,252,0.18)", stroke: "rgba(192,132,252,1)" },
    { fill: "rgba(34,211,238,0.18)",  stroke: "rgba(34,211,238,1)"  },
    { fill: "rgba(251,146,60,0.18)",  stroke: "rgba(251,146,60,1)"  },
    { fill: "rgba(244,114,182,0.18)", stroke: "rgba(244,114,182,1)" },
    { fill: "rgba(132,204,22,0.18)",  stroke: "rgba(132,204,22,1)"  },
    { fill: "rgba(160,160,200,0.18)", stroke: "rgba(160,160,200,1)" },
  ];
  const DIMS = ["semantic_alignment", "acceptability"];
  const DIM_LABEL = {
    semantic_alignment: ["语义对齐"],
    acceptability:      ["可接受度"],
  };
  // Per-dimension max points (must mirror gold_rubric_metric.DIMENSION_MAX).
  // Scores are normalised to 0..1 (score / max) so charts share one scale.
  const DIM_MAX = {
    semantic_alignment: 67,
    acceptability:      33,
  };
  const _norm = (r, k) => (r.scores?.[k] ?? 0) / (DIM_MAX[k] || 1);

  function darkOpts(extra = {}) {
    return Object.assign({
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { labels: { color: "#e6e9ef", font: { size: 11 } } },
        tooltip: {
          backgroundColor: "rgba(11,14,20,0.95)", titleColor: "#fff",
          bodyColor: "#cfd6e3", borderColor: "#2a3140", borderWidth: 1
        },
      },
    }, extra);
  }

  function destroy(canvasId) {
    if (CHART_CACHE[canvasId]) { CHART_CACHE[canvasId].destroy(); delete CHART_CACHE[canvasId]; }
  }

  function renderRadar(rows, canvasId = "radar-canvas") {
    const el = document.getElementById(canvasId);
    if (!el || !rows.length) return;
    destroy(canvasId);
    const ctx = el.getContext("2d");
    const labels = DIMS.map(d => DIM_LABEL[d]);
    const datasets = rows.map((r, i) => {
      const c = PALETTE[i % PALETTE.length];
      return {
        label: r.agent_id,
        data: DIMS.map(k => _norm(r, k)),
        backgroundColor: c.fill,
        borderColor: c.stroke,
        borderWidth: 2,
        pointBackgroundColor: c.stroke,
      };
    });
    CHART_CACHE[canvasId] = new Chart(ctx, {
      type: "radar",
      data: { labels, datasets },
      options: darkOpts({
        scales: {
          r: {
            beginAtZero: true, min: 0, max: 1,
            angleLines: { color: "#2a3140" },
            grid: { color: "#2a3140" },
            ticks: { color: "#8a93a6", backdropColor: "transparent", stepSize: 0.2 },
            pointLabels: { color: "#cfd6e3", font: { size: 11 } },
          },
        },
      }),
    });
  }

  function renderBars(rows, canvasId = "bars-canvas") {
    const el = document.getElementById(canvasId);
    if (!el || !rows.length) return;
    destroy(canvasId);
    const ctx = el.getContext("2d");
    const datasets = rows.map((r, i) => {
      const c = PALETTE[i % PALETTE.length];
      return {
        label: r.agent_id,
        data: DIMS.map(k => _norm(r, k)),
        backgroundColor: c.fill, borderColor: c.stroke, borderWidth: 2, borderRadius: 4,
      };
    });
    CHART_CACHE[canvasId] = new Chart(ctx, {
      type: "bar",
      data: { labels: DIMS.map(d => DIM_LABEL[d].join(" ")), datasets },
      options: darkOpts({
        scales: {
          x: { ticks: { color: "#cfd6e3" }, grid: { color: "#2a3140" } },
          y: { beginAtZero: true, max: 1, ticks: { color: "#8a93a6", stepSize: 0.2 }, grid: { color: "#2a3140" } },
        },
      }),
    });
  }

  function renderTiming(rows, canvasId = "timing-canvas") {
    const el = document.getElementById(canvasId);
    if (!el || !rows.length) return;
    destroy(canvasId);
    const ctx = el.getContext("2d");
    const labels = rows.map(r => r.agent_id);
    CHART_CACHE[canvasId] = new Chart(ctx, {
      type: "bar",
      data: {
        labels,
        datasets: [
          {
            label: "agent (question generation)",
            data: rows.map(r => r.agent_wall_time_s || 0),
            backgroundColor: "rgba(108,193,255,0.45)",
            borderColor: "rgba(108,193,255,1)",
            borderWidth: 1, borderRadius: 4,
          },
          {
            label: "judge (rubric scoring)",
            data: rows.map(r => r.judge_wall_time_s || 0),
            backgroundColor: "rgba(154,123,255,0.45)",
            borderColor: "rgba(154,123,255,1)",
            borderWidth: 1, borderRadius: 4,
          },
        ],
      },
      options: darkOpts({
        indexAxis: "y",
        scales: {
          x: { stacked: true, ticks: { color: "#8a93a6" }, grid: { color: "#2a3140" }, title: { display: true, text: "seconds", color: "#8a93a6" } },
          y: { stacked: true, ticks: { color: "#cfd6e3" }, grid: { color: "#2a3140" } },
        },
      }),
    });
  }

  function renderAll(rows, radarId = "radar-canvas", barsId = "bars-canvas", timingId = "timing-canvas") {
    if (!rows?.length) return;
    renderRadar(rows, radarId);
    renderBars(rows, barsId);
    renderTiming(rows, timingId);
  }
  function relayoutAll() {
    Object.values(CHART_CACHE).forEach(c => c?.resize?.());
  }
  function destroyAll() {
    // Wipe every cached Chart instance + its bound canvas, so the result
    // panes show no leftover series from the previous run when the user
    // kicks off a fresh evaluation.
    Object.keys(CHART_CACHE).forEach(destroy);
  }
  return { renderAll, renderRadar, renderBars, renderTiming, relayoutAll, destroyAll };
})();
