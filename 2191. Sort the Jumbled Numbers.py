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
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def convert(num):
            return int("".join([str(mapping[int(c)]) for c in str(num)]))
        
        return [num for converted, index, num in sorted([(convert(num), index, num) for index,num in enumerate(nums)])]
start_time = time.time()
t = Solution()
root = t.sortJumbled([8,9,4,0,2,1,3,5,7,6], [991,338,38])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
