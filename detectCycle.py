
import sys

class LinkNode:
    
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = LinkNode(1)
node2 = LinkNode(2)
node3 = LinkNode(3)
node4 = LinkNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

class LinkNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = LinkNode(1)
node2 = LinkNode(2)
node3 = LinkNode(3)
node4 = LinkNode(4)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node2

def detectCycle(head):
    if not head:
        return None
    else:
        while not head.next == None:
            try:
                if head.marker == 1:
                    return head
            except:
                head.marker = 1
                head = head.next
        return None

print detectCycle(node1)
