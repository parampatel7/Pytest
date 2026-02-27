#File used for creating global fixtures


#For functions: to initialize values in beginning we use fixtures
import pytest

from samplecode import shapes


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def wierd_rectangle():
    return shapes.Rectangle(5,5)