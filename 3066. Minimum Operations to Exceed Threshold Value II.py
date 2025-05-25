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
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            if x < k: 
                heapq.heappush(heap, x)
        result = 0
        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)
            result += 1
            if x*2+y < k:
                heapq.heappush(heap, x*2+y)
            else:
                result += (len(heap)+1)//2
                return result
        if heap:
            result +=1
        return result 

start_time = time.time()
t = Solution()
root = t.minOperations([69,89,57,31,84,97,50,38,91,86], 91)

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
