# Dokumentacja techniczna

## Zakres i organizacja

Repozytorium jest zbiorem 26 niezależnych ćwiczeń Python, a nie jedną aplikacją
lub pakietem. Każdy plik `.py` w katalogu `src/` pokazuje wybrany temat z kursu
Paradygmaty programowania i korzysta wyłącznie z biblioteki standardowej.

| Obszar | Główne pliki |
|---|---|
| Własna iteracja | `my_range.py`, `generator.py`, `iterator.py`, `dekorator_my_range.py` |
| Styl funkcyjny | `reduce.py`, `wspolne.py`, `list_sum_rek.py` |
| Obiekty wartości i OOP | `fraction.py`, `figury.py`, `bryly.py`, `liczba.py`, `napis.py` |
| Algorytmy numeryczne | `bisekcja.py`, `pochodna.py`, `wariancja_srednia.py`, `wariancja rek.py` |
| Rekurencja/wyszukiwanie | `findA.py`, `findAv2.py`, `100comb.py` |
| Małe programy interaktywne | `kontakty.py`, `zgadujZgadula.py`, `choinka.py`, `krotki.py` |

Polskie nazwy i celowo zwarte implementacje są częścią materiału kursowego.
Repozytorium nie ma wspólnego stanu wykonania, instalowalnego pakietu ani usług
zewnętrznych.

## Kontrakty ćwiczeń wielokrotnego użytku

### Implementacje zakresu

`my_range.my_range`, `generator.generate`, `iterator.My_range` i wersja z
dekoratorem realizują przejście start/stop/krok dla dodatniego i ujemnego kroku.
Tak jak wbudowany `range`, granica stop jest wyłączna, a krok zero zgłasza
`ValueError`. Lista, generator i iterator celowo pokazują różne modele wykonania
i przechowywania.

### Funkcje w stylu funkcyjnym

`reduce.py` zawiera średnią, maksimum, spłaszczanie, wspólne litery i wstawianie
do posortowanej listy z użyciem `functools.reduce`. Puste wejście jest dozwolone
tam, gdzie istnieje naturalny pusty wynik, natomiast średnia i maksimum zgłaszają
`ValueError`.

### Obiekt ułamka

`fraction.Fraction` skraca licznik i mianownik przez NWD, zachowuje znak w
liczniku i odrzuca mianownik zero przez `ZeroDivisionError`.

### Parser polskich liczb

`liczba.fun` zamienia ograniczony słownik polskich liczb użyty w ćwiczeniu, w tym
jedności i dziesiątki takie jak `dwadzieścia jeden`. Błędne wejście zwraca
oryginalny komunikat `Nieprawidłowe dane`, zamiast zgłaszać wyjątek.

## Uruchamianie i zachowanie przy imporcie

Wybrane ćwiczenie uruchamia się z katalogu repozytorium:

```bash
python src/my_range.py
python 'src/wariancja rek.py'
```

Wszystkie ćwiczenia mają guard `if __name__ == "__main__":`, dzięki czemu runner
demonstracyjny może je wczytać bez uruchamiania pytań ani wypisywania wyników
podczas importu. Zachowanie interaktywne pozostaje bez zmian przy bezpośrednim
uruchomieniu skryptu.

Zwięzłą, nieinteraktywną demonstrację wszystkich ćwiczeń uruchamia polecenie:

```bash
python demo/main.py
```

## Testy automatyczne

```bash
python -m unittest discover -s tests -v
```

Sześć testów regresyjnych obejmuje:

- dodatnie i ujemne kroki czterech implementacji zakresu,
- odrzucanie kroku zero,
- funkcje `reduce` dla zwykłych, pustych i brzegowych danych,
- normalizację ułamka i mianownik zero,
- parser polskich jedności i dziesiątek.

Pozostałe programy interaktywne lub nastawione na wydruk nie mają testów
snapshot/integracyjnych.

## Zasady utrzymania i ograniczenia

- Należy zachować dydaktyczny cel każdego pliku i nie zmieniać zbioru w jeden
  framework lub pakiet.
- Zmiana testowanych funkcji pomocniczych powinna otrzymać skupiony test.
- Część algorytmów zakłada poprawne dane ćwiczeniowe i nie gwarantuje produkcyjnej
  walidacji ani wydajności.
- Komunikaty są głównie polskie i zależą od kodowania terminala.
- Nazwy należą do oryginalnego zadania, w tym spacja w `wariancja rek.py`; ścieżkę
  trzeba cytować w poleceniach.
- Efekty uboczne importu są udokumentowane i powinny być usuwane tylko wtedy, gdy
  dany plik naprawdę ma być bezpiecznie importowany lub testowany.
