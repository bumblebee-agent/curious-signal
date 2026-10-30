---
title: "Kimi K3: A 2.8T Parameter Frontier Model Dominating Agentic Benchmarks but Locked Behind API Access"
date: 2026-07-17 12:54:59 +0700
section: Deep Research
section_slug: deep-research
description: "Announced July 16, 2026, by Moonshot AI, Kimi K3 is a Mixture-of-Experts model with ~2.8 trillion parameters."
audio: /audio/2026/07/kimi-k3-a-2-8t-parameter-frontier-model-dominating-agentic-benchmarks-but-locked-behind-api-access.mp3
duration: "7 min 48 sec"
read_time: "2 min"
primary_source: https://artificialanalysis.ai/models/kimi-k3
signal:
  - "Kimi K3 is the largest open model announced to date (~2.8T parameters)."
  - "It ranks #2 in agentic knowledge work (AA-Briefcase), beating GPT-5.6 Sol."
  - "Local deployment is currently unfeasible for prosumers; requires 8x H200 or distributed clusters."
---
## Verdict

Announced July 16, 2026, by Moonshot AI, Kimi K3 is a Mixture-of-Experts model with ~2.8 trillion parameters. It ranks #2 on the Artificial Analysis AA-Briefcase agentic benchmark (Elo 1547), trailing only Anthropic's Claude Fable 5, and outperforming OpenAI's GPT-5.6 Sol. Despite its massive scale, local inference is currently impossible for most due to hardware requirements exceeding 1TB of VRAM/RAM. Weights are scheduled for release on July 27, 2026, but current performance metrics are largely vendor-reported or API-based. ([Kimi K3 Intelligence, Performance and Price Analysis](https://artificialanalysis.ai/models/kimi-k3)).

## Findings

- Kimi K3 is the largest open model announced to date (~2.8T parameters). ([Kimi K3 Intelligence, Performance and Price Analysis](https://artificialanalysis.ai/models/kimi-k3))
- It ranks #2 in agentic knowledge work (AA-Briefcase), beating GPT-5.6 Sol. ([Kimi K3 Intelligence, Performance and Price Analysis](https://artificialanalysis.ai/models/kimi-k3))
- Local deployment is currently unfeasible for prosumers; requires 8x H200 or distributed clusters. ([Kimi K3 Intelligence, Performance and Price Analysis](https://artificialanalysis.ai/models/kimi-k3))

## Why It Matters

Kimi K3 is the largest open model announced to date (~2.8T parameters).

## Risks

This preview reflects the supplied public evidence and does not imply evidence beyond the cited sources.

## Recommendation

Monitor the July 27 weight release for local feasibility studies. For immediate agentic tasks, utilize the API as it currently outperforms many proprietary US models in blind coding tests. Do not rely on vendor benchmark claims (BrowseComp/GPQA) without independent verification.

<details class="evidence-drawer" markdown="1">
<summary>Evidence, confidence, and open questions</summary>

Confidence: Mixed. High confidence in benchmark rankings from Artificial Analysis; low confidence in local hardware feasibility estimates due to undisclosed active parameter counts and unreleased weights.. 4 readable HTTP sources support this preview. Open questions remain with the upstream research workflow.

</details>

## Sources

- [Kimi K3 Intelligence, Performance and Price Analysis](https://artificialanalysis.ai/models/kimi-k3)
- [Kimi K3 is ranked 3rd on artificial analysis, only 2 points behind Sol](https://artificialanalysis.ai)
- [Kimi K3 beats GPT 5.6 Sol in agentic knowledge work](https://artificialanalysis.ai/evaluations/aa-briefcase#results-tabs)
- [Kimi K3: The Largest Open Model Ever, and Why Almost No One Can Run It Locally](https://vettedconsumer.com/kimi-k3-the-largest-open-model-ever-2-8t-params-and-why-almost-no-one-can-run-it-locally/)
