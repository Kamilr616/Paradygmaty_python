# Technical documentation

## Scope and organization

This repository is a set of 26 independent Python exercises rather than one
application or package. Each `.py` file in `src/` demonstrates a focused topic
from the Programming Paradigms course and uses only the Python standard library.

| Area | Principal files |
|---|---|
| Custom iteration | `my_range.py`, `generator.py`, `iterator.py`, `dekorator_my_range.py` |
| Functional style | `reduce.py`, `wspolne.py`, `list_sum_rek.py` |
| Value objects and OOP | `fraction.py`, `figury.py`, `bryly.py`, `liczba.py`, `napis.py` |
| Numerical algorithms | `bisekcja.py`, `pochodna.py`, `wariancja_srednia.py`, `wariancja rek.py` |
| Recursion/search | `findA.py`, `findAv2.py`, `100comb.py` |
| Small interactive scripts | `kontakty.py`, `zgadujZgadula.py`, `choinka.py`, `krotki.py` |

The Polish filenames and intentionally compact implementations are part of the
course material. The repository has no shared runtime state, installable package
metadata or external service.

## Reusable exercise contracts

### Range implementations

`my_range.my_range`, `generator.generate`, `iterator.My_range` and the decorated
range implement start/stop/step traversal with positive and negative steps. Like
the built-in `range`, the stop boundary is exclusive and a zero step raises
`ValueError`. The list, generator and iterator forms intentionally demonstrate
different execution and storage models.

### Functional helpers

`reduce.py` contains mean, maximum, flattening, common-letter and sorted insertion
examples built around `functools.reduce`. Empty input is valid for helpers with a
natural empty result, while mean and maximum raise `ValueError` because their
result would be undefined.

### Fraction value object

`fraction.Fraction` normalizes numerator and denominator by their greatest common
divisor, keeps the sign in the numerator and rejects a zero denominator with
`ZeroDivisionError`.

### Polish number parser

`liczba.fun` converts the limited Polish number vocabulary used by the exercise,
including units and tens such as `dwadzieścia jeden`. Unsupported or malformed
input returns the original exercise message `Nieprawidłowe dane` rather than
raising an exception.

## Execution and import behaviour

Run an individual exercise from the repository root:

```bash
python src/my_range.py
python 'src/wariancja rek.py'
```

All exercises use `if __name__ == "__main__":` guards, so they can be loaded by
the demonstration runner without starting prompts or producing output during
import. Interactive behavior is preserved when a script is executed directly.

Run a compact, non-interactive demonstration of all exercises with:

```bash
python demo/main.py
```

## Automated tests

```bash
python -m unittest discover -s tests -v
```

The six regression tests cover:

- positive and negative range steps across four implementations,
- rejection of a zero step,
- functional helpers on normal, empty and boundary inputs,
- fraction normalization and a zero denominator,
- Polish unit/tens parsing.

The remaining exercises are small interactive or print-oriented programs and
are not covered by snapshot/integration tests.

## Maintenance rules and limitations

- Preserve each file's educational intent and avoid turning the collection into
  a single framework or package.
- Add a focused test when changing the reusable helpers listed above.
- Some algorithms assume valid educational input and do not provide production
  validation or performance guarantees.
- Output and prompts are primarily Polish; terminal encoding affects rendering.
- Filenames are part of the original submission, including the space in
  `wariancja rek.py`; quote that path in shell commands.
- Import side effects are documented above and should only be removed when a file
  genuinely needs to become reusable or testable.
