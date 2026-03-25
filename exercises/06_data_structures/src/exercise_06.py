from typing import Optional


class LinkedListItem:
    def __init__(self,
                 key: str,
                 prev: Optional["LinkedListItem"] = None,
                 next: Optional["LinkedListItem"] = None
    ) -> None:
        self.key = key
        self.prev = prev
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def insert(self, key: str) -> None:
        """Inserts an element at the beginning of the list."""
        # TODO
        pass

    def index(self, key: str) -> int:
        """Returns the index of the key or -1 if the key is not in the list."""
        # TODO
        pass

    def get(self, index: int) -> str:
        """Returns the key at the specified index in the list."""
        # TODO
        pass

    def delete(self, key: str) -> None:
        """Deletes the first occurence of the key from the list."""
        # TODO
        pass


if __name__ == "__main__":
    # TODO: test your implementation
    pass
