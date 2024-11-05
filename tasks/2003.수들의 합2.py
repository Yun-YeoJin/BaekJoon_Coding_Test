N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

start = 0
end = 0
sum = A[0]

count = 0

while True:
    # 현재 구간의 합이 M인지 확인
    if sum == M:
        count += 1
        
    # 시작점 옮기기
    if sum >= M:
        start += 1
        sum -= A[start - 1]
    else: # sum < M
        if end == N - 1:
            break
        end += 1
        sum += A[end]

print(count)