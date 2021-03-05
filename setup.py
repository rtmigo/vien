from importlib.machinery import SourceFileLoader
from pathlib import Path

from setuptools import setup, find_packages

constants = SourceFileLoader('constants', 'vep/constants.py').load_module()

setup(
  name="svet",
  version=constants.__version__,

  author="Art Galkin",
  author_email="ortemeo@gmail.com",
  url='https://github.com/rtmigo',

  packages=find_packages(),
  install_requires=[],

  description="Command-line shortcuts for Python virtual environments",

  long_description=(Path(__file__).parent / 'README.md').read_text(),
  long_description_content_type='text/markdown',

  license='BSD-3-Clause',

  entry_points={
    'console_scripts': [
      'svet = svet:runmain',
    ]},

  keywords="""
     virtual-environment venv virtualenv python
  	""".split(),

  # https://pypi.org/classifiers/
  classifiers=[
    # "Development Status :: 4 - Beta",
    # "Development Status :: 2 - Pre-Alpha",
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    'License :: OSI Approved :: BSD License',
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Typing :: Typed",
    "Topic :: Software Development :: Build Tools",
    "Operating System :: POSIX"
  ],

  # test_suite='nose.collector',
  # tests_require=['nose'],
  #zip_safe=False
)