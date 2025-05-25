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
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        edges = [defaultdict(int) for _ in range(n)]
        if n == 1:
            return 1
        for r in roads:
            edges[r[0]][r[1]] = r[2]
            edges[r[1]][r[0]] = r[2]
        d = [(math.inf,0)]*n
        d[0] = (0,0)
        for v,w in edges[0].items():
            d[v] = (w,1)
        visited = [0] * n
        visited[0] = 1
        v = 0
        while not(visited[-1]):
            #print(v)
            #print(d)
            _, v = min((w,i) for i, w in enumerate(d) if not(visited[i]))
            visited[v] = 1
            
            for v1, w in edges[v].items():
                if not(visited[v1]):
                    if d[v1][0] > d[v][0]+w:
                        d[v1] = (d[v][0]+w, d[v][1])
                    elif d[v1][0] == d[v][0]+w:
                        d[v1] = (d[v1][0], d[v1][1]+d[v][1])
        #print(v)
        #print(d)
        return d[-1][1]%(10**9+7)
        
start_time = time.time()
t = Solution()
root = t.countPaths(6, [[3,0,4],[0,2,3],[1,2,2],[4,1,3],[2,5,5],[2,3,1],[0,4,1],[2,4,6],[4,3,1]])

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
