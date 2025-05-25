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
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        map = {v:k for k,v in enumerate(arr)}
        n = len(arr)
        tails = [defaultdict(int) for _ in range(n)]
        m_val = arr[-1]
        mid = 0
        while arr[mid] < m_val/2:
            mid += 1
        if mid == 0: 
            return 0

        result = 0
        for i in range(1, n):
            for j in range(i):
                s = arr[i]+arr[j]
                if s > m_val:
                    break

                if s in map:
                    k = map[s]
                    tails[k][i] = tails[i][j]+1
                    if tails[k][i] > result: 
                        result = tails[k][i] 
        return result+2 if result > 0 else 0
start_time = time.time()
t = Solution()
root = t.lenLongestFibSubseq([1,2,3,4,5,6,7,8])
#if root:
#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
