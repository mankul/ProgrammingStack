from setuptools import setup, Extension
import numpy as np

module = Extension(
    name="MatrixOperations",
    sources=["matrix_operations.c"],
    include_dirs=[np.get_include()])
setup(name="MatrixOperations",
      version="1.0",
      description="Matrix Operations Module",
      ext_modules=[module])