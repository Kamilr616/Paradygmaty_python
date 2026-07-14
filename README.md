# 🐍 Programming Paradigms — Python Exercises

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> 🇵🇱 [Polish version](README.pl.md)

> 🗓️ **Project period:** 2023

> 📘 [Technical documentation](docs/TECHNICAL_DOCUMENTATION.md)

A collection of solved exercises from the **Programming Paradigms** university course. Most scripts are self-contained solutions demonstrating a specific Python concept — from basic algorithms and recursion to object-oriented programming, iterators, generators, decorators, and functional programming. The course spanned the **imperative, object-oriented and functional** styles in Python, so this repo doubles as a compact reference of those fundamentals.

All exercise scripts are stored in the `src/` directory.

## 📚 Topics covered

| Topic | Example scripts |
|-------|-----------------|
| **Algorithms & math** | `bisekcja.py` (bisection method), `pochodna.py` (derivative), `liczyPierwsze.py` (primes), `100comb.py`, `wariancja_srednia.py` (variance/mean), `wariancja rek.py` (recursive variance) |
| **Recursion** | `list_sum_rek.py`, `findA.py` / `findAv2.py` |
| **Object-oriented programming** | `figury.py` (2D shapes), `bryly.py` (3D solids), `fraction.py`, `liczba.py`, `napis.py` |
| **Iterators & generators** | `iterator.py`, `generator.py`, `my_range.py` |
| **Decorators** | `dekorator_my_range.py`, `dekorator_time_suma_lst.py` (timing decorator) |
| **Functional programming** | `reduce.py` (mean, max and flatten via `functools.reduce`) |
| **Data structures** | `krotki.py` (tuples), `kontakty.py` (contact book), `wspolne.py` (common elements) |
| **Small programs** | `zgadujZgadula.py` (guessing game), `choinka.py` (ASCII Christmas tree), `przestepne.py` (leap years) |

## ⭐ Worth a look

- 🎀 **`dekorator_time_suma_lst.py`** — a decorator that measures and prints a function's execution time
- 🔁 **`my_range.py`** / **`generator.py`** — a custom `range` built as an iterator and as a generator
- 🧮 **`reduce.py`** — mean, maximum and list-flattening expressed purely with `functools.reduce`
- 📐 **`figury.py`** / **`bryly.py`** — OOP class hierarchies for 2D shapes and 3D solids

## ▶️ Demo

The [demo runner](demo/main.py) presents a short example from each of the 26
exercises. It supplies sample input automatically for interactive scripts, so
the complete collection can be reviewed in one run:

```bash
python demo/main.py
```

## 🚀 Running

Each file is independent — run any exercise from the repository root:

```bash
python src/bisekcja.py
```

No external dependencies are required (Python 3 standard library only).

Run the regression tests with:

```bash
python -m unittest discover -s tests -v
```

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 👤 Author

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) · [LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
