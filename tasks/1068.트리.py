N = int(input())
parent = list(map(int, input().split()))
remove = int(input())

#루트 노드
for i in range(N):
    if parent[i] == -1:
        root = i
        break
    
#사라지는 노드들 판별
black = [0] * N
for i in range(N):
    u = i
    while True:
        if u == remove:
            black[i] = 1
            break
        if u == root:
            break
        
        u = parent[u]
        
#자식이 있는 노드 판별
red = [0] * N
for i in range(N):
    if black[i] == 1:
        continue
    
    if i == root:
        continue
    red[parent[i]] = 1
    
count = 0
for i in range(N):
    if black[i] == 1 or red[i] == 1:
        continue
    count += 1
    
print(count)