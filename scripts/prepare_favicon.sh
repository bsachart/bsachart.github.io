#!/usr/bin/env bash

set -euo pipefail

USERNAME="${1:-bsachart}"
SIZE="${2:-256}"
OUT="${3:-static/favicon.png}"

if ! command -v curl >/dev/null 2>&1; then
  echo "ERROR: curl is required" >&2
  exit 1
fi

if ! command -v magick >/dev/null 2>&1; then
  echo "ERROR: ImageMagick (magick) is required" >&2
  exit 1
fi

if ! [[ "$SIZE" =~ ^[0-9]+$ ]] || [[ "$SIZE" -le 0 ]]; then
  echo "ERROR: size must be a positive integer" >&2
  exit 1
fi

mkdir -p "$(dirname "$OUT")"

tmp_avatar="$(mktemp /tmp/avatar.XXXXXX.png)"
tmp_mask="$(mktemp /tmp/mask.XXXXXX.png)"
trap 'rm -f "$tmp_avatar" "$tmp_mask"' EXIT

curl -fsSL "https://github.com/${USERNAME}.png?size=${SIZE}" -o "$tmp_avatar"
magick -size "${SIZE}x${SIZE}" xc:none -fill white \
  -draw "circle $((SIZE / 2)),$((SIZE / 2)) $((SIZE / 2)),$((SIZE - 1))" \
  "$tmp_mask"

magick "$tmp_avatar" -gravity center -crop "${SIZE}x${SIZE}+0+0" +repage \
  "$tmp_mask" -alpha off -compose copy_opacity -composite "$OUT"

echo "Generated rounded favicon at $OUT from https://github.com/${USERNAME}.png"
