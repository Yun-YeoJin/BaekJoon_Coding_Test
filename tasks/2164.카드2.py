from collections import deque

N = int(input())
d = deque(list(range(1, N+1)))

drop = True

while len(d) > 1:
    if drop:
        d.popleft()
        drop = False
    else:
        x = d.popleft()
        d.append(x)
        drop = True
        
print(d[0])