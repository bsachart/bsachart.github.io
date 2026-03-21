---
description: 'Task list template for feature implementation'
---

# Tasks: Anthemion Editorial Design System

**Input**: Design documents from `/specs/001-design-system/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 [P] Ensure Hugo structure contains `assets/css/` directory and `layouts/_default/` directory
- [x] T002 [P] Create base Hugo HTML wrapper in `layouts/_default/baseof.html` if it does not exist

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Add Google Fonts `<link>` tags for Newsreader and Manrope to the document head (`layouts/partials/head.html` or `layouts/_default/baseof.html`)

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Apply Global Typography and Colors (Priority: P1) 🎯 MVP

**Goal**: Experience a unified light/dark mode color palette and typography utilizing Newsreader and Manrope.

**Independent Test**: Can be verified by checking the global CSS variables and toggling between light and dark modes on a test page.

### Implementation for User Story 1

- [x] T004 [P] [US1] Create global stylesheet `assets/css/main.css` containing all `:root` typographic and color design tokens per `data-model.md`
- [x] T005 [P] [US1] Append `@media (prefers-color-scheme: dark)` mode overrides to `assets/css/main.css`
- [x] T006 [US1] Link `assets/css/main.css` into the HTML layout head (`layouts/_default/baseof.html` or `layouts/partials/head.html`)
- [x] T007 [US1] Ensure `body` tag applies the background variable and global text color variable

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Homepage Minimalist Redesign (Priority: P2)

**Goal**: Typography-focused minimalist layout for the homepage.

**Independent Test**: Can be tested by loading the index page and verifying the absence of the 'About' link and the correct font pairings.

### Implementation for User Story 2

- [x] T008 [P] [US2] Update `layouts/index.html` to remove any 'About' link or decorative elements
- [x] T009 [US2] Apply layout container logic in `layouts/index.html` to center content
- [x] T010 [US2] Ensure Newsreader is mapped for post titles and Manrope for dates/descriptions in `layouts/index.html` structure

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Article Page Single Column Layout (Priority: P3)

**Goal**: Read content in a single, clean column with generous whitespace so that it is a distraction-free experience.

**Independent Test**: Can be tested by navigating to a single post and measuring column width and whitespace.

### Implementation for User Story 3

- [ ] T011 [P] [US3] Create or update `layouts/_default/single.html` to feature a semantic `<article>` block
- [ ] T012 [US3] Apply single column CSS constraints (max-width, generous margins) to the main wrapper affecting `single.html`
- [ ] T013 [US3] Implement emerald green link hover interaction globally or specifically for article links in `assets/css/main.css`

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T014 Review Lighthouse metrics locally to ensure a strictly 100 accessibility and performance score
- [ ] T015 Verify CSS uses variables everywhere instead of hard-coded font families or hexadecimal colors

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - Integrates with US1 global CSS directly
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - Integrates with US1 global CSS directly

### Parallel Opportunities

- CSS variable parsing (T004, T005) can be developed independently of the Hugo structural edits (T008, T011).
- Font embedding (T003) and HTML wrapper structures (T002) run parallel to specific page layouts.
