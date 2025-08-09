import sys
input = sys.stdin.readline


N = int(input())

bit_range = 1 << 10

MOD = int(1e9)

dp = [[[0] * (bit_range) for _ in range(10)] for _ in range(N + 1)]

for k in range(1, 10):
    dp[1][k][1<<k] = 1
    
for i in range(2, N + 1):
    for j in range(10):
        for b in range(bit_range):
            if j == 0:
                dp[i][j][b | (1 << j)] += dp[i - 1][j + 1][b]
            elif j == 9:
                dp[i][j][b | (1 << j)] += dp[i - 1][j - 1][b]
            else:
                dp[i][j][b | (1 << j)] += (dp[i - 1][j + 1][b] + dp[i - 1][j - 1][b])
                
            dp[i][j][b | (1 << j)] %= MOD
                
total = 0
for i in range(10):
    total += dp[N][i][1023]
print(total % MOD)