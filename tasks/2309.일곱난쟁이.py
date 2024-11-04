from itertools import combinations

heights = []
for _ in range(9):
    height = int(input())
    heights.append(height)
    
for i in combinations(heights, 7):
    if sum(i) == 100:
        i = list(i)
        i.sort()
        for x in i:
            print(x)
        break