from typing import List


def most_frequent_element(list: List[int]) -> int:
    # A dictionary stores key-value pairs, where all keys have to be distinct
    # We use a dict that will store the frequency of every unique element in
    # the list, where unique elements are the keys, and their frequencies are
    # the values
    frequency_counter = dict()
    max_frequency_element = 0
    max_frequency = 0

    for element in list:
        # If the element exists in the dict, increase its frequency
        if element in frequency_counter:
            frequency_counter[element] += 1

        # Otherwise, add the element to the dict with a frequency of 1
        else:
            frequency_counter[element] = 1

        # Update the element with the max frequency if necessary
        if frequency_counter[element] >= max_frequency:
            max_frequency_element = element
            max_frequency = frequency_counter[element]

    return max_frequency_element



if __name__ == "__main__":
    output = None

    # TEST #1
    try:
        output = most_frequent_element([1, 2, 1, 3, 1, 2])
        assert output == 1
        print("Test #1 passed!")
    except AssertionError:
        print("Test #1 failed! "
              f"Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = most_frequent_element([1, 2, 1, 2, 3])
        assert output == 2
        print("Test #2 passed!")
    except AssertionError:
        print("Test #2 failed! "
              f"Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")
