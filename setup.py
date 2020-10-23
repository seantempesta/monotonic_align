from setuptools import setup, find_packages
from Cython.Build import cythonize
import numpy

setup(
    name='monotonic_align',
    packages=find_packages(),
    ext_modules=cythonize("core.pyx"),
    include_dirs=[numpy.get_include()],
    install_requires=[
        'Cython',
        'numpy',
        'torch'
    ]
)
