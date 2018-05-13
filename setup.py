from setuptools import setup

from autocommit import __version__

setup(
    name='autocommit',
    version=__version__,
    author='Raja Simon',
    author_email='rajasimon@icloud.com',
    entry_points={
        'console_scripts': [
            "autocommit = autocommit.cli:CommandLineInterface.entrypoint"
        ]
    }
)