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
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        result = 0
        if len(nums2)%2 == 1:
            for x in nums1:
                result ^= x
        if len(nums1)%2 == 1:
            for x in nums2:
                result ^= x
        return result 
start_time = time.time()
t = Solution()
root = t.xorAllNums([2,1,3], [10,2,5,0])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
