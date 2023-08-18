
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = head
        prev = None
        lleft = left
        while lleft > 1:
            prev = dummy
            dummy = dummy.next
            lleft -= 1
        end = None
        def recur(index, cur_node, prev):
            if index == 1:
                nonlocal end
                end = cur_node.next
                cur_node.next = prev
                return cur_node
            save = recur(index-1, cur_node.next, cur_node)
            cur_node.next = prev
            return save
        save_head = dummy
        if prev:
            prev.next = recur(right-left+1, dummy, prev)
        else:
            head = recur(right-left+1, dummy, prev)
        save_head.next = end
        return head 



