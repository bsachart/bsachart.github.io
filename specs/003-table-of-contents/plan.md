# Implementation Plan: Table of Contents

**Branch**: `003-table-of-contents` | **Date**: 2026-03-21 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/003-table-of-contents/spec.md`

## Summary

This feature adds an automatic Table of Contents (TOC) to all blog posts using Hugo's built-in `.TableOfContents` capability. The TOC will focus on H2 and H3 headings, providing a structured, hierarchical navigation list before the main article content. Styling will align with the Anthemion Editorial design system, utilizing existing CSS tokens for typography and layout.

## Technical Context

- **Language/Version**: Hugo (v0.120+), HTML5, Vanilla CSS.
- **Primary Dependencies**: Goldmark (Hugo's default Markdown parser).
- **Storage**: N/A (Static generation).
- **Testing**: Manual verification on various screen sizes and build characterization.
- **Target Platform**: Desktop and Mobile browsers.
- **Project Type**: Static Site (Hugo Blog).
- **Performance Goals**: No measurable impact on page load (build-time generation).
- **Constraints**: Adhere to `assets/css/main.css` design tokens.
- **Scale/Scope**: All posts in `content/posts/` with 2+ headings.

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

- [x] **I. Incremental Velocity**: Feature is broken into small, functional steps (Config -> Layout -> Styles).
- [x] **II. Atomic Pull Requests**: Each logical change will be a single commit in the branch.
- [x] **III. Hugo Standards**: Uses built-in `.TableOfContents` instead of custom JS parsers.
- [x] **IV. Philosophy of Software Design**: Deep functionality (automatic TOC) with simple implementation (layout injection).
- [x] **V. Code Quality & Technical Writing**: All documentation and variable names will be precise.
- [x] **VI. High Leverage Prioritization**: High impact (better navigation) with low effort (leveraging Hugo built-ins).
- [x] **VII. Specification as Source of Truth**: Specs/Plans are updated in sync with implementation.
- [x] **VIII. Verification & Validation**: All changes verified by `hugo server`.
- [x] **IX. Design System Adherence**: Uses `var(--font-ui)` and existing color tokens.

## Project Structure

### Documentation (this feature)

```text
specs/003-table-of-contents/
├── plan.md              # This file
├── spec.md              # Feature specification
├── research.md          # Research findings (Hugo TOC config)
├── data-model.md        # Hierarchical TOC model
├── quickstart.md        # Implementation checklist
├── checklists/          # Quality validation
└── tasks.md             # Implementation tasks
```

### Source Code (repository root)

```text
hugo.toml                # markup.goldmark.tableOfContents configuration
layouts/
└── _default/
    └── single.html      # TOC placement inside <article>
assets/css/
└── main.css             # TOC styling using design tokens
```

**Structure Decision**: Modified existing layouts and configuration to integrate the feature into the core blog structure.
