---
title: "Why Cloudflare Became a Neolab — Michelle Chen, Cloudflare"
date: 2026-11-28 09:12:08 +0700
section: Research Summary
section_slug: research-summary
description: "Cloudflare transitioned from a distributed CDN and developer platform provider to a \"Neolab\" to address architectural misalignments in serving large language models LLMs and to capitalize on the emerging \"System One\" inference paradigm."
audio: /audio/2026/11/why-cloudflare-became-a-neolab-michelle-chen-cloudflare.mp3
duration: "4 min 26 sec"
read_time: "4 min"
primary_source: https://www.youtube.com/watch?v=cYcYfM9Mvwo
youtube_id: cYcYfM9Mvwo
signal:
  - "Cloudflare transitioned from a distributed CDN and developer platform provider to a \"Neolab\" to address architectural misalignments in serving large language models LLMs and to capitalize on the emerging \"System One\" inference paradigm."
  - "This shift enabled the development and deployment of proprietary decision and extraction models Clef and Cleric designed to operate at the edge, reducing latency, token consumption, and cost while augmenting traditional autoregressive LLM workflows."
  - "Core Architecture: Globally distributed edge infrastructure data centers positioned near users , contrasting with centralized hyperscaler regions."
---
## Executive Summary
Cloudflare transitioned from a distributed CDN and developer platform provider to a "Neolab" to address architectural misalignments in serving large language models (LLMs) and to capitalize on the emerging "System One" inference paradigm. This shift enabled the development and deployment of proprietary decision and extraction models (`Clef` and `Cleric`) designed to operate at the edge, reducing latency, token consumption, and cost while augmenting traditional autoregressive LLM workflows.

## Infrastructure & Platform Evolution
* **Core Architecture:** Globally distributed edge infrastructure (data centers positioned near users), contrasting with centralized hyperscaler regions.
* **Compute Primitives:** 
  * `Workers` (2017): Serverless functions with millisecond startup; stateless execution.
  * `Durable Objects`: Stateful compute primitives.
  * `Containers` (2025): VM-like workloads for heavier requirements.
* **Storage Primitives:** `KV` (key-value), `R2` (object storage), `D1` (database). Enables full-stack application deployment.
* **AI Infrastructure History:** 
  * `Workers AI` (2023): Initial GPU deployment at the edge based on the hypothesis that models would shrink and network latency would dominate.
  * **Pivot (March 2026):** Models scaled to trillions of parameters (e.g., Kimi, GLM, DeepSeek), rendering the initial hypothesis obsolete. Cloudflare pivoted to host large models serverlessly to support the "Agent Cloud" narrative.

## System One Model Paradigm
* **Concept:** Contrasts with autoregressive "System Two" LLMs. System One models utilize a single forward pass to generate outputs, prioritizing speed, cost-efficiency, and deterministic decision-making over iterative token generation.
* **Catalyst:** TypeSafe's closed-source `Jev` model (September 2026) demonstrated the viability of System One architectures. Cloudflare's inability to host closed-source models necessitated internal development.
* **Strategic Shift:** Cloudflare adopted "Neolab" status to invent missing infrastructure components, mitigating closed-source dependency and regulatory risks while aligning with edge-native performance requirements.

## Proprietary Model Specifications
| Model | Type | Primary Function | Architecture/Behavior | Input/Output |
| :--- | :--- | :--- | :--- | :--- |
| **Clef** | Decision Model | Autonomous agent routing & action selection | Single forward pass; replaces iterative LLM reasoning traces | Structured/Unstructured context → Decision/Action flag |
| **Cleric** | Extraction Model | Data parsing & schema enforcement | Single forward pass; optimized for unstructured data ingestion | Unstructured text/images/logs → Perfectly typed JSON |

## Implementation Guidance & Workflow Integration
* **Tandem Operation:** System One models (`Clef`/`Cleric`) are designed to augment, not replace, System Two LLMs. They handle high-frequency, low-complexity tasks to reduce load on larger models.
* **Context Optimization:** `Cleric` extracts and structures data from raw inputs (e.g., CI logs, emails, support tickets), significantly shrinking context windows before downstream LLM processing.
* **Tool Pruning:** `Clef` (e.g., `Clef Flash`) can evaluate available toolsets and select only relevant subsets, reducing prompt size and computational overhead.
* **Demo Metrics (CI Triage Agent):**
  * **Traditional LLM Workflow:** 5 LLM calls, ~40,000 tokens, ~17.2s latency.
  * **System One Augmented Workflow:** 1 LLM call, ~1,800 tokens, ~9.2s latency.
  * **Efficiency Gains:** ~2x faster, 72% cost reduction, 94% token reduction.
* **Recommended Use Cases:** 
  * Agent routing & tool selection
  * Fraud/spam/phishing detection
  * Unstructured data extraction (web pages, tickets, logs)
  * High-concurrency, low-latency decision gates

## Risks & Constraints
* **Closed-Source Dependency:** Reliance on external System One models (e.g., `Jev`) poses regulatory and availability risks, directly motivating Cloudflare's internal training efforts.
* **Infrastructure Alignment:** Large models historically conflicted with Cloudflare's edge-native, low-latency architecture. System One models resolve this by returning to small, fast, distributed inference.
* **Workflow Complexity:** Integrating System One and System Two models requires careful orchestration to avoid context bloat and ensure deterministic handoffs between decision/extraction layers and reasoning layers.
* **Model Maturity:** `Cleric` and `Clef` represent new paradigms; operators should anticipate evolving capabilities and potential edge cases in unstructured data handling.

## Follow-Up Verification Points
* Verify current availability and API endpoints for `Clef` and `Cleric` on the Cloudflare developer platform.
* Assess compatibility of existing agent architectures with single-forward-pass inference constraints.
* Benchmark token/context savings in production workloads using `Cleric` for log/data extraction.
* Review Cloudflare's documentation on `Workers AI` GPU allocation and edge deployment limits for System One models.
* Monitor updates regarding `Cleric`'s early preview release and supported input modalities (text, image, structured/unstructured formats).

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Why Cloudflare Became a Neolab — Michelle Chen, Cloudflare](https://www.youtube.com/watch?v=cYcYfM9Mvwo)
