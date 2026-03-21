# Data Model: Table of Contents

**Feature**: [Table of Contents](../spec.md)
**Status**: Ready

## Entities

### TOC Node (Implicit)

Represents a single entry in the hierarchical TOC.

- **Title**: The text content of the heading.
- **Link**: The anchor link (`#fragment`) pointing to the heading's unique ID.
- **Level**: The depth of the heading (e.g., 2 for H2, 3 for H3).

## Relationships

- **Article content** contains multiple **TOC Nodes**.
- **TOC Node** may have **children** (nested sub-headings).

## Validation Rules

- **Minimum Headings**: TOC should only render if at least 2 headings are present (configurable in Hugo with `.TableOfContents`).
- **Maximum Depth**: Only H2 and H3 should be included as per requirements.

## State Transitions

- **Static Site Generation**: Headings are extracted from Markdown content at build time.
- **Client-side Interaction**: Clicking a TOC Node link scrolls the viewport to the target.
