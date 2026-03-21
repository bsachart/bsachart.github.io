# Quickstart: Implementing Table of Contents

This guide follows the **Anthemion Editorial** design system for adding an automatic Table of Contents (TOC) to Hugo blog posts.

## 1. Configure TOC Levels

Update `hugo.toml` to include the appropriate heading levels (H2 and H3).

```toml
[markup.goldmark.tableOfContents]
startLevel = 2
endLevel = 3
ordered = false
```

## 2. Update Layout Template

Modify `layouts/_default/single.html` to insert the TOC before the main content. Use Hugo's `{{ .TableOfContents }}` variable.

```html
<div class="toc-container" style="margin-bottom: 2rem;">
  <h2>Table of Contents</h2>
  {{ .TableOfContents }}
</div>
```

## 3. Style the TOC

Use the project's design tokens in `assets/css/main.css` to style the TOC appropriately. It should use `var(--font-ui)` for list items to distinguish it from the body text.

```css
#TableOfContents {
  font-family: var(--font-ui);
  list-style: none;
  padding: 0;
}

#TableOfContents ul {
  list-style: none;
  padding-left: 1.5rem;
}

#TableOfContents a {
  text-decoration: none;
  color: var(--link-color);
}
```

## 4. Verify Implementation

1. Start the Hugo server: `hugo server -D`.
2. Navigate to a post with several H2/H3 headings.
3. Confirm the TOC is visible at the top and links are functional.
