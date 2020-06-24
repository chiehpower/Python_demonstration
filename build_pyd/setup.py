import os
from distutils.core import setup
from Cython.Build import cythonize

root_path = os.path.join(os.path.abspath(os.getcwd()))

py_list = ['class_for_test_pyd.py']

py_list = [os.path.join(root_path, name) for name in py_list]

setup(ext_modules=cythonize(py_list))
