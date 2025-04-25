from typing import List, Tuple


def wikipedia_game(pages: List[str],
                   links: List[Tuple[str, str]],
                   start: str,
                   dest: str
) -> int:
    # TODO
    pass


if __name__ == "__main__":

    # Toy example: the vertices A, B, C and D make a full subgraph, there is an
    # edge from D to E, but there are no edges from E
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

    try:
        assert wikipedia_game(pages, links, "A", "A") == 0
        assert wikipedia_game(pages, links, "A", "B") == 1
        assert wikipedia_game(pages, links, "A", "C") == 1
        assert wikipedia_game(pages, links, "A", "D") == 1
        assert wikipedia_game(pages, links, "A", "E") == 2
        assert wikipedia_game(pages, links, "B", "E") == 2
        assert wikipedia_game(pages, links, "D", "E") == 1
    except:
        print("Test 1 failed!")

    try:
        assert wikipedia_game(pages, links, "E", "A") == -1
        assert wikipedia_game(pages, links, "E", "B") == -1
        assert wikipedia_game(pages, links, "E", "C") == -1
        assert wikipedia_game(pages, links, "E", "D") == -1
    except:
        print("Test 2 failed! You can't leave pages without outgoing links!")

    # Realistic, but significantly oversimplified example
    pages = [
        "Albert Einstein",
        "J. Robert Oppenheimer",
        "Leo Szilard",
        "Edward Teller",
        "Cilian Murphy",
        "Queen Elizabeth II",
        "Queen Elizabeth I",
        "Henry VIII",
        "USA",
        "UK",
        "Hungary",
    ]

    links = [
        ("Albert Einstein", "J. Robert Oppenheimer"),
        ("Albert Einstein", "Edward Teller"),
        ("Albert Einstein", "USA"),
        ("J. Robert Oppenheimer", "Albert Einstein"),
        ("J. Robert Oppenheimer", "Leo Szilard"),
        ("J. Robert Oppenheimer", "Edward Teller"),
        ("J. Robert Oppenheimer", "Cilian Murphy"),
        ("J. Robert Oppenheimer", "USA"),
        ("Leo Szilard", "J. Robert Oppenheimer"),
        ("Leo Szilard", "Edward Teller"),
        ("Leo Szilard", "Hungary"),
        ("Leo Szilard", "USA"),
        ("Edward Teller", "J. Robert Oppenheimer"),
        ("Edward Teller", "Albert Einstein"),
        ("Edward Teller", "Leo Szilard"),
        ("Edward Teller", "Hungary"),
        ("Edward Teller", "USA"),
        ("Cilian Murphy", "J. Robert Oppenheimer"),
        ("Queen Elizabeth II", "Queen Elizabeth I"),
        ("Queen Elizabeth II", "UK"),
        ("Queen Elizabeth II", "USA"),
        ("Queen Elizabeth I", "Queen Elizabeth II"),
        ("Queen Elizabeth I", "Henry VIII"),
        ("Queen Elizabeth I", "UK"),
        ("Henry VIII", "Queen Elizabeth I"),
        ("Henry VIII", "UK"),
        ("USA", "J. Robert Oppenheimer"),
        ("USA", "Edward Teller"),
        ("USA", "UK"),
        ("UK", "USA"),
        ("UK", "Henry VIII"),
        ("UK", "Queen Elizabeth I"),
        ("UK", "Queen Elizabeth II"),
        ("Hungary", "USA"),
        ("Hungary", "UK"),
        ("Hungary", "Edward Teller"),
        ("Hungary", "Leo Szilard")
    ]

    try:
        assert wikipedia_game(pages, links, "Leo Szilard", "Henry VIII") == 3
        assert wikipedia_game(pages, links, "Henry VIII", "Leo Szilard") == 4
        assert wikipedia_game(pages, links, "Queen Elizabeth I", "Hungary") == 4
        assert wikipedia_game(pages, links, "Hungary", "Queen Elizabeth II") == 2
        assert wikipedia_game(pages, links, "Henry VIII", "Albert Einstein") == 4
        assert wikipedia_game(pages, links, "Albert Einstein", "Henry VIII") == 3
    except:
        print("Test 3 failed!")
