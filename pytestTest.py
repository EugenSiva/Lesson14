import pytest

from main import Calc

def test_add_positive():
    calc = Calc()
    assert calc.add(1,2) == 3