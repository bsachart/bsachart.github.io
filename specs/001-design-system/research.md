# Research: Anthemion Editorial Design System

## 1. Technical Implementation of Design Tokens

**Decision**: Utilize CSS Custom Properties (CSS variables) in a centralized stylesheet (`assets/css/main.css` or equivalent).

**Rationale**: CSS variables allow for a dynamic, unified light/dark mode implementation without requiring a CSS preprocessor or complex JavaScript tooling. They provide the flexibility to override tokens cleanly. This approach adheres to the _Hugo Standards_ and _Philosophy of Software Design_ principles by keeping interfaces simple and maximizing functionality without over-engineering.

**Alternatives considered**:

- _TailwindCSS_: Avoided unless explicitly requested, as vanilla CSS supports our minimalist goal and is highly performant. Tailwind adds build steps and complexity which contradicts our _High Leverage Prioritization_.
- _Sass/SCSS_: Not strictly necessary for simple token definitions since CSS Custom Properties have excellent native support and easier runtime modification.

## 2. Light/Dark Mode Toggle Mechanism

**Decision**: Implement dark mode primarily via CSS `@media (prefers-color-scheme: dark)`, falling back to a structured class (e.g. `[data-theme="dark"]`) if a manual toggle is requested later.

**Rationale**: `prefers-color-scheme` provides an automatic, zero-JS solution that perfectly aligns with the minimalist intent. The user seamlessly transitions between themes based on system preferences, requiring zero added maintenance or interactive state tracking right out of the gate.

**Alternatives considered**:

- JS-based toggle out of the gate: Excluded from MVP to keep the feature minimal and focus solely on the visual integration first.

## 3. Font Loading Strategy

**Decision**: Self-host the fonts (Newsreader and Manrope) or link securely from Google Fonts via standard `<link>` tags in the document `&lt;head&gt;`.

**Rationale**: Simplest approach for Hugo static sites. Using `preconnect` to Google Fonts speeds up loading while keeping complexity minimal. If privacy constraints exist, self-hosting in the `static/fonts` directory is trivial to swap in later.

**Alternatives considered**: Web Font Loader JavaScript block (adds latency and JS dependency we do not need).
