from typing import List


def differ_by_one_character(s1: str, s2: str) -> bool:
    if len(s1) != len(s2): return False

    n_diff = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            n_diff += 1
            if n_diff > 1: return False

    return True


def num_transformations(start_word: str,
                        dest_word: str,
                        word_list: List[str]
) -> int:
    # If the destination word is not in the word list, the transformation
    # cannot be completed
    if dest_word not in word_list: return -1

    # Build a graph where words in the word list (including the start word)
    # are vertices, and two words are connected with an undirected edge if
    # they differ by one character
    word_list.append(start_word)
    graph = {}

    # Vertices
    for word in word_list: graph[word] = []

    # Edges
    for i in range(len(word_list)):
        for j in range(i + 1, len(word_list)):
            w1 = word_list[i]
            w2 = word_list[j]
            if differ_by_one_character(w1, w2):
                graph[w1].append(w2)
                graph[w2].append(w1)

    # Run BFS from the start word
    from exercise_03 import breadth_first_search
    bfs_distances, _ = breadth_first_search(graph, start_word)

    # Return the number of transformations if the start --> ... --> dest
    # transformation can be completed, otherwise return -1. The transformation
    # cannot be completed if the destination word's distance is infinity
    # (i.e., it is unreachable from the start).
    import math
    if bfs_distances[dest_word] != math.inf:
        return bfs_distances[dest_word]
    else:
        return -1


if __name__ == "__main__":

    output = None

    # TEST #1
    try:
        output = num_transformations("hit",
                                     "cog",
                                     ["hot", "dot", "dog", "lot", "log", "cog"])
        assert output == 4
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 4, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = num_transformations("hit",
                                     "cog",
                                     ["hot", "dot", "dog", "lot", "log"])
        assert output == -1
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: -1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = num_transformations("hit",
                                     "lit",
                                     ["hot", "dot", "lot", "log", "lit"])
        assert output == 1
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")

    # TEST #4
    try:
        output = num_transformations("hit",
                                     "god",
                                     ["hot", "god", "lot", "log", "lit"])
        assert output == -1
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: -1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")
