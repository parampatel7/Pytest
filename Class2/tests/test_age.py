
#python3 -m pytest ran from inside the Class2 folder hence below statement has different path
import pytest

from samplecode.sample import validate_age

#Pass testcase
def test_validate_age_valid_age(): 
        validate_age(10)

#Failed testcase
def test_validate_age_valid_age(): 
        #Below statement tells pytest that an error is expected here, hence no need to flag it
#        with pytest.raises(ValueError) as exc_info:
#                validate_age(-10)
#        print("Exception message:", str(exc_info.value))
#        assert (str(exc_info.value)) == "Age cannot be less than 0"

#                #This will raise an error, as its correct case
#                #validate_age(10)

        #Below line will raise error as statement is not matched 
        with pytest.raises(ValueError, match = "Ag cannot be less than 0"):    
                validate_age(-1)
