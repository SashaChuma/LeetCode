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
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        dd = [-1]*(amount+1)
        for c in coins:
            if c <= amount:
                dd[c] = 1
        for i in range(1, amount):
            if dd[i] > 0:
                for c in coins:
                    if i + c <= amount and (dd[i+c]==-1 or dd[i]+1<dd[i+c]):
                        dd[i+c] = dd[i]+1
        return dd[amount]
start_time = time.time()
t = Solution()
root = t.coinChange([2],3)
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
