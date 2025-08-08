import sys
input = sys.stdin.readline

N = int(input())
arr1 = []
arr2 = []
INF = int(1e10)
for _ in range(N):
    a, b = map(int, input().split())
    arr1.append(a)
    arr2.append(b)
answer = INF
for i in range(1, 1 << N ):
    acidity = 1 #신맛
    acerbity = 0 #쓴맛
    for j in range(N):
        if (1 << j) & i:
            acidity *= arr1[j]
            acerbity += arr2[j]
    answer = min(answer, abs(acidity - acerbity))
    
print(answer)