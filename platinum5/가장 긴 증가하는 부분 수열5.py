import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

INF = int(1e10)

dp = [-INF]
table = []

for i in range(N):
    if dp[-1] < arr[i]:
        dp.append(arr[i])
        table.append((len(dp) - 1, arr[i]))
    else:
        loc = bisect_left(dp, arr[i])
        dp[loc] = arr[i]
        table.append((loc, arr[i]))
        
idx = len(dp) - 1
print(idx)

result = []
for i in range(len(table)-1, -1, -1):
    if table[i][0] == idx:
        result.append(table[i][1])
        idx -= 1
        
print(*result[::-1])