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
def print_m(m):
    for r in m:
        print(" ".join(f"{num:4d}" for num in r))
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        dir = [(1,0),(0,1),(-1,0),(0,-1)]
        n = len(grid)
        m = len(grid[0])
        visited = [[0]*m for _ in range(n)]
        pushed = [[0]*m for _ in range(n)]
        v_count = 0
        result = [[math.inf]*m for _ in range(n)]
        h = [(grid[0][0], 0, 0)]
        heapq.heapify(h)
        while v_count < m*n:
            w, r, c = heapq.heappop(h)
            if (not(visited[r][c])):
                v_count += 1
                result[r][c] = w
                visited[r][c] = 1
                for dr,dc in dir:
                    if r+dr < 0 or r+dr >= n:
                        continue
                    if c+dc < 0 or c+dc >= m:
                        continue
                    if visited[r+dr][c+dc]:
                        continue
                    neww = max(w, grid[r+dr][c+dc])
                    if result[r+dr][c+dc] > neww:
                        result[r+dr][c+dc] = neww
                        pushed[r+dr][c+dc] = 0
                    if not(pushed[r+dr][c+dc]):
                        heapq.heappush(h,(neww, r+dr, c+dc))
                        pushed[r+dr][c+dc] = 1
        print(result)
        arr = []
        for r in result:
            arr += r
        arr.sort()
        qres = []
        for q in queries:
            qres.append(bisect.bisect_left(arr, q))
        return qres
start_time = time.time()
t = Solution()
root = t.maxPoints([[1,2,3],[2,5,7],[3,5,1]], [5,6,2])

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
