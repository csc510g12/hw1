import sys

def test_fail_on_specific_py_version():
    if sys.version_info < (3, 10):
        raise Exception("Python version is too old")