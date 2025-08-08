import heapq
import sys
input = sys.stdin.readline

def dijkstra(max_cost, N, K, graph):
    dist = [float('inf')] * (N + 1)
    dist[1] = 0
    pq = [(0, 1)]  # (무료 설치 수, 노드 번호)

    while pq:
        free_cnt, u = heapq.heappop(pq)

        if dist[u] < free_cnt:
            continue

        for v, cost in graph[u]:
            # 설치 비용이 max_cost 이하인 경우는 그냥 지나갈 수 있음
            if cost <= max_cost:
                if dist[v] > free_cnt:
                    dist[v] = free_cnt
                    heapq.heappush(pq, (free_cnt, v))
            else:
                # 설치 비용이 max_cost 초과면, 무료 설치권을 써야 함
                if free_cnt + 1 <= K and dist[v] > free_cnt + 1:
                    dist[v] = free_cnt + 1
                    heapq.heappush(pq, (free_cnt + 1, v))

    return dist[N] <= K

def solve():
    N, P, K = map(int, input().split())
    graph = [[] for _ in range(N + 1)]

    max_edge_cost = 0
    for _ in range(P):
        u, v, c = map(int, input().split())
        graph[u].append((v, c))
        graph[v].append((u, c))
        max_edge_cost = max(max_edge_cost, c)

    # 이분 탐색: 최대 허용 비용
    left, right = 0, max_edge_cost
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        if dijkstra(mid, N, K, graph):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)

if __name__ == "__main__":
    solve()