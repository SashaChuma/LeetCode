def bucket_sort(arr):
    if len(arr) == 0:
        return arr

    # Determine the number of buckets
    bucket_count = len(arr)
    min_val, max_val = min(arr), max(arr)
    range_per_bucket = (max_val - min_val) / bucket_count

    # Create empty buckets
    buckets = [[] for _ in range(bucket_count)]

    # Place elements in their respective buckets
    for num in arr:
        index = int((num - min_val) / range_per_bucket)
        if index == bucket_count:  # Handle edge case when num == max_val
            index -= 1
        buckets[index].append(num)


from collections import deque

def bfs(root):
    if root is None:
        return []
    queue, result = deque([root]), []
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Recursive DFS
def dfs_recursive(node):
    if node is None:
        return []
    return [node.value] + dfs_recursive(node.left) + dfs_recursive(node.right)

# Iterative DFS (Using Stack)
def dfs_iterative(root):
    if root is None:
        return []
    stack, result = [root], []
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:
            stack.append(node.right)  # Push right child first (LIFO order)
        if node.left:
            stack.append(node.left)   # Push left child next
    return result

import heapq

def dijkstra(graph, start):
    # Priority queue to store (cost, node)
    pq = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # If a shorter path has already been found, skip processing
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If the new path is shorter, update and push to priority queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

from functools import lru_cache

@lru_cache(maxsize=None)  # Cache results indefinitely
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def floyd_warshall(graph):
    # Number of vertices
    V = len(graph)

    # Initialize distances with the given graph
    dist = [[graph[i][j] for j in range(V)] for i in range(V)]

    # Compute shortest paths
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]  # DP table

    # Build the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:  # Characters match
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:  # No match, take max of left and top
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruct LCS from dp table
    lcs_str = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:  # Move diagonally
            lcs_str.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
            i -= 1
        else:  # Move left
            j -= 1

    return ''.join(reversed(lcs_str)) 