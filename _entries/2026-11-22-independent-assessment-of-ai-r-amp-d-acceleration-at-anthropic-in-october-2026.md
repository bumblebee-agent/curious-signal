---
title: "Independent Assessment of AI R&amp;D Acceleration at Anthropic in October 2026"
date: 2026-11-22 10:49:58 +0700
section: Research Summary
section_slug: research-summary
description: "Assessment: August 12–October 29, 2026 Final public report submitted: November 3; supplied text includes a November 6 checklist correction. Basis: Supplied report only; linked claims have not been independently verified."
audio: /audio/2026/11/independent-assessment-of-ai-r-amp-d-acceleration-at-anthropic-in-october-2026.mp3
duration: "4 min 24 sec"
read_time: "9 min"
primary_source: https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/#executive-summary
signal:
  - "Assessment: August 12–October 29, 2026 Final public report submitted: November 3; supplied text includes a November 6 checklist correction."
  - "Basis: Supplied report only; linked claims have not been independently verified."
  - "METR’s assessment suggests that Anthropic’s model capabilities on well-specified tasks were improving approximately twice as fast in October 2026 as during March 2024–October 2025."
---
**Assessment:** August 12–October 29, 2026  
**Final public report submitted:** November 3; supplied text includes a November 6 checklist correction.  
**Basis:** Supplied report only; linked claims have not been independently verified.

## Bottom line

METR’s assessment suggests that Anthropic’s model capabilities on **well-specified tasks** were improving approximately **twice as fast in October 2026** as during March 2024–October 2025. METR believes AI assistance likely explains a majority of the current acceleration, but this is a **highly uncertain causal judgment**, not an experimentally established result.

**The central qualification is transparency:** Anthropic redacted a majority of the evidence METR considered most informative. METR could publish its highest-level risk conclusions, but readers cannot independently evaluate much of their evidential basis.

## Main findings and their strength

| Finding | Reported result | Important qualification |
|---|---|---|
| Benchmark acceleration | AECI growth accelerated **1.9x**, with **95% CI: 1.5–2.8x**, since October 2025. | Measures benchmark progress, not directly real-world impact or research productivity. |
| Broader capability assessment | METR’s subjective central judgment is approximately **2x** historical progress on well-specified tasks. | METR would not be surprised by **1.3x or 3x**; this is distinct from the statistical confidence interval. |
| Attribution to AI | METR guesses a majority—“perhaps **≈80%**”—of **current October 2026 acceleration** is due to AI. | Substantial uncertainty; no decisive evidence or consensus among Anthropic staff. This is not 80% of all progress. |
| Training compute | METR is confident acceleration was **not caused by acceleration in training-compute scaling**. | Does not mean compute stopped growing or contributed nothing. Supporting details were redacted. |
| Near-term constraints | METR identified no convincing bottleneck in algorithms, training compute, experiment compute, or data taking effect over the next **12 months**. | Its interpretation changed repeatedly; absence of an identified bottleneck is not proof that none exists. |
| Autonomous R&D | Current gains primarily involve **AI assistance**, not highly significant fully autonomous contributions to the most important training stages. | Researchers reported “signs of life” for autonomy, with uneven maturity and redacted details. |

Here, **2x acceleration means two years of historical progress in one year**, not twice the model’s capability or twice a benchmark score.

## Measurement approach and robustness

### AECI analysis

AECI is Anthropic’s version of the **Epoch Capabilities Index**. METR used Epoch’s public code and fitted ordinary least squares trends with **one imposed, estimated breakpoint**. The main specification placed that breakpoint at **October 7, 2025**.

Key choices:

- Models were dated by availability to **most Anthropic employees**, rather than public release, enabling comparison with unreleased models.
- Publicly released models used their released snapshot; never-released models used snapshots with substantial internal usage.
- Frontier snapshots received equal weight.
- Bootstrap confidence intervals sampled benchmark scores with replacement, stratified by model.
- The trend interval captures uncertainty in model AECI scores, **not sampling uncertainty over model inclusion**.

The analysis included internal-only models labeled **Unreleased 2022**, **Model 2**, **Model 3**, and **Model 4**. These were labels shared with METR, not necessarily Anthropic’s actual internal codenames.

### Sensitivity to analysis choices

| Analysis choice varied | Acceleration estimates |
|---|---:|
| Link function | **1.1x–2.9x** |
| Snapshot selection | **1.9x–2.2x** |
| Benchmark selection | **1.9x–2.2x** |
| Regularization | **1.9x–2.1x** |

The largest sensitivity concerns the assumed distribution of benchmark task difficulty. Standard logistic gives **1.9x**; complementary log-log gives **1.1x**; log-log gives **2.9x**. Most alternatives fit the observed data similarly well, so fit alone does not settle the choice.

Additional context:

- Including non-Anthropic frontier models lowers the estimate to approximately **1.4x**. This could reflect Anthropic catching up from a slower historical baseline, or differences in benchmark optimization.
- METR’s **1.9x** exceeds the **Haiku 5.5 system card’s 1.7x**, primarily because METR included newer internal-only models.
- Recent internal models make a sustained slope change look more plausible than a one-time jump at **Mythos Preview**.

## Evidence linking acceleration to AI

### Interviews and self-reports

METR received approximately **15 key-staff interviews**, alongside surveys, internal analyses, code and pull-request information, inference-spend data, and research-process metrics.

