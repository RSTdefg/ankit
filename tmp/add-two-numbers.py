
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        result = dummy
        carry = 0
        while l1 or l2:
            l1val = l1.val if l1 else 0
            l2val = l2.val if l2 else 0
            result.next = ListNode((l1val+l2val+carry)%10)
            carry = 1 if l1val + l2val + carry >= 10 else 0
            result = result.next
            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2
        if carry:
            result.next = ListNode(carry)
        return dummy.next

