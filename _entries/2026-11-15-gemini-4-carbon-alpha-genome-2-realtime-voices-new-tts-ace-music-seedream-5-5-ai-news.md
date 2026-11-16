---
title: "Gemini 4 Carbon, Alpha Genome 2, realtime voices, new TTS, ACE Music, Seedream 5.5: AI NEWS"
date: 2026-11-15 10:49:29 +0700
section: Research Summary
section_slug: research-summary
description: "Source Context: Video transcript summarizing recent releases in AI models, open-source tools, robotics, and scientific AI."
audio: /audio/2026/11/gemini-4-carbon-alpha-genome-2-realtime-voices-new-tts-ace-music-seedream-5-5-ai-news.mp3
duration: "6 min 30 sec"
read_time: "8 min"
primary_source: https://www.youtube.com/watch?v=woWo80dPkVk
youtube_id: woWo80dPkVk
signal:
  - "Source Context: Video transcript summarizing recent releases in AI models, open-source tools, robotics, and scientific…"
  - "Operator Note: This summary preserves technical specifications, licensing, and setup constraints for review purposes on…"
  - "No authorization is granted to execute any commands or deploy software mentioned."
---
**Source Context:** Video transcript summarizing recent releases in AI models, open-source tools, robotics, and scientific AI.
**Operator Note:** This summary preserves technical specifications, licensing, and setup constraints for review purposes only. No authorization is granted to execute any commands or deploy software mentioned.

---

## 1. Generative AI: Text, Code, & Multimodal Models

### **Google Gemini 4 Carbon**
*   **Role:** Frontier multimodal model (text, image, video, audio, document).
*   **Key Metrics & Benchmarks:**
    *   Ranked #2 in Artificial Analysis Intelligence Index (behind Claude Fable, above GPT6 Astra).
    *   Ranked #1 in Vending Bench (business automation simulation) and Blueprint Bench (real estate floor plans).
    *   Ranked #3 in MazeBench and ClockBench.
    *   Ranked #1 in Agents Last Exam (when used with the "anti-gravity" harness).
    *   Software Engineering: Ranked #3 (tied with top tier).
    *   **Cost:** Cheaper than Claude Opus/Fable (2-5x less expensive).
    *   **Speed:** Faster than Claude Fable 5.2; reported as slower than GPT models in this review.
*   **Performance Observations:**
    *   Struggled with complex creative coding tasks (explainer animation, procedural Unreal Engine game).
    *   Multimodal capabilities (image/video/audio understanding) are strong.
    *   Passed the "finding the frog" test (visual identification); failed cancer diagnosis test (1/6 correct).
*   **Access Constraints:** Available only to Google "Ultra" subscribers (~$100+/month).
*   **Recommended Harness:** "Anti-gravity" (allows multi-agent workflows, local file access). Note: Usage stats/token tracking via slash commands is non-functional in current version.

### **Google Gemini 4 Hydrogen**
*   **Role:** Smaller, faster, efficient model for everyday tasks.
*   **Capabilities:**
    *   Context window: Up to 1 million tokens.
    *   Multimodal: Text, images, audio, video.
    *   Demonstrated ability to create interactive 3D worlds, e-commerce sites with 3D viz, and animate spreadsheets via code/formulas.
    *   Beats competing models in its class on coding, knowledge work, and reasoning benchmarks.
*   **Access:** Available via Gemini App and Google Search for all users, including free tier.

### **Google Gemini Decision 1**
*   **Role:** Multimodal decision-making model.
*   **Function:** Optimized for quick yes/no or multiple-choice decisions rather than long-form generation. Returns answers with confidence scores.
*   **Use Cases:** Agent tool selection, high-volume data classification (e.g., spam detection).
*   **Performance:** Outperforms "Jev" and other similar models on average benchmarks.
*   **Access:** Available via Gemini API (includes free tier).

