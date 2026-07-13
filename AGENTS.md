# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project
A collection of small **Python exercises** from a *programming paradigms* course —
generators/iterators, custom ranges, fractions, `functools.reduce`, a Polish
number-word parser, and assorted beginner scripts. Files use Polish names
(e.g. `choinka.py`, `przestepne.py`, `liczyPierwsze.py`).

## Layout
- Individual exercise scripts at the repo root (one topic each).
- `reduce.py`, `fraction.py`, `liczba.py`, `my_range.py`, `generator.py`,
  `iterator.py`, `dekorator_my_range.py` — the ones covered by tests.
- `tests/test_exercises.py` — regression tests.

## Build / run / test
- Run any script directly: `python <script>.py`.
- Tests: `python -m unittest discover -s tests -v`.

## Conventions & good practices
- Preserve each exercise's **teaching intent**; fix edge cases (empty inputs,
  negative-step ranges, zero denominators) without changing the exercise's purpose.
- Add a regression test in `tests/test_exercises.py` for any behavior fix.
- Preserve the teaching structure of unrelated scripts. Use an
  `if __name__ == "__main__":` guard when a script must also be safely imported or
  tested, but do not reformat the whole exercise collection for consistency alone.
- Update **both** `README.md` and `README.pl.md` together.

## Documentation
- [README.md](README.md) · [README.pl.md](README.pl.md)
- [Technical documentation](docs/TECHNICAL_DOCUMENTATION.md) · [Polski](docs/TECHNICAL_DOCUMENTATION.pl.md)
- License: **MIT** — see [LICENSE](LICENSE).

_Educational / portfolio project._
