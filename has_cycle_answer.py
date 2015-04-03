class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        d = ListNode(0)
        d.next = head
        a = b = d
        while b.next and b.next.next:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False