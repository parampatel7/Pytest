
import time
from unittest import result

import pytest

#Below line can be used to import every function of another file insted of doing
#from samplecode.sample import add_my, divide_my
import samplecode.sample as samplepy_function


def test_add():
    result= samplepy_function.add_my(4,3)
    assert result == 7

def test_add_strings():
    result = samplepy_function.add_my("I am", " Param Patel")
    assert result == "I am Param Patel"

def test_div():
    result= samplepy_function.divide_my(8,2)
    assert result == 4

def test_div_by_zero():
    #with pytest.raises(ZeroDivisionError):
    with pytest.raises(ValueError):     
        x = samplepy_function.divide_my(10, 0)

#Added below line to indicate this is a slow test
#To test slow test use: python3 -m pytest slow //not working currently need to find
@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result= samplepy_function.divide_my(8,2)
    assert result == 4    

@pytest.mark.skip(reason="Skipping the test")
def test_add():
    assert samplepy_function.add_my(1,4) == 5

@pytest.mark.xfail(reason="Cannot divide by zero")
def test_divide_zero_broken():
    samplepy_function.divide_my(4, 0)
