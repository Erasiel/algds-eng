from typing import List, Set


def not_unique(strings: List[str], n: int) -> Set[str]:
    # TODO
    pass


if __name__ == "__main__":
    strings1 = ["apple", "peach", "apple", "strawberry", "peach", "apple"]
    exp1 = {"apple", "peach"}
    out1 = not_unique(strings1, len(strings1))
    try:
        assert out1 == exp1
        print("Assertion 1 succeeded")
    except:
        print(f"Assertion 1 failed!\nInput: {strings1}\n"
              f"Output: {out1}\nExpected output: {exp1}")

    strings2 = ["A", "B", "C", "D", "E"]
    exp2 = set()
    out2 = not_unique(strings2, len(strings2))
    try:
        assert out2 == exp2
        print("Assertion 2 succeeded")
    except:
        print(f"Assertion 2 failed!\nInput: {strings2}\n"
              f"Output: {out2}\nExpected output: {exp2}")
