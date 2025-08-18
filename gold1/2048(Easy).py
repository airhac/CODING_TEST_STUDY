import sys

input = sys.stdin.readline

N = int(input())

graph = [list(map(int, input().strip().split())) for _ in range(N)]

cnt = 0
#해당 경우 최댓값
def cal(arr):
    res = 0
    for i in range(N):
        res = max(res, max(arr[i]))
    return res

def add(N, d, arr):
    if d == 0:
        for i in range(N):
            top = N - 1
            for j in range(N - 2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    
                    if arr[i][top] == 0:
                        arr[i][top] = tmp
                    elif arr[i][top] == tmp:
                        arr[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        arr[i][top] = tmp
    elif d == 1:
        for i in range(N):
            top = 0
            for j in range(1, N):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    
                    if arr[i][top] == 0:
                        arr[i][top] = tmp
                    elif arr[i][top] == tmp:
                        arr[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        arr[i][top] = tmp
                    
                    
    elif d == 2:
        for j in range(N):
            top = N - 1
            for i in range(N - 2, -1, -1):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    
                    if arr[top][j] == 0:
                        arr[top][j] = tmp
                    elif arr[top][j] == tmp:
                        arr[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        arr[top][j] = tmp
    else:
        for j in range(N):
            top = 0
            for i in range(1, N):
                if arr[i][j]:
                    tmp = arr[i][j]
                    arr[i][j] = 0
                    
                    if arr[top][j] == 0:
                        arr[top][j] = tmp
                    elif arr[top][j] == tmp:
                        arr[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        arr[top][j] = tmp
    return arr

answer = 0

def dfs(answer, cnt, N, graph):
    
    answer = max(answer, cal(graph))
    
    if cnt == 5:
        return answer
    
    for d in range(4):
        tmp_arr = [row[:] for row in graph]
        tmp = add(N, d, tmp_arr)
        if tmp == graph:
            continue
        answer = dfs(answer, cnt + 1, N, tmp)    
        
    return answer
    
answer = dfs(answer, cnt, N, graph)
print(answer)