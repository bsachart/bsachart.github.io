# Feature Specification: Typography & Container Responsiveness

**Feature Branch**: `002-responsiveness`  
**Created**: 2026-03-21  
**Status**: Draft  
**Input**: User description: "Can you improve the responsiveness of the pages? Currently the text and main container seems small to me."

## User Scenarios & Testing _(mandatory)_

### User Story 1 - Fluid Responsive Typography & Scaling (Priority: P1)

As a reader viewing the blog on a large high-resolution monitor, I want the text and layout to scale up appropriately so that the content is comfortable to read and doesn't feel like a tiny column trapped in the center of the screen.

**Why this priority**: Essential to fix the immediate visual constraint where text is difficult to read on wide pages.

**Independent Test**: Resize the browser window from mobile width to ultra-wide desktop width. The base font size should increase fluidly, and the container width should adapt and feel proportionate to the screen while maintaining readability.

**Acceptance Scenarios**:

1. **Given** a user loads the blog on a 1080p or 4K screen, **When** they view the homepage or article, **Then** the text is noticeably larger and the main content container proportionally uses more screen width without exceeding optimal reading lengths.
2. **Given** a user views the site on a mobile device, **When** they read an article, **Then** the font size drops down smoothly so it doesn't break the layout.

---

### Edge Cases

- Extreme ultra-wide monitors might stretch the text too wide if we rely solely on percentages, so a maximum absolute clamp or unit limit should still ensure optimal reading lengths (typically around 65-80 characters, but rendered larger).
- The transition between mobile and desktop layout sizes should be continuous without jarring jumps.

## Requirements _(mandatory)_

### Functional Requirements

- **FR-001**: System MUST implement fluid typography, allowing the base font size to scale relative to the viewport width.
- **FR-002**: System MUST adjust the primary container's width constraint to comfortably occupy modern high-resolution displays horizontally.
- **FR-003**: System MUST NOT exceed a maximum width that sacrifices readability line lengths.
- **FR-004**: System MUST maintain the design system aesthetics, ensuring Newsreader and Manrope stay proportional when scaling up.

### Key Entities

- **CSS Variables / Root**: Modifications to the underlying CSS typography setup to include responsive or fluid sizing functions.
- **`.container` class**: The targeted layout entity receiving width updates.

## Success Criteria _(mandatory)_

### Measurable Outcomes

- **SC-001**: Lighthouse visual accessibility score remains 100 on both light and dark modes with the new font sizes.
- **SC-002**: The base font-size scales up correctly on viewports larger than 1200px.
- **SC-003**: No horizontal scrolling is introduced on small mobile viewports (e.g. 320px logic stays intact).
