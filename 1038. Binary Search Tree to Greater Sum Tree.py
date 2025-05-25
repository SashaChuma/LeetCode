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
    def process(self, root, acc)->int:
        if not(root):
            return acc 
        acc = self.process(root.right, acc)
        new_val = root.val + acc 
        acc += root.val
        root.val = new_val
        acc = self.process(root.left, acc)
        return acc
    
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.process(root, 0)
        return root
        #print(acc)    
start_time = time.time()
app = Solution()
root = app.bstToGst(TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5))))
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


