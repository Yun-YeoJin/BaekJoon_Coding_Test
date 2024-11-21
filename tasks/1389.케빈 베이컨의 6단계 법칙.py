from collections import deque

N, M = list(map(int, input().split()))

adj = [[] for _ in range(6)]

for _ in range(M):
    a, b = list(map(int, input().split()))
    
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
    
min_kevin = 1e9
min_person = -1    

for i in range(N):
    # i를 시작점으로 하는 BFS
    # 각 노드까지의 최단거리를 구해서 다 합하기
    visit = [False] * N
    dist = [-1] * N
    
    queue = deque([i])
    visit[i] = True
    dist[i] = 0
    
    while len(queue) != 0:
        u = queue.popleft()
        
        for v in adj[u]:
            if not visit[v]:
                queue.append(v)
                visit[v] = True
                dist[v] = dist[u] + 1
            
    kevin_bacon = sum(dist)
    
    if min_kevin > kevin_bacon:
        min_kevin = kevin_bacon
        min_person = i
    
print(min_person + 1)