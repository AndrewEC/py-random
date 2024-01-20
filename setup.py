from setuptools import setup

if __name__ == '__main__':
    setup(
        name='xorrandom',
        version='1.0',
        description='A POC implementation of a predictable, pseudo-random, number generator.',
        author='Andrew Cumming',
        author_email='andrew.e.cumming@gmail.com',
        url='https://github.com/AndrewEC/py-random',
        packages=['xorrandom', 'xorrandom.lib']
    )
