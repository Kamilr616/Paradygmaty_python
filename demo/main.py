import builtins
import importlib.util
import sys
from contextlib import contextmanager
from pathlib import Path


SOURCE_DIR = Path(__file__).resolve().parents[1] / 'src'
sys.path.insert(0, str(SOURCE_DIR))


def load_exercise(filename):
    '''Load scripts even when their filenames are not valid module names.'''
    path = SOURCE_DIR / filename
    module_name = 'demo_' + path.stem.replace(' ', '_')
    spec = importlib.util.spec_from_file_location(module_name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f'Cannot load {path}')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@contextmanager
def supplied_input(*answers):
    '''Supply predefined answers to functions which call input().'''
    iterator = iter(answers)
    original_input = builtins.input

    def fake_input(prompt=''):
        answer = next(iterator)
        print(f'{prompt}{answer}')
        return answer

    builtins.input = fake_input
    try:
        yield
    finally:
        builtins.input = original_input


def call_with_input(function, *answers):
    with supplied_input(*answers):
        return function()


def show(filename, example):
    print(f'\n=== {filename} ===')
    result = example(load_exercise(filename))
    if result is not None:
        print(result)


def guessing_game(module):
    original_randint = module.randint
    module.randint = lambda _start, _stop: 7
    try:
        call_with_input(module.main, '3', '7')
    finally:
        module.randint = original_randint


def main():
    show('100comb.py', lambda module: module.main())
    show('bisekcja.py', lambda module: module.bisekcja(module.wielomian, -10, 10))
    show('bryly.py', lambda module: module.Cube('Szescian', 3).get_area())
    show('choinka.py', lambda module: call_with_input(module.main, '7'))
    show('dekorator_my_range.py', lambda module: module.my_range(1, 5))
    show(
        'dekorator_time_suma_lst.py',
        lambda module: module.list_sum_iter([1, 2, 3, 4]),
    )
    show('figury.py', lambda module: module.Circle('Kolo', 2).get_area())
    show('findA.py', lambda module: call_with_input(module.main, 'Ala ma kota'))
    show('findAv2.py', lambda module: call_with_input(module.main, 'Ala'))
    show(
        'fraction.py',
        lambda module: module.Fraction(1, 2) + module.Fraction(1, 3),
    )
    show('generator.py', lambda module: list(module.generate(1, 6, 2)))
    show('iterator.py', lambda module: list(module.My_range(5, 0, -2)))
    show(
        'kontakty.py',
        lambda module: module.fun(
            {('Jan', 'Kowalski'): '123456789', ('Anna', 'Kowalska'): '987654321'},
            'Kowalski',
        ),
    )
    show('krotki.py', lambda module: module.suma([(1, 2), (3, 4)]))
    show('liczba.py', lambda module: module.fun('dwadzieścia jeden'))
    show('liczyPierwsze.py', lambda module: call_with_input(module.main, '10'))
    show('list_sum_rek.py', lambda module: module.list_sum([1, 2, 3, 4]))
    show('my_range.py', lambda module: module.my_range(0, 5, 2))
    show('napis.py', lambda module: module.napis('2026'))
    show(
        'pochodna.py',
        lambda module: module.derivative(module.kwadrat, 3),
    )
    show('przestepne.py', lambda module: module.fun(1996, 2024))
    show(
        'reduce.py',
        lambda module: (module.mean([1, 2, 3, 4]), module.splaszcz([[1, 2], [3, 4]])),
    )
    values = [5, 6, 7, 8, 9]
    show(
        'wariancja rek.py',
        lambda module: module.fun(values, len(values)),
    )
    show('wariancja_srednia.py', lambda module: module.fun(values))
    show('wspolne.py', lambda module: module.wspolne([1, 2, 3], [2, 3, 4]))
    show('zgadujZgadula.py', guessing_game)


if __name__ == '__main__':
    main()
