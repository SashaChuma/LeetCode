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
    def maxPoints(self, points: List[List[int]]) -> int:
        prev = points[0]
        for i in range(1,len(points)):
            next = []
            mv, mi = prev[0], 0
            for j in range(len(points[0])):
                if prev[j] > mv-j+mi:
                    mv = prev[j]
                    mi = j
                    k = j-1
                    while k >= 0: 
                        if next[k] < points[i][k]+mv+k-j:
                            next[k] = points[i][k]+mv+k-j
                        else:
                            break
                        k-=1
                next.append(points[i][j]+mv-j+mi)    
            prev = next
        return max(prev)
start_time = time.time()
t = Solution()
root = t.maxPoints([[1,2,3],[1,5,1],[3,1,1]])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
