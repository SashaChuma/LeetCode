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
class Word:
    def __init__(self):
        self.data = defaultdict(Word)
        self.ind = set()
    def add(self, w, start, i):
        self.ind.add(i)
        if len(w) == start:
            return 
        self.data[w[start]].add(w, start+1, i)
    def max_exclusive(self, k, i, pos):
        l = len(self.ind) if i not in self.ind else len(self.ind)-1
        if l < k: 
            return 0
        result = 1
        for letter, sub in self.data.items():
            val = sub.max_exclusive(k, i, pos+1)
            if val: 
                result = max(1+val, result)
        return result 
    def best(self, k, l):
        ll = len(self.ind)
        if ll < k: 
            return ""
        result = l
        for letter, sub in self.data.items():
            val = sub.best(k,letter)
            if val and 1+len(val) > len(result): 
                result = l+val
        return result
class Solution:
    def longestCommonPrefix(self, words: List[str], k: int) -> List[int]:
        dic = Word()
        for i,w in enumerate(words):
            dic.add(w, 0, i)
        b =dic.best(2, "")
        result = []
        for i in range(len(words)):
            if words[i][0] == b[0]:
                v = dic.max_exclusive(k, i, 0)
                result.append(v-1 if v > 0 else 0)
            else: 
                result.append(len(b))
        return result 
start_time = time.time()

t = Solution()
root = t.longestCommonPrefix(["jump","run","run","jump","run"], 2)

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
