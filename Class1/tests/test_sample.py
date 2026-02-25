from Class1.samplecode.sample import add
# Make sure to name this file starting from test_ else pytest would show collected 0 items
#use python3 -m pytest to to run testfile

def test_add_num(): #function name must start with test_
    assert add(1,3) == 4

def test_add_str():     
    assert add("a", "b") == "ab"
    #Fail test case, look at the result
    #assert add("a", "m") == "ab"


#Name must start with Test else it won't be collected by pytest
#class SampleTest:  #Won't be collected
class TestSample:
    def test_add_num(self): 
        assert add(1,3) == 4

    def test_add_str(self):     
        assert add("a", "b") == "ab"