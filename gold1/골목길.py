# import sys
# from heapq import *

# input = sys.stdin.readline

# PLUS_INF = -int(1e10)
# MINUS_INF = int(1e10)

# N, M = map(int, input().split())
# graph = [[] for _ in range(N + 1)]

# for _ in range(M):
#     u, v, w = map(int, input().split())
#     graph[u].append((v, w))
    
# visited_cnt = [0] * (N + 1)
# visited = visited_cnt[::]
# distance = [PLUS_INF] * (N + 1)

# distance[1] = 0
# q = [(0, 1)]

# route = [0] * (N + 1)


# while q:
#     dist, cur = heappop(q)
#     if -dist < dist[cur]:
#         continue
#     for next, cost in graph[cur]:
#         next_cost = cost - dist
#         if distance[next] >= next_cost:
#             continue
#         if visited[next]:
#             continue
#         if visited_cnt[next] + 1 >= v:
#             next_cost = MINUS_INF
#             visited[next] = 1
            
#         visited_cnt[next] += 1
#         route[next] = cur
#         distance[next] = next_cost
#         heappush(q, (-next_cost, next))

# result = []
# while N and dist[N] < MINUS_INF:
#     result.append(N)
#     N = route[N]
# if result and result[-1] == 1:
#     print(*result[::-1])
# else:
#     print(-1)





import sys
INF = int(1e10)

def bf(graph, start, N):
    distance = [-INF] * (N + 1)
    result = []
    distance[start] = 0
    route = [0] * (N + 1)
    
    for i in range(N):
        for cur in range(1, N + 1):
            if distance[cur] == -INF:
                continue
            
            for next, dist in graph[cur]:
                if distance[next] < distance[cur] + dist:
                    distance[next] = distance[cur] + dist
                    route[next] = cur
                    if i == N - 1:
                        distance[next] = INF
    
    if distance[N] == INF:
        print(-1)
        return
    else:
        result.append(N)
        while(N!=1):
            result.append(route[N])
            N = route[N]
            
        result.reverse()
        print(*result)
        return
    
N,M= map(int, input().split())
 
graph=[[] for _ in range(N+1)]

for _ in range(M):
  a,b,c= map(int, input().split())
  graph[a].append((b,c))


bf(graph, 1, N)
        