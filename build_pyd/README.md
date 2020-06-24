# Build PYD files

First of all, we created a sample, `class_for_test_pyd.py`, that there is a class and one dictionary in this py file.
We attempt to build a pyd file by `cythonize` via `setup`.

### Write a setup.py
Second, we still need to write a `setup.py` file. 

Format like: 

```
root_path = os.path.join(os.path.abspath(os.getcwd()))

py_list = ['all of your py files name in here.']

py_list = [os.path.join(root_path, name) for name in py_list]

setup(ext_modules=cythonize(py_list))
```

py_list need to put all of your py files name in here. Ex: `py_list = ['class_for_test_pyd.py']`

### Compile it

Third, we use python setup to build it.

**Command:**
```
python3 setup.py build_ext --inplace 
```

If you are on Linux, output should be like this :
`class_for_test_pyd.cpython-36m-x86_64-linux-gnu`

If you are on Windows, output should be like this :
`class_for_test_pyd.pyd`

### Check it

Let's do a simple test, so write a file named as `test.py`.

```
from class_for_test_pyd import *

a = ForTest()
a.test()
```

Implement it:

```
python3 test.py
```

Output:
```
Hello world!
```