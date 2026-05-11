from typing import List, Tuple


def wikipedia_game(pages: List[str],
                   links: List[Tuple[str, str]],
                   start: str,
                   dest: str
) -> int:
    # Build a graph where vertices are webpages and directed edges are links
    # between webpages
    graph = {}

    # Vertices
    for page in pages:
        graph[page] = []

    # Edges
    for page_from, page_to in links:
        graph[page_from].append(page_to)

    # Run BFS on the graph from the starting page
    from exercise_03 import breadth_first_search
    bfs_distances, _ = breadth_first_search(graph, start)

    # If the game can be competed, return the minimum distance, otherwise
    # return -1. The game cannot be completed if the destination vertex's
    # distance is infinity (i.e., it is unreachable from the start)
    import math
    if bfs_distances[dest] != math.inf:
        return bfs_distances[dest]
    else:
        return -1


if __name__ == "__main__":
    pages = ["A", "B", "C", "D", "E"]
    links = [
        ("A", "B"),
        ("A", "C"),
        ("A", "D"),
        ("B", "A"),
        ("B", "C"),
        ("B", "D"),
        ("C", "A"),
        ("C", "B"),
        ("C", "D"),
        ("D", "A"),
        ("D", "B"),
        ("D", "C"),
        ("D", "E")
    ]
    output = None

    # TEST #1
    try:
        output = wikipedia_game(pages, links, "A", "A")
        assert output == 0
        print("Test #1 passed!")
    except AssertionError:
        print(f"Test #1 failed! Expected output: 0, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #1:\n{exception}")

    # TEST #2
    try:
        output = wikipedia_game(pages, links, "A", "B")
        assert output == 1
        print("Test #2 passed!")
    except AssertionError:
        print(f"Test #2 failed! Expected output: 1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #2:\n{exception}")

    # TEST #3
    try:
        output = wikipedia_game(pages, links, "B", "E")
        assert output == 2
        print("Test #3 passed!")
    except AssertionError:
        print(f"Test #3 failed! Expected output: 2, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #3:\n{exception}")

    # TEST #4
    try:
        output = wikipedia_game(pages, links, "E", "B")
        assert output == -1
        print("Test #4 passed!")
    except AssertionError:
        print(f"Test #4 failed! Expected output: -1, actual output: {output}")
    except Exception as exception:
        print(f"The following exception occured during Test #4:\n{exception}")


    # Realistic, but significantly oversimplified example
    # Uncomment for further testing
    # pages = [
    #     "Albert Einstein",
    #     "J. Robert Oppenheimer",
    #     "Leo Szilard",
    #     "Edward Teller",
    #     "Cilian Murphy",
    #     "Queen Elizabeth II",
    #     "Queen Elizabeth I",
    #     "Henry VIII",
    #     "USA",
    #     "UK",
    #     "Hungary",
    # ]

    # links = [
    #     ("Albert Einstein", "J. Robert Oppenheimer"),
    #     ("Albert Einstein", "Edward Teller"),
    #     ("Albert Einstein", "USA"),
    #     ("J. Robert Oppenheimer", "Albert Einstein"),
    #     ("J. Robert Oppenheimer", "Leo Szilard"),
    #     ("J. Robert Oppenheimer", "Edward Teller"),
    #     ("J. Robert Oppenheimer", "Cilian Murphy"),
    #     ("J. Robert Oppenheimer", "USA"),
    #     ("Leo Szilard", "J. Robert Oppenheimer"),
    #     ("Leo Szilard", "Edward Teller"),
    #     ("Leo Szilard", "Hungary"),
    #     ("Leo Szilard", "USA"),
    #     ("Edward Teller", "J. Robert Oppenheimer"),
    #     ("Edward Teller", "Albert Einstein"),
    #     ("Edward Teller", "Leo Szilard"),
    #     ("Edward Teller", "Hungary"),
    #     ("Edward Teller", "USA"),
    #     ("Cilian Murphy", "J. Robert Oppenheimer"),
    #     ("Queen Elizabeth II", "Queen Elizabeth I"),
    #     ("Queen Elizabeth II", "UK"),
    #     ("Queen Elizabeth II", "USA"),
    #     ("Queen Elizabeth I", "Queen Elizabeth II"),
    #     ("Queen Elizabeth I", "Henry VIII"),
    #     ("Queen Elizabeth I", "UK"),
    #     ("Henry VIII", "Queen Elizabeth I"),
    #     ("Henry VIII", "UK"),
    #     ("USA", "J. Robert Oppenheimer"),
    #     ("USA", "Edward Teller"),
    #     ("USA", "UK"),
    #     ("UK", "USA"),
    #     ("UK", "Henry VIII"),
    #     ("UK", "Queen Elizabeth I"),
    #     ("UK", "Queen Elizabeth II"),
    #     ("Hungary", "USA"),
    #     ("Hungary", "UK"),
    #     ("Hungary", "Edward Teller"),
    #     ("Hungary", "Leo Szilard")
    # ]

    # try:
    #     assert wikipedia_game(pages, links, "Leo Szilard", "Henry VIII") == 3
    #     assert wikipedia_game(pages, links, "Henry VIII", "Leo Szilard") == 4
    #     assert wikipedia_game(pages, links, "Queen Elizabeth I", "Hungary") == 4
    #     assert wikipedia_game(pages, links, "Hungary", "Queen Elizabeth II") == 2
    #     assert wikipedia_game(pages, links, "Henry VIII", "Albert Einstein") == 4
    #     assert wikipedia_game(pages, links, "Albert Einstein", "Henry VIII") == 3
    #     print("Test succeeded!")
    # except:
    #     print("Test failed!")
