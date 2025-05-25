from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(list)
        remainder = 0
        res = 0
        dic[0] = [-1]
        for i in range(len(nums)):
            remainder = (remainder + nums[i])%k
            dic[remainder].append(i)
            res += len(dic[remainder])-1
        return res
    
start_time = time.time()
app = Solution()
root = app.subarraysDivByK([5], 9)
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


