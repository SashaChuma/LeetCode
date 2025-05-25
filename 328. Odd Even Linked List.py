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
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def calc(r,c) -> int:
            if result[r][c] == -1:
                res = 1
                for d in dirs:
                    r1 = r+d[0]
                    c1 = c+d[1]
                    if r1>=0 and r1<m and c1>=0 and c1<n and matrix[r][c] > matrix[r1][c1]:
                        res = max(calc(r1,c1)+1, res)
                result[r][c] = res
            return result[r][c]
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        m = len(matrix)
        n = len(matrix[0])
        m_val = 1
        result = [[-1]*n for _ in range(m)]
        for r in range(m):
            for c in range(n):
                m_val = max(calc(r,c), m_val)
        return m_val
start_time = time.time()
t = Solution()
root = t.longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
