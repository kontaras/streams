from setuptools import setup, find_packages
import sys

_py_major, _py_minor, _py_release, _py_level, _py_serial = sys.version_info

setup_reqs = []
if _py_major == 2 and _py_minor == 6:
    setup_reqs.append('pytest-runner==2.12.2')
else:
    setup_reqs.append('pytest-runner')

if (_py_major == 2 and _py_minor == 6) or (_py_major == 3 and _py_minor == 3):
    setup_reqs.append('sphinx==1.4.9')
elif _py_major == 3 and _py_minor == 2:
    setup_reqs.append('sphinx==1.2.3')
else:
    setup_reqs.append('sphinx')



tests_reqs = []
if _py_major == 2 and _py_minor == 6:
    tests_reqs.append('pytest=3.2.5')
else:
    tests_reqs.append('pytest')
tests_reqs.append('pytest-cov')

setup(
    name = "Streams",
    version = "0.1",
    setup_requires=setup_reqs,
    tests_require=tests_reqs,
    packages=['streams'],
    zip_safe=True
)