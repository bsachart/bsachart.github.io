# Quickstart: Working with the Design System

The Anthemion Editorial Design System relies on a structured, minimalist approach driven entirely by CSS Custom Properties (CSS variables) to support seamless light/dark mode transitions and high-contrast typography.

## Local Development

Start the Hugo server locally to view design token modifications in real-time.

```bash
hugo server -D --disableFastRender
```

## Adding and Modifying Design Tokens

All core design tokens (colors, fonts, sizing) are defined in the global stylesheet (`assets/css/main.css` or an equivalent global `style.css`).

1. Open `assets/css/main.css`.
2. Locate the `:root` pseudo-class for light mode tokens and the `@media (prefers-color-scheme: dark)` block for dark mode tokens.

```css
:root {
  /* Example token update */
  --link-hover-color: #10b981; /* Emerald */
}
```

3. Modifications to existing tokens (`--color-bg`, `--font-heading`) will instantly propagate across the homepage and single-article layouts because no styles should be hard-coded outside of the `:root` definitions.

## Layout Implementation Rules

When modifying templates in `layouts/`, adhere to the following simple rules:

1. **Use Variables**: Never hard-code fonts like `font-family: 'Newsreader';`. Always use `font-family: var(--font-heading);`.
2. **Generous Whitespace**: Let paragraphs breathe. We rely heavily on CSS margins (e.g. `margin-bottom: 1.5rem` or a `gap` rule on the central container).
3. **No Decorative Elements**: The focus is the typography. No borders or complex styling are needed. Limit UI elements to Manrope (`--font-metadata`) for distinct clarity against the body copy.
