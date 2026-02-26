#File with name conftest can be used to store fixtures

from datetime import datetime
import pytest
from sampecode.student import Studentz


@pytest.fixture
def dummy_student():
    return Studentz("Param", datetime(2002,9,7,), "coe", 20)

@pytest.fixture
def make_dummy_student():
     def _make_dummy_student(name, credit):
          return Studentz(name, datetime(2002,9,7,), "coe", credit)
     return _make_dummy_student
