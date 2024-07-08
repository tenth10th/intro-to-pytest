import time
from collections import namedtuple
from uuid import uuid4

class ExpensiveClass(object):
    """
    A fake Class that takes a long time to fully initialize
    (simulating a large file, database, etc...)
    """

    def __init__(self):
        print("$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $")
        print("(Initializing ExpensiveClass instance...)")
        print("$ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $")
        time.sleep(0.1)
        self.id = str(uuid4())[-6:]
        print("(ExpensiveClass instance {} complete!)".format(self.id))

    def __repr__(self):
        return "<ExpensiveClass(id=\"{}\")>".format(self.id)

    def cleanup(self):
        print("\n(Cleaning up ExpensiveClass {})".format(self.id))


FakeRow = namedtuple("FakeRow", ("id", "name", "value"))


class SimulatedDBFailure(Exception):
    pass


def db_service(query_parameters):
    """
    A fake DB service that takes a remarkably long time to yield results
    """
    print("(Doing expensive database stuff!)")

    time.sleep(5.0)

    data = [FakeRow(0, "Foo", 19.95), FakeRow(1, "Bar", 1.99), FakeRow(2, "Baz", 9.99)]

    print("(Done doing expensive database stuff)")
    return data


def count_service(query_parameters):
    print("count_service: Performing a query (and counting the results)...")

    data = db_service(query_parameters)

    count = len(data)

    print("Found {} result(s)!".format(count))
    return count


DATA_SET_A = {
    "Foo": "Bar",
    "Baz": [5, 7, 11],
    "Qux": {"A": "Boston", "B": "Python", "C": "TDD"},
}

DATA_SET_B = DATA_SET_A

DATA_SET_C = {
    "Foo": "Bar",
    "Baz": [3, 5, 7],
    "Qux": {"A": "Boston", "B": "Python", "C": "TDD"},
}
