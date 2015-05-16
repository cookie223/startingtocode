# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

node1 = TreeNode("a")
node2 = TreeNode("b")
node3 = TreeNode("c")
node4 = TreeNode("d")
node5 = TreeNode("e")
node6 = TreeNode("f")
node1.left = node2
node1.right = node5
node2.left = node3
node2.right = node4
node5.right = node6

class Solution:
    # @param {TreeNode} root
    # @return {void} Do not return anything, modify root in-place instead.
    
    def transverse(self, root):
        nodelist = []
        l = []
        r = []
        if root.left is not None:
            l = self.transverse(root.left)
        if root.right is not None:
            r = self.transverse(root.right)
        nodelist = [root] + l + r
        return nodelist

    def flatten(self, root):
        if not root:
            return None
        nodelist = self.transverse(root)
        for i in range(len(nodelist)):
            nodelist[i].left = None
            try:
                nodelist[i].right = nodelist[i+1]
            except:
                nodelist[i].right = None

s= Solution()
s.flatten(node1)

pointer = node1
while pointer is not None:
    print pointer.val
    pointer = pointer.right
        

        
