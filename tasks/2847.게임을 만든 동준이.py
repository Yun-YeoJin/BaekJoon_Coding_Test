#최대한 덜 깎자
N = int(input())
level = [0] * N

for i in range(N):
    level[i] = int(input())
    
count = 0
for i in range(N - 2, -1, -1):
    if level[i] >= level[i + 1]:
        count += level[i] - (level[i + 1] - 1)
        level[i] = level[i + 1] - 1
        
print(count)