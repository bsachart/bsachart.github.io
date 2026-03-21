# Research: Table of Contents for Anthemion Editorial

**Feature**: [Table of Contents](../spec.md)
**Status**: Completed

## Decision Log

### Decision: TOC Implementation Strategy

- **Decision**: Use Hugo's built-in `.TableOfContents` variable in the `single.html` layout.
- **Rationale**: Hugo automatically parses headings and generates a structured HTML list. This is highly efficient and follows the "Hugo Standards" core principle.
- **Alternatives considered**:
  - **Manual parsing in JS**: Rejected because it increases client-side complexity and contradicts the minimalist design.
  - **Custom Hugo shortcode**: Rejected because it requires manual insertion in every post, violating the "Incremental Velocity" principle (automated is better).

### Decision: TOC Placement and Visibility

- **Decision**: Place the TOC before the article content, wrapped in a `<nav id="TableOfContents">` element. It will only show if headings are present.
- **Rationale**: Provides immediate utility for long-form content.
- **Alternatives considered**:
  - **Sticky Sidebar**: Rejected for the initial version to maintain simplicity and focus on "Editorial" layout. Can be added later if needed.

### Decision: Heading Levels

- **Decision**: Configure Hugo to include H2 and H3 in the TOC.
- **Rationale**: H2 and H3 provide sufficient structural detail without overwhelming the reader.
- **Alternatives considered**:
  - **H1-H6**: Too much detail. H1 is usually the page title.

## Findings

### Hugo TOC Configuration

Hugo's `markup.goldmark.tableOfContents` settings in `hugo.toml` allow controlling:

- `startLevel`: 2
- `endLevel`: 3
- `ordered`: false

### CSS Tokens

The Anthemion Design System (from `assets/css/main.css`) uses:

- `--font-heading`: Newsreader
- `--font-ui`: Manrope
- `--metadata-text-color`: For subtle UI elements.

The TOC should use `var(--font-ui)` for the list items to distinguish it from the body text, following the "No Decorative Elements" rule in `quickstart.md`.

## Verification Tasks

- [ ] Verify Hugo generates IDs for all headings (Goldmark does this by default).
- [ ] Test `.TableOfContents` output with a sample post containing H2 and H3.
