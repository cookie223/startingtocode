class ListNode:
    def __init__(self, x):
        "list Node with a value and a pointer"
        self.val = x
        self.next = None


node1 = ListNode('a')
node2 = ListNode('b')
node3 = ListNode('c')
node1.next = node2
node2.next = node3


def removeNthFromend(head, n):
    nodedict = {}
    i = 0
    if not head:
        return None
    while head:
        nodedict[i] = head
        i += 1
        head = head.next
    if i == 2:
        return None
    elif n == 1:
        nodedict[i-2].next = None
        return nodedict[0]
    elif n == i:
        return nodedict[1]
    else:
        nodedict[i-n-1].next = nodedict[i-n+1]
        return nodedict[0]


if __name__ == '__main__':
    testres = removeNthFromend(node1, 1)
    if testres == node1:
        print '1true'
    if testres.next == node2:
        print '2true'
