import math
from typing import List, Tuple


def network_rebuild(cities: List[str],
                    costs: List[Tuple[str, str, float]],
                    k: int,
                    n: int,
                    m: int
) -> float:
    # TODO
    pass


if __name__ == "__main__":
    cities = ["A", "B", "C"]
    costs = [
        ("A", "B", 10.2),
        ("B", "C", 5.3),
        ("A", "C", 7.2)
    ]
    assert network_rebuild(cities, costs, 1, 3, 3) == 5.3   # note: k = 1
    assert network_rebuild(cities, costs, 2, 3, 3) == 0     # note: k = 2

    cities = ["A", "B", "C", "D"]
    costs = [
        ("A", "B", 2.0),
        ("C", "D", 3.0)
    ]
    assert network_rebuild(cities, costs, 1, 4, 2) == 5.0   # note: k = 1
