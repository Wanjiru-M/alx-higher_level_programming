# Alx-Higher_Level_Programming

This repository contains Python scripts for the Alx Higher Level Programming course. It includes modules, classes, and functions that have been unit tested and follow the PEP 8 coding style guidelines.

## Table of Contents

- [File Structure and Editors](#file-structure-and-editors)
- [Coding Style and Execution](#coding-style-and-execution)
- [Documentation](#documentation)
- [Python Unit Tests](#python-unit-tests)

## File Structure and Editors

- All files in this project should be edited using vi, vim, or emacs.
- The first line of every file should be `#!/usr/bin/python3`.
- All files must end with a new line.
- The project folder structure should be organized as follows:
alx-higher_level_programming/
├── module1/
│ ├── file1.py
│ ├── file2.py
│ └── ...
├── module2/
│ ├── file1.py
│ ├── file2.py
│ └── ...
├── tests/
│ ├── test_module1/
│ │ ├── test_file1.py
│ │ ├── test_file2.py
│ │ └── ...
│ ├── test_module2/
│ │ ├── test_file1.py
│ │ ├── test_file2.py
│ │ └── ...
└── README.md
## Coding Style and Execution

- The pycodestyle (version 2.8.*) tool is used to validate the coding style.
- All files should be executable.
- The Python scripts are interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.8.5).
- File lengths are tested using the `wc` command.

## Documentation

- All modules, classes, and functions are documented with real sentences explaining their purpose.
- You can check the documentation for a module, class, or function using the following commands:
- `python3 -c 'print(__import__("my_module").__doc__)'` for modules.
- `python3 -c 'print(__import__("my_module").MyClass.__doc__)'` for classes.
- `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and
  `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'` for functions.

## Python Unit Tests

- Unit tests for all files, classes, and methods are provided in the `tests` folder.
- The `unittest` module is used for writing and executing the tests.
- All test files and folders start with the prefix `test_`.
- To run all the tests, use the command: `python3 -m unittest discover tests`.
- To run tests for a specific file, use the command: `python3 -m unittest tests/test_module/test_file.py`.
