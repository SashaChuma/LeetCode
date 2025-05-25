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
from collections import deque 
class UnionFind:
    def __init__(self, size):  
        self.parent = list(range(size))
        self.edges = [0]*size
    def find(self, i):
        if self.parent[i] == i:
            return i
        return self.find(self.parent[i])
    
    def unite(self, i, j):
        irep = self.find(i)
        jrep = self.find(j)
        if irep != jrep:
            if self.edges[irep] > self.edges[jrep]:
                irep, jrep = jrep, irep
            self.parent[irep] = jrep
            self.edges[jrep] += self.edges[irep]+1
        else: 
            self.edges[jrep] += 1
    def countFull(self):
        c = Counter([self.find(i) for i in range(len(self.parent))])
        result = 0
        for root, vnum in c.items(): 
            if vnum*(vnum-1)//2 == self.edges[root]:
                result += 1
        return result 

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        ds = UnionFind(n)
        for edge in edges:
            ds.unite(edge[0], edge[1])
        return ds.countFull()
        
start_time = time.time()
t = Solution()
root = t.countCompleteComponents(5, [[1,2],[3,4],[1,4],[2,3],[1,3],[2,4]])

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
