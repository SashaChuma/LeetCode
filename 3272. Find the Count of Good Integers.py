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

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        l = n%2+n//2
        fac = [1]*n
        for i in range(1,n):
            fac[i] = fac[i-1]*(i+1)
        groups = {}
        for num in range(pow(10, l-1), pow(10,l)):
            s = str(num)
            s += ''.join(reversed(s[:n//2]))
            if int(s) % k == 0:
                c = Counter(s)
                key = '_'.join([f"{k}_{v}" for k,v in sorted(c.items())])
                if key not in groups: 
                    groups[key] = c
        result = 0
        for c in groups.values():
            p = fac[n-1]
            for d_count in c.values():
                p /= fac[d_count-1]
            result += p
            if '0' in c:
                c['0'] -= 1
                pp = fac[n-2]
                for d_count in c.values():
                    if d_count > 0:
                        pp /= fac[d_count-1]
                result -= pp
        return int(result)
start_time = time.time()
t = Solution()
root = t.countGoodIntegers(1, 4)
#print(root.val)
#    root.print_tree()
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
