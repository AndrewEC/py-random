# xorrandom
This python library is a POC predictable random number generator.

The implementation is based on the existing C implementation by David Blackman and Sebastiano Vigna:
https://prng.di.unimi.it/xoroshiro128plus.c

### Clone Repo
To clone the repository and all submodules using the Git CLI:
> git clone --recurse-submodules https://github.com/AndrewEC/py-random.git

### Playground
First run the powershell script CreateVenv.ps1 from the root of this project then run the run.py script:
> python run.py --help.

### Quality Metrics
To run the unit and integration tests simply run the CreateVenv.ps1 script the run the build script via: python build.py

This build script, in addition to the running the unit and mutation tests, will also generate coverage reports, install required dependencies, ensure a proper virtual environment is active, generate Sphinx docs, and run Flake8.

Separate mutation and unit test coverage reports will be generated at the following locations:

    Unit Tests - html/index.html
    Mutation Tests - html/index.html
