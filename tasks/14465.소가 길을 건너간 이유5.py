N, K, B = list(map(int, input().split()))

check = [0] * N

for _ in range(B):
    id = int(input()) #고장난 신호등
    check[id - 1] = 1 #고장난 신호등에 1체크 해주기
    
psum = [0] * N
psum[0] = check[0]

for i in range(1, N):
    psum[i] = psum[i - 1] + check[i]
    
need = [] #고쳐야하는 신호등
for i in range(0, N - K + 1):
    # i ~ i + K - 1
    if i == 0:
        num = psum[K - 1]
    else:
        num = psum[i + K - 1] - psum[i - 1]
        
    need.append(num)
    
print(min(need))