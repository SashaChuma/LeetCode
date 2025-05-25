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
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        pos = 0
        n = len(traversal)
        def scan():
            level = 0
            nonlocal pos
            num_str = ""
            if pos >= n: 
                return (False, 0, 0)
            while traversal[pos] == "-":
                level += 1 
                pos += 1
            while pos < n and traversal[pos].isnumeric():
                num_str += traversal[pos]
                pos += 1
            return True, int(num_str), level
        eof, val, lvl = scan()
        if not(eof):
            return None
        root = TreeNode(val)
        s = []
        s.append((root, lvl))
        while eof:
            eof, val, lvl = scan()
            if (not(eof)):
                break
            node = TreeNode(val)
            while s[-1][1] > lvl:
                s.pop()
            if s[-1][1] == lvl-1:
                s[-1][0].left = node 
            else:
                s[-2][0].right = node
            s.append((node, lvl))
            #print(val, lvl)
        return root
start_time = time.time()
t = Solution()
root = t.recoverFromPreorder("1-2--3--4-5--6--7")
if root:
    root.print_tree()
#print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
