from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
from collections import Counter
import pprint

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        def process(node, delete_set, add_self):
            res = []
            delete_self = node.val in delete_set
            if add_self and not(delete_self):
                res.append(node)
            
            if node.left:
                res = res + process(node.left, delete_set, delete_self)
                if node.left.val in delete_set:
                    node.left = None
            if node.right:
                res = res + process(node.right, delete_set, delete_self)
                if node.right.val in delete_set:
                    node.right = None
            return res 
        if not(root):
            return []
        roots = []
        return process(root, set(to_delete), True) 
         
    
start_time = time.time()
app = Solution()
root = app.delNodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7))), [3,5])
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

