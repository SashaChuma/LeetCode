from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 0: 
            return []
        c = Counter(words[0])
        for w in words:
            c1 = Counter(w)
            for ch,count in c.items():
                print(ch,count)
                if ch in c1:
                    c[ch] = min(count, c1[ch])
                else: 
                    c[ch] = 0
        res = [] 
        #print(c)
        for ch,count in c.items():
            res += [ch]*count
        return res
start_time = time.time()
app = Solution()
root = app.commonChars(["bella","label","roller"])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


