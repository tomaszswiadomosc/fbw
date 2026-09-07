#!/usr/bin/env python3
"""Buduje wersję standalone (GitHub Pages) ze źródła artefaktu."""
import pathlib, re
src = pathlib.Path(__file__).parent / "src" / "plan.html"
out = pathlib.Path(__file__).parent / "index.html"
body = src.read_text(encoding="utf-8")
m = re.search(r"<title>(.*?)</title>", body)
title = m.group(1) if m else "Cykl FBW 79"
out.write_text(
    "<!doctype html>\n<html lang=\"pl\">\n<head>\n"
    "<meta charset=\"utf-8\">\n"
    "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
    "<meta name=\"description\" content=\"12-tygodniowy plan treningowy FBW z dziennikiem i wykresem progresu.\">\n"
    "<meta name=\"theme-color\" content=\"#1D5FA5\">\n"
    f"<meta property=\"og:title\" content=\"{title}\">\n"
    "<link rel=\"icon\" href=\"data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>%F0%9F%8F%8B%EF%B8%8F</text></svg>\">\n"
    "<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n"
    "</head>\n<body>\n" + body + "\n</body>\n</html>\n",
    encoding="utf-8")
print("index.html:", out.stat().st_size, "bajtów")
