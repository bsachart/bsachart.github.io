# Tasks: Table of Contents

**Input**: Design documents from `/specs/003-table-of-contents/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, quickstart.md

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2)
- Include exact file paths in descriptions

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Configure Hugo Goldmark TOC levels (startLevel=2, endLevel=3) in `hugo.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

- [ ] T002 [P] Create `.toc-container` CSS class placeholder in `assets/css/main.css`

**Checkpoint**: Foundation ready - user story implementation can now begin.

---

## Phase 3: User Story 1 - Navigation and Scannability (Priority: P1) 🎯 MVP

**Goal**: Automatically generate a clickable TOC for blog posts.

**Independent Test**: Navigate to a post with H2/H3 headings and verify the TOC appears and links work.

### Implementation for User Story 1

- [ ] T003 [US1] Insert Hugo's `{{ .TableOfContents }}` variable into `layouts/_default/single.html`
- [ ] T004 [US1] Add "Table of Contents" title and container wrap to TOC in `layouts/_default/single.html`
- [ ] T005 [P] [US1] Apply typography and list styling for `#TableOfContents` in `assets/css/main.css`
- [ ] T006 [P] [US1] Style TOC links using design system color tokens in `assets/css/main.css`

**Checkpoint**: User Story 1 (MVP) is fully functional and testable independently.

---

## Phase 4: User Story 2 - Mobile Accessibility (Priority: P2)

**Goal**: Ensure the TOC is readable and functional on mobile devices.

**Independent Test**: Resize browser to mobile width and verify TOC layout and link spacing.

### Implementation for User Story 2

- [ ] T007 [P] [US2] Add responsive media queries for `.toc-container` in `assets/css/main.css`
- [ ] T008 [US2] Increase line-height and padding for TOC links on mobile in `assets/css/main.css`

**Checkpoint**: User Story 2 is functional and improves mobile experience.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final refinements and verification.

- [ ] T009 Verify TOC does not render for articles with fewer than 2 headings.
- [ ] T010 [P] Final audit of TOC accessibility (ARIA roles and semantic HTML).
- [ ] T011 Run `quickstart.md` validation.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies.
- **Foundational (Phase 2)**: Depends on Setup completion.
- **User Story 1 (Phase 3)**: Depends on Foundational completion.
- **User Story 2 (Phase 4)**: Depends on User Story 1 completion (for basic structure).
- **Polish (Final Phase)**: Depends on all user stories being complete.

### Parallel Opportunities

- T002 [P] can run during Phase 2.
- T005 [P] and T006 [P] can run in parallel within Phase 3.
- T007 [P] can run in parallel during Phase 4.

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently.

### Incremental Delivery

1. Foundation ready.
2. Add User Story 1 → MVP functional.
3. Add User Story 2 → Mobile optimized.
4. Total 11 tasks.
