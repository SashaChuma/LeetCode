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
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(t, k)->bool:
            if t == 0:
                return True
            if k <= n and t <= min_val:
                return True
            if len(candies) > 1000:
                tt = t 
                while k > 0:
                    pos = bisect.bisect_left(candies, tt)
                    if pos == n: 
                        return False
                    k -= n - pos
                    tt += t
                return True
            else: 
                count = 0
                for c in candies:
                    count += c//t
                return count >=k 
        candies.sort()
        min_val = min(candies)    
        sum_val = sum(candies)
        if sum_val < k:
            return 0
        elif sum_val < 2*k: 
            return 1

        n = len(candies)
        left = 0
        right = min(max(candies), sum_val//k)
        while left < right: 
            mid = (left+right)//2
            if check(mid, k):
                left = mid+1
            else:
                right = mid-1
        return left if check(left, k) else left-1       
start_time = time.time()
t = Solution()
root = t.maximumCandies([8249021,995692,3769504,2664179,4805275,9318902,9892266,4395580,2629315],45067556)
#if root:

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
