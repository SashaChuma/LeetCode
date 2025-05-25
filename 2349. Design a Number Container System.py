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

class SortedArray:
    def __init__(self):
        self.data = []

    def insert(self, val):
        bisect.insort(self.data, val)  # O(log n) insertion

    def remove(self, val):
        index = bisect.bisect_left(self.data, val)
        if index < len(self.data) and self.data[index] == val:
            self.data.pop(index)  # O(n) worst case, but usually fast

    def peek_min(self):
        return self.data[0] if self.data else -1

    def pop_min(self):
        return self.data.pop(0) if self.data else -1  # O(n) worst case

    def __str__(self):
        return str(self.data)
            
class NumberContainers:
    def __init__(self):
        self.dic = {}
        self.index_map = defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if number not in self.dic: 
            self.dic[number] = SortedArray()
        if index in self.index_map and self.index_map[index] > 0:
            self.dic[self.index_map[index]].remove(index)
            self.index_map[index] = 0 
        self.dic[number].insert(index)
        self.index_map[index] = number
    def find(self, number: int) -> int:
        if number not in self.dic:
            return -1
        return self.dic[number].peek_min()
# Your NumberContainers object will be instantiated and called as such:
obj = NumberContainers()
#[[],[75,40],[14],[41],[40],[27,40],[22,14],[85,14],[22,40],[18,34],[92,41],[22,40],[75,40],[59,34],[40],[27,14],[34],[14]
# ,[13,34],[40],[18,41]]
obj.change(75,40)
obj.find(14)
obj.find(41)
obj.find(40)
obj.change(27,40)
obj.change(22,14)
obj.change(85,14)
obj.change(22,40)
obj.change(18,34)
obj.change(92,41)
obj.change(22,40)
obj.change(75,40)
obj.change(59,34)
print(obj.find(40))
obj.change(27,14)
obj.find(34)
obj.find(14)
obj.change(13,34)
obj.find(40)
obj.change(18,41)
start_time = time.time()
#t = Solution()
#root = t.tupleSameProduct([2,3,4,6])
#print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
