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
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        def process(r,c):
            border = set()
            dir = [(1,0),(0,1),(-1,0),(0,-1)]
            stack = [(r,c)]
            grid[r][c] = 2
            area = 1
            while stack:
                r1,c1 = stack.pop()
                for dr, dc in dir:
                    r2 = r1+dr
                    c2 = c1+dc 
                    if r2 >= 0 and r2 < n and c2 >= 0 and c2 < m:
                        if grid[r2][c2] == 1:
                            stack.append((r2,c2))
                            area += 1                
                            grid[r2][c2] = 2
                        elif grid[r2][c2] <= 0 and (r2,c2) not in border:
                            border.add((r2,c2))
            for r1, c1 in border: 
                grid[r1][c1] -= area
        n = len(grid)
        m = len(grid[0])
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    process(r,c)
        result = min(min(row) for row in grid)
        if result > 0:
            return m*n
        if result == 0:
            return 1
        if result < 0:
            return -result+1
        return 1
start_time = time.time()
t = Solution()
root = t.largestIsland([[1,0],[0,1]])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
