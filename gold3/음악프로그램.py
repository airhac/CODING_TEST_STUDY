import sys
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().strip().split())

graph = [[] for _ in range(N + 1)]
indegree = [0] * (N + 1)

for _ in range(N):
    priority = list(map(int, input().strip().split()))
    for i in range(1, len(priority) - 1):
        graph[priority[i]].append(priority[i + 1])
        indegree[priority[i + 1]] += 1
q = deque([])   
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        
result = []
while q:
    node = q.popleft()
    result.append(node)
    
    for next in graph[node]:
        indegree[next] -= 1
        
        if indegree[next] == 0:
            q.append(next)
            
if len(result) == N:
    for num in result:
        print(num)
    
else:
    print(0)