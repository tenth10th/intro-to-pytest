from pytest import fixture, mark


@fixture
def class_fixture():
    print("   (running class_fixture)")


@fixture
def extra_fixture():
    print("      (running extra_fixture)")


@mark.usefixtures("class_fixture")
class TestAdvancedClassFeatures(object):
    @fixture(autouse=True)
    def method_fixture(self):
        """
        Class Methods can be turned into fixtures!
        autouse will apply them to all other methods on the class...
        """
        print("\n(method_fixture is autouse on TestIntermediateClass)")

    def test1(self):
        print("      Running TestIntermediateClass.test1")
        assert True

    def test2(self, extra_fixture):
        print("          Running TestIntermediateClass.test2")
        assert True

    @mark.skip(reason="you can skip classmethod-based test cases too!")
    def test3(self):
        print("(This test will never actually get run...)")
        assert False