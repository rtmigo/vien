# [svet](https://github.com/rtmigo/svet#readme)

[![Generic badge](https://img.shields.io/badge/ready_for_use-maybe-orange.svg)](#)
[![PyPI version shields.io](https://img.shields.io/pypi/v/svet.svg)](https://pypi.python.org/pypi/svet/)
[![Actions Status](https://github.com/rtmigo/svet/workflows/CI/badge.svg?branch=master)](https://github.com/rtmigo/svet/actions)
[![Generic badge](https://img.shields.io/badge/CI_OS-MacOS,_Ubuntu-blue.svg)](#)
[![Generic badge](https://img.shields.io/badge/CI_Python-3.7--3.9-blue.svg)](#)

SVET is an acronym for Simple Virtual Environments Tool.

It provides command-line shortcuts for managing Python [virtualenvs](https://docs.python.org/3/library/venv.html).

# Why

Switching between different projects in Python should be simple. A short command 
that I would type even half asleep.

Something like
```base
$ svet create 
$ svet shell
```

And definitely not like
```base
$ python3 -m venv ./i/have/no/idea/where/to/put/this/.venv
$ source /where/is/that/damn/directory/.venv/bin/activate
$ /omg/forget/it/i/will/not/.venv/bin/deactivate
```


<details>
  <summary>[click to open] Ready-made solutions did not help.</summary><br/>


I tried [pipenv](https://pipenv.pypa.io/). It kind of solved the problem, but also brought new 
challenges that dwarfed the old ones. I did not sign up to this. I just wanted to manage virtualenvs.

I also tried [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/). 
A package whose name is easier to copy than to type. I hoped it was only a name. Alas, this is the philosophy of the whole package.

</details>

So I made `svet`. A stupidly simple tool for a half asleep developer.

# What is does

`svet` offers a simple rule of where to place the virtualenv.

|project dir|virtualenv dir|
|-----|----|
|`/abc/thisProject`|`$HOME/.svet/thisProject_venv`|
|`/abc/otherProject`|`$HOME/.svet/otherProject_venv`|
|`/moved/to/otherProject`|`$HOME/.svet/otherProject_venv`|

So only the local name of the project directory matters. And all the virtualenvs 
are in `$HOME/.svet`. Until you decide to [change this dir](#vepdir).

# Install

Get a working [Python](https://www.python.org/) ≥3.7 and [pip](https://pip.pypa.io/en/stable/installing/). You may also need a computer. Then:

```bash
$ pip3 install svet
```

create sure that it is installed:

```bash
$ svet --help
```

Upgrade it later:
```bash
$ pip3 install svet --upgrade
```


# Usage

### Create a new virtualenv

```bash
$ cd /path/to/myProject
$ svet create 
```

By default `svet` will try to use `python3` as the interpreter will be used for virtualenv. If you have 
more than one Python version, just point to the proper binary the way you execute it:

```bash
$ svet create python3.8
```
```bash
$ svet create /path/to/bin/python3
```

### Run a python script inside the virtualenv 
```bash 		
$ cd /path/to/myProject
$ svet run python ./my_program.py arg1 arg2 ...
```

<details>
  <summary>is an equivalent to</summary><br/>

```bash 		
$ cd /path/to/myProject
$ source /path/to/the/venv/bin/activate
$ python ./my_program.py arg1 arg2 ...
$ /path/to/the/venv/bin/deactivate
```
</details>

### Run a bash subshell inside the virtualenv 
```bash	
$ cd /path/to/myProject
$ svet shell
```

# The `$SVETDIR`

You can set the directory where `svet` places the virtualenvs. By default, it's `$HOME/.svet`. If you're not happy with this, you can define the environment variable `SVETDIR`:
```bash
$ export SVETDIR="/x/y/z"
```
So for the project `aaa` the virtualenv will be located in `/x/y/z/aaa_venv`.

The `_venv` suffix tells the utility that this directory can be safely removed.

# Other commands

### Delete virtualenv

```bash
$ cd /path/to/myProject
$ svet delete 
```

### Delete old and create new virtualenv

Useful, when you want to start from scratch.
```bash
$ cd /path/to/myProject
$ svet recreate 
```
Optionally point to the interpreter:
```bash
$ cd /path/to/myProject
$ svet recreate /path/to/bin/python3
```

