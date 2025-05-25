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
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        left = right = cStart
        top = bottom = rStart
        result = [[rStart, cStart]]
        while True:
            right += 1
            if top >= 0:
                for c in range(max(0, left+1), min(right+1, cols)):
                    result.append([top, c])
            bottom += 1
            if right < cols:
                for r in range(max(0, top+1), min(bottom+1, rows)):
                    result.append([r, right])
            left -= 1
            if bottom < rows:
                for c in range(min(cols-1, right-1), max(-1, left-1), -1):
                    result.append([bottom, c])
            top -= 1
            if left >= 0:
                for r in range(min(rows-1, bottom-1), max(-1, top-1), -1):
                    result.append([r, left])
            
            if top < 0 and left < 0 and right >= cols and bottom >= rows:
                break
        return result
start_time = time.time()
t = Solution()
root = t.spiralMatrixIII(5,6, 1, 4)
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
