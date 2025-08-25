import sys
from collections import deque

N, L = map(int, input().strip().split())

arr = list(map(int, input().strip().split()))

q = deque([])

for i in range(N):
    while q and q[-1][1] > arr[i]:
        q.pop()
    q.append((i, arr[i]))
    
    if q[0][0] <= i - L:
        q.popleft()
    print(q[0][1], end = ' ')