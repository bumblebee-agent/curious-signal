---
title: "Building agents: When to fold subagents into your main agent loop"
date: 2026-10-26 21:33:54 +0700
section: Research Summary
section_slug: research-summary
description: "The article argues that routers, planners, and tightly coupled domain subagents often work better as skills and tools within one agent loop."
audio: /audio/2026/10/building-agents-when-to-fold-subagents-into-your-main-agent-loop.mp3
duration: "4 min 21 sec"
read_time: "4 min"
primary_source: https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop
signal:
  - "The article argues that routers, planners, and tightly coupled domain subagents often work better as skills and tools w…"
  - "Keep subagents where measurable context limits, independent parallel work, tool-selection difficulties, or conflicting…"
  - "One model, one context window, with an open-ended tool loop bounded by turn/cost budgets and write gates."
---
## Main takeaway

The article argues that **routers, planners, and tightly coupled domain subagents often work better as skills and tools within one agent loop**. Keep subagents where measurable context limits, independent parallel work, tool-selection difficulties, or conflicting instructions justify them—not simply to mirror team ownership.

### Proposed architecture
- **One model, one context window**, with an open-ended tool loop bounded by turn/cost budgets and write gates.
- The same model plans, executes, and revises its plan; the harness executes tool-call batches in parallel and returns raw results.
- **Skills:** domain procedures, ordering, rules, and judgment.
- **Tools:** live data, actions, fixed-shape results, validation, approval gates, permissions, and mechanical processing.
- **Knowledge bases:** intermittently needed reference material accessed through lookup/search or skill reference files.
- Progressively disclose skills and tools instead of loading everything into the system prompt.

### Evidence and limitations
Anthropic reports that a single agent with skills frequently beat both monolithic prompts and subagent designs across several enterprise deployments on quality, often with lower cost and latency. One customer observed roughly **2× faster runtime**. These are reported deployment observations, not a universal benchmark.

Multi-agent risks include lossy handoffs, overlapping specialists, conflicting prompts, fragmented evaluations, inconsistent voice, and nested-loop latency. A single loop still requires disciplined context management, memory, note-taking, and well-triggered skill/tool descriptions.

### Migration guidance
1. Establish shared end-to-end evaluations; **10 golden examples** can be a starting point.
2. Prioritize frequently used specialists that share data, chain outputs, or commonly run together.
3. Fold in **one subagent at a time**, translating prompts into skills and API interactions into tools.
4. Compare individual task regressions—not just aggregate scores—and repeat cases because failures can be intermittent. Cover production agent chains and every non-negotiable rule.
5. Retain subagents when the folded alternative performs worse.

For retained subagents, prefer tool invocation with a shared response schema while the main agent owns the conversation and checks conclusions against real data. Reserve full handoffs for specialists that must converse directly with the user.

### Ownership and implementation cautions
- A small central team owns the system prompt and end-to-end quality; domain teams own vetted skills, tools, and supporting evaluations.
- Group tools by **user intent**, not individual API endpoints. The article warns that tool selection tends to degrade beyond **30–50 tool definitions in the system prompt**; deferred tool search is the suggested mitigation.
- Enforce prerequisites and per-user permissions inside tools, rather than relying on prompt instructions.
- When dividing work, split by **independent context boundaries**, not organizational departments.

### Referenced resource
\[`anthropics/single-agent-loop-kit`\](https://github.com/anthropics/single-agent-loop-kit) provides a guided assessment/migration workflow and mock-system demo. The article also names `/claude-api build-eval`, `/claude-api prompt-audit`, `/claude-api hillclimb`, and `/claude-api cost-optimize`.

**Read-only next check:** compare the current agent graph and existing eval coverage against these criteria, identifying tightly coupled specialists and genuinely independent verification or research tasks. Repository contents, kit requirements, and model-specific claims were not independently verified.

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Building agents: When to fold subagents into your main agent loop](https://claude.com/resources/articles/building-agents-when-to-fold-subagents-into-your-main-agent-loop)
