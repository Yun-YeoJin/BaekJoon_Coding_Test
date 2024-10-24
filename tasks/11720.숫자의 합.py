n = 25
stringInput = input()

sum = 0
for i in range(n):
    sum += (ord(stringInput[i]) - ord('0'))

print(sum)