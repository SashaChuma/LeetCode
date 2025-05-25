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
class Solution:
     def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a':1,
                'e':2,
                'i':4,
                'o':8,
                'u':16}   
        dict = {0: -1}
        result = 0
        mask = 0
        for i in range(len(s)):
            c = s[i]
            if (c in vowels):
                mask ^= vowels[c]
                if mask in dict:
                    result = max(result, i-dict[mask])
                else: 
                    dict[mask] = i
            else:
                result = max(result, i-dict[mask])
        return result 
        

start_time = time.time()
t = Solution()
root = t.findTheLongestSubstring("eleetminicoworoep")

print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
