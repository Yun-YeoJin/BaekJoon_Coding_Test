N = int(input())
M = int(input())
S = input()

# 해시 계산을 위한 준비
mod = int(1e9 + 7)
po = [0] * M
po[0] = 1

# 거듭제곱 값 미리 계산
for i in range(1, M):
    po[i] = po[i - 1] * 31 % mod

# P_n의 해시 값 계산
K = 2 * N + 1
Pn_hash = 0
for i in range(K):
    if i % 2 == 0:
        Pn_hash = (Pn_hash * 31 + (ord('I') - ord('A') + 1)) % mod
    else:
        Pn_hash = (Pn_hash * 31 + (ord('O') - ord('A') + 1)) % mod

# 첫 부분 문자열의 해시 값 계산
S_hash = 0
for i in range(K):
    S_hash = (S_hash * 31 + (ord(S[i]) - ord('A') + 1)) % mod

# 슬라이딩 윈도우를 통한 해시 비교
count = 0
for i in range(M - K + 1):
    if S_hash == Pn_hash:
        count += 1
    
    if i + K < M:
        # 해시 값 갱신
        largest = ord(S[i]) - ord('A') + 1
        S_hash = (S_hash + mod - largest * po[K - 1] % mod) % mod
        S_hash = (S_hash * 31 + (ord(S[i + K]) - ord('A') + 1)) % mod

print(count)
