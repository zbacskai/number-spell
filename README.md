# number-spell

This tool takes an integer in the range of 0 to 100,000 and converts it into grammatically correct
British English words. Some examples:

```
./bin/numbers-to-words 52
fifty-two

./bin/numbers-to-words 1000
one thousand

./bin/numbers-to-words 101
one hundred and one

./bin/numbers-to-words 352
three hundred and fifty-two

./bin/numbers-to-words 12300
twelve thousand, three hundred

./bin/numbers-to-words 12345
twelve thousand, three hundred and forty-five
```

# Installation

To run the tool you need to install `Python >= 3.9.10`.

**NOTE:** The code has been tested running the above minimum Python version, but it shall be able to run on lower 
 Python versions.

# Run The Code

There is a wrapper script designed to be run on `Linux/Unix/MacOs` systems.

From the project base execute the following command:

`./bin/numbers-to-words < number >`

The number shall be a number between`0..100000`. `0` and `100000` included.

On Windows machines the above will not work, but you can run the following command.

`python ./bin/numbers-to-words < number >`

# Development

It is highly recommend to create a Python virtual environment. I use 
[pyenv](https://github.com/pyenv/pyenv/blob/master/README.md)
and 
[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv/blob/master/README.md) 
for development, but any other solution works.

## Install dependencies

`Setuptools` is used to install dependencies. Execute the following command:

`make install-dev`

## Run Tests
```
make test_integration
make test_unit
```

## Get MyPy Type Checks
`make mypy`

## Get Coverage Data
`make coverage`

The coverage data will be written to `coverage_html` directory. Open `index.html`

## Creating Distributable Binaries

Run

`./build-binary.sh`

This will generate a set of files distributable on any machine with the 
same OS and arch as yours, without installing `Python`. The files are 
stored in the following directory.

`dist/numbers-to-words/`