import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().strip().split())) for _ in range(N)]
answer = 0
for i in range(N):
    answer += (arr[i][0] * arr[i + 1][1] - arr[i][1] * arr[i + 1][0])
    
print(abs(answer) / 2)