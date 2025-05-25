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
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @lru_cache(None)
        def minHeight(i, n):
            if i == n:
                return 0
            l = 0
            h = 0
            offset = 0
            result = -1
            while i+offset < n and l + books[i+offset][0] <= shelfWidth: 
                l += books[i+offset][0]
                h = max(h, books[i+offset][1])
                r = h + minHeight(i+offset+1, n)
                if result == -1 or result > r:
                    result = r
                offset += 1
            return result           
        return minHeight(0, len(books))
start_time = time.time()
t = Solution()
root = t.minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
