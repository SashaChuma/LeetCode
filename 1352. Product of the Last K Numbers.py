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

class ProductOfNumbers:
    def __init__(self):
        self.nums = []    
        self.dic = {}
    def add(self, num: int) -> None:
        if num > 0: 
            self.nums.append(num)
        else: 
            self.nums = []
            self.dic = {}
    def get_val(self, start, end):
        if (start == end):
            return self.nums[end]
        if ((start, end) in self.dic):
            return self.dic[(start, end)]
        val = self.get_val(start, end-1)*self.nums[end]
        self.dic[(start, end)] = val
        return val
    def getProduct(self, k: int) -> int:
        end = len(self.nums)-1
        start = len(self.nums)-k
        
        return self.get_val(start, end) if start >= 0 else 0

start_time = time.time()
# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
#["ProductOfNumbers","
obj.add(3)
obj.add(0)
obj.add(2)
obj.add(5)
obj.add(4)
print(obj.getProduct(2))
print(obj.getProduct(3))
print(obj.getProduct(4))
obj.add(8)
print(obj.getProduct(2))
#t = Solution()
#root = t.minOperations([69,89,57,31,84,97,50,38,91,86], 91)

#print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
