from setuptools import setup, find_packages
setup(
    name = "Streams",
    version = "0.1",
    setup_requires=['pytest-runner', 'sphinx==1.7.0'],
    tests_require=['pytest', 'pytest-cov'],
    packages=['streams'],
    zip_safe=True
)