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
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0

        nums = [0 for i in range(n+1)]
        result = 0
        k = 2
        while n > 1:
            if nums[k] == 0:
                while n % k == 0:
                    n = n//k
                    result += k
                x = k*2
                while x < n:
                    nums[x] = 1
                    x += k
            k += 1
            
        return result
start_time = time.time()
t = Solution()
root = t.minSteps(3)
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
