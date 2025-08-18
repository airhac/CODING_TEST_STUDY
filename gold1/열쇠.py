import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

def wall(x, y):
    if graph[x][y] == '*':
        return False
    else:
        return True
        
dx, dy = [0, -1, 0, 1], [-1, 0, 1, 0]

for _ in range(K):
    h, w = map(int,input().split().split())
    
    graph = [list(map(int, input().strip().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    
    keys = list(input().strip())
    #일단 입구 위치 부터 찾아야한다.
    entrance = []
    
    for i in range(h):
        if wall(i, 0):
            entrance.append((i, 0))
        if wall(i, w - 1):
            entrance.append((i, w - 1))
    
    for j in range(w):
        if wall(0, j):
            entrance.append((0, j))
        if wall(h - 1, j):
            entrance.append((h - 1, j))
            
    answer = 0
    
    for x, y in entrance:
        q = deque([(x, y)])
        
        if graph[x][y] == '$':
            visited[x][y] == 1
            answer += 1
        
        if graph[x][y] != '.' and graph[x][y].lower() not in keys:
            continue
        
        while q:        
            x, y = q.popleft()
            #문서이면 회득
            if graph[x][y] == '$':
                visited[x][y] == 1
                answer += 1
            
            if graph[x][y] != '.' and graph[x][y].lower() in keys:
                entrance.append()
                
            for d in range(4):
                pass
    print(answer)