
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}
        # Initialize dummy nodes
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        # Set up the double linked list.
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self._remove(node)
            self._add(node)
            return node.value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self._remove(self.hashmap[key])
        node = Node(key, value)
        self._add(node)
        self.hashmap[key] = node
        if len(self.hashmap) > self.capacity:
            node = self.head.next
            self._remove(node)
            del self.hashmap[node.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        self.tail.prev = node
        node.prev = p
        node.next = self.tail

