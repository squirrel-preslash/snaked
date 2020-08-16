""" Tests whether the Snaked wrapper can convert other cases to snake-case access """

import pytest

def test_method(camel_class, pascal_class, snake_class):
    assert camel_class.method_one() is True
    assert pascal_class.method_one() is True
    assert snake_class.method_one() is True

def test_attribute(camel_class, pascal_class, snake_class):
    assert camel_class.attribute_one is True
    assert pascal_class.attribute_one is True
    assert snake_class.attribute_one is True

def test_non_existent(camel_class, pascal_class, snake_class):
    with pytest.raises(AttributeError):
        camel_class.non_existent()
    with pytest.raises(AttributeError):
        pascal_class.non_existent()
    with pytest.raises(AttributeError):
        snake_class.non_existent()
