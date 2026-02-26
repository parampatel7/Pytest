import pytest
from datetime import datetime
from sampecode.student import Studentz, get_topper

#create a factory fixture


def test_Studentz_get_age(dummy_student):
     dummy_student_age = (datetime.now() - dummy_student.dob).days 
     assert dummy_student.get_age() == dummy_student_age

def test_Studentz_get_credits(dummy_student):
     assert dummy_student.get_credits() == 20

def test_get_topper(make_dummy_student):
     students= [
          make_dummy_student("ram", 21),
          make_dummy_student("Ram", 22),
          make_dummy_student("RAM", 20)
     ]
     topper = get_topper(students)
     assert topper == students[1]