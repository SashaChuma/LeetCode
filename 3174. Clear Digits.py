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
    def clearDigits(self, s: str) -> str:
        stack = []
        for c in s: 
            if c.isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
start_time = time.time()
t = Solution()
root = t.clearDigits("abcb34")
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
