import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="pyth-py",
    version="0.0.2",
    description="A basic framework for interacting with Solana's Pyth network",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/johnstonematt/pythpy",
    author="Matthew Johnstone",
    author_email="johnstone.mattjames@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "solana>=0.16.0",
    ]
)