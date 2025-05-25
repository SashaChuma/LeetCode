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
import numpy 
import pprint
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        dir = [(1,0), (0,1), (0,-1), (-1,0)]
        m = len(grid1)
        n = len(grid1[0])
        result = 0
        for r in range(m):
            for c in range(n):
                if grid2[r][c] == 1:
                    stack = [(r,c)]
                    grid2[r][c] = 2
                    match = True
                    while stack:
                        r1, c1 = stack.pop()
                        match &= grid1[r1][c1] == 1
                        for dr, dc in dir:
                            if r1+dr >= 0 and r1+dr < m and\
                               c1+dc >= 0 and c1+dc < n and\
                               grid2[r1+dr][c1+dc] == 1:
                                stack.append((r1+dr, c1+dc))
                                grid2[r1+dr][c1+dc] = 2
                    if match: 
                        result += 1
        return result
start_time = time.time()
t = Solution()
root = t.countSubIslands([[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], 
                        [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
