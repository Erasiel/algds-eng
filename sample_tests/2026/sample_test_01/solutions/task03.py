# Name: Chester the Tester
# Neptun: T3ST3R
# h-id: h000000


from typing import List, Tuple


def timestamp_str_to_int(str_timestamp: str) -> int:
    tokens = str_timestamp.split(":")
    hours = int(tokens[0])
    minutes = int(tokens[1])
    return hours * 60 + minutes


def is_overlapping(task1: Tuple[int, int], task2: Tuple[int, int]) -> bool:
    return task1[0] < task2[1] and task2[0] < task1[1]


def max_tasks(tasks: List[Tuple[str, str]]) -> int:
    # Handle the 0 tasks edge case separately
    if len(tasks) == 0: return 0

    # Convert tasks into (int, int) representation
    converted_tasks = [(timestamp_str_to_int(start), timestamp_str_to_int(end))
                       for start, end in tasks]

    # Sort tasks by starting time in descending order; if multiple tasks have
    # the same starting time, use their ending time as tiebreaker
    converted_tasks = sorted(converted_tasks, reverse=True)

    # Greedy choice: pick the task that we can start the latest (the first
    # task in the sorted order), discard all that overlap with it, continue
    # with the next non-overlapping task until there are no more tasks
    last_task = converted_tasks[0]
    n_tasks = 1

    for task in converted_tasks:
        if not is_overlapping(last_task, task):
            last_task = task
            n_tasks += 1

    return n_tasks


def max_tasks2(tasks: List[Tuple[str, str]]) -> int:
    # Another correct greedy approach is to pick the task that we can finish
    # earliest. To do this, we sort the tasks by their ending time in
    # ascending order; if multiple tasks have the same ending time, use their
    # starting time as a tiebreaker. Everything else is the same.

    if len(tasks) == 0: return 0

    converted_tasks = [(timestamp_str_to_int(start), timestamp_str_to_int(end))
                       for start, end in tasks]

    # When the following function is used as the key in sorting intervals, the
    # basis of comparison between two intervals is their ending point, and the
    # tiebreaker is their starting point
    def end_time_first(interval: Tuple[int, int]) -> Tuple[int, int]:
        return (interval[1], interval[0])

    converted_tasks = sorted(converted_tasks, key=end_time_first)

    last_task = converted_tasks[0]
    n_tasks = 1

    for task in converted_tasks:
        if not is_overlapping(last_task, task):
            last_task = task
            n_tasks += 1

    return n_tasks


if __name__ == "__main__":
    import traceback

    output = None

    # TEST #1
    try:
        output = max_tasks([("09:15", "09:45"), ("09:45", "13:00")])
        assert output == 2
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")
        traceback.print_exc()

    # TEST #2
    try:
        output = max_tasks([("09:15", "09:45"), ("09:30", "13:00")])
        assert output == 1
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
        traceback.print_exc()

    # TEST #3
    try:
        output = max_tasks([("09:30", "13:00"),
                            ("09:15", "09:45"),
                            ("10:00", "18:00")])
        assert output == 2
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")
        traceback.print_exc()
