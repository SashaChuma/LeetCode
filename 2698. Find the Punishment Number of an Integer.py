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
    def check(self, nums, c1, c2, target) -> bool:
        if c1 == c2: 
            return int(nums[c1]) == target
        for i in range(1, c2-c1+2):
            d1 = int(nums[c1:c1+i])
            if d1 > target:
                return False
            elif d1 == target and c1+i-1 == c2: 
                return True
            elif c1+i <= c2 and self.check(nums, c1+i, c2, target-d1):
                return True
        return False 
    def punishmentNumber(self, n: int) -> int:
        result = 0
        for x in range(1, n+1):
            nums = str(x*x)
            if (self.check(nums, 0, len(nums)-1, x)):
                result += x*x
        return result 
start_time = time.time()
t = Solution()
root = t.punishmentNumber(45)

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
