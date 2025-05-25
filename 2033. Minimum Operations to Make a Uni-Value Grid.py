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
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = [] 
        for r in grid:
            nums += r
        c = Counter(nums)
        nums = sorted(c.keys())
        print(nums)
        for num in nums:
            if (num-nums[0])%x != 0:
                return -1
        if len(nums) == 1:
            return 0
        frw = [0]
        items = 0
        s = 0
        for i in range(1, len(nums)): 
            items += c[nums[i-1]]
            s += items*(nums[i]-nums[i-1])//x
            frw.append(s)
        bcw = [0]
        items = 0
        s = 0
        for i in range(len(nums)-2, -1, -1): 
            items += c[nums[i+1]]
            s += items*(nums[i+1]-nums[i])//x
            bcw.append(s)
        return min(x+y for x,y in zip(reversed(frw),bcw))
start_time = time.time()
t = Solution()
root = t.minOperations([[2,4],[6,8]], 2)

#    root.print_tree()
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
