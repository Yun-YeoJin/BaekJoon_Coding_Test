L = int(input())
S = input()

# 해시 계산을 위한 준비
mod = int(1e9 + 7)
po = [0] * L
po[0] = 1
for i in range(1, L):
    po[i] = po[i - 1] * 31 % mod

low = 1
high = L - 1
answer = 0

#이분 탐색
while low <= high:
    mid = (low + high) // 2
    
    #길이가 mid인 부분 문자열 중에 2번 이상 등장하는 것이 있는지 확인
    found = False
    
    hash = 0
    #가장 맨 앞 문자열의 해쉬값
    for i in range(mid):
        hash *= 31
        hash %= mod
        hash += ord(S[i]) - ord("a") + 1
        hash %= mod
    
    check = {} #딕셔너리 생성
    
    for i in range(0, L - mid + 1):
        #S[i:i+mid] 해쉬값 체크
        if hash in check:
            for j in check[hash]:
                if S[j:j+mid] == S[i:i+mid]:
                    found = True
                    break
            check[hash].append(i)
            if found:
                break
        else:
            check[hash] = [i]
        #해쉬값 갱신하기
        hash += mod - (ord(S[i]) - ord("a") + 1) * po[mid - 1]
        hash %= mod
        hash *= 31
        hash %= mod
        if i + mid < L:
            hash += ord(S[i + mid]) - ord("a") + 1
            hash %= mod
        
    if found:
        #2개 이상 발견
        answer = mid
        low = mid + 1
    else:
        #2개 이상 없음
        high = mid - 1
        
print(answer)