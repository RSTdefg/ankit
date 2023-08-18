
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dum = head
        cnt = 0
        while dum:
            dum = dum.next
            cnt += 1
        prev, cur = None, head
        cnt -= n
        while cnt > 0:
            prev = cur
            cur = cur.next
            cnt -= 1
        if prev:
            prev.next = cur.next
        else:
            head = cur.next
        return head

        


