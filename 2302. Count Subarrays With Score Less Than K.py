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
    def countSubarrays(self, nums: List[int], k: int) -> int:
        def search(start, end):
            left = start
            right = end
            offset = pref[start] - nums[start]
            if nums[start] >= k:
                return -1
            while left < right:
                mid = (left+right)//2
                s = (pref[mid]-offset)*(mid-start+1)
                if s < k:
                    left = mid+1
                else: 
                    right = mid-1
            if left == start:
                return left
            s = (pref[left]-offset)*(left-start+1)
            if s >= k:
                left -= 1
            return left
        
        if len(nums) == 1:
            return 1 if nums[0] < k else 0
        s = 0
        pref = [0]*len(nums)
        for i,num in enumerate(nums):
            s += num
            pref[i] = s
        result = 0
        for i in range(len(nums)):
            ind = search(i, len(nums)-1)
            if (ind >= 0):
                result += ind-i+1

        return result

start_time = time.time()
t = Solution()
root = t.countSubarrays([2, 3], 10)        
#print(root.val)
#    root.print_tree()
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
