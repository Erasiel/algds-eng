class MyType:
    def __init__(self, a: int, b: int):
        self.a = a
        self.b = b

    # TODO: extend the implementation of MyType so that neither of the
    # assertions below fail.


if __name__ == "__main__":
    v1 = MyType(1, 2)
    v2 = MyType(1, 2)
    try:
        assert v1 == v2
        print("Assertion 1 succeeded.")
    except:
        print("Assertion 1 failed: v1 and v2 should be equal, since their "
              "attributes are the same.")

    s = set()
    s.add(v1)
    s.add(v2)

    try:
        assert len(s) == 1
        print("Assertion 2 succeeded.")
    except:
        print("Assertion 2 failed: after inserting v1 and v2 into a set, the "
              "size of the set should be 1, since v1 and v2 are equal.")
