import pytest
from datetime import datetime
from sampecode.student import Studentz
from sampecode.student import is_eligible_for_degree

#create a factory fixture



def test_student_is_eligible_for_degree_true(make_dummy_student):
     assert is_eligible_for_degree(make_dummy_student("P", 19)) is False

def test_student_is_eligible_for_degree_false(make_dummy_student):
     assert is_eligible_for_degree(make_dummy_student("P", 23)) is True    

@pytest.mark.parametrize("credits, expected", [(19, False), (21, True)])
def test_student_is_eligible_for_degree(make_dummy_student, credits, expected):
     assert is_eligible_for_degree(make_dummy_student("P", credits)) is expected  

#provided a fixture as a parameter
@pytest.mark.parametrize("dummy_student, expected", [(19, False), (21, True)],
                          indirect=["dummy_student"], ids=["ineligible", "eligible"])
def test_student_is_eligible_for_degree(dummy_student, expected):
     assert is_eligible_for_degree(dummy_student) is expected  