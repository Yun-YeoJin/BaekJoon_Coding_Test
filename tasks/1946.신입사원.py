import sys
input = sys.stdin.readline

T = int(input()) #테스트 케이스 갯수

for _ in range(T):
    N = int(input()) #지원자 수
    candidates = []
    
    for _ in range(N): #지원자 수를 돌면서
        s, m = map(int, input().split())
        candidates.append((s, m)) #후보자의 성적 입력
        
    # (s, m)
    candidates.sort()
    
    top_ranking = 1e9
    count = 0
    
    for i in range(N):
        if candidates[i][1] < top_ranking:
            count += 1 #합격
            top_ranking = candidates[i][1]
        
    print(count)