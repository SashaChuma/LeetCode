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
    def maxProduct(self, words: List[str]) -> int:
        by_letter = defaultdict(set)
        word_set = set() 
        result = 0
        for index in range(len(words)):
            word = words[index]
            matching_words = set()
            for l in set(word):
                matching_words.update(by_letter[l])
                by_letter[l].add(index)
            non_matching_words = word_set.difference(matching_words)
            for i in non_matching_words:
                result = max(result, len(word)*len(words[i]))
            word_set.add(index)
        return result
start_time = time.time()
t = Solution()
root = t.maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"])
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
