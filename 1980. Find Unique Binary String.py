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
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        s = set(nums)
        n = len(nums[0])
        i = 0
        while True:
            x = bin(i)[2:]
            if len(x) > n:
                break
            if len(x) < n:
                x = "0"*(n-len(x)) + x
            if x not in s:
                return x 
            i+= 1
            
            
        return ""

start_time = time.time()
t = Solution()
root = t.findDifferentBinaryString(["1"])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
