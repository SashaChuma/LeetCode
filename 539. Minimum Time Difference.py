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
# Definition for singly-linked list.
class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        secs = sorted([int(t[:2])*60+int(t[3:]) for t in timePoints])
        secs.append(secs[0]+1440)
        return min(secs[i]-secs[i-1] for i in range(1, len(secs)))
start_time = time.time()
t = Solution()
root = t.findMinDifference(["00:00", "23:59"])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
