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
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [1]*(right+1)
        is_prime[1] = 0
        
        for i in range(2, int(math.sqrt(right+1))+1):
            if is_prime[i]:
                k = i*2
                while k <= right:
                    is_prime[k] = 0
                    k += i
        #print([i for i in range(left, right+1) if is_prime[i]])      
        x = -1
        r1,r2 = -1,-1
        result = right-left+1
        for i in range(left, right+1):
            if is_prime[i]:
                if x > 0 and i - x < result:
                    r1, r2 = x, i
                    result = i-x
                x = i
        return [r1, r2]
start_time = time.time()
t = Solution()
root = t.closestPrimes(10,19)
#if root:
#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
