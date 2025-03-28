from typing import List, Tuple


def timestamp_str_to_int(str_timestamp: str) -> int:
    tokens = str_timestamp.split(":")
    hours = int(tokens[0])
    minutes = int(tokens[1])
    return hours * 60 + minutes


def is_overlapping(task1: Tuple[int, int], task2: Tuple[int, int]) -> bool:
    # Overlap by more than one common point
    cond1 = task1[0] < task2[1] and task2[0] < task1[0]

    # Overlap by same starting points or same ending points
    cond2 = task1[0] == task2[0] or task1[1] == task2[1]

    # If either of the conditions is true, the two tasks overlap
    return cond1 or cond2


def max_tasks(tasks: List[Tuple[str, str]], n: int) -> int:
    # Handle `n` == 0 separately
    if len(tasks) == 0: return 0

    # Convert tasks into (int, int) representation
    converted_tasks = [(timestamp_str_to_int(start), timestamp_str_to_int(end))
                       for start, end in tasks]

    # Sort tasks by starting time in descending order; if multiple tasks have
    # the same starting time, sort them by ending time
    converted_tasks = sorted(converted_tasks, reverse=True)

    # Greedy choice: pick the task that we can start the latest (the first task in
    # the sorted order), discard all that overlap with it, continue with the
    # next non-overlapping task until there are no more tasks
    last_task = converted_tasks[0]
    n_tasks = 1

    for task in converted_tasks:
        if not is_overlapping(last_task, task):
            last_task = task
            n_tasks += 1

    return n_tasks


if __name__ == "__main__":
    assert max_tasks([("09:15", "09:45"), ("09:45", "13:00")], 2) == 2
    assert max_tasks([("09:15", "09:45"), ("09:30", "13:00")], 2) == 1
    assert max_tasks([("09:15", "09:45"), ("09:30", "13:00"), ("10:00", "18:00")], 3) == 2
