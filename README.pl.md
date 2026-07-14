# 🐍 Paradygmaty Programowania — zadania w Pythonie

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Licencja: MIT](https://img.shields.io/badge/Licencja-MIT-yellow.svg)](LICENSE)

> 🇬🇧 [English version](README.md)

> 🗓️ **Okres realizacji:** 2023

> 📘 [Dokumentacja techniczna](docs/TECHNICAL_DOCUMENTATION.pl.md)

Zbiór rozwiązanych zadań z przedmiotu **Paradygmaty Programowania**. Większość skryptów to samodzielne rozwiązania demonstrujące konkretny koncept Pythona — od podstawowych algorytmów i rekurencji, przez programowanie obiektowe, po iteratory, generatory, dekoratory i programowanie funkcyjne. Kurs obejmował style **imperatywny, obiektowy i funkcyjny** w Pythonie, więc repo stanowi też zwięzły przegląd tych podstaw.

Wszystkie skrypty z ćwiczeniami znajdują się w katalogu `src/`.

## 📚 Omawiane zagadnienia

| Zagadnienie | Przykładowe skrypty |
|-------------|---------------------|
| **Algorytmy i matematyka** | `bisekcja.py` (metoda bisekcji), `pochodna.py` (pochodna), `liczyPierwsze.py` (liczby pierwsze), `100comb.py`, `wariancja_srednia.py` (wariancja/średnia), `wariancja rek.py` (wariancja rekurencyjnie) |
| **Rekurencja** | `list_sum_rek.py`, `findA.py` / `findAv2.py` |
| **Programowanie obiektowe** | `figury.py` (figury 2D), `bryly.py` (bryły 3D), `fraction.py` (ułamki), `liczba.py`, `napis.py` |
| **Iteratory i generatory** | `iterator.py`, `generator.py`, `my_range.py` |
| **Dekoratory** | `dekorator_my_range.py`, `dekorator_time_suma_lst.py` (dekorator mierzący czas) |
| **Programowanie funkcyjne** | `reduce.py` (średnia, maksimum i spłaszczanie listy przez `functools.reduce`) |
| **Struktury danych** | `krotki.py`, `kontakty.py` (książka kontaktów), `wspolne.py` (elementy wspólne) |
| **Małe programy** | `zgadujZgadula.py` (zgadywanka), `choinka.py` (choinka ASCII), `przestepne.py` (lata przestępne) |

## ⭐ Warte uwagi

- 🎀 **`dekorator_time_suma_lst.py`** — dekorator mierzący i wypisujący czas wykonania funkcji
- 🔁 **`my_range.py`** / **`generator.py`** — własne `range` jako iterator i jako generator
- 🧮 **`reduce.py`** — średnia, maksimum i spłaszczanie listy wyłącznie przez `functools.reduce`
- 📐 **`figury.py`** / **`bryly.py`** — obiektowe hierarchie klas dla figur 2D i brył 3D

## ▶️ Demo

[Runner demonstracyjny](demo/main.py) prezentuje krótki przykład z każdego z 26
ćwiczeń. Dla skryptów interaktywnych automatycznie podaje przykładowe dane, dzięki
czemu cały zbiór można obejrzeć podczas jednego uruchomienia:

```bash
python demo/main.py
```

## 🚀 Uruchamianie

Każdy plik jest niezależny — dowolne zadanie uruchomisz z katalogu repozytorium:

```bash
python src/bisekcja.py
```

Nie są wymagane żadne zewnętrzne zależności (wyłącznie biblioteka standardowa Pythona 3).

Testy regresyjne uruchomisz poleceniem:

```bash
python -m unittest discover -s tests -v
```

## 📄 Licencja

Projekt udostępniony na licencji [MIT](LICENSE).

## 👤 Autor

**Kamil Rataj** — [GitHub](https://github.com/Kamilr616) · [LinkedIn](https://www.linkedin.com/in/kamil-r-153ab7121/)
