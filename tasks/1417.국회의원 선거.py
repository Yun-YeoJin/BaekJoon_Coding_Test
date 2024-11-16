from queue import PriorityQueue

N = int(input())
P = [0] * N 

for i in range(N):
    P[i] = int(input())
    
pq = PriorityQueue()

for i in range(1, N):
    #최댓값을 반환해주고 싶음.
    pq.put(-P[i])
    
if N == 1:
    print(0)
else:
    count = 0
    while True:
        #뽑아서 가져오기
        max_val = -pq.get()
        if max_val < P[0]:
            break
        max_val -= 1
        P[0] += 1
        count += 1
        #다시 우선순위 큐에 넣어주기
        pq.put(-max_val)
    print(count)    
