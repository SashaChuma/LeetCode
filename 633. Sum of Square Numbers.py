from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        dic = {}
        i = 0
        x = 0
        dic[0] = 0
        while x <= c//2:
            i += 1
            x = i*i
            dic[x] = i
        i -= 1
        x = i*i
        while x <= c:
            if c - x in dic:
                return True
            i += 1
            x = i*i 
        return False
start_time = time.time()
app = Solution()
root = app.judgeSquareSum(4)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


