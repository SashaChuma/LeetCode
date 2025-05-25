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
    def scoreOfStudents(self, s: str, answers: List[int]) -> int:
        def calc(start,end) -> int:
            if start == end:
                return int(tokens[start])
            for i in range((end-start)//2):
                if tokens[start+2*i+1] == "+":
                    return calc(start, start+2*i)+calc(start+2*i+2, end)
            return calc(start,start)*calc(start+2, end)
        
        memo=dict()
        def try_calc(start, end):
            if (start,end) in memo:
                return memo[(start,end)]
            if start == end:
                memo[(start, end)]= set([int(tokens[start])])
                return memo[(start,end)]            
            opts = set()
            if (tokens[end-1] == "*" and tokens[end] == "0") \
                or (tokens[start+1] == "*" and tokens[start] == "0"):
                opts.add(0) 
            for i in range((end-start)//2):
                opt1 = try_calc(start, start+2*i)
                opt2 = try_calc(start+2*i+2, end)
                if tokens[start+2*i+1] == "+":
                    for x1 in opt1:
                        for x2 in opt2:
                            if x1 + x2 <= top:
                                opts.add(x1+x2)
                elif tokens[start+2*i+1] == "*":
                    for x1 in opt1:
                        for x2 in opt2:
                            if x1*x2 <= top:
                                opts.add(x1*x2)
            memo[(start,end)] = opts
            return opts

        tokens = []
        t = 0
        i = 0
        top = max(answers)
        while i < len(s):
            if not(s[i].isnumeric()):
                tokens.append(s[t:i])
                tokens.append(s[i])
                t = i+1
            i += 1
        tokens.append(s[t:])
        corr = calc(0, len(tokens)-1)
        opt = try_calc(0, len(tokens)-1)
        res = 0
       # print(corr, opt)
        for ans in answers:
            if ans == corr: 
                res += 5
            elif ans in opt:
                res += 2
        return res
start_time = time.time()
t = Solution()
root = t.scoreOfStudents("9+8*0", [0])
#if root:

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