### **Meta Muse Ember**
*   **Role:** Lightweight multimodal model.
*   **Capabilities:** Text, images, documents. Optimized for speed and cost efficiency, not deep reasoning.
*   **Use Cases:** Document inspection, code review, bulk image classification.
*   **Performance:** More efficient than equivalent-class models from Claude and GPT; outperforms competitors in Agentic Work, coding, and multimodal benchmarks.
*   **Access:** API or "Muse Code" agentic harness. Not open-sourced.

### **Baidu Ernie 5.5 Flash Preview**
*   **Role:** Language model.
*   **Architecture:** 280 billion total parameters; **14 billion active parameters** (MoE architecture implied).
*   **Capabilities:** Autonomously codes playable games from design docs, builds detailed 3D environments (Blender), creates complete videos from single prompts.
*   **Benchmarks:** Competitive with leading open models in agentic coding, knowledge work, and reasoning.
*   **Access:** Currently via API. Weights planned for Apache 2 release soon.

---

## 2. Open-Source Local Tools & Repositories

### **Budget 3D**
*   **Role:** Single-image to 3D object generation with compute control.
*   **Architecture:** Identifies less important regions (empty space) to use fewer tokens, allocating more compute to important details.
*   **Versions:**
    *   **Budget 3D Idle:** Prioritizes quality.
    *   **Budget 3D Idle Turbo:** Uses only 5 generation steps for speed.
*   **Performance:** Up to ~2x faster than standard models; reduced GPU memory usage.
*   **Licensing:** Apache 2.0.
*   **Setup:** Code and instructions available via GitHub repository.

### **Reshoot 4D**
*   **Role:** Video camera angle transformation.
*   **Workflow:**
    1.  Reconstructs person/scene in 3D over time.
    2.  Virtual camera editor for new paths (circle, zoom, perspective).
    3.  AI video model (e.g., LTX) generates new footage.
*   **Controls:** Camera focus, aperture, lens effects.
*   **Licensing:** Open source.
*   **Setup:** Code and instructions available via GitHub repository.

### **Splat Anything**
*   **Role:** Multi-photo to 3D Gaussian Splat reconstruction.
*   **Capabilities:** Works across scene sizes (small objects to aerial landscapes); supports multiple cameras and 360° panoramas.
*   **Model Size:** ~11 GB on Hugging Face.
*   **Hardware Constraint:** Fits comfortably in most consumer GPUs.
*   **Licensing:** Open source.
*   **Setup:** Code and instructions available via GitHub/Hugging Face.

### **IC (In-Context Learning) for OpenH3 Regenerate**
*   **Role:** Video upscaler (2K/4K) based on Miniax H3.
*   **Improvement:** Fixes detail degradation (faces, fine textures) present in previous versions using In-Context Learning.
*   **Licensing:** Open source.
*   **Setup:** Code and instructions available via GitHub repository.

### **Haru 4B**
*   **Role:** Open real-time voice model.
*   **Capabilities:**
    *   Full duplex (listens and speaks simultaneously).
    *   Direct voice-to-voice processing (reduces latency, preserves emotion/tone).
    *   Emotion detection and responsive acknowledgments.
    *   Zero-shot voice cloning.
*   **Hardware Constraint:** Requires ~12 GB VRAM. Apple Silicon implementation provided.
*   **Licensing:** Apache 2.0 (Commercial use permitted).
*   **Setup:** Code and weights available via GitHub.

### **Zonos 3 Mini (by Zyra)**
*   **Role:** Text-to-Speech (TTS).
*   **Architecture:** 800 million total parameters; **100 million active parameters**.
*   **Size:** ~1.8 GB.
*   **Hardware Constraint:** Compatible with Nvidia GPUs, Apple Silicon, or CPU. Suitable for edge devices.
*   **Controls:** Accent, age, emotion, delivery.
*   **Licensing:** Apache 2.0 (implied by "released code and models").
*   **Setup:** Code and weights available via GitHub.

