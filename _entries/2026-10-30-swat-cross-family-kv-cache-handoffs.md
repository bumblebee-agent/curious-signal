---
title: "SwaT: cross-family KV-cache handoffs"
date: 2026-10-30 10:57:32 +0700
section: Research Summary
section_slug: research-summary
description: "Bottom line: SwaT Swarm Telepathy trains a mapper that translates one LLM’s KV-cache into another model’s cache format, avoiding receiver prefill of the transferred document."
audio: /audio/2026/10/swat-cross-family-kv-cache-handoffs.mp3
duration: "4 min 54 sec"
read_time: "4 min"
primary_source: https://arxiv.org/pdf/2610.15095
signal:
  - "Bottom line: SwaT Swarm Telepathy trains a mapper that translates one LLM’s KV-cache into another model’s cache format,…"
  - "Combined with Attention Matching AM compaction, it reports better task scores and faster communication than text summar…"
  - "This is a pair-specific research method—not a universal cache interchange protocol."
---
## SwaT: cross-family KV-cache handoffs

**Bottom line:** SwaT (Swarm Telepathy) trains a mapper that translates one LLM’s KV-cache into another model’s cache format, avoiding receiver prefill of the transferred document. Combined with Attention Matching (AM) compaction, it reports better task scores and faster communication than text summaries. This is a pair-specific research method—not a universal cache interchange protocol.

**Source:** Supplied paper by MIT CSAIL and MIT–IBM researchers. \[Project repository\](https://github.com/Ar-Kareem/SwaT); repository contents were not independently verified.

### How it works
- Sender and receiver models remain **frozen**; only an approximately **300M-parameter transformer mapper** is trained.
- Sender and receiver layers are divided into contiguous groups. Each mapper block uses causal self-attention, causal cross-attention over a sender-layer group, and a GELU feed-forward network to predict a receiver-layer group’s keys and values.
- Sender RoPE is removed before mapping. Predicted caches receive per-layer/head RMS calibration and receiver RoPE.
- Different tokenizers are aligned through **character spans**, fractional cross-attention positions, and causal masks, preserving both native tokenizations rather than dropping unmatched tokens.
- **“Prefill-free” is qualified:** the receiver skips document prefill, but the mapper still requires the document’s receiver-tokenized embeddings. The implementation requires sender text to remain available; a subsequent receiver query is still processed.
- For sliding-window sender layers, the method retains all historical KV entries without changing their attention behavior—an important storage consideration.

### Training requirements
Each sender–receiver pair needs its own mapper. Reported settings:
- `B ∈ {7,8,9}`, `D = 1024`, `H = 16`, `F = 4096`; bf16.
- Two stages: **5,000 steps** of RMS-normalized cache-reconstruction MSE, then **24,000 steps** of downstream next-token loss through the frozen receiver.
- **44M unique English-text tokens**; claimed training cost **&lt;1 GPU-day**. The supplied text does not establish Mac support or local memory requirements.
- Ablations show large losses when either training stage is omitted.

### Reported evidence
- **17 text benchmarks**, **10 cross-family pairs**, **12 models**, **6 families**, spanning **3B–32B parameters**.
- Mean receiver-performance retention ranges approximately **92%–143%** across pairs. These are ratios against the receiver’s own performance—not absolute accuracy—and individual tasks can regress substantially.
- **SwaT+AM versus text summaries:** across three pairs, seven datasets, and five approximately matched cache budgets, pooled arithmetic task score rises **41.3 → 58.6 (+17.4 points)**. Reported geometric-mean sender GPU time improves **4.2×**, and receiver time-to-first-token **4.3×**.
- Budgets match receiver cache-token counts, **not transmitted byte sizes**; the headline speedup should not be read as demonstrated network-transfer performance.
- English-only training nevertheless supports Chinese knowledge transfer: Qwen3-4B → Llama3-8B raises CMMLU accuracy **51.2% → 65.1%**, versus the sender’s **69.7%**.
- Vision transfer improves several VQA results, but is **not full vision transfer**. On detail-heavy DocVQA/InfoVQA, it trails sender VLMs substantially and can also lose to text communication.

### Limits and operator relevance
- Directed pair-specific mapping scales as **n(n−1)**; repeated handoffs and multi-message composition remain unresolved.
- Caches may carry information not explicit in visible text, complicating auditing and safety monitoring.
- Potential applications include agent handoffs, model switching, and routing without repeated document prefill.

**Read-only next checks:** inspect mapper/checkpoint availability, runtime cache-access requirements, benchmark hardware and timing boundaries, licensing, and compatibility with Bumblebee’s model formats before assessing integration feasibility.

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [arxiv.org](https://arxiv.org/pdf/2610.15095)
