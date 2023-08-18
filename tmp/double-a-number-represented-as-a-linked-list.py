
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode(0)
        dummy = result
        carry = 0
        def reverse(cur, prev):
            if not cur:
                return prev
            nxt = cur.next
            cur.next = prev
            return reverse(nxt, cur)
        head = reverse(head, None)
        
        while head:
            new_val = (head.val * 2+carry) %10
            carry = (head.val * 2+carry) //10
            dummy.next = ListNode(new_val)
            dummy = dummy.next
            head = head.next
        if carry:
            dummy.next = ListNode(1)
            dummy = dummy.next
        res = reverse(result.next, None)
        return res
            
            
        
        
