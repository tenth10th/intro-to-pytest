class TestSimpleClass(object):
    """
    Classes can still be used to organize collections of test cases, with
    each test being a Method on the Class, rather than a standalone function.
    """
    x = 1
    y = 2
    value = 1

    def regular_method(self):
        """
        Test Classes can have "normal" methods that are not test cases
        """
        print("\n   (This is a regular, non-test-case method. Pytest won't run it.)")

    def get_doubled_value(self):
        """
        A method that uses data from the class (also not a test case)
        """
        return self.value * 2

    def test_method_simple(self):
        """
        Methods whose name starts with "test_" are recognized as test cases
        """
        print("\n   Running TestSimpleClass.test_method_simple")
        assert True

    def test_method_interesting(self):
        """
        Test methods can use other features of the class...
        """
        print("\n   Running TestSimpleClass.test_method_interesting")
        doubled_value = self.get_doubled_value()
        assert self.x != doubled_value
        assert self.y == doubled_value
