from setuptools import setup, find_packages
setup(
    name = "Streams",
    version = "0.1",
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    packages=['streams']
)