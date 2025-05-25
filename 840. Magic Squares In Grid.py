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
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def r(i, j):
            return grid[i][j]+grid[i][j-1]+grid[i][j-2]
        def c(i, j):
            return grid[i][j]+grid[i-1][j]+grid[i-2][j]
        def d1(i, j): 
            return grid[i][j]+grid[i-1][j-1]+grid[i-2][j-2]
        def d2(i, j):
            return grid[i-2][j]+grid[i-1][j-1]+grid[i][j-2]
        def ismagic(i,j):
            arr = grid[i][j-2:j+1]+grid[i-1][j-2:j+1]+grid[i-2][j-2:j+1]
            s = set(arr)
            return len(s) == len(arr) and sum(arr) == 45 and 0 not in s
        n = len(grid)
        if n < 3:
            return 0
        m = len(grid[0])
        result = 0
        for i in range(2, n):
            for j in range(2, m):
                x = r(i,j)
                if x==r(i-1,j) and x==r(i-2,j) and x==c(i,j) and x==c(i,j-1)\
               and x==c(i,j-2) and x==d1(i,j) and x==d2(i,j) and ismagic(i,j):
                    result += 1  
        return result 
start_time = time.time()
t = Solution()
root = t.numMagicSquaresInside([[4,3,8,4],[9,5,1,9],[2,7,6,2]])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
