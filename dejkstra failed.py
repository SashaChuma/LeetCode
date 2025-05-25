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
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        def find_first_row(list_of_lists):
            for row in list_of_lists:
                for val in row:
                    if val[0] == -1:
                        return row
            return None
        def build_path(parents, pos):
            if len(parents[pos]) == 0:
                return [[]]
            result = []
            for p in parents[pos]:
                sub = build_path(parents, p)
                for s in sub:
                    result.append([(m[pos][p],pos,p)]+s)
            return result
        def dejikstra(s1, d1):
            parents = [[] for _ in range(n)]
            visited = set()
            path = [-1]*n
            path[s1] = 0 
            while len(visited) < n:
                node, weight = -1,-1
                for i in range(n):
                    if path[i] > weight and i not in visited:
                        node = i
                        weight = path[i]
                if node == -1:
                    break
                if node == d1:
                    visited.add(node)
                    continue
                visited.add(node)
                for i in range(n):
                    if m[node][i] > -2 and i not in visited:
                        w = 1 if m[node][i] == -1 else m[node][i]
                        if path[i] == -1 or path[node]+w <= path[i]:
                            if path[node]+w == path[i]:
                                parents[i].append(node)
                            else: 
                                parents[i] = [node]
                            path[i] = path[node] + w
            return [path, parents]
        if n == 1:
            return []
        m = [[-2 for _ in range(n)] for _ in range(n)]
        for edge in edges:
            m[edge[0]][edge[1]] = edge[2]
            m[edge[1]][edge[0]] = edge[2]
        
        f = dejikstra(source, destination)
        b = dejikstra(destination, source)
        if f[0][destination] == -1:
            return []
        ''' for i in range(n):
            for j in range(n):
                if m[i][j] == -1 and f[0][i] >= 0 and b[0][j] >= 0 and i != j and f[0][i] + b[0][j]+1 <= target:
                    fp = build_path(f[1], i)
                    bp = build_path(b[1], j)
                    fs = set(edge[1] for edge in fp[0])
                    bs = set(edge[1]for edge in bp[0])
                    if len(fs.intersection(bs)) == 0:
                        for edge in edges:
                            if edge[2] == -1:
                                edge[2] = 1
                            if (edge[0] == i and edge[1] == j) or (edge[1] == i and edge[0] == j):
                                edge[2] = target-b[0][j]-f[0][i]

                        return edges'''
        fp = build_path(f[1], destination)
        p_len = sum([1 if v[0] == -1 else v[0] for v in fp[0]])
        i,j = -1,-1
        if p_len > target:
            return []
        if p_len == target:
            i = -1
            j = -1
        

        #print(b)
        #l = build_path(destination)
        #p_len = sum([1 if v[0] == -1 else v[0] for v in l[0]])
        #print(p_len)
        #if p_len > target:
        #    return []
        
        #print(find_first_row(l))
start_time = time.time()
t = Solution()
root = t.modifiedGraphEdges(4,[[0,1,-1],[1,2,-1],[3,1,-1],[3,0,2],[0,2,5]],2,3,8)
print(root)

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} seconds")
