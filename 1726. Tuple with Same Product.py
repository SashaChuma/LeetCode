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
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        result = 0
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                p = nums[i]*nums[j]
                dic[p] += 1
                result += (dic[p]-1)*8
        return result
start_time = time.time()
t = Solution()
root = t.tupleSameProduct([2,3,4,6])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
