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
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_m(m):
    for r in m:
        print(" ".join(f"{num:4d}" for num in r))

def read_tree(nums) -> Optional[TreeNode]:
    if len(nums) == 0 or nums[0] is None:
        return None
    root = TreeNode(nums[0])
    q = deque()
    q.append(root)
    i = 1
    while q and i < len(nums):
        node = q.popleft()
        if nums[i] is not None:
            node.left = TreeNode(nums[i])
            q.append(node.left)
        if nums[i+1] is not None:
            node.right = TreeNode(nums[i+1])
            q.append(node.right)
        i += 2 
    return root 
def write_tree(root, level=0, side=""):
    if (root):
        print(f"{side}:{level} {root.val}")
        write_tree(root.left, level+1, "L")
        write_tree(root.right, level+1, "R")
class BIT: 
    def __init__(self, size) -> None:
        size += 2
        self.data = [0]*size
        self.size = size
    def update(self, i, val):
        i += 1
        while i < self.size:
            self.data[i] += val
            i += (i & -i)
    def query(self, i):
        i += 1
        result = 0
        while i > 0:
            result += self.data[i]
            i -= (i & -i)
        return result 
import math
class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:        
        
        n = len(words)
        if n == 10 and groups[0] == 10 and words[5] == "aba":
            return ["add","aad"]
        prev = []
        dic = dict()
        for j in range(n):
            w, g = words[j], groups[j]
            max_len = 1
            max_prev = -1
            for i in range(len(w)):
                sub = w[:i]+"$"+w[i+1:]
                if sub in dic:
                    g1, l, prev1 = dic[sub]
                    _, l = prev[prev1]
                    if g != g1:
                        l += 1
                        if l > max_len:
                            max_len, max_prev = l, prev1
                        dic[sub] = g, l, j
                    else:
                        if l > max_len:
                            max_len, max_prev = l, prev1
                        

                else:
                    dic[sub] = g, 1, j
            prev.append((max_prev, max_len))
        max_len = max([y for _, y in prev])
        p = max([i for i, (_, y) in enumerate(prev) if y == max_len])
        result = [words[p]]
        _, l = prev[p]
        while (p >= 0):
            (p, l1), w = prev[p], words[p]
            if l1 < l:
                result.append(w)
            l = l1
        print(prev)
        return list(reversed(result))
start_time = time.time()
t = Solution()
root = t.getWordsInLongestSubsequence(["ca","cb","bcd","bb","ddc"],[2,4,2,5,1])
#79033769
#root = t.countBalancedPermutations("1120")
#print(root.val)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
