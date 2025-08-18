import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

graph = [list(input().strip()) for _ in range(N)]
visited = {}


B_loc = ()
R_loc = ()
H_loc = ()

#B와 R의 위치 찾기 
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if graph[i][j] == 'B':
            B_loc = (i, j)
            graph[i][j] == '.'    
        if graph[i][j] == 'R':
            R_loc = (i, j)
            graph[i][j] == '.'
        
q = deque([(R_loc[0], R_loc[1], B_loc[0], B_loc[1])])

visited[R_loc[0], R_loc[1], B_loc[0], B_loc[1]] = 0

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def move(d, x, y):
    cnt = 0
    
    while graph[x + dx[d]][y + dy[d]] != '#':
        if graph[x + dx[d]][y + dy[d]] == 'O':
            return 0, 0, 0
        x += dx[d]
        y += dy[d]
        cnt += 1  
    return x, y, cnt
def bfs():
    while q:
        rx, ry, bx, by = q.popleft()
        
        #온길은 돌아가면 안되는데
        for d in range(4):
            nrx, nry, r_cnt = move(d, rx, ry)
            nbx, nby, b_cnt = move(d, bx, by)
            
            if not nbx and not nby:
                continue
            elif not nrx and not nry:
                print(visited[rx, ry, bx, by] + 1)
                return 
            elif nrx == nbx and nry == nby:
                if r_cnt > b_cnt:
                    nrx -= dx[d]
                    nry -= dy[d]
                else:
                    nbx -= dx[d]
                    nby -= dy[d]
            
            if (nrx, nry, nbx, nby) not in visited:
                visited[nrx, nry, nbx, nby] = visited[rx, ry, bx, by] + 1
                q.append((nrx, nry, nbx, nby))
                
        if not q or visited[rx, ry, bx, by] >= 10:
            print(-1)
            return 
        
bfs()