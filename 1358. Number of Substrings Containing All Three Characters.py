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
    def numberOfSubstrings(self, s: str) -> int:
        d = defaultdict(int)
        l, r, n, result = 0, 0, len(s), 0
        while l < n:
            while r < n and len(d) < 3:
                d[s[r]] += 1
                r += 1
            if len(d) == 3: 
                result += n-r+1
            if len(d) == 3:
                while True:
                    c = s[l]
                    d[c]-=1
                    l += 1
                    if d[c] > 0:
                        result += n-r+1
                    else:
                        del d[c]
                        break
            else:
                break
        return result 
start_time = time.time()
t = Solution()
root = t.numberOfSubstrings("abcabc")
#if root:

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
