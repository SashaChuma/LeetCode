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
    def longestSubarray(self, nums: List[int]) -> int:
        v = 0
        l = 0
        result = 0
        for num in nums: 
            if num > v:
                result = 0
                l = 1
                v = num
            elif num == v:
                l += 1
            else:
                result = max(result, l)
                l = 0    
        return max(result, l)
start_time = time.time()
t = Solution()
root = t.longestSubarray([323376, 323376, 323376, 323376, 323376, 323376, 323376, 75940, 323376, 323377, 323377])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
