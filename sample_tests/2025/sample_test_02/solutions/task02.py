from typing import List


def repeating_row_filter(mtx: List[List[int]],
                         n: int,
                         m: int
) -> List[List[int]]:
    # Prepare the filtered matrix
    filtered_mtx = []

    # Store a set of unique rows
    unique_encoded_rows = set()

    # Traverse the rows in the matrix
    for row in mtx:

        # Encode the row to a format that is hashable (e.g. str, tuple, or
        # convert it to an integer) and where different rows have different
        # encodings - converting to a string is the simplest solution
        encoded_row = str(row)

        # If the row is not in the previously seen rows, add it to the unique
        # rows and to the filtered matrix
        if encoded_row not in unique_encoded_rows:
            unique_encoded_rows.add(encoded_row)
            filtered_mtx.append(row)

    return filtered_mtx



if __name__ == "__main__":
    mtx1 = [
        [1],
        [0]
    ]
    assert repeating_row_filter(mtx1, 2, 1) == [[1], [0]]

    mtx2 = [
        [1, 1],
        [1, 1]
    ]
    assert repeating_row_filter(mtx2, 2, 2) == [[1, 1]]

    mtx3 = [
        [0, 0, 1, 1],
        [1, 0, 1, 0],
        [1, 0, 1, 0],
        [1, 1, 1, 1],
        [0, 0, 1, 1],
    ]
    assert repeating_row_filter(mtx3, 5, 4) == [[0, 0, 1, 1],
                                                [1, 0, 1, 0],
                                                [1, 1, 1, 1]]

