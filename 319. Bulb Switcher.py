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
    def bulbSwitch(self, n: int) -> int:
        return math.floor(math.sqrt(n))
start_time = time.time()
t = Solution()
root = t.bulbSwitch(3)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
