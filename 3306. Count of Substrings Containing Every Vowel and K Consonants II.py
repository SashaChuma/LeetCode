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
    def good(self, dic):
        for v in dic.values():
            if v == 0: 
                return False
        return True
    def concat(self, d1, d2):
        for k,v in d2.items():
            d1[k] += v
    def subtract(self, d1, d2):
        for k,v in d2.items():
            d1[k] -= v
    def calc(self, l,r,base, kk):
        i = 0
        base = base.copy()
        if self.good(base):
            return (len(l)+1)*(len(r)+1)
        result = 0
        k = 0
        j = 0
        while j < len(l):
            while i < len(l) and not(self.good(base)):
                base[l[i]] += 1
                i += 1
            while k < len(r) and not(self.good(base)):
                base[r[k]] += 1
                k += 1
            if self.good(base):
                result += len(r)-k+1
                if kk == 0:
                    result += len(l)-i
                base[l[j]] -= 1
                j += 1
            else: 
                break
        if j == len(l):
            while k < len(r) and not(self.good(base)):
                base[r[k]] += 1
                k += 1
            if (self.good(base)):
                result += len(r)-k+1
        print([l,r],base,result)
        return result

    def countOfSubstrings(self, word: str, k: int) -> int:
        vow = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        parts = []
        i = 0
        j = 0
        while i < len(word):
            if word[i] not in vow:
                parts.append(word[j:i])
                j = i+1
            i += 1
        parts.append(word[j:i])
        if len(parts) < k+1:
            return 0
        for i in range(1,k):
            self.concat(vow, Counter(parts[i]))
        result = 0
        for i in range(k, len(parts)):
            l = parts[i-k]
            r = parts[i] if k > 0 else ""
            result += self.calc(l, r, vow, k)
            if k >= 2:
                self.subtract(vow, Counter(parts[i-k+1]))
                self.concat(vow, Counter(parts[i]))
        print(parts)
        return result
start_time = time.time()
t = Solution()
root = t.countOfSubstrings("aouiei", 0)
#if root:

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
