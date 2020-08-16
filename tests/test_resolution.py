def test_order(camel_class, pascal_class, snake_class):
    # Check that Snaked prefers the provided attributes and only converts them to camelCase
    # or PascalCase if it doesn't find the accessed snake_case versions
    assert camel_class.method_two() is False
    assert pascal_class.method_two() is False
    assert snake_class.method_two() is False

    assert camel_class.methodTwo() is True
    assert pascal_class.MethodTwo() is True
    assert snake_class.method_two() is False
