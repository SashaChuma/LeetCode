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
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        res = [[-1]*m for _ in range(n)]
        visited = set()
        h = []
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        heapq.heappush(h, (0, 0, 0, 2))
        while h:
            t,r,c,move = heapq.heappop(h)
            if (r,c) in visited:
                continue
            if r == n-1 and c == m-1:
                return t
            visited.add((r,c))
            print(r,c)
            print_m(res)
            res[r][c] = t
            for dr, dc in dirs:
                r2 = r+dr
                c2 = c+dc
                if r2 >= 0 and r2 < n:
                    if c2 >= 0 and c2 < m and (r2,c2) not in visited:
                        nm = 1 if move == 2 else 2
                        nt = max(t+nm,moveTime[r2][c2]+nm)
                        if res[r2][c2] == -1 or res[r2][c2] > nt:
                            res[r2][c2] = nt
                            heapq.heappush(h, (nt, r2,c2, nm))
        print_m(res)
        return 0
start_time = time.time()
t = Solution()
root = t.minTimeToReach([[0,58],[27,69]])
#print(root.val)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
