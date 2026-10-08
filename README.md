# python-crash-course

My first ever interaction with a programming language: exercise scripts I wrote while working through the book *Python Crash Course*.

**Note:** This repository is archived and read-only.

Each script opens with a comment banner ("Hi! I'm Mister B ...") that numbers the program in the order it was written and names the book chapter it follows. They are plain Python 3 files with no dependencies, tabs for indentation and inline notes taken while learning.

## Contents

Chapter numbers are copied from each file's header comment and may differ between editions of the book.

- **`hello_world.py`**, **`cc_hello_world.py`** — First program, variables and strings (chapter 2)
- **`cc_lists.py`** — Lists (chapters 2 and 3)
- **`cc_loops.py`** — Looping (chapter 4)
- **`cc_if.py`** — `if` statements (chapter 5)
- **`cc_dictionaries.py`** — Dictionaries (chapter 6)
- **`cc_input.py`**, **`cc_while.py`** — User input and `while` loops (chapter 7)
- **`cc_functions.py`**, **`cc_modules.py`** — Functions, and functions in modules (`make_pizza`) (chapter 8)
- **`cc_classes.py`**, **`cc_modules_0.py`**, **`cc_modules_1.py`**, **`cc_modules_2.py`** — Classes, and classes across modules (chapter 9)
- **`cc_files.py`**, **`pi_digits.txt`** — Files and exceptions, and the data file it reads (chapter 10)

## Usage

Any Python 3 interpreter works. Run scripts from this directory: `cc_files.py` needs `pi_digits.txt`, and `cc_modules_2.py` imports `Car` from `cc_modules_1`.

```sh
python3 cc_hello_world.py
python3 cc_files.py
```
