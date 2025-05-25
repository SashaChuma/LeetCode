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
    def minSwaps(self, nums: List[int]) -> int:
        c = Counter(nums)
        ones = c[1]
        n = len(nums)
        l = 1 
        r = ones
        window = sum(nums[i] for i in range(ones))
        result = ones-window
        
        while l < n:
            window += nums[r]-nums[l-1]
            if result > ones-window:
                result = ones - window
            l += 1
            r = (r + 1)%n
        return result
start_time = time.time()
t = Solution()
root = t.minSwaps([0,1,1,1,0,0,1,1,0])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
