# In the worst case, all keys are hashed to the same slot. Iterating over the
# list of in this slot can only be done in O(n) time in all three operations.
# In the average case, the average length of the lists - given by the load
# factor - determines the running time. If we keep the load factor low, i.e.,
# at all times, n/m = O(1), the average case running time will be constant.


class HashSetChaining:
    def __init__(self,
                 num_slots: int = 10,
                 max_load_factor: float = 1.0
    ) -> None:
        self.table = [[] for _ in range(num_slots)]
        self.num_slots = num_slots
        self.num_keys = 0
        self.max_load_factor = max_load_factor

    def insert(self, key: int) -> None:
        # Insert the key in the slot given by the key's hash value
        slot = self._hash_value(key)

        # In a set a key is stored at most once
        if key not in self.table[slot]:
            self.table[slot].append(key)
            self.num_keys += 1

        # If the load factor exceeds the allowed maximum, double the number of
        # slots and re-hash every key in the data structure
        if self._load_factor() > self.max_load_factor: self._double_size()

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

    def _load_factor(self) -> float:
        return self.num_keys / self.num_slots

    def _double_size(self) -> None:
        # Create a new table with double size and re-insert every key into
        # this new table. Note that hashing is based on the doubled size.
        self.num_slots *= 2
        new_table = [[] for _ in range(self.num_slots)]

        for chain in self.table:
            for key in chain:
                slot = self._hash_value(key)
                new_table[slot].append(key)

        self.table = new_table

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
    hs.insert(12)
    hs.insert(23)
    hs.insert(34)
    hs.insert(45)
    print(hs) # Note the doubled size
