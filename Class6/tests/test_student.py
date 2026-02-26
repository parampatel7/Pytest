import pytest
from datetime import datetime
from sampecode.student import Studentz

#create a custom fixture
 
#if scope= module is not added, default scope is function, hence this pytest fixture is created for each function
#This pytest fixture will be called every time a unit test function runs

@pytest.fixture(scope="module")
def dummy_student():
    print("Making dummy student")
    return Studentz("Param", datetime(2002,9,7,), "coe")


def test_Studentz_get_age(dummy_student):
     dummy_student_age = (datetime.now() - dummy_student.dob).days 
     assert dummy_student.get_age() == dummy_student_age

     
def test_Studentz_add_credits(dummy_student):
     dummy_student.add_credits(5)
     assert dummy_student.get_credits() == 5
    
#This case will fail as credits = 5. Because it inherits above executed values.
#Had scope=function been added, each function will create a student hence passing a newly created student, 
#   this will pass below test case
def test_Studentz_get_credits(dummy_student):
     assert dummy_student.get_credits() == 0
