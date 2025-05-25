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
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        q = []
        n = len(isWater)
        m = len(isWater[0])
        for row in range(n):
            for col in range(m):
                if isWater[row][col] == 1:
                    q.append((row,col))
                    isWater[row][col] = 0
                else:
                    isWater[row][col] = -1
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]    
        while q:
            r, c = q.pop(0)
            for dr, dc in dir:
                r1 = r+dr 
                c1 = c+dc
                if r1>=0 and r1<n and c1>=0 and c1<m and isWater[r1][c1]==-1:
                    isWater[r1][c1] = isWater[r][c]+1
                    q.append((r1,c1))

        return isWater
start_time = time.time()
t = Solution()
root = t.highestPeak([[0,1],[0,0]])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
