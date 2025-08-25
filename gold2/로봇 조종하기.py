import sys
input = sys.stdin.readline

N, M  = map(int, input().split())

graph = [list(map(int, input().strip().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]

dp[0][::] = graph[0][::]

for j in range(1, M):
    dp[0][j] += dp[0][j - 1]
    
for i in range(1, N):
    tmp1 = [0] * M
    tmp2 = [0] * M
    
    for j in range(M):
        if j == 0:
            tmp1[j] = dp[i - 1][j] + graph[i][j]
            tmp2[M - j - 1] = dp[i - 1][M - j - 1] + graph[i][M - j - 1]
            continue
        
        tmp1[j] = graph[i][j] + max(dp[i - 1][j], tmp1[j - 1])
        tmp2[M - j - 1] = graph[i][M - j - 1] + max(dp[i - 1][M - j - 1],tmp2[M - j])
        
    
    tmp = [max(tmp1[i], tmp2[i]) for i in range(M)]
    dp[i] = tmp[::]

print(dp[N - 1][M - 1])