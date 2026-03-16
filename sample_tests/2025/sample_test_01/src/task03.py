from typing import List, Tuple


def max_tasks(tasks: List[Tuple[str, str]], n: int) -> int:
    # TODO
    pass


if __name__ == "__main__":
    assert max_tasks([("09:15", "09:45"), ("09:45", "13:00")], 2) == 2
    assert max_tasks([("09:15", "09:45"), ("09:30", "13:00")], 2) == 1
    assert max_tasks([("09:15", "09:45"), ("09:30", "13:00"), ("10:00", "18:00")], 2) == 2
