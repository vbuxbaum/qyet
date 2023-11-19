"""Main module."""


import contextlib
import functools
import os
from typing import Any, Callable

"""Top-level package for qyet."""

__author__ = """Vitor Buxbaum"""
__email__ = 'vitorbuxbaum@gmail.com'
__version__ = '0.1.2'


def shhh(func: Callable[[Any], Any]) -> Callable[[Any], Any]:
    """Silence stdout. Use this as a decorator.

    Example:

    >>> @shhh
    >>> def my_loud_function(param1, param2):
    >>>     ...
    """

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with open(os.devnull, 'w') as student_output:
            with contextlib.redirect_stdout(student_output):
                return func(*args, **kwargs)

    return wrapper
