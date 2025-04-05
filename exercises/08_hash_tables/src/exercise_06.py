class HashSetOpenAddressing:
    def __init__(self, num_slots: int = 10) -> None:
        self.table = [None for _ in range(num_slots)]
        self.num_slots = num_slots
        self.num_keys = 0

    def insert(self, key: int) -> None:
        # Iterate over the probe sequence h(k, i), where i = 0 ... num_slots - 1
        for i in range(self.num_slots):

            # The probed slot is given by h(k, i)
            slot = self._probe(key, i)

            # In a set a key is stored at most once
            if self.table[slot] == key:
                return

            # If the slot is empty, insert the key
            elif self.table[slot] is None:
                self.table[slot] = key
                self.num_keys += 1
                return

        # If there are no more empty slots, raise an error
        raise ValueError("The hash table is full!")

    def delete(self, key: int) -> None:
        # Iterate over the probe sequence h(k, i), where i = 0 ... num_slots - 1
        for i in range(self.num_slots):

            # The probed slot is given by h(k, i)
            slot = self._probe(key, i)

            # If the current slot is empty, the key is not in the hash table
            if self.table[slot] is None:
                return

            # If the slot contains the key, set the slot's content to None
            if self.table[slot] == key:
                self.table[slot] = None
                self.num_keys -= 1
                return

    def contains(self, key: int) -> bool:
        # Iterate over the probe sequence h(k, i), where i = 0 ... num_slots - 1
        for i in range(self.num_slots):

            # The probed slot is given by h(k, i)
            slot = self._probe(key, i)

            # If the current slot is empty, the key is not in the hash table
            if self.table[slot] is None:
                return False
            elif self.table[slot] == key:
                return True

        # This line is only executed if the table is full and the key is not in
        # the table
        return False

    def _probe(self, key: int, i: int) -> int:
        return self._probe_linear(key, i)
        # Feel free to try quadratic probing:
        # return self._probe_quadratic(key, i)

    def _probe_linear(self, key, i) -> int:
        return (hash(key) + i) % self.num_slots

    def _probe_quadratic(self, key, i) -> int:
        # Feel free to try different values for c1 and c2
        c1 = 1
        c2 = 1
        return (hash(key) + c1 * i + c2 * (i ** 2)) % self.num_slots

    def __str__(self) -> str:
        return str(self.table)


if __name__ == "__main__":
    # Exercise 5
    hs = HashSetOpenAddressing()
    hs.insert(1)
    hs.insert(5)
    hs.insert(21)
    hs.insert(42)
    hs.insert(61)
    hs.insert(64)
    hs.insert(52)
    print(hs)
