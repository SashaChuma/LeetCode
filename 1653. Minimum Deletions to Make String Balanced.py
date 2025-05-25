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
    def minimumDeletions(self, s: str) -> int:
        def read(s, pos, x):
            l = 0
            while pos+l < len(s) and pos+l >= 0 and s[pos+l] == x:
                l += 1
            return l
        pos = 0
        n = len(s)
        ta = 0
        pairs = []
        while pos < n:
            la = read(s, pos, 'a')
            pos += la
            ta += la
            lb = read(s, pos, 'b')
            pos += lb
            pairs.append((la,lb))
        if len(pairs) < 2:
            return 0
        
        ta -= pairs[0][0]
        tb = pairs[0][1]
        result = ta 
        for i in range(1,len(pairs)):
            ta -= pairs[i][0]
            result = min(result, ta+tb)
            tb += pairs[i][1]
        return result

start_time = time.time()
t = Solution()
#root = t.minimumDeletions("ababaaaabbbbbaaababbbbbbaaabbaababbabbbbaabbbbaabbabbabaabbbababaa")
root = t.minimumDeletions("aaabbaababbbabababbaabbbbaaaaaaabbbbababbaabbabaabbbbabbbbbbbaaababbababaaabaaabaababbbbbabbaabbaaabbbbbbbbbabbbbbbbaaababbaabaaaaababbaaaababbabbaaaba")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
