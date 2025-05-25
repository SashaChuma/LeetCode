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

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        self.parent[irep] = jrep

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def binarySearch(arr, low, high, x):
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] == x:
                    return mid
                elif arr[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
            return low+1 if low < len(arr) and arr[low] < x else low
        n = len(nums)
        
        nums = sorted(list(set(nums)))
        dupl = n - len(nums)
        result = 0
        for i, num in enumerate(nums): 
            x = num+n-1
            end = binarySearch(nums, 0, len(nums)-1, x)
            k = end - i if end >= len(nums) or nums[end] > x else end - i + 1 
            result = max(k, result)
            
            if end >= len(nums):
                break
        return n-result
start_time = time.time()
t = Solution()
root = t.minOperations([8,10,16,18,10,10,16,13,13,16])
#if root:

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
