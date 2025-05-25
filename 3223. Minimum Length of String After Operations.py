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
    def minimumLength(self, s: str) -> int:
        return sum([1 if v%2 else 2 for k,v in Counter(s).items()])
start_time = time.time()
t = Solution()
root = t.minimumLength("abaacbcbb")

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
