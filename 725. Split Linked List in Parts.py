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
# Definition for singly-linked list.
class ListNode:
   def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if k == 1:
            return [head]
        node = head 
        n = 0
        while (node):
            node = node.next
            n += 1
        splits = []
        j = 0
        for i in range(k-1 if n//k > 0 else n%k-1):
            j += n//k + (1 if i < n%k else 0)
            splits.append(j)
        result = [head]
        i = 1
        j = 0 
        node = head 
        #print(splits)
        while j < len(splits):
            while i < splits[j] and node:
                node = node.next
                i += 1
            if node:
                prev = node
                node = node.next
                prev.next = None
                result.append(node)
                i += 1
            j += 1
        for i in range(k-len(result)):
            result.append(None) 
        return result 
start_time = time.time()
t = Solution()
root = t.splitListToParts(ListNode(1, ListNode(2, ListNode(3, ListNode(4, 
                          ListNode(5))))), 7)

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
