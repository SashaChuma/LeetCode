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
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        s = []
        def collect(ind) -> bool:
            if ind == n:
                result.append(''.join(chr(ord('a')+c) for c in s))
                return len(result) == k
            prev = s[-1] if len(s) > 0 else -1
            for i in range(3):
                if prev != i:
                    s.append(i)
                    if (collect(ind+1)):
                        return True
                    s.pop()
            return False
        collect(0)
        return result[k-1] if len(result) >= k else ""
start_time = time.time()
t = Solution()
root = t.getHappyString(3, 9)

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
