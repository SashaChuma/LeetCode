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
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        x = 0
        for i in range(len(derived)-1):
            x ^= derived[i]
        return (x ^ derived[-1]) == 0
start_time = time.time()
t = Solution()
root = t.doesValidArrayExist([1,1,0])

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
