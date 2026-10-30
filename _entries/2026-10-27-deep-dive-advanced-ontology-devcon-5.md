---
title: "Deep Dive: Advanced Ontology | DevCon 5"
date: 2026-10-27 22:31:17 +0700
section: Research Summary
section_slug: research-summary
description: "Landon, a Palantir ontology group lead, presents advanced ontology features as a set of composable software primitives. The central argument: model real-world entities and operational workflows—not merely the structure of upstream datasets."
audio: /audio/2026/10/deep-dive-advanced-ontology-devcon-5.mp3
duration: "4 min 40 sec"
read_time: "7 min"
primary_source: https://www.youtube.com/watch?v=_b2qsKz_Ifk
youtube_id: _b2qsKz_Ifk
signal:
  - "Landon, a Palantir ontology group lead, presents advanced ontology features as a set of composable software primitives."
  - "The central argument: model real-world entities and operational workflows—not merely the structure of upstream datasets."
  - "The talk traces the ontology’s evolution from integrated “golden tables,” through operational decision-making with acti…"
---
## Overview

Landon, a Palantir ontology group lead, presents advanced ontology features as a set of composable software primitives. The central argument: **model real-world entities and operational workflows—not merely the structure of upstream datasets.**

The talk traces the ontology’s evolution from integrated “golden tables,” through operational decision-making with actions, functions, and models, to AI-first automation. Gotham’s history with unstructured intelligence data provides the background for features now discussed across Foundry and AIP.

## Four design principles

1. **Domain-driven design:** Represent real-world concepts with meaningful objects, links, and API names. Most real-world objects should have a one-to-one representation in the ontology.
2. **Don’t repeat yourself:** Apply the “rule of three”—after implementing the same pattern three times, consider extracting a shared data model or workflow. Reducing near-duplicate object types also simplifies agent context management.
3. **Open for extension, closed for modification:** Protect stable, critical interfaces while allowing other builders to add object types and workflows around them.
4. **Producer extends, consumer super:** Borrow covariance and contravariance concepts from programming languages so interface-based workflows can accept compatible specialized types and functions.

The speaker’s broader framing is that an ontology acts as organizational software, making established software-engineering principles applicable.

## Core features

### Interfaces: reusable workflows across object types

A workflow built against a `building` interface can work with restaurants, office buildings, and arenas—together or through a type-specific selection—without separate application copies.

- **Multiple inheritance:** An arena can implement both `building` and `schedulable resource`, supporting building-oriented and scheduling workflows independently.
- **Multi-level interfaces:** Interfaces can extend other interfaces.
- **Composition:** Combining independent capabilities avoids creating awkward combined abstractions such as a dedicated “schedulable building” hierarchy.
- **Type flexibility:** The talk illustrates event-based workflows accepting NBA games or DevCon keynotes, and compatible functions consuming specialized event objects.

**Implementation guidance:** Automatically mapping every dataset column into ontology properties may provide a starting point, but it does not replace deliberate domain modeling.

### Structs: grouped values with nearby metadata

Struct properties package related fields into a single meaningful property.

Examples include:
- An address containing street address, city, state, and postal code.
- An address value accompanied by source, creator, creation time, and modification metadata.
- An AIP Logic Slack-helper output containing a response, relevant Slack message, documentation URL, and model-generated reasoning for downstream processing.

Structs keep metadata adjacent to the value it describes instead of scattering it across hidden properties or sidecar structures. The transcript describes captured model reasoning as an output field; it does not establish its reliability as an explanation.

### Reducers: prioritize a value without discarding history

The speaker introduces reducers using a multi-valued address property:

- Historical addresses remain in a list.
- A reducer selects the struct with the most recent `last modified on` metadata.
- Many UIs present that address first.
- Other values remain available through expansion or hover, depending on the UI, and remain searchable.

**Important distinction:** Selecting the most recently modified address is the example’s rule; it does not inherently establish which address is currently valid.

### Struct main fields: preserve normal value behavior

A struct main field identifies the primary semantic value inside a struct.

For a geolocation struct:
- The geo point is designated as the only main field.
- Creator and timestamp information remain additional fields.
- The property can behave like a geo point in geo workflows and display as one in the UI.
- Supporting metadata remains inspectable.

Together, reducers and main fields reduce presentation complexity while retaining richer underlying information.

### Derived properties: semantic calculations over normalized data

Derived properties express business logic using existing objects and links rather than duplicating stored values.

In the reporting-line example:
- Report names are collected from linked worker objects.
- Report count is calculated from the relevant linked workers.

This avoids the brittleness of copying names and counts onto a manager object, where changes to names or reporting relationships could otherwise create stale data.

## Advanced combinations

### Fine-grained security

The talk presents progressively finer security models:

| Granularity | Mechanism described |
|---|---|
| Dataset | Shared dataset-backed security |
| Row/object | Restricted views or object security policies |
| Cell | Combined row-wise and column-wise security using object security policies; historically also restricted views plus multi-dataset objects (`MDOs`) |
| Individual array element | Derived-property modeling that gives each patient-note element its own security level |

The key architectural idea is that security can follow semantically meaningful records or observations, rather than applying only to an entire table or property.

### Entity resolution while preserving source security

Derived properties and carefully arranged links can expose combined information from objects later recognized as the same entity.

The described model includes:
- Entity objects, illustrated with equipment.
- Separate equipment-observation objects.
- Resolution links.
- A three-step derived-property chain.

Viewing either resolved entity exposes the combined information while preserving the original individual security restrictions. Adding another resolved entity updates the combined view.

**Constraint:** The transcript illustrates the architecture but does not provide the exact link definitions or derived-property expressions needed to reproduce it.

### Object-backed link types

A `venture staffing` object connects an employee to a venture and stores relationship metadata, such as when the employee worked there.

Object-backed link types support two views:
- **Direct relationship:** Navigate from employee to venture when staffing details are irrelevant.
- **Explicit relationship object:** Traverse and filter staffing records when details matter—for example, determining the current venture.

This preserves a meaningful relationship object without forcing every workflow to expose the intermediate step.

## Operator assessment

**Most useful takeaway:** Interfaces, structs, reducers, derived properties, security policies, and object-backed links are complementary primitives—not isolated features. Their value comes from combining reusable workflows, normalized data, contextual metadata, and precise access control.

**Risks and evidence limits**
- Automatic dataset mirroring and repeated object types can produce a fragmented ontology.
- Denormalized copies of linked data can become stale.
- Reducer selection rules must match the intended business meaning.
- Fine-grained security and entity-resolution examples are complex and require careful review of what each user can see.
- The talk provides no release versions, availability matrix, performance measurements, or complete configuration examples.
- Claims about Palantir’s battle-tested depth and competitive advantage are the speaker’s positioning, not independently demonstrated findings.

**Read-only follow-up:** Compare these patterns with the existing domain model, inspect feature-availability documentation, and review interface contracts, reducer semantics, derived-property definitions, and security behavior before assessing implementation fit.

<details class="evidence-drawer" markdown="1">
<summary>Evidence note</summary>

The source registry contains one readable HTTP source. No private source fields are rendered.

</details>

## Sources

- [Deep Dive: Advanced Ontology | DevCon 5](https://www.youtube.com/watch?v=_b2qsKz_Ifk)
