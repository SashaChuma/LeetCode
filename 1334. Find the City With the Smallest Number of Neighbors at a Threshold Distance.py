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
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [defaultdict(int) for _ in range(n)]
        heap = []
        for edge in edges:
            if edge[2] > distanceThreshold:
                continue
            matrix[edge[0]][edge[1]] = matrix[edge[1]][edge[0]] = edge[2]
            heapq.heappush(heap, (edge[2], edge[0], edge[1]))
        while heap:
            d, i, j = heapq.heappop(heap)
            for v, vd in matrix[i].items():
                if v == j: 
                    continue
                if d + vd <= distanceThreshold and matrix[v][j] == 0:
                    matrix[v][j] = d+vd
                    matrix[j][v] = d+vd
                    heapq.heappush(heap, (d+vd, v, j))
            for v, vd in matrix[j].items():
                if v == i: 
                    continue
                if d + vd <= distanceThreshold and matrix[v][i] == 0:
                    matrix[v][i] = d+vd
                    matrix[i][v] = d+vd
                    heapq.heappush(heap, (d+vd, v, i))
        print(matrix)
        minval = n,-1
        for i in range(n):
            l = len(matrix[i])
            if l <= minval[0]:
                minval = l, i
            
        return minval[1]

        
start_time = time.time()
t = Solution()
root = t.findTheCity(6, [[0,3,5],[2,3,7],[0,5,2],[0,2,5],[1,2,6],[1,4,7],[3,4,4],[2,5,5],[1,5,8]], 4000)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
