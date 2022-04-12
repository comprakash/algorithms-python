from typing import Optional


class SingleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next: Optional[SingleLinkedListNode] = None


class SingleLinkedList:
    def __init__(self):
        self.head: Optional[SingleLinkedListNode] = None
        self.tail: Optional[SingleLinkedListNode] = None
        self.length: int = 0

    def append_node(self, value):
        node = SingleLinkedListNode(value)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        self.length += 1

    def insert_node(self, value, position):
        if position > self.length:
            raise IndexError("The specified position is out of range")
        node = SingleLinkedListNode(value)
        current_node = self.head
        while position > 1:
            position -= 1
            current_node = current_node.next
        node.next = current_node.next
        current_node.next = node
        self.length += 1
