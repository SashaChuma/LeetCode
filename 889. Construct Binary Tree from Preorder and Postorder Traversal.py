import time
from typing import List
from typing import Optional
from functools import lru_cache
from collections import defaultdict
from queue import Queue
import math
import itertools
import heapq
from collections import Counter
from collections import deque 
import numpy 
import pprint
from typing import List
import bisect
#class Solution:
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def print_tree(self, level=0, prefix="Root: "):
        print(" " * (level * 4) + prefix + str(self.val))
        if self.left:
            self.left.print_tree(level + 1, "L--- ")
        if self.right:
            self.right.print_tree(level + 1, "R--- ")
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def build(p1,q1, p2,q2):
            result = TreeNode(preorder[p1])
            p1 += 1
            
            if p1 > q1:
                return result
            q2 -= 1
            if preorder[p1] == postorder[q2]:
                result.left = build(p1, q1, p2, q2)
            else:
                split2 = map2[preorder[p1]]
                split1 = map1[postorder[q2]]
                result.left = build(p1, split1-1, p2, split2)
                result.right = build(split1, q1, split2, q2)
            return result
        map1 = {v:k for k,v in enumerate(preorder)}
        map2 = {v:k for k,v in enumerate(postorder)}
        root = build(0, len(preorder)-1, 0, len(postorder)-1) 
        return root 

start_time = time.time()
t = Solution()
root = t.constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1])
if root:
    root.print_tree()
#print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
