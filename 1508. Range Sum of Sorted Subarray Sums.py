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
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        heap = []
        for i in range(n):
            heapq.heappush(heap, (nums[i],i))
        j = 0
        result = 0
        while j < right:
            v, i = heapq.heappop(heap)
            j += 1
            if j >= left:
                result += v
                if result > 1000000000:
                    result = result%(1000000000+7)
            if i < n-1:
                heapq.heappush(heap, (v+nums[i+1], i+1))
        return result 
start_time = time.time()
t = Solution()
root = t.rangeSum([1,2,3,4],4,1,5)
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
