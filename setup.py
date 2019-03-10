from setuptools import setup, find_packages
import sys

_py_major, _py_minor, _py_release, _py_level, _py_serial = sys.version_info

setup_reqs = []
tests_reqs = []

print("Python version")
print(_py_major, _py_minor, _py_release, _py_level, _py_serial)

setup_reqs.append('pytest==3.2.5')

setup_reqs.append('pytest-runner==2.5.1')


setup_reqs.append('sphinx==1.2.3')

tests_reqs.append('pytest-cov==2.5.1')

setup(
    name = "Streams",
    version = "0.1",
    setup_requires=setup_reqs,
    tests_require=tests_reqs,
    packages=['streams'],
    zip_safe=True
)