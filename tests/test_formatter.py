import pytest

from formatter2 import Formatter


@pytest.mark.xfail(SyntaxError)
def test_syntax_error():
    Formatter.format_string('a = '),

if __name__ == '__main__':
    from .base_test import main
    main('-vv')

