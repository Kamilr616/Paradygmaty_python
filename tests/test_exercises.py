import contextlib
import io
import unittest

from dekorator_my_range import my_range as decorated_range
from fraction import Fraction
from generator import generate
from iterator import My_range
from liczba import fun as parse_polish_number
from my_range import my_range
from reduce import largest_el, list_add, mean, splaszcz, wspolne_litery


class RangeTests(unittest.TestCase):
    def test_positive_and_negative_steps_match_range_semantics(self):
        self.assertEqual([1, 3, 5], my_range(1, 7, 2))
        self.assertEqual([5, 3, 1], my_range(5, 0, -2))
        self.assertEqual([5, 3, 1], list(generate(5, 0, -2)))
        self.assertEqual([5, 3, 1], list(My_range(5, 0, -2)))

        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual([5, 3, 1], decorated_range(5, 0, -2))

    def test_zero_step_is_rejected(self):
        with self.assertRaises(ValueError):
            my_range(0, 5, 0)
        with self.assertRaises(ValueError):
            list(generate(0, 5, 0))
        with self.assertRaises(ValueError):
            My_range(0, 5, 0)
        with contextlib.redirect_stdout(io.StringIO()):
            with self.assertRaises(ValueError):
                decorated_range(0, 5, 0)


class FunctionalTests(unittest.TestCase):
    def test_reduce_exercises_cover_empty_and_boundary_inputs(self):
        self.assertEqual([], splaszcz([]))
        self.assertEqual([], wspolne_litery([]))
        self.assertEqual([1, 3, 5, 7], list_add([1, 3, 5], 7))
        self.assertEqual([1, 3, 4, 5], list_add([1, 3, 5], 4))
        self.assertEqual([1, 3, 5], list_add([1, 3, 5], 3))
        self.assertEqual(3, mean([1, 3, 5]))
        self.assertEqual(5, largest_el([1, 5, 3]))

    def test_empty_aggregates_are_rejected(self):
        with self.assertRaises(ValueError):
            mean([])
        with self.assertRaises(ValueError):
            largest_el([])


class ValueObjectTests(unittest.TestCase):
    def test_fraction_is_normalized_and_rejects_zero_denominator(self):
        self.assertEqual("1/2", str(Fraction(6, 12)))
        self.assertEqual("1/2", str(Fraction(-2, -4)))
        self.assertEqual("-1/2", str(Fraction(2, -4)))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_polish_number_parser_distinguishes_units_and_tens(self):
        self.assertEqual(1, parse_polish_number("jeden"))
        self.assertEqual(20, parse_polish_number("dwadzieścia"))
        self.assertEqual(21, parse_polish_number("dwadzieścia jeden"))
        self.assertEqual("Nieprawidłowe dane", parse_polish_number("czterdzieści 1"))


if __name__ == "__main__":
    unittest.main()
