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
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        nodes = {}
        roots = set()
        for desc in descriptions:
            node = None
            if desc[0] in nodes: 
                node = nodes[desc[0]]
            else: 
                node = TreeNode(desc[0])
                nodes[desc[0]] = node
                roots.add(node)
            if desc[1] in nodes:
                child = nodes[desc[1]]
                if child in roots:
                    roots.remove(child)
            else: 
                child = TreeNode(desc[1])
                nodes[desc[1]] = child
            if desc[2]:
                node.left = child 
            else: 
                node.right = child
        return roots.pop()
    
start_time = time.time()
app = Solution()
root = app.createBinaryTree([[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]])
#root = app.calculateMinimumHP([[0]])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")

