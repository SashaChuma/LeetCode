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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_m(m):
    for r in m:
        print(" ".join(f"{num:4d}" for num in r))

def read_tree(nums) -> Optional[TreeNode]:
    if len(nums) == 0 or nums[0] is None:
        return None
    root = TreeNode(nums[0])
    q = deque()
    q.append(root)
    i = 1
    while q and i < len(nums):
        node = q.popleft()
        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            q.append(node.left)
        if nums[i+1] is not None:
            node.right = TreeNode(nums[i+1])
            q.append(node.right)
        i += 2 
    return root 
def write_tree(root, level=0, side=""):
    if (root):
        print(f"{side}:{level} {root.val}")
        write_tree(root.left, level+1, "L")
        write_tree(root.right, level+1, "R")
class BIT: 
    def __init__(self, size) -> None:
        size += 2
        self.data = [0]*size
        self.size = size
    def update(self, i, val):
        i += 1
        while i < self.size:
            self.data[i] += val
            i += (i & -i)
    def query(self, i):
        i += 1
        result = 0
        while i > 0:
            result += self.data[i]
            i -= (i & -i)
        return result 
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        start = 0
        n = len(nums)
        e1 = n-1
        e2 = n-1
        result = 0
        if len(nums) < 2:
            return 0
        if nums[-1] + nums[-2] < lower:
            return 0
        while start < n:
            while e1 > start and nums[start]+nums[e1] >= lower:
                e1 -= 1
             
            while e2 > e1 and nums[start]+nums[e2] > upper:
                e2 -= 1
            if start == e2: 
                break
            if e2 == e1 and nums[start]+nums[e2] > upper:
                break
            result += e2-e1
            if e1 > start and nums[start]+nums[e1] == lower:
                result += 1
            start += 1
            if e1 < start: 
                e1 = start
        return result

start_time = time.time()
t = Solution()
root = t.countFairPairs([1,7,9,2,5], 11,11)        
#print(root.val)
#    root.print_tree()
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
