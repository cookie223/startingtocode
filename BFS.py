import Queue

class TreeNode():
    val = 0
    left = None
    right = None
    # visited = False
    
    def __init__(self, x, left = None, right = None):
        self.val = x
        self.left = left
        self.right = right
    
class Solution():
    def BFS(self, root):
        vallist = [root.val]
        # root.visited = True
        nodeQueue = Queue.Queue()
        nodeQueue.put(root)
        while (not nodeQueue.empty()):
            u = nodeQueue.get()
            v = u.left
            w = u.right
            if v:
                # if (not v.visited):
                vallist.append(v.val)
                nodeQueue.put(v)
            else:
                vallist.append(-23)
            if w:
                # if (not w.visited):
                vallist.append(w.val)
                nodeQueue.put(w)
            else:
                vallist.append(-23)
        return vallist
        
s = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print s.BFS(root)
            
            