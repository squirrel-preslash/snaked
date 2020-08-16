import sys
import os
sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), ".."))

from snaked import Snaked
import pytest

class CamelClass(object):
    def methodOne(self):
        return True
    def method_two(self):
        return False
    def methodTwo(self):
        return True
    attributeOne = True

class PascalClass(object):
    def MethodOne(self):
        return True
    def method_two(self):
        return False
    def MethodTwo(self):
        return True
    AttributeOne = True

class SnakeClass(object):
    def method_one(self):
        return True
    def method_two(self):
        return False
    def methodTwo(self):
        return False
    attribute_one = True

@pytest.fixture
def camel_class():
    return Snaked(CamelClass())

@pytest.fixture
def pascal_class():
    return Snaked(PascalClass())

@pytest.fixture
def snake_class():
    return Snaked(SnakeClass())