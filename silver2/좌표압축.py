import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().strip().split()))

arr2 = sorted(set(arr))

dic = defaultdict(int)
for idx, a in enumerate(arr2):
    dic[a] = idx
result = []
for i in range(n):
    result.append(dic[arr[i]])
print(*result)