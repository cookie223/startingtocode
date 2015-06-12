class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head:
            return None
        pointer = head
        while pointer and pointer.next:
            while pointer.next and pointer.val == pointer.next.val:
                pointer.next = pointer.next.next
            pointer = pointer.next
        return head


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(1)
    node4 = ListNode(1)
    node5 = ListNode(3)
    node6 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    s = Solution()
    node1 = s.deleteDuplicates(node1)
    while node1:
        print node1.val
        node1 = node1.next
