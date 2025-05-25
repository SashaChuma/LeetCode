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
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def calc(row, col) -> int:
            res = grid[row][col]
            dir = [(1,0), (0,1), (-1,0), (0,-1)]
            q = deque([(row,col)])
            grid[row][col] = 0
            while q:
                r,c = q.popleft()
                for dr, dc in dir:
                    if r+dr < n and r+dr >= 0 and c+dc < m and c+dc >= 0 and grid[r+dr][c+dc] > 0:
                        q.append((r+dr, c+dc))
                        res += grid[r+dr][c+dc]
                        grid[r+dr][c+dc] = 0
            return res
        result = 0
        n = len(grid)
        m = len(grid[0])
        for row in range(n):
            for col in range(m):
                if grid[row][col] > 0: 
                    result = max(result, calc(row,col))
        return result 

start_time = time.time()
t = Solution()
root = t.findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
