from queue import PriorityQueue

N = int(input())
P = [0] * N

pq = PriorityQueue()

for i in range(N):
    num_cards =  int(input())
    pq.put(num_cards)

answer = 0
while pq.qsize() > 1:
    min_value_1 = pq.get()
    min_value_2 = pq.get()
    
    pq.put(min_value_1 + min_value_2)
    answer += min_value_1 + min_value_2

print(answer)