class Xor128Prng:

    """
    A predictable pseudo-random number generator. The predictable nature of this means that, even if multiple
    instances of this generator are created, they will all generate the same random numbers as long as all generators
    were initialized with the same seed.

    Based on the existing implementation by David Blackman and Sebastiano Vigna:
    https://prng.di.unimi.it/xoroshiro128plus.c
    """

    def __init__(self, seed: int):
        """
        Initializes the seeded random number generator.

        :param seed: The value to initialize the random number generator to. This value cannot be None or zero but
            can be a negative number.
        """

        if seed is None:
            raise ValueError('seed argument cannot be None.')
        elif seed == 0:
            raise ValueError('seed argument cannot be zero.')

        self._s = [0, 0]
        self._s[0] = seed
        self._s[1] = seed
        for i in range(seed):
            self.next()

    def next(self, upper: int | None = None, lower: int | None = None) -> int:
        """
        Generate a pseudo-random number greater than or equal to the lower bound and less than, not equal to,
        the upper bound.

        If the lower bound has been specified then the upper bound must also be specified.

        The upper bound can be specified on its own.

        :param lower: The minimum value the number can be (inclusive). If the value of this argument is not
            None then it must the upper argument must also be provided with a value that is not None.
        :param upper: The maximum value the number can be (exclusive). This can be specified without the lower bound.
        :return: A random number with a value between the lower and upper limits
        """

        s0 = self._s[0]
        s1 = self._s[1]
        result = s0 + s1

        s1 = s1 ^ s0
        self._s[0] = self._rotl(s0, 24) ^ s1 ^ (s1 << 16)
        self._s[1] = self._rotl(s1, 37)
        return self._keep_in_range(result, lower, upper)

    def _keep_in_range(self, result: int, lower: int | None, upper: int | None) -> int:
        if lower is None:
            if upper is None:
                return result
            return result % upper
        else:
            if upper is None:
                raise ValueError('The \'upper\' bound cannot be None when a \'lower\' bound has been specified.')
            else:
                if lower >= upper:
                    raise ValueError('The \'lower\' bound must be less than the \'upper\' bound.')
                return result % (upper - lower) + lower

    def _rotl(self, x: int, k: int) -> int:
        return x << k | x >> (64 - k)
