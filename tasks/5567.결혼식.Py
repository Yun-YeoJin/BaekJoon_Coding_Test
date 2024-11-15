N = int(input())
M = int(input())

friends = [[] for _ in range(N)]

for i in range(M):
    a, b = list(map(int, input().split()))
    friends[a - 1].append(b - 1)
    friends[b - 1].append(a - 1)
    
#1. 친구 배열
friend = [0] * N

for i in friends[0]:
    friend[i] = 1
    
#2. 친구의 친구 배열 채우기
friend2 = [0] * N

for i in range(N):
    if friend[i] == 0:
        continue

    for j in friends[i]:
        #친구도 아니고, 친구의 친구도 아닐 때만
        if j != 0 and friend[j] == 0:
            friend2[j] = 1
            
            
print(sum(friend + friend2))