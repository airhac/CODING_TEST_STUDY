import sys
from collections import deque, defaultdict

input = sys.stdin.readline

K = int(input())

def wall(x, y):
    if graph[x][y] == '*':
        return False
    else:
        return True
        
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

for _ in range(K):
    h, w = map(int,input().strip().split())
    
    graph = [list(input().strip()) for _ in range(h)]
    
    
    keys_str = input().strip()
    
    H, W = h + 2, w + 2
    
    board = [['.' for _ in range(W)] for _ in range(H)]
    for i in range(h):
        for j in range(w):
            board[i + 1][j + 1] = graph[i][j]
            
    has_key = [False] * 26
    if keys_str != '0':
        for c in keys_str:
            has_key[ord(c) - 97] = True  # 'a'->0
    #일단 입구 위치 부터 찾아야한다.
            
    door = defaultdict(set)
    visited = [[0] * W for _ in range(H)]   
    answer = 0
    #열쇠를 회득했을때 문을 열면 된다.
    
    q = deque()
    q.append((0, 0))
    visited[0][0] = 1

    wait_doors = [[] for _ in range(26)]
    
    while q:        
        x, y = q.popleft()
        
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            
            if not (0 <= nx < H and 0 <= ny < W):
                continue
            if visited[nx][ny]:
                continue
            
            cell = board[nx][ny]
            if cell == '*':  # 벽
                continue
        
            #얻어야하는 문서인 경우
            if cell == '$':
                visited[nx][ny] = 1
                board[nx][ny] = '.'
                answer += 1
                q.append((nx, ny))
            #이동가능한 경로인 경우
            elif board[nx][ny] == '.':
                visited[nx][ny] = 1
                q.append((nx, ny))
            #열쇠인 경우
            elif 'a' <= cell <= 'z':
                idx = ord(cell) - 97
                
                if not has_key[idx]:
                    has_key[idx] = True
                    
                    for wx, wy in wait_doors[idx]:
                        if not visited[wx][wy]:
                            visited[wx][wy] = 1
                            board[wx][wy] = '.'
                            q.append((wx, wy))
                    wait_doors[idx].clear()
                board[nx][ny] = '.'
                visited[nx][ny] = 1
                q.append((nx, ny))
            #이동한 곳에 문인 경우 
            else:
                idx = ord(cell) - 65
                if has_key[idx]:
                    board[nx][ny] = '.'
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    # 아직 못 여는 문: 방문 처리 금지, 대기리스트에 저장
                    wait_doors[idx].append((nx, ny))
    print(answer)