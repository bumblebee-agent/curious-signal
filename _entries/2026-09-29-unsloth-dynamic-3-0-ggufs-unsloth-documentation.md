---
title: "Unsloth Dynamic 3.0 GGUFs | Unsloth Documentation"
date: 2026-09-29 21:05:47 +0700
section: Research Summary
section_slug: research-summary
description: "Date Context: Updates referenced as of Sept 10, 2025; last updated 5 days ago. Primary Subject: Unsloth’s Dynamic quantization methods for GGUF models, specifically focusing on Dynamic v3.0 latest and Dynamic v2.0 legacy/standard ."
audio: /audio/2026/09/unsloth-dynamic-3-0-ggufs-unsloth-documentation.mp3
duration: "4 min 52 sec"
read_time: "5 min"
primary_source: https://unsloth.ai/docs/basics/dynamic-3.0-ggufs
signal:
  - "Date Context: Updates referenced as of Sept 10, 2025; last updated 5 days ago."
  - "Primary Subject: Unsloth’s Dynamic quantization methods for GGUF models, specifically focusing on Dynamic v3.0 latest a…"
  - "Unsloth Dynamic v3.0:"
---
**Source:** Unsloth Documentation (Basics/GGUFs)
**Date Context:** Updates referenced as of Sept 10, 2025; last updated 5 days ago.
**Primary Subject:** Unsloth’s Dynamic quantization methods for GGUF models, specifically focusing on **Dynamic v3.0** (latest) and **Dynamic v2.0** (legacy/standard).

## 1. Product Overview & Key Releases
*   **Unsloth Dynamic v3.0:**
    *   **Status:** Latest iteration, major improvement over v2.0.
    *   **Key Model:** **Qwen3.8-27B** Dynamic v3.0 GGUFs.
    *   **Performance Claim:** Delivers **&gt;10% top-1 better accuracy** at the same size compared to every other provider.
    *   **Compatibility:** Works with most inference engines including **llama.cpp** and **Unsloth Desktop**.
    *   **Quality Metrics:** Preserves more model quality with stronger results in **Divergence-300 @32** and **KL Divergence**.
    *   **Methodology:** Pure **post-training quantization (PTQ)**. No training on the imatrix calibration dataset. No **QAT** (Quantization-Aware Training) or **QAD** (Quantization-Aware Distillation).
    *   **Calibration:** Uses a high-quality **imatrix** calibration dataset refined for **agentic coding, chat, and multilingual performance**. The imatrix file is available for community use.

*   **Unsloth Dynamic v2.0:**
    *   **Status:** Established standard for future GGUF uploads.
    *   **Scope:** Works on **all models** (including MoE and non-MoE), whereas previous versions were effective only for MoE architectures.
    *   **Methodology:** Revamped layer selection; dynamically adjusts quantization type for every layer/model combination.
    *   **Calibration:** Dataset contains &gt;1.5M tokens, hand-curated for conversational chat performance.
    *   **Formats:** Adds **Q4_NL, Q5.1, Q5.0, Q4.1, Q4.0** for efficiency on Apple Silicon/ARM.

## 2. Quantization Variants & Specifications (v3.0 Focus)
*   **UD-Q2_K_XL (8.37GB):**
    *   Accuracy: ~+8% more accurate on top-1 than next best.
    *   Capability: Successfully generated working HTML program (with 1 small JS bug).
    *   Note: MTP module removed to save space.
*   **UD-IQ1_S (6.2GB):**
    *   Accuracy: Retains ~72% top-1 accuracy.
    *   Size: 89% smaller than base.
    *   Note: MTP module removed.
*   **MTP Module:**
    *   Removed from smaller quants under `UD-Q2_K_XL` (8.37GB and lower) to conserve ~500MB disk space.
    *   `Q4_0` MTP separate module available if needed.

## 3. Evaluation Metrics & Benchmarks
*   **KL Divergence (KLD):**
    *   Preferred metric over perplexity or top-1 accuracy alone.
    *   Rationale: Perplexity can cancel out errors; top-1 is an argmax on single prediction. KLD measures trajectory similarity over multiple tokens.
    *   Goal: Reduce mean KLD while minimizing disk space increase.
*   **Divergence-300 @32:**
    *   Dataset: 300 held-out examples from Terminal-Bench 2.1, DeepSWE, Harbor, MathArena 2025-26, non-Latin/long-doc prompts.
    *   Method: Greedy argmax decoding for 32 tokens. Compares BF16 vs. all quants/providers.
    *   Purpose: Gauges overfitting and actual inference workload performance.
*   **MMLU 5-Shot:**
    *   Unsloth built an internal evaluation framework to replicate official scores, addressing subtle implementation issues in other harnesses (e.g., tokenization of "A" vs "_A", prompt templates).
    *   **Gemma 3 (27B) Comparison:** Unsloth Dynamic 4-bit (Q4_K_XL) is **2GB smaller** than Google’s QAT version with **+1% extra accuracy**.
    *   **Efficiency Metric:** Defined as `(MMLU 5 shot score - 25) / Disk Space GB`. Minus 25 accounts for random chance baseline.

## 4. Critical Usage Constraints & Risks
*   **1-bit Quantization (e.g., UD-IQ1_S, UD-IQ2_S):**
    *   **Warning:** **Should not be used for agentic use-cases.**
    *   **Performance Drop:** Sharp drop in Divergence-300 @32 accuracy (from ~25% for Q2_K_XL to &lt;8-10% for IQ2_S).
    *   **Tool Calling:** Fails to call tools, loops excessively, or outputs empty responses. Only general knowledge is retained.
    *   **Mitigations (if used):**
        1.  Set `presence_penalty = 1.5` (or higher) to prevent excessive looping.
        2.  Enable "thinking" mode (even low reasoning) to prevent empty responses.
        3.  Restrict to short general knowledge fact questions.
*   **Overfitting Controls:**
    *   Unsloth does not use its own chat-optimized calibration dataset for KLD benchmarking to avoid domain bias.
    *   Tests use standard Wikipedia datasets or unseen datasets (DeepSWE, Terminal Bench) to ensure fair comparison against baseline imatrix approaches.

## 5. Infrastructure & Bug Fixes
*   **Llama 4 Support:**
    *   Unsloth contributed fixes to **llama.cpp** and **transformers** for Llama 4 Scout/Maverick:
        *   Resolved RoPE Scaling configuration changes.
        *   Fixed QK Norm epsilon (changed from 1e-06 to **1e-05** per config).
        *   Addressed QK Norm sharing across heads (fixed in vLLM as well).
    *   Impact: MMLU Pro accuracy increased from 68.58% to 71.53% after fixes.
*   **Inference Engines:**
    *   GGUFs are compatible with **llama.cpp**, **Unsloth Desktop**, and **Unsloth Studio**.

## 6. Implementation Notes for Operators
*   **Calibration Data:** The imatrix file used for v3.0 is public. Researchers/developers are encouraged to create variations/fine-tunes using Unsloth quants/imatrix.
*   **Benchmarking Fairness:** Disk space calculations for benchmarks remove the MTP head to ensure fair comparison with other providers.
*   **Model Specificity:** Quantization schemes are model-specific (e.g., Gemma 3 layers differ from L

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Unsloth Dynamic 3.0 GGUFs | Unsloth Documentation](https://unsloth.ai/docs/basics/dynamic-3.0-ggufs)
