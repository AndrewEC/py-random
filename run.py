import click

from xorrandom import Xor128Prng


@click.command('generate')
@click.argument('seed', type=int)
@click.option('--number-of-numbers', '-n', default=10, help='Specifies the number of random numbers to generate.', type=int)
@click.option('--maximum', '-max', help='Specifies the max value that each random number can have (exclusive).', type=int)
@click.option('--minimum', '-min', help='Specifies the min value that each random number can have (inclusive).', type=int)
def generate(seed: int, number_of_numbers: int, maximum: int, minimum: int):
    if number_of_numbers <= 0:
        raise ValueError('The number-of-numbers must be value greater than 0')

    generator = Xor128Prng(seed)
    for i in range(number_of_numbers):
        print(generator.next(maximum, minimum))


if __name__ == '__main__':
    generate()
