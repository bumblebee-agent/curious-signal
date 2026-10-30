---
title: "Meet All-New Kling 4.0!"
date: 2026-10-17 09:28:57 +0700
section: Research Summary
section_slug: research-summary
description: "Kling says 4.0 became available to everyone on October 15, emphasizing more realistic video, stronger reference control, synchronized audio, and longer narrative sequences."
audio: /audio/2026/10/meet-all-new-kling-4-0.mp3
duration: "3 min 55 sec"
read_time: "3 min"
primary_source: https://kling.ai/release-note/release-notes/Kling_4?type=dialog
signal:
  - "Kling says 4.0 became available to everyone on October 15, emphasizing more realistic video, stronger reference control…"
  - "These are vendor claims; the supplied announcement contains no independent benchmarks."
  - "Generation: text-to-video, image-to-video, first/last frames, Omni Reference, and up to 10 keyframe images."
---
## Kling 4.0 — announcement summary

Kling says **4.0 became available to everyone on October 15**, emphasizing more realistic video, stronger reference control, synchronized audio, and longer narrative sequences. These are vendor claims; the supplied announcement contains no independent benchmarks.

### Core capabilities
- **Generation:** text-to-video, image-to-video, first/last frames, Omni Reference, and up to **10 keyframe images**.
- **Output:** **3–30 seconds**, **720p / 1080p / 4K**; aspect ratios **21:9 / 16:9 / 1:1 / 9:16 / Auto**; two-channel stereo.
- **Prompts:** up to **8,000 tokens**.
- **References:** up to **10 images**, **5 videos totaling up to 30 seconds**, and **7 elements**, including up to **3 video-based elements**. The combined cap is **15 items across images, videos, voice references, and elements**; individual maxima are not additive. Reference audio is **voice reference only**, and video elements count toward the video-duration allowance.
- **Editing inputs:** up to **5 clips**, including **1 primary video**; each clip must be **3–30 seconds**, with all clips totaling no more than **30 seconds**.

### Notable creative controls
Video references can guide performance, action, camera motion, and pacing; **white-model and depth-map videos** are supported. Image references can specify characters, layouts, styles, graphics, composition, and story beats. Targeted editing covers expressions, movement, cameras, backgrounds, style, and character replacement or removal while claiming to preserve the rest of the scene.

The announcement also claims improved motion stability, lip-sync, subtle facial expression, character consistency, and text legibility during camera movement. Language and text support includes Chinese, English, Japanese, Korean, Spanish, Portuguese, German, French, and Hindi, with additional languages, accents, dialects, and emoji support.

### Kling 4.0 Flash
A speed/value-oriented variant supporting text-to-video, first-frame image-to-video, and Omni Reference:
- **3–20 seconds**
- **720p**
- **8-bit SDR**

No measured generation times or pricing are supplied.

### Availability caveats
- **10-bit HDR at 1080p and 4K is “coming soon,”** despite appearing in the main specifications table.
- Repeated video extension to **up to 2 minutes** is also **coming soon**, not the current single-generation limit.

### Workflow and operator relevance
The redesigned interface combines reference inputs, grid/list views, timeline editing, and a node-based canvas with an Agent that can use tools and perform tasks. **MCP and CLI support are announced for Kling 4.0**, including Omni Reference and keyframe generation.

**Read-only follow-up:** compare the documented MCP/CLI contract, authentication, pricing, quotas, asset-handling terms, and actual feature availability against existing Media Studio/KIE capabilities. The announcement does not establish local runtime compatibility or an existing Flight Deck integration.

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Meet All-New Kling 4.0!](https://kling.ai/release-note/release-notes/Kling_4?type=dialog)
