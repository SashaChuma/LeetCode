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
    def multiply_m(self, m1, m2):
        mod = 10**9+7
        mat = [[0]*26 for _ in range(26)]
        for row in range(26):
            for col in range(26):
                mat[row][col] = sum([m1[row][i]*m2[i][col] for i in range(26)])%mod
        return mat
    def multiply_r(self, m, r):
        mod = 10**9+7
        res = [0]*26
        for i in range(26):
            res[i] = sum([r[j]*m[j][i] for j in range(26)])%mod
        return res
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        mod = 10**9+7
        c = Counter(s)
        ord_a = ord('a')
        freq = [c[chr(ord_a+i)] for i in range(26)]
        bt = list(reversed(bin(t)[2:]))
        print(bt)
        mat = [[0]*26 for _ in range(26)]
        for row in range(26):
            for col in range(nums[row]):
                mat[row][(row+col+1)%26] = 1
        if bt[0] == '1':
            freq = self.multiply_r(mat, freq)
        for i in range(1, len(bt)):
            mat = self.multiply_m(mat, mat)
            if bt[i] == '1':
                freq = self.multiply_r(mat, freq)    
        
        return sum(freq)%mod
start_time = time.time()
t = Solution()
root = t.lengthAfterTransformations("jqktcurgdvlibczdsvnsg", 7517, [1]*25+[2])
#79033769
#root = t.countBalancedPermutations("1120")
#print(root.val)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
