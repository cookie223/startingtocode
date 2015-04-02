class ListNode:
	def __init__(self,x):
		self.val=x
		self.next = None

test1 = ListNode(1)
test2 = ListNode(2)
test3 = ListNode(3)

test1.next = test2
test2.next = test3



def swapPairs(head):
	if not head or head.next == None:
		return head
	else:
		nbor = head.next
		senti = head
		while nbor and (not head.next == None) and (not nbor.next == None):
			head.val, nbor.val = nbor.val, head.val
			head = nbor.next
			try:
				nbor=head.next
			except:
				nbor= False
		if nbor:
			head.val, nbor.val = nbor.val, head.val
		return senti



node = swapPairs(test1)
while not node.next == None:
	print node.val
	node = node.next
print node.val