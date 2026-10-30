---
title: "OpenAI Claims Jalapeño ASIC Outperforms Nvidia GB200/GB300 in Efficiency and Latency"
date: 2026-08-29 02:24:47 +0700
section: Deep Research
section_slug: deep-research
description: "OpenAI released initial benchmarks for Jalapeño, its first custom inference chip co-developed with Broadcom."
audio: /audio/2026/08/openai-claims-jalape-o-asic-outperforms-nvidia-gb200-gb300-in-efficiency-and-latency.mp3
duration: "5 min 52 sec"
read_time: "2 min"
primary_source: https://openai.com/index/jalapeno-first-results/
signal:
  - "Jalapeño achieves 1.5–1.9x more AI work per watt and 1.7–3.6x lower end-to-end latency than Nvidia GB200/GB300."
  - "The chip is a 700W ASIC optimized for both prefill and decode phases, using HBM4 memory."
  - "Benchmarks were conducted on GPT-OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T using the InferenceX suite."
---
## Verdict

OpenAI released initial benchmarks for Jalapeño, its first custom inference chip co-developed with Broadcom. The chip claims 1.5–1.9x higher throughput per watt and 1.7–3.6x lower latency than Nvidia’s Blackwell systems (GB200/GB300) on the InferenceX benchmark. While the metrics are significant, they are vendor-reported, unverified by independent third parties, and specific to OpenAI’s internal workload patterns. Deployment is targeted for late 2026. ([https://openai.com/index/jalapeno-first-results/](https://openai.com/index/jalapeno-first-results/)).

## Findings

- Jalapeño achieves 1.5–1.9x more AI work per watt and 1.7–3.6x lower end-to-end latency than Nvidia GB200/GB300. ([https://openai.com/index/jalapeno-first-results/](https://openai.com/index/jalapeno-first-results/))
- The chip is a 700W ASIC optimized for both prefill and decode phases, using HBM4 memory. ([https://openai.com/index/jalapeno-first-results/](https://openai.com/index/jalapeno-first-results/))
- Benchmarks were conducted on GPT-OSS 120B, DeepSeek R1 670B, and Kimi K2.5 1T using the InferenceX suite. ([https://openai.com/index/jalapeno-first-results/](https://openai.com/index/jalapeno-first-results/))

## Why It Matters

Jalapeño achieves 1.5–1.9x more AI work per watt and 1.7–3.6x lower end-to-end latency than Nvidia GB200/GB300.

## Risks

This preview reflects the supplied public evidence and does not imply evidence beyond the cited sources.

## Recommendation

Monitor for independent replication of InferenceX benchmarks. Treat current claims as strong directional indicators of OpenAI’s hardware strategy rather than finalized industry standards. Watch for supply chain impacts on HBM4 availability.

<details class="evidence-drawer" markdown="1">
<summary>Evidence, confidence, and open questions</summary>

Confidence: Mixed. The source data is from OpenAI (self-reported) and lacks independent corroboration. Community reaction is present but limited to summary discussions rather than technical critique.. 7 readable HTTP sources support this preview. Open questions remain with the upstream research workflow.

</details>

## Sources

- [https://openai.com/index/jalapeno-first-results/](https://openai.com/index/jalapeno-first-results/)
- [This week: OpenAI's Jalapeño inference chip, Nvidia's ~$12.9B move for Hugging Face, and Alibaba's Qwen3.8-Flash — the cost and control of AI both shifted](https://www.reddit.com/r/artificial/comments/1w0wf8z/this_week_openais_jalape%C3%B1o_inference_chip_nvidias/)
- [OpenAI’s Jalapeno chip outperformed the GB300 on power and speed, according to OpenAI - The Next Web](https://thenextweb.com/news/openai-jalapeno-benchmark-nvidia-gb300-europe-gigafactories)
- [Jalapeño’s first results show industry-leading speed and efficiency in AI inference - OpenAI](https://openai.com/index/jalapeno-first-results/)
- [OpenAI's 700W Jalapeño ASIC outpaces 1,400W Nvidia flagship GPU](https://www.tomshardware.com/tech-industry/semiconductors/openai-says-its-jalapeno-chip-beats-nvidias-gb300-in-first-published-benchmarks)
- [Jalapeño Is OpenAI’s First Custom Chip: It Claims to Beat Nvidia With 1.9x More Efficiency - Gadget Review](https://www.gadgetreview.com/jalapeno-is-openais-first-custom-chip-it-claims-to-beat-nvidia-with-1-9x-more-efficiency)
- [OpenAI’s Jalapeño Chip Delivers Faster, Cheaper AI Inference - TUN - The University Network](https://www.tun.com/home/openais-jalapeno-chip-delivers-faster-cheaper-ai-inference/)
