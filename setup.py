from setuptools import setup, find_packages
setup(
    name = "Streams",
    version = "0.1",
    setup_requires=['pytest-runner', 'setuptools_scm'],
    tests_require=['pytest', 'pytest-cov'],
    use_scm_version=True,
    packages=['streams']
)