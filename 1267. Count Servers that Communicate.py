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
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        cols = [-1]*m
        rows = [-1]*n
        s = set()
        for r in range(n):
            for c in range(m):
                if grid[r][c] == 0:
                    continue
                conn = 0
            
                if cols[c] >= 0:
                    s.add((cols[c], c))
                    conn = 1
                if rows[r] >= 0:
                    s.add((r, rows[r]))
                    conn = 1
                if (conn):
                    s.add((r,c))
                cols[c] = r
                rows[r] = c
        return len(s)
start_time = time.time()
t = Solution()
root = t.countServers([[0,0,1,0,1],[0,1,0,1,0],[0,1,1,1,0],[1,0,0,1,1],[0,0,1,1,0]])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
