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
import math
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def get_count(x) -> int:
            return len(tops)-max(tops.count(x), bottoms.count(x))    
        s = set([tops[0], bottoms[0]])
        for i in range(1, len(tops)):
            s = s.intersection(set([tops[i], bottoms[i]]))
        if len(s) == 0:
            return -1
        l = list(s)
        if len(s) == 1:
            return get_count(l[0])
        return min(get_count(l[0]),get_count(l[1]))
start_time = time.time()
t = Solution()
root = t.minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2])
#print(root.val)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
