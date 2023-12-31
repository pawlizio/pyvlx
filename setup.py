"""Module for setting up PyVLX pypi object."""
import os
from os import path

from setuptools import find_packages, setup

REQUIRES = ["PyYAML"]

PKG_ROOT = os.path.dirname(__file__)

VERSION = "0.2.21"


def get_long_description() -> str:
    """Read long description from README.md."""
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, "README.md"), encoding="utf-8") as readme:
        long_description = readme.read()
        return long_description


setup(
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
)
