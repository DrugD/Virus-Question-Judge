# Technical Report: LLM Agent Design Patterns for Drug Discovery

## 1. Data Summary

The dataset comprises **47 research papers** (PDFs with extracted text) constituting a systematic literature collection on LLM-based agent systems for drug discovery and biomedical research, spanning **2023–2026**. The corpus was assembled to support a high-level survey on agentic AI methods in pharmaceutical R&D.

**File inventory:**
- `PDFs/`: 47 PDF documents (original papers)
- `notes/`: 47 plain-text extractions (one per paper)
- `Read.md`: Research directive describing scope and inclusion criteria

**Source distribution:**
- PMC/journal-published: 16 papers (34%) — outlets include *Briefings in Bioinformatics*, *Communications Chemistry*, *iScience*, *Machine Learning: Science and Technology*, *ACS Central Science*
- arXiv/preprint: 31 papers (66%)

**Temporal distribution (by arXiv ID or publication date):**
- 2023: 3 papers (ChemCrow, BioPlanner, ChemistX)
- 2024: ~11 papers
- 2025: ~14 papers
- 2026: ~16 papers (including several PMC-published reviews)

**Key papers include:** Mozi (governed autonomy), CACM (constraint-aware corrective memory), CLADD (RAG-enhanced collaborative agents), DrugPilot (parameterized reasoning), LIDDiA (language-based intelligent drug discovery agent), PharmAgents, PharmaSwarm, FROGENT, CoFEE, and survey papers from *Briefings in Bioinformatics* (2026).

---

## 2. Analysis

### Derived Statistic 1: Agent Architecture Prevalence

Systematic keyword search across all 47 text files reveals the following architecture frequencies:

| Architecture Feature | Count | Fraction |
|---|---|---|
| Multi-agent collaboration | 31 | 66% |
| Closed-loop / end-to-end pipeline | 30 | 64% |
| Memory mechanisms | 27 | 57% |
| RAG-enhanced retrieval | 25 | 53% |
| Governance / constraint control | 17 | 36% |
| Human-in-the-loop (HITL) checkpoints | 17 | 36% |
| Hierarchical supervisor–worker | 11 | 23% |

Multi-agent and closed-loop architectures dominate, but governance and HITL mechanisms — though present in roughly one third of papers — are markedly less studied relative to their stated importance.

### Derived Statistic 2: Drug Discovery Task Coverage

| Task Domain | Count | Fraction |
|---|---|---|
| Molecular generation / lead optimization | 24 | 51% |
| Virtual screening / docking | 15 | 32% |
| Wet-lab integration (claimed or actual) | 21 | 45% |
| Drug repurposing | 12 | 26% |
| Target identification | 11 | 23% |
| ADMET prediction | 9 | 19% |

Molecular generation is the most studied downstream task. Wet-lab integration appears in nearly half the papers, but close reading of representative works (Mozi, PharmAgents, PharmaSwarm) reveals that most claimed wet-lab capabilities are in-silico simulations rather than closed experimental loops.

### Derived Statistic 3: Safety/Reliability Signal Prevalence

| Safety/Reliability Feature | Count | Fraction |
|---|---|---|
| Hallucination / reliability concerns raised | 41 | 87% |
| Constraint / governance / safety mechanisms | 36 | 77% |
| Audit trail / traceability / reproducibility | 33 | 70% |

Reliability is the **dominant stated concern** in the field: 87% of papers explicitly raise hallucination or reliability problems, yet only 36% propose constraint-enforcement or governance mechanisms, and fewer still provide empirically validated governance solutions. CACM (2604.09308) achieves a 36.4% improvement in target-level success rate (TSR) on the 30-target LIDDiA benchmark by adding constraint-aware corrective memory; Mozi proposes PharmaBench (88 tasks covering full pipeline) and demonstrates that governed dual-layer architecture outperforms unconstrained ReAct baselines; CoFEE achieves 15.2% higher feature-discovery success at 53% lower cost through cognitive reasoning control.

---

## 3. Reasoning

The corpus documents a **progression from single-tool-augmented LLMs → multi-agent collaboration → governed autonomous pipelines**. Three tensions emerge:

1. **Architecture richness vs. reliability**: Papers widely adopt multi-agent and closed-loop designs (>60%), but reliability-oriented mechanisms (constraint enforcement, HITL, audit trails) lag behind in systematic evaluation.
2. **Claimed vs. validated wet-lab integration**: Nearly half the papers mention wet-lab tasks, but actual experimental closure (real compound synthesis, cell assays) is rare — most evaluation is in-silico.
3. **Benchmark heterogeneity**: Each paper introduces its own benchmark (LIDDiA's 30 targets, Mozi's PharmaBench with 88 tasks, DrugPilot's 8-task instruction dataset, FROGENT's 8 benchmarks). The field lacks a shared evaluation protocol that spans governance dimensions (constraint satisfaction, reproducibility, error recovery) alongside task performance.

The critical scientific opportunity the corpus motivates is: **whether specific governance architecture patterns — role-based tool isolation, constraint-aware memory, HITL checkpoints, skill-graph-enforced data contracts — causally improve agent reliability across multi-step drug discovery pipelines**, and which combination of patterns is sufficient for reproducible, auditable drug discovery.

---

## 4. Top Scientific Question

**Do specific agent governance architecture patterns — specifically the combination of role-based tool isolation, constraint-aware corrective memory, and human-in-the-loop checkpoints — causally and additively improve target-level success rate and reproducibility in multi-step LLM-based drug discovery pipelines, as measured across a standardized multi-target benchmark spanning target identification, lead optimization, ADMET screening, and virtual docking?**

---

## 5. Why This Question Is Testable on the Provided Dataset

The 47-paper corpus contains all components needed to answer this question:

- **Ground-truth performance data**: LIDDiA's 30-target benchmark provides a shared evaluation protocol; CACM reports +36.4% TSR improvement from constraint-aware corrective memory alone; Mozi's PharmaBench (88 tasks) tests full-pipeline governance.
- **Comparative architecture data**: Papers span the full spectrum from ungoverned ReAct (ChemCrow, LIDDiA baseline) to partially governed (DrugPilot's parameterized memory, CLADD's RAG collaboration) to fully governed (Mozi's dual-layer architecture, CACM's corrective memory). Their feature annotations (governance: yes/no, HITL: yes/no, constraint-memory: yes/no) enable systematic ablation analysis across the paper collection.
- **Additive contribution analysis**: By coding each paper's architecture features (role isolation, corrective memory, HITL) and correlating with reported TSR or task-completion metrics, this corpus enables a meta-analytic test of which governance patterns yield the largest, most robust reliability gains.
- **Reproducibility signals**: Papers reporting audit trails and traceability can be cross-referenced with those achieving multi-target success, testing whether traceable architectures are also higher-performing.
