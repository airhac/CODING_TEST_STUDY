import sys
input = sys.stdin.readline

graph = [list(map(int, list(input().strip()))) for _ in range(9)]

visited = []

for i in range(9):
    for j in range(9):
        if not graph[i][j]:
            visited.append((i, j))
            
def check_row(x, i):
    for j in range(9):
        if graph[x][j] == i:
            return False
    return True

def check_col(y, i):
    for j in range(9):
        if graph[j][y] == i:
            return False
    return True

def check_rec(x, y, i):
    nx = x // 3 * 3
    ny = y // 3 * 3
    
    for j in range(3):
        for k in range(3):
            if graph[nx + j][ny + k] == i:
                return False
    return True

def dfs(idx):
    if idx == len(visited):
        for i in range(9):
            print(''.join(map(str, graph[i])))
        return True  # 종료 신호
    
    x, y = visited[idx]
    for i in range(1, 10):
        
        if check_row(x, i) and check_col(y, i) and check_rec(x, y, i):
            graph[x][y] = i
            if dfs(idx + 1):  # 하위 호출에서 True면 바로 종료
                return True
            graph[x][y] = 0

    return False

dfs(0)
