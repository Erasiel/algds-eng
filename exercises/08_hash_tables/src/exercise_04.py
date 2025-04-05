# TODO: analyze the the time complexity of the insert, delete and contains
# operations in the worst and average cases, and modify the implementation to
# ensure that the time complexity of all operations is O(1) in the average case.

class HashSetChaining:
    def __init__(self, num_slots: int = 10) -> None:
        self.table = [[] for _ in range(num_slots)]
        self.num_slots = num_slots
        self.num_keys = 0

    def insert(self, key: int) -> None:
        # Insert the key in the slot given by the key's hash value
        slot = self._hash_value(key)

        # In a set a key is stored at most once
        if key not in self.table[slot]:
            self.table[slot].append(key)
            self.num_keys += 1

    def delete(self, key: int) -> None:
        # Delete the key from the slot given by the key's hash value
        slot = self._hash_value(key)

        # Only delete the key if it's in the slot's list
        if key in self.table[slot]:
            self.table[slot].remove(key)
            self.num_keys -= 1

    def contains(self, key: int) -> bool:
        # Find the key in the slot given by the key's hash value
        slot = self._hash_value(key)
        return key in self.table[slot]

    def _hash_value(self, key: int) -> int:
        # Note: for integer keys, hash(key) == key, but for other types the
        # hash(...) call would be required. We write hash(key) instead of key
        # to emphasize the use of hashing.
        return hash(key) % self.num_slots

    def __str__(self) -> str:
        return str(self.table)


if __name__ == "__main__":
    # Exercise 3
    hs = HashSetChaining()
    hs.insert(1)
    hs.insert(5)
    hs.insert(21)
    hs.insert(42)
    hs.insert(61)
    hs.insert(64)
    hs.insert(52)
    print(hs)
