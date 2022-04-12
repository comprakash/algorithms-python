from typing import Optional


class DoubleLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next: Optional[DoubleLinkedListNode] = None
        self.prev: Optional[DoubleLinkedListNode] = None


class DoubleLinkedList:
    def __init__(self):
        self.head: Optional[DoubleLinkedListNode] = None
        self.tail: Optional[DoubleLinkedListNode] = None

    def insert_node(self, value):
        node = DoubleLinkedListNode(value)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node
