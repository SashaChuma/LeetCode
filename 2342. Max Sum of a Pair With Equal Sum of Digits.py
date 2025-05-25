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
    def maximumSum(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        dic = {}
        result = -1
        print(nums)
        for num in nums:
            dsum = sum(int(c) for c in str(num))
            if dsum in dic:
                result = max(dic[dsum]+num, result)
            else:
                dic[dsum] = num 
        return result
start_time = time.time()
t = Solution()
root = t.maximumSum([368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183])
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
