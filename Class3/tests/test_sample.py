import sys

from samplecode.sample import add
import pytest

def test_add_num(): 
    assert add(1,3) == 4

#Below test will be skipped
@pytest.mark.skip(reason="Just wanted to skip")
def test_add_str():     
    assert add("a", "b") == "abm"
#Have a look in the terminal, it shows .s.. means second test is skipped
# It will show FS.. if first test fails

@pytest.mark.skipif(sys.version_info > (3, 12), reason="Skipped the condditional test")
def test_add_str_conditional_skip():     
    assert add("a", "b") == "ab"

#xfail is used when test can throw some exceptions but you want to continue
#Will not throw exception as we are on windows.
@pytest.mark.xfail(sys.platform == "linux", reason = "Don't run on linux")
#@pytest.mark.xfail(sys.platform == "win32", reason = "Don't run on windows") #Throws exception errors
def test_add_list():      
    assert add([1], [2]) == [1, 2]
    raise Exception()

class TestSample:
    def test_add_num(self): 
        assert add(1,3) == 4

    def test_add_str(self):     
        assert add("a", "b") == "ab"