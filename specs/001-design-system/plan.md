# Implementation Plan: Anthemion Editorial Design System

**Branch**: `001-design-system` | **Date**: 2026-03-21 | **Spec**: [spec.md](../spec.md)
**Input**: Feature specification from `/specs/001-design-system/spec.md`

## Summary

Implement the Anthemion Editorial design system utilizing Newsreader for headings and Manrope for body text, metadata, and UI elements. Establish a unified light/dark color palette accessible via CSS Custom Properties, and apply these tokens to create a typography-focused layout across the homepage and individual article pages.

## Technical Context

**Language/Version**: HTML5, Vanilla CSS3 (Custom Properties)
**Primary Dependencies**: Hugo (Static Site Generator), Google Fonts (Newsreader, Manrope)
**Storage**: N/A
**Testing**: Manual Visual Testing, Lighthouse Accessibility Audit
**Target Platform**: Web Browsers (Mobile and Desktop)
**Project Type**: Hugo Static Web Site
**Performance Goals**: 100 on Lighthouse Performance & Accessibility; Zero layout shift; Avoid render-blocking Javascript.
**Constraints**: No CSS preprocessors (SASS/Tailwind); No client-side Javascript for basic theme toggling.
**Scale/Scope**: Minimalist deployment spanning one homepage (`layouts/index.html`), one single page (`layouts/_default/single.html`), and global CSS assets (`assets/css/main.css`).

## Constitution Check

_GATE: Must pass before Phase 0 research. Re-check after Phase 1 design._

- [x] **Incremental Velocity**: Yes, styling tokens and foundational layouts.
- [x] **Atomic Pull Requests**: Yes, updating tokens and templates cleanly.
- [x] **Hugo Standards**: Yes, utilizing Hugo's default `layouts` and `assets` structures.
- [x] **Philosophy of Software Design**: Yes, deep modules achieved via centralized CSS custom properties defining standard design variables.
- [x] **Code Quality & Technical Writing**: Yes.
- [x] **High Leverage Prioritization**: Yes, relying on native `prefers-color-scheme` over JS overrides.
- [x] **Specification as Source of Truth**: Yes.
- [x] **Verification & Validation**: Yes.
- [x] **Design System Adherence**: The primary goal of this implementation.

## Project Structure

### Documentation (this feature)

```text
specs/001-design-system/
├── plan.md              # This file (/speckit.plan command output)
├── research.md          # Phase 0 output (/speckit.plan command)
├── data-model.md        # Phase 1 output (/speckit.plan command)
├── quickstart.md        # Phase 1 output (/speckit.plan command)
└── checklists/          # Checklists required for the specification
```

### Source Code (repository root)

```text
layouts/
├── index.html           # Homepage minimalist listing
└── _default/
    └── single.html      # Article page single column layout

assets/
└── css/
    └── main.css         # Global stylesheet for Anthemion tokens

config.toml / hugo.toml  # Verify theme settings or parameter configuration
```

**Structure Decision**: The system will act as its own minimal Hugo theme or override the standard layout files by placing them directly in the root `layouts/` directory, adhering to standard Hugo lookup prioritization. Tokens will be housed securely in `assets/css/main.css` to be piped through Hugo processing if needed, though raw CSS in `static/css/` is also an acceptable fallback.

## Complexity Tracking

_None needed. Constitution check passed securely._
