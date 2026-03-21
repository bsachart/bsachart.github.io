<!--
Sync Impact Report:
- Version change: 1.1.0 → 1.2.0
- List of modified principles:
  - Added VI. High Leverage Prioritization
  - Added VII. Specification as Source of Truth
  - Added VIII. Verification & Validation
- Added sections: None
- Removed sections: None
- Templates requiring updates: ✅ None
- Follow-up TODOs: None
-->

# bsachart.github.io Constitution

## Core Principles

### I. Incremental Velocity

Changes MUST be done incrementally to improve development velocity. Break down features into the smallest possible functional units that provide value or progress.

### II. Atomic Pull Requests

A pull request MUST only include exactly one commit. This ensures a clean history and simplifies reverts if necessary. Each commit should represent a single logical change.

### III. Hugo Standards

All development MUST follow official Hugo standards and best practices for themes, templates, and configuration. Refer to official documentation for any structural or syntax decisions.

### IV. Philosophy of Software Design

Design and implementation MUST be guided by principles from John Ousterhout’s "A Philosophy of Software Design." Focus on reducing complexity by creating deep modules with simple interfaces and significant functionality.

### V. Code Quality & Technical Writing

High standards of clarity and conciseness MUST be maintained:

- **Variable Naming**: Use evocative, precise, and meaningful variable names.
- **Concise Commenting**: Comments MUST be meaningful. Avoid "fluffy" or redundant comments that merely restate what is obvious from the code itself.
- **Professional Writing**: All technical documentation (specifications, implementation plans, and commits) MUST demonstrate professional technical writing standards.

### VI. High Leverage Prioritization

We MUST prioritize tasks according to the principle of "High Impact, Low Effort." Focus on "Big Wins"—changes that deliver the maximum project value or progress for the minimum implementation complexity. Avoid over-engineering solutions that do not contribute significantly to the project's primary goals.

### VII. Specification as Source of Truth

Because our collaboration relies on design documents (`spec.md`, `plan.md`, `constitution.md`) to serve as our collective "memory," these files MUST be kept in perfect sync with the implementation. All changes to project architecture or behavior MUST be reflected in these documents immediately.

### VIII. Verification & Validation

To ensure no broken code is shipped, all changes MUST be verified via command-line execution, build checks, or automated tests before being reported as complete. No task is considered "Ready" or "Done" based on output alone.

## External Documentation

This project relies on the following official resources for guidance and best practices:

- [Official Hugo Documentation](https://gohugo.io/)
- [Getting Started with Hugo](https://gohugo.io/getting-started/)
- [Hugo Themes](https://gohugo.io/themes/)
- [Hugo Templates](https://gohugo.io/templates/)
- [Hugo Configuration](https://gohugo.io/getting-started/configuration/)

## Governance

Amendments to this constitution require a version bump following semantic versioning rules and should be documented in the Sync Impact Report. All contributions must comply with these principles.

**Version**: 1.2.0 | **Ratified**: 2026-03-21 | **Last Amended**: 2026-03-21
