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
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        dic = defaultdict(list)
        for edge in edges:
            dic[edge[0]].append(edge[1])
            dic[edge[1]].append(edge[0])
        parent = [-1] * len(amount)
        price = [(0,0) for i in range(len(amount))]
        stack = [0]
        while stack:
            node = stack.pop()
            for sib in dic[node]:
                if sib != parent[node]:
                    stack.append(sib)
                    parent[sib] = node
        bobs = [len(amount)+1]*len(amount)
        node = bob
        step = 0
        while node != -1:
            bobs[node] = step 
            node = parent[node]
            step+=1
        price = [0.0] * len(amount)
        stack = [(0,0)]
        result = -math.inf
        while stack:
            node, level = stack.pop()
            wage = amount[node]
            if bobs[node] < level:
                wage = 0
            elif bobs[node] == level:
                wage = wage/2
            price[node] = (price[parent[node]] if parent[node] >= 0 else 0)+wage
            is_leaf = True
            for sib in dic[node]:
                if sib == parent[node]:
                    continue
                stack.append((sib,level+1))
                is_leaf = False
            if (is_leaf and price[node] > result):
                result = price[node]
        return int(result)
start_time = time.time()
t = Solution()
root = t.mostProfitablePath([[0,1],[1,2],[1,3],[3,4]], 3, [-2,4,2,-4,6])
#if root:
#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
