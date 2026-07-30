# Python 2 line. setup.py rather than pyproject.toml is itself the signal: the
# 2.7 toolchain predates PEP 621, so the version constraint lives here.
from setuptools import setup, find_packages

setup(
    name="zedtest-multiversion-lib-py2",
    version="0.1.0",
    description="Python 2 line of multiversion-lib",
    license="MIT",
    packages=find_packages(),
    python_requires=">=2.7, <3",
)