### **Sofon Real Time**
*   **Role:** Full duplex conversational voice model.
*   **Capabilities:**
    *   Detects tone, emotions, laughter, and word stress.
    *   Zero-shot voice cloning.
*   **Model Variants:**
    *   **Subtle/Expressive:** Adds metatags, more expressive.
    *   **Flash:** Optimized for speed and scale.
    *   **ETE:** Supports zero-shot cloning.
    *   **Non-Cloning Version:** Available.
*   **Licensing:** Apache 2.0.
*   **Setup:** Models released; check repository for specific variant codes.

### **Lingbot Touch**
*   **Role:** Robotics tactile sensor interpretation.
*   **Function:** Unified representation for different robotic hand sensors (pressure, contact, movement).
*   **Training Data:** ~5,000 hours of tactile recordings.
*   **Model Sizes:**
    *   Tiny: 21.9 MB.
    *   Small: 87.1 MB.
*   **Licensing:** Apache 2.0.
*   **Setup:** Code and models available via GitHub/Hugging Face.

### **Flash Aloha**
*   **Role:** Robotics learning from human demonstration.
*   **Hardware:** Two-armed robot.
*   **Method:** Physical guidance (kinesthetic teaching) rather than joystick control.
*   **Performance:** &gt;80% success rate on complex tasks (tossing/catching, folding, inserting batteries) with only **50 human demonstrations** per task.
*   **Technique:** AI reproduces movements; smoothing algorithm prevents jerky actions.
*   **Licensing:** MIT.
*   **Setup:** Code available via GitHub for training and running.

### **Iris Z**
*   **Role:** Image generation with simultaneous depth map estimation.
*   **Capabilities:** Generates image + depth map; supports image-to-depth and depth-to-image.
*   **Architecture:** Single unified model for appearance and depth.
*   **Model Sizes:**
    *   Small: 18 GB (Consumer GPU compatible).
    *   Big: 64 GB (High-end hardware required).
*   **Licensing:** Open source.
*   **Setup:** Weights and inference code available via GitHub/Hugging Face.

### **Pan 2**
*   **Role:** World model for physical simulation.
*   **Capabilities:** Predicts physical changes in scenes; generates video based on image + action prompt. Useful for robot training simulation data.
*   **Limitation:** Max clip length of 20 seconds.
*   **Model Size:** ~86 GB.
*   **Licensing:** Apache 2.0.
*   **Setup:** Model available on Hugging Face.

### **Pith3**
*   **Role:** Modified Miniax H3 video generator.
*   **Optimization:** Reduced diffusion steps to 2-4; removed final video decoding process.
*   **Performance:** 5-second 768p video in 3.8 seconds (on B200 GPU); &gt;2x faster than "Soul H3".
*   **Setup:** Demo on Hugging Face. Weights/code promised for "next week."

### **Pix Vid**
*   **Role:** Video generation in pixel space (skips VAE compression).
*   **Advantages:** Higher resolution (2x), precise control, frame-by-frame response to new commands.
*   **Setup:** Code and weights promised as "coming soon."

### **Ace Music V1**
*   **Role:** Music generation from text/lyrics.
*   **Capabilities:** Controls performance style (hum, raspy voice). Beats Suno on leaderboards.
*   **Platform:** Ace Studio (includes vocal/instrument separation, MIDI conversion).
*   **Future:** "Ace Music Flash" planned for open-source release later this year.
*   **Access:** Website/API.

### **Fish Audio Live 3**
*   **Role:** Real-time voice agent.
*   **Capabilities:** Full duplex, interruption support, emotional acknowledgment.
*   **Status:** API only. Weights not yet released (past history of open-sourcing suggests potential future release).

---

## 3. Scientific

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Gemini 4 Carbon, Alpha Genome 2, realtime voices, new TTS, ACE Music, Seedream 5.5: AI NEWS](https://www.youtube.com/watch?v=woWo80dPkVk)
