---
title: "ChatGPT Work and the New Desktop Center"
date: 2026-07-10 08:34:00 +0700
section: Deep Research
section_slug: deep-research
description: "A deeper look at OpenAI's unified desktop direction, the Work and Codex modes, migration friction, source confidence, and open questions."
read_time: "7 min"
primary_source: https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex
signal:
  - "OpenAI is consolidating Chat, Work, and Codex into a desktop-centered workflow."
  - "The split between the new app and ChatGPT Classic reduces migration risk but creates short-term product confusion."
  - "The largest unanswered question is how consistently conversations and files move between cloud, desktop, and mobile surfaces."
---
## Verdict

The meaningful change is not another model picker. OpenAI is trying to make one desktop application the center of general conversation, research deliverables, and technical work. The [ChatGPT Work and Codex guide](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex) defines the three modes, while the [desktop migration guide](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app) explains how the new app relates to existing installations.

## What Changed

- **Chat** remains the general conversational mode.
- **Work** is aimed at research and finished deliverables.
- **Codex** remains the technical and coding environment.
- Codex users move to the unified application through an update.
- ChatGPT Classic remains available as a separate, more conservative option for supported enterprise workflows.

The rollout arrived alongside GPT-5.6, with reporting that the timing was staggered after coordination with the U.S. government ([Axios](https://www.axios.com/2026/07/09/ai-openai-gpt-release)).

## Why It Matters

This is a desktop-first product strategy. OpenAI can push agent features forward in the unified app while leaving a more stable path for organizations that are not ready to change deployment or compliance assumptions.

For users, the upside is less context switching between conversation, research, and coding. The risk is that “unified” describes the interface before it describes the underlying data model.

## Risks

- **Synchronization gaps:** Cloud Work conversations may not appear everywhere at launch ([OpenAI Help](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app)).
- **Migration confusion:** Users may have both the new app and ChatGPT Classic installed.
- **Mode ambiguity:** The boundary between a sophisticated Chat request and a Work task is not yet obvious.
- **Enterprise uncertainty:** Organizations need to confirm which app, storage behavior, and feature set satisfy their policies.

## Recommendation

Individual users can update and test the unified application, but should verify where each conversation and file is stored before relying on cross-device continuity. Enterprise teams should treat the new app as a separate deployment decision rather than an automatic replacement for ChatGPT Classic.

<details class="evidence-drawer" markdown="1">
<summary>Evidence, confidence, and open questions</summary>

### Confidence

Confidence is medium. The help documentation is useful for product shape and migration behavior, while broader reporting adds rollout context. Community discussion was limited when this brief was assembled, so there is not yet a strong independent picture of day-to-day reliability.

### Open Questions

- When will Work conversations synchronize consistently across desktop, cloud, and mobile?
- Which capabilities belong uniquely to Work rather than an advanced Chat session?
- How will enterprise deployment and support differ between the unified app and ChatGPT Classic?
- Will the desktop-centered design replace browser workflows or simply add another surface?

</details>

## Sources

- [OpenAI Help: ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)
- [OpenAI Help: Moving to the new ChatGPT desktop app](https://help.openai.com/en/articles/20001276-moving-to-the-new-chatgpt-desktop-app)
- [Axios: OpenAI releases GPT-5.6 and ChatGPT Work](https://www.axios.com/2026/07/09/ai-openai-gpt-release)
