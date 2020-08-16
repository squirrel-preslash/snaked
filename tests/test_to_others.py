""" Tests whether the Snaked wrapper will NOT convert other-case access to snake-case attributes """

import pytest

def test_method(snake_class):
    with pytest.raises(AttributeError):
        snake_class.methodOne()
    with pytest.raises(AttributeError):
        snake_class.MethodOne()

def test_attribute(snake_class):
    with pytest.raises(AttributeError):
        snake_class.attributeOne
    with pytest.raises(AttributeError):
        snake_class.AttributeOne