Claude-assisted classification of the published interview material yielded:

- **Yes:** 2
- **Leans yes:** 3
- **Borderline/unclear:** 4
- **Leans no:** 0
- **No:** 2

METR interpreted this as mildly supporting roughly 2x-or-greater acceleration from AI. However, interviewees differed in whether they meant personal versus organizational gains, or cumulative versus instantaneous effects.

Slack polls reported average perceived uplift of **≈12x** for the most capable internal model in October 2026. METR treats this as **very loose evidence** because respondents may be unrepresentative, answers required little deliberation, and self-reports can overestimate measured productivity.

**Individual speedup is not organizational acceleration.** Sustaining capability growth despite diminishing returns requires continued growth in research inputs or productivity. A high absolute uplift does not establish a corresponding acceleration in capabilities progress.

### Reported mechanism

Interviewees described faster implementation, less experiment-management overhead, and the ability to investigate many more ideas. Some attributed much of the improvement to AI; others emphasized hiring or other non-AI factors.

METR believes non-AI factors likely mattered substantially in late 2025, while AI’s relative contribution increased over time. Detailed attribution across training stages was redacted.

## Access, redactions, and scope

The engagement involved **2.5 full-time equivalents over 11 weeks**. Access exceeded METR’s expectations but was mediated, not employee-like: Anthropic could approve or reject information requests, and METR had no unmediated access to internal systems. METR neither requested nor received query access to unreleased models.

| Evidence category | Available to METR | Results publicly described |
|---|---|---|
| Internal-model benchmark capabilities | Yes | Yes |
| Key intermediate capability measures | Yes | No |
| Algorithmic progress estimates | Yes | No |
| AI contribution evidence | Yes | Partly |
| Key R&D input measurements | Mostly | No |
| Bottleneck details and forecasts | Partly | No |
| Staff interviews | Yes | Partly |

Anthropic’s stated reason for redactions was protecting confidential information that could accelerate other AI developers. METR agreed that the redacted material fit that description, while declining to judge whether the redactions were justified overall.

**Separate scope gap:** Anthropic canceled planned verification of **capabilities-versus-safety compute allocation** before METR reached substantive conclusions. This report therefore does not verify that allocation.

The approximately **100-page Full Report** was delivered privately to Anthropic. It should not be confused with the public report or assumed publicly accessible.

## Principal limitations

### Acceleration could be overstated

- Hiring, data improvements, algorithmic discoveries, or other non-AI factors might explain more of the acceleration.
- Easily graded, well-specified tasks may improve faster than messy real-world work.
- Benchmark-distribution overfitting or AECI methodology could inflate apparent progress.
- Anthropic’s historical baseline may have been unusually slow relative to the industry frontier.

### Acceleration could be understated

- Completed-model measurements lag underlying R&D by training time.
- Recent acceleration could be increasing further, although AECI does not clearly demonstrate continuous or hyperbolic acceleration.
- Autonomous research could become important sooner than expected.
- Real-world effects may increase abruptly when models cross capability thresholds.

### Measurement constraints

**Model 4 exceeded 50% on all 15 benchmarks used for it.** This means fewer benchmarks remain difficult for frontier models, raising measurement concerns—not that every benchmark is fully saturated. Excluding benchmark observations after 85% still produced a **1.9x** estimate.

Inference budgets may also limit capability elicitation. Typical reported per-attempt expenditure was:

- Internal benchmarks: **2.5M input / 72k output tokens**
- Agentic coding benchmarks: **10M input / 94k output tokens**

METR guessed larger budgets could add a handful of AECI points with similar effects across models, but did not investigate this deeply. Comparisons with other organizations’ token accounting were explicitly tentative.

## Independence and governance

- METR received **no payment**; Anthropic supplied devices and token credits.
- Most information flowed through two technical contacts, supplemented by broader interviews.
- Claude was heavily involved in supplied analyses, documents, and METR’s own analysis. METR found no significant discrepancies suggesting systematic manipulation, but this is its judgment rather than independent validation.
- One assessor held competitor equity and discussed employment with Anthropic, received an offer, and declined it. An unconflicted colleague thoroughly reviewed their work. METR’s newer policy would require recusal in that situation.
- METR disclosed incentives to preserve future company access and significant communication feedback from Anthropic; it did not believe the final conclusions were significantly distorted.

Notable **AEF-1** failures included insufficient public methodological detail for independent review, lack of direct/query access, and Anthropic’s authority to redact non-public findings. The redaction-authority finding does **not** establish that Anthropic used that authority to conceal concerning findings.

## Read-only follow-up priorities

1. Compare the **1.9x company-specific**, **1.4x broader-frontier**, and **1.7x system-card** estimates with their differing model sets and dating conventions.
2. Keep benchmark acceleration, subjective AI attribution, individual uplift, and real-world impact separate in dashboard labels.
3. Review public expenditure curves and robustness analyses for evidence that measurement assumptions change the trend.
4. Look for subsequent public evidence of autonomous R&D contributions or emerging bottlenecks.
5. Preserve the redaction warning alongside headline numbers; treat compute-allocation verification as an unresolved, separate question.

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Independent Assessment of AI R&amp;D Acceleration at Anthropic in October 2026](https://metr.org/blog/2026-11-05-anthropic-ai-rd-acceleration-assessment/#executive-summary)
