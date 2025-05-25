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
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        s = 0
        result = 0
        for num in nums: 
            s += num 
            if s < 0: 
                s = 0
            elif result < s: 
                result = s 
        s = 0 
        for num in nums:
            s += num
            if s > 0:
                s = 0
            elif result < -s:
                result = -s  
        return result 
start_time = time.time()
t = Solution()
root = t.maxAbsoluteSum([1,-3,2,3,-4])
#if root:
#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
