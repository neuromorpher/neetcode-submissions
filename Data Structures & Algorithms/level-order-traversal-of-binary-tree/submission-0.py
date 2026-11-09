# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(node):

            if not root:
                return []

            res = []
            queue = deque([node]) 

            while queue:

                k = len(queue)
                sublist = []
                for i in range(k):

                    node = queue.popleft() 
                    sublist.append(node.val)


                    if node.left is not None:

                        queue.append(node.left)

                    if node.right is not None:
                        
                        queue.append(node.right)

                res.append(sublist) 

            return res 
        
        return bfs(root)





        