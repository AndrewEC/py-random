from unittest import TestCase

from xorrandom import Xor128Prng


class Xor128PrngTests(TestCase):

    _UPPER_LIMIT = 1000
    _LOWER_LIMIT = 100
    _ITERATION_COUNT = 100

    def test_initialize_generator_with_invalid_seed_raises_exception(self):
        with self.assertRaises(ValueError) as context1:
            Xor128Prng(None)
        self.assertEqual('seed argument cannot be None.', str(context1.exception))

        with self.assertRaises(ValueError) as context2:
            Xor128Prng(0)
        self.assertEqual('seed argument cannot be zero.', str(context2.exception))

    def test_generate_number_with_invalid_bounds(self):
        generator = Xor128Prng(1)

        with self.assertRaises(ValueError) as context1:
            generator.next(None, 1)
        self.assertEqual('The \'upper\' bound cannot be None when a \'lower\' bound has been specified.', str(context1.exception))

        with self.assertRaises(ValueError) as context2:
            generator.next(1, 2)
        self.assertEqual('The \'lower\' bound must be less than the \'upper\' bound.', str(context2.exception))

    def test_generate_number_within_upper_limit(self):
        for i in range(Xor128PrngTests._ITERATION_COUNT):
            generator = Xor128Prng(i + 1)
            for j in range(Xor128PrngTests._ITERATION_COUNT):
                number = generator.next(1000)
                self.assertLess(number, 1000)

    def test_generate_number_within_upper_and_lower_limit(self):
        for i in range(Xor128PrngTests._ITERATION_COUNT):
            generator = Xor128Prng(i + 1)
            for j in range(Xor128PrngTests._ITERATION_COUNT):
                number = generator.next(1000, 100)
                self.assertLess(number, 1000)
                self.assertGreaterEqual(number, 100)

    def test_same_results_with_same_seed(self):
        for i in range(Xor128PrngTests._ITERATION_COUNT):
            generator1 = Xor128Prng(i + 1)
            generator2 = Xor128Prng(i + 1)
            for j in range(Xor128PrngTests._ITERATION_COUNT):
                first = generator1.next()
                second = generator2.next()
                self.assertEqual(first, second)

    def test_different_results_with_different_seed(self):
        for i in range(Xor128PrngTests._ITERATION_COUNT):
            generator1 = Xor128Prng(i + 1)
            generator2 = Xor128Prng((i + 1) * 2)
            for j in range(Xor128PrngTests._ITERATION_COUNT):
                first = generator1.next()
                second = generator2.next()
                self.assertNotEqual(first, second)

    def test_random_number_distribution(self):
        for i in range(Xor128PrngTests._ITERATION_COUNT):
            generator = Xor128Prng(i + 1)
            numbers = set()
            for j in range(Xor128PrngTests._ITERATION_COUNT):
                numbers.add(generator.next(100))
            self.assertGreaterEqual(len(numbers), 50)
