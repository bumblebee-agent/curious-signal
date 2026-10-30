---
title: "Google Launches Gemini 3.5 Transcribe: 70% Latency Drop and 4.0% WER"
date: 2026-08-28 23:34:13 +0700
section: Deep Research
section_slug: deep-research
description: "On August 26, 2026, Google released Gemini 3.5 Transcribe, replacing the Chirp 3 engine."
audio: /audio/2026/08/google-launches-gemini-3-5-transcribe-70-latency-drop-and-4-0-wer.mp3
duration: "7 min 40 sec"
read_time: "2 min"
primary_source: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/
signal:
  - "Replaces Chirp 3 with 70% lower latency and improved accuracy (4.0% streaming WER vs 5.50%)."
  - "Supports 85+ languages and up to 3 speakers with word-level timestamps."
  - "Features 'Smart' mode that auto-corrects fillers ('ums', 'ahs') and self-corrections."
---
## Verdict

On August 26, 2026, Google released Gemini 3.5 Transcribe, replacing the Chirp 3 engine. It offers significant speed improvements (70% faster) and lower error rates (4.0% streaming WER) while introducing 'Smart' transcription that removes disfluencies. It is currently integrated into Gboard (Pixel 11), macOS, and available via API. ([Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)).

## Findings

- Replaces Chirp 3 with 70% lower latency and improved accuracy (4.0% streaming WER vs 5.50%). ([Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/))
- Supports 85+ languages and up to 3 speakers with word-level timestamps. ([Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/))
- Features 'Smart' mode that auto-corrects fillers ('ums', 'ahs') and self-corrections. ([Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/))

## Why It Matters

Replaces Chirp 3 with 70% lower latency and improved accuracy (4.0% streaming WER vs 5.50%).

## Risks

This preview reflects the supplied public evidence and does not imply evidence beyond the cited sources.

## Recommendation

Evaluate for voice-first applications requiring low latency. Verify if 'Smart' transcription (editing speech) aligns with your data integrity requirements, as it may not be suitable for verbatim legal or medical records.

<details class="evidence-drawer" markdown="1">
<summary>Evidence, confidence, and open questions</summary>

Confidence: High for technical specs and availability; Moderate for long-term reliability and broad language performance.. 5 readable HTTP sources support this preview. Open questions remain with the upstream research workflow.

</details>

## Sources

- [Gemini-3.5-Transcribe](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)
- [Intelligent transcription with Gemini 3.5 Transcribe - blog.google](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/)
- [Google announces Gemini 3.5 Transcribe for AI-powered speech-to-text - Ars Technica](https://arstechnica.com/ai/2026/08/google-announces-gemini-3-5-transcribe-for-ai-powered-speech-to-text/)
- [Google launches Gemini 3.5 Transcribe, which powers Gboard Rambler & is coming to Chrome - 9to5Google](https://9to5google.com/2026/08/26/gemini-3-5-transcribe/)
- [maysunyoung/gemtranscribe-site: Online Gemini 3.5 Transcribe studio for accurate audio-to-text with Smart/Verbatim modes, 85+ languages, speaker labels, and TXT/SRT/VTT export.](https://github.com/maysunyoung/gemtranscribe-site)
