import sys
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
INF = int(1e9)
answer = INF

def cal(arr):
    sum = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            sum += (graph[arr[i]][arr[j]] + graph[arr[j]][arr[i]])
    return sum

for i in range(1 << N):
    a_team = []
    b_team = []
    for j in range(N):
        if (1 << j) & i:
            a_team.append(j)
        else:
            b_team.append(j)
    if a_team and b_team:
        answer = min(answer, abs(cal(a_team) - cal(b_team)))
        
print(answer)


###DP로 문제