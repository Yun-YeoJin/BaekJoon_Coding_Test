from itertools import permutations

N = int(input()) #배열의 길이
numsList = list(map(int, input().split())) #정수들

maxSum = 0

for a in permutations(numsList, N):
    sum = 0
    for i in range(N - 1):
        sum += abs(a[i] - a[i + 1])
    maxSum = max(maxSum, sum)
    
print(maxSum)