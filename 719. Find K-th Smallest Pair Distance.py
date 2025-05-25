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
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        cl = list(c.items())
        n = max(nums)+1
        dist = [0]*(n+1)
        for i in range(len(cl)):
            xv = cl[i][0]
            xc = cl[i][1]
            if xc > 1:
                dist[0] += xc*(xc-1)//2
            for j in range(i+1,len(cl)):
                dist[abs(xv-cl[j][0])] += xc*cl[j][1]
       # print(dist)
        print(list(enumerate(dist)))
        for i, v in enumerate(dist):
            k -= v
            if k <= 0:
                return i
        return 0

start_time = time.time()
t = Solution()
root = t.smallestDistancePair([95,29,47,58,80,65,26,7,69,0,1,53,61,46,66,30,78,25,1,62,5,1,78,60,81,100,52,33,9,52,7,74,94,93,47,68,80,81,50,31,9,96,8,8,64,4,40,22,50,93], 1142)
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
