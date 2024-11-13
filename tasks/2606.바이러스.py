computer = int(input())
pair = int(input())

adj = [[] for _ in range(computer)] #인접 리스트

for i in range(pair):
    a, b = list(map(int, input().split()))
    adj[a - 1].append(b - 1)
    adj[b - 1].append(a - 1)
    
check = [0] * computer
check[0] = 1

while True:
    new = False
    
    for i in range(computer):
        if check[i] == 0:
            continue
        for j in adj[i]:
            if check[j] == 0:
                check[j] = 1
                new = True
    if not new:
        break
    
count = 0
for i in range(1, computer):
    if check[i] == 1:
        count += 1
        
print(count)
