from typing import List
from typing import Optional
from collections import defaultdict
import time
from collections import Counter
import math
import hashlib
import heapq
class Trie:
    def __init__(self):
        self.subTrie = defaultdict(Trie)
        self.leaves = set()

    def insert(self, word: str) -> None:
        self.insertSub(word, 0, len(word))

    def insertSub(self, word: str, index: int, l: int) -> None:
        if index == l:
            return 
        self.subTrie[word[index]].insertSub(word, index+1, l)
        if index == l-1:
            self.leaves.add(word[-1])

    def getSub(self, word: str, index: int, l: int) -> int:
        if index == l:
            return -1
        if word[index] in self.leaves:
            return index
        
        if word[index] in self.subTrie:
            return self.subTrie[word[index]].getSub(word, index+1, l)

        return -1
        

    
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Trie()
        for w in dictionary:
            t.insert(w)
        res = []
        for w in sentence.split(' '):
            sub = t.getSub(w, 0, len(w))
            res.append(w[0:sub+1] if sub >= 0 else w)
        return " ".join(res)
start_time = time.time()
app = Solution()
root = app.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
print(root)
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")


