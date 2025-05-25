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

def print_matrix(matrix, rowheader=None, colheader=None):
    if not matrix:
        print("Empty matrix")
        return    
    col_widths = [max(len(str(item)) for item in col) for col in zip(*matrix)]
    if colheader:
        if (rowheader):
            print(" ", end=" ")
        print(" ".join(f"{item:>{width}}" for item, width in zip(colheader, col_widths)))
    for i, row in enumerate(matrix):
        if rowheader: 
            print(f"{rowheader[i]:>{col_widths[0]}}", end=" ")
        print(" ".join(f"{item:>{width}}" for item, width in zip(row, col_widths)))
import bisect
class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def verify(k) -> bool:
            a = 0
            for i in range(n):
                d_i = bisect.bisect(d[i],(k,10001))-1
                a += d[i][d_i][1]
                if nums[i] > a:
                    return False
            return True
        n = len(nums)
        d = [[(-1,0)] for _ in range(n+1)]
        for i,q in enumerate(queries):
            d[q[0]].append((i,d[q[0]][-1][1]+q[2]))
            d[q[1]+1].append((i, d[q[1]+1][-1][1]-q[2]))
        #for i, dd in enumerate(d):
        #    print(i, dd)

        left = 0
        right = len(queries)-1
        while left < right:
            mid = (right+left)//2
            if (verify(mid)):
                right = mid-1
            else:
                left = mid+1
        if max(nums) == 0:
            return 0
        if verify(left):
            return left+1
        if (left < len(queries)-1 and verify(left+1)):
            return left+2
        return -1
start_time = time.time()
t = Solution()
root = t.minZeroArray([10], [[0,0,5],[0,0,3],[0,0,2],[0,0,1],[0,0,4],[0,0,1],[0,0,4],[0,0,5],[0,0,3],[0,0,4],[0,0,1]])
#root = t.minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]])
#if root:

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
