N = int(input())
people = list(map(int, input().split()))

people = sorted(people)
waiting = [0] * N
waiting[0] = people[0]
for i in range(1, N):
    waiting[i] = waiting[i - 1] + people[i]
    
print(sum(waiting))