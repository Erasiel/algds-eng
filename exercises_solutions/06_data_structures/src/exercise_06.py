from typing import Optional, Any


class LinkedListItem:
    def __init__(self,
                 key: Any,
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

    def insert(self, key: Any) -> None:
        """Inserts an element at the beginning of the list."""
        new_item = LinkedListItem(key=key)

        if self.head is None:
            self.head = new_item
        else:
            old_first = self.head
            new_item.next = old_first
            old_first.prev = new_item
            self.head = new_item

        self.length += 1

    def index(self, key: Any) -> int:
        """Returns the index of the key or -1 if the key is not in the list."""
        if self.head is None: return -1

        current_item = self.head
        index = 0
        while current_item is not None:
            if current_item.key == key: return index

            current_item = current_item.next
            index += 1

        return -1

    def get(self, index: int) -> Any:
        """Returns the key at the specified index in the list."""
        if self.head is None:
            raise ValueError("You can't query an empty list!")

        current_index = 0
        current_item = self.head

        while current_item is not None:
            if current_index == index:
                return current_item.key

            current_item = current_item.next
            current_index += 1

        raise ValueError(f"Index {index} does not exist in the list!")

    def delete(self, key: Any) -> None:
        """Deletes the first occurence of the key from the list."""
        if self.head is None:
            raise ValueError("You can't delete from an empty list")

        current_item = self.head
        while current_item is not None:
            if current_item.key == key: break
            current_item = current_item.next

        if current_item is None:
            raise ValueError(f"Element {key} is not in the list!")

        # current_item contains the key we want to delete
        prev_element = current_item.prev
        next_element = current_item.next
        if prev_element is not None: prev_element.next = next_element
        if next_element is not None: next_element.prev = prev_element
        current_item.next = None
        current_item.prev = None

        # Handle the case of deleting the first item
        if current_item == self.head:
            self.head = next_element

        self.length -= 1

    def __len__(self) -> int:
        print("len() is called")
        return self.length

    def __contains__(self, item: Any) -> bool:
        return self.index(item) != -1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)

    print("Testing the index function")
    print(ll.index(5)) # 0
    print(ll.index(1)) # 4
    print(ll.index(-432)) # -1
    print("-"*10)

    print("Testing the get function")
    print(ll.get(0)) # 5
    print(ll.get(4)) # 1
    # print(ll.get(6)) # error
    # ll2 = LinkedList()
    # print(ll2.get(0)) # error
    print("-"*10)

    print("Testing the len() function")
    print(len(ll))

    print("-"*10)
    print("Testing the in operator")
    print(5 in ll)
    print(234 in ll)
    print(234 in LinkedList())
