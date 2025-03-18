from typing import List, Union


def rpn_eval(rpn: List[Union[str, float]], n: int) -> float:
    # TODO
    pass


if __name__ == "__main__":
    assert rpn_eval([5.0, 4.0, "*", 3.0, "+"], 5) == 23
    assert rpn_eval([5.0, 4.0, 3.0, "*", "+"], 5) == 17
    assert rpn_eval([5.0, 4.0, "*", 3.0, 2.0, "*", "+"], 7) == 26
    assert rpn_eval([5.0, 3.0, "+", 4.0, 2.0, "-", "/"], 7) == 4
    assert rpn_eval([1.0, 2.0, "+", 3.0, "*", 6.0, "+", 8.0, 5.0, "-", "/"], 11) == 5
