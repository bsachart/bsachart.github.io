# Design Tokens (Data Model)

While not a traditional backend data model, the design system requires a "database" of foundational CSS Custom Properties (tokens) that drive the layout.

## Typographic Tokens

```css
:root {
  /* Font Families */
  --font-heading: 'Newsreader', serif;
  --font-body: 'Manrope', sans-serif;
  --font-metadata: var(--font-body);
  --font-ui: var(--font-body);

  /* Font Weights */
  --weight-regular: 400;
  --weight-medium: 500;
  --weight-bold: 700;

  /* Line Heights */
  --lh-body: 1.6;
  --lh-heading: 1.2;
}
```

## Color Palette Tokens (Light/Dark Mode)

```css
:root {
  /* Light Mode Base Variables */
  --bg-color: #f8f9fa; /* Example off-white */
  --text-color: #212529; /* Deep charcoal, almost black */
  --metadata-text-color: #6c757d; /* Muted gray for dates/nav */

  /* Link Interactions */
  --link-color: inherit;
  --link-hover-color: #10b981; /* Default emerald green */
}

@media (prefers-color-scheme: dark) {
  :root {
    /* Dark Mode Variable Overrides */
    --bg-color: #121212; /* Deep dark gray */
    --text-color: #f8f9fa; /* High contrast off-white */
    --metadata-text-color: #adb5bd; /* Lighter muted gray */

    /* Ensure emerald is high contrast against dark bg */
    --link-hover-color: #34d399; /* Slightly brighter emerald */
  }
}
```

## Layout Entities

- **Homepage Layout**: A CSS Grid or Flex container centering content and restricting max-width, exclusively rendering an index of markdown content iteratively (titles and dates).
- **Article Layout**: A wrapper `main` tag containing a semantic `article`. Standardized paddings, max-width stringently enforced for reader focus (`ch` length units).
