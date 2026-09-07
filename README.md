# Cykl FBW 79

12-tygodniowy plan treningowy Full Body Workout — 4 sesje w tygodniu (A / B / A′ / B′),
trzy bloki progresji, wbudowany dziennik treningowy i wykres szacowanego 1RM.

**Strona:** https://tomaszswiadomosc.github.io/fbw/

## Co jest w środku

| Plik | Rola |
|---|---|
| `src/plan.html` | Źródło — fragment publikowany jako artefakt Claude (bez `<html>`/`<head>`) |
| `index.html` | Wersja standalone dla GitHub Pages, generowana z `src/plan.html` |
| `build.py` | Opakowuje źródło w pełny dokument HTML |

Po edycji `src/plan.html` uruchom `python3 build.py` i zacommituj oba pliki.

## Dwie kopie, dwa magazyny danych

Strona sama wykrywa, gdzie działa:

- **Na GitHub Pages** — dziennik zapisuje się w `localStorage` przeglądarki.
  Dane zostają tylko na tym jednym urządzeniu i znikają przy czyszczeniu danych strony.
- **Jako artefakt na claude.ai** — dziennik zapisuje się na serwerze i synchronizuje
  między urządzeniami. To wersja do używania na siłowni.

Dzienniki obu kopii są niezależne — nie wymieniają się danymi. Przycisk **Eksport CSV**
działa w obu.

## Struktura planu

- **Blok 1** (tyg. 1–4) Akumulacja — 4×6 RIR 3→2
- **Blok 2** (tyg. 5–8) Intensyfikacja — 5×4 RIR 2→1
- **Blok 3** (tyg. 9–11) Ekspresja — 5×3 RIR 1→0
- **Tydzień 12** Deload + testy

Metodyka FBW wg wykładu Szymona Mosznego (wzorce ruchowe, zasada priorytetu, dobór objętości).
