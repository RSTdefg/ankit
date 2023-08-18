
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        m = {head: Node(head.val)}
        dummy = head

        while head and head.next:
            if head.next and head.next not in m:
                m[head.next] = Node(head.next.val)
            if head.random and head.random not in m:
                m[head.random] = Node(head.random.val)
            m[head].next = m[head.next] if head.next else None
            m[head].random = m[head.random] if head.random else None
            head = head.next
        m[head].random = m[head.random] if head and head.random else None
        return m[dummy]


