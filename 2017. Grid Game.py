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
    def gridGame(self, grid: List[List[int]]) -> int:
        def res(i):
            if i < 0:
                return grid[0][1]
            
            return max(min(grid[1][i], grid[0][i+1]), grid[1][i-1] if i > 0 else 0)

        print(grid)
        n = len(grid[0])
        if n == 1:
            return 0
        s, p = 0, 0
        for i in range(n):
            grid[1][i] += p
            p = grid[1][i]
            grid[0][-i-1] += s
            s = grid[0][-i-1]
        i = 0
        print(grid)
        while i < n-1 and grid[1][i] < grid[0][i+1]:
            i += 1 
        if i == n-1:
            return grid[1][i-1]
        return max(res(i), res(i-1))
start_time = time.time()
t = Solution()
root = t.gridGame([[1,3,1,15],[1,3,3,1]])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
