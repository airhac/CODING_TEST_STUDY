import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
m = int(input()) #한 소형차가 최대 끌수 있는 칸 수 
sum = [0] * (n + 1)
dp = [[0] * (n + 1) for _ in range(4)]
#m개 만큼 합한 값을 저장해야함
for i in range(1, n + 1): 
    sum[i] = sum[i - 1] + arr[i - 1]
    
for i in range(1, 4):
    for j in range(m, n + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - m] + sum[j] - sum[j - m])
        
print(dp[-1][-1])  