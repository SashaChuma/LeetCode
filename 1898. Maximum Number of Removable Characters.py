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

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        def is_subsequence(s1, s2, step):
            i, j = 0, 0
            while i < len(s1) and j < len(s2):
                if removed[j]>step and s1[i] == s2[j]:  
                    i += 1  
                j += 1  
            return i == len(s1)
        removed = [len(removable)+2 for _ in s]
        for k, i in enumerate(removable):
            removed[i] = k
        #print(removed)
        #for i in range(len(removable)):
        #    print(i, is_subsequence(p, s, i))
        left = 0
        right = len(removable)-1
        while left < right: 
            mid = (right+left)//2
            if is_subsequence(p, s, mid):
                left = mid+1
            else: 
                right = mid-1
        if is_subsequence(p, s, left):
            return left+1
        if left > 0 and is_subsequence(p, s, left-1):
            return left
        return 0
        
start_time = time.time()
t = Solution()
root = t.maximumRemovals("abcacb", "ab", [3,1,0])
#if root:

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
