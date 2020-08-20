""" Tests whether the Snaked wrapper can set camelCase/PascalCase attributes on the target when snake_case attributes are being set """

def test_attribute(camel_class, pascal_class, snake_class):
    camel_class.attribute_one = False
    pascal_class.attribute_one = False
    snake_class.attribute_one = False

    assert camel_class.attributeOne == False
    assert pascal_class.AttributeOne == False
    assert snake_class.attribute_one == False
