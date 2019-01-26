# MurmurHash3 was written by Austin Appleby, and is placed in the public domain.
# mmh3 Python module was written by Hajime Senuma, and is also placed in the public domain.
# The authors hereby disclaim copyright to these source codes.

# Edited based on https://github.com/honnibal/mmh3 to allow Sentry installation on OSX 10.7+

from sys import platform as _platform
from setuptools import setup, Extension

COMPILE_OPTIONS = []
LINK_OPTIONS = []

if _platform == "darwin":
    COMPILE_OPTIONS.append("-stdlib=libc++")
    COMPILE_OPTIONS.append("-mmacosx-version-min=10.7")
    LINK_OPTIONS.append("-lc++")
    LINK_OPTIONS.append("-nodefaultlibs")

mmh3module = Extension('mmh3',
                       sources = ['mmh3module.cpp', 'MurmurHash3.cpp'],
                       extra_compile_args=COMPILE_OPTIONS,
                       extra_link_args=LINK_OPTIONS)

setup(name = 'mmh3',
    version = '2.3.1',
    description = 'Python library for MurmurHash (MurmurHash3), a set of fast and robust hash functions.',
    license = 'Public Domain',
    author = 'Hajime Senuma',
    author_email = 'hajime.senuma@gmail.com',
    url = 'http://packages.python.org/mmh3',
    ext_modules = [mmh3module],
    keywords = "utility hash MurmurHash",
    long_description = open('README.rst').read(),
    classifiers = ['Development Status :: 5 - Production/Stable',
    'Intended Audience :: Developers',
    'License :: Public Domain',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Topic :: Utilities']
)
