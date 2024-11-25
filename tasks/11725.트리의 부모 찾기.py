import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline().strip())

# 인접 리스트 생성
adj = [[] for _ in range(N)]

# 간선 입력
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())

    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)

# 방문 여부 및 부모 노드 초기화
visit = [False] * N
parent = [-1] * N

# DFS 구현
def dfs(u):
    visit[u] = True
    for v in adj[u]:
        if not visit[v]:
            parent[v] = u
            dfs(v)

# DFS 호출 (0번 노드를 루트로 가정)
dfs(0)

# 부모 노드 출력
for i in range(1, N):
    print(parent[i] + 1)