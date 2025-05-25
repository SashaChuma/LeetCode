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
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        result = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                if abs(arr[i]-arr[j])<=a:
                    for k in range(j+1, n):
                        if abs(arr[j]-arr[k]) <= b and abs(arr[i]-arr[k]) <= c:
                            result += 1
        return result
        '''vals = sorted(list(set(arr + [xi - a-1 for xi in arr] + [xi + a for xi in arr] 
                               + [xi - c-1 for xi in arr] + [xi + c for xi in arr]
                               + [xi - b-1 for xi in arr] + [xi + b for xi in arr] )))

        index = {v:i for i, v in enumerate(vals)}
        bindex = sorted((v,i) for i, v in enumerate(arr))
        abit = BIT(len(vals)+1)
        cbit = BIT(len(vals)+1)
        bbit = BIT(len(vals)+1)
        aval = []
        cval = []
        bval = []
        for xi in arr:
            xa = index[xi-a-1]
            xb = index[xi+a]
            aval.append(abit.query(xb)-abit.query(xa))
            abit.update(index[xi], 1)
        for xi in reversed(arr):
            xa = index[xi-c-1]
            xb = index[xi+c]
            cval.append(cbit.query(xb)-cbit.query(xa))
            cbit.update(index[xi], 1)
        for xi, ai in zip(arr, aval):
            xa = index[xi-b-1]
            xb = index[xi+b]
            bval.append(bbit.query(xb)-bbit.query(xa))
            bbit.update(index[xi], ai)
        print(arr)
        print(aval)
        print(bval)
        cval.reverse()
        print(cval)
        print(bindex)
        result = 0'''
        '''for i, xi in enumerate(arr):
            xa = xi-b-1
            xb = xi+b+1
            xai = bisect.bisect_right(bindex, xa, key=lambda x:x[0])
            xbi = bisect.bisect_left(bindex, xb, key=lambda x:x[0])
            print(xi, xai, xbi)
            for xj in range(xai, xbi):
                vj, j = bindex[xj]
                if j > i:
                    result += aval[i]*cval[j]'''
        return result
start_time = time.time()
t = Solution()
root = t.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3)        
#print(root.val)
#    root.print_tree()
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
