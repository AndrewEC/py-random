from xorrandom import Xor128Prng


def main():
    generator = Xor128Prng(20)
    for i in range(10):
        print(generator.next(0, 100))


if __name__ == '__main__':
    main()
