from samplecode.sample import add
import pytest

def test_add_num(): 
    assert add(1,3) == 4

def test_add_str():     
    assert add("a", "b") == "ab"

def test_add_list():   
    assert add([1,2], [3]) == [1,2,3]

#a,b,c are parameters passed with values in (). Hence total collected test will be numbered accordingly
@pytest.mark.parametrize("a,b,c", [(5,2,7),("x", "y", "xy"), ([1,2], [3], [1,2,3])], ids=["num", "str", "list"])
def test_add(a,b,c):
    assert add(a,b) == c