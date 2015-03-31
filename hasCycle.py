class ListNode:
    def __init__(self,x):
        self.val=x
        self.next = None


node1=ListNode(1)
node2=ListNode(2)
node3=ListNode(3)

node1.next=node2
node2.next=node3


def hasCycle(head):
    nodelist=[]
    current=head
    judge=0
    while not current.next==None:
        nodelist.append(current)
        current = current.next
        if current in nodelist:
            judge=1
            break
    if judge == 1:
        return True
    else:
        return False
        
print hasCycle(node1)