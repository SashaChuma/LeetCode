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

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        offset = defaultdict(int)
        for i, v in enumerate(nums):
            offset[v-i] += 1
        result = sum([v*(v-1)//2 for v in offset.values()])
        n = len(nums)
        return n*(n-1)//2 - result
start_time = time.time()
t = Solution()
root = t.countBadPairs([4,1,3,3])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
