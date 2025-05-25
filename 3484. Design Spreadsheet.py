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
class Spreadsheet:
    
    def __init__(self, rows: int):
        self.data = [defaultdict(int) for i in range(26)]             

    def setCell(self, cell: str, value: int) -> None:
        i = int(cell[1:])
        self.data[ord(cell[0])-ord('A')][i] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getArg(self, arg):
        if arg[0].isdigit():
            return int(arg)
        i = int(arg[1:])
        return self.data[ord(arg[0])-ord('A')][i]
    def getValue(self, formula: str) -> int:
        p = formula.index('+')
        arg1 = formula[1:p]
        arg2 = formula[p+1:]
        x1 = self.getArg(arg1)
        x2 = self.getArg(arg2)
        return x1+x2
                     
start_time = time.time()

#t = Solution()
#root = t.longestCommonPrefix(["jump","run","run","jump","run"], 2)

#    root.print_tree()
#print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
