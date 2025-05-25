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
    def minCost(self, grid: List[List[int]]) -> int:
        result = [[-1 for col in row] for row in grid]
        heap = []
        heapq.heappush(heap, (0,0,0))
        n = len(grid)
        m = len(grid[0])
        while heap:
            d, row, col = heapq.heappop(heap)    
            if result[row][col] == -1:
                result[row][col] = d
                if col < m-1 and result[row][col+1] == -1:
                    nd = d if grid[row][col] == 1 else d+1
                    heapq.heappush(heap, (nd, row, col+1))
                if row < n-1 and result[row+1][col] == -1:
                    nd = d if grid[row][col] == 3 else d+1
                    heapq.heappush(heap, (nd, row+1, col))
                if col > 0 and result[row][col-1] == -1:
                    nd = d if grid[row][col] == 2 else d+1
                    heapq.heappush(heap, (nd, row, col-1))
                if row > 0 and result[row-1][col] == -1:
                    nd = d if grid[row][col] == 4 else d+1
                    heapq.heappush(heap, (nd, row-1, col))
        return result[-1][-1]
                
start_time = time.time()
t = Solution()
root = t.minCost([[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
