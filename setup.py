from setuptools import find_packages, setup

# format 'dependency~=MAJOR.MINOR' ensures that only MAJOR version is locked

install_requires = []

dev_requires = [
    "pytest",
    "pyinstaller",
    "coverage"
]

setup(
    name="number-spell",
    version="0.0.1",
    url="git@github.com:zbacskai/number-spell.git",
    author="Zoltan Bacskai",
    author_email="z.bacskai.jr@gmail.com",
    description="A simple CLI to spell numbers in British English",
    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=install_requires,
    setup_requires=["pytest-runner"],
    tests_require=dev_requires,
    extras_require={"dev": dev_requires},
)
