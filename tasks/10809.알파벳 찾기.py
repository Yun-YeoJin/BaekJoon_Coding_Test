s = input().lower()  # 소문자로 변환

check = [-1] * 26

for i in range(len(s)):
    if 'a' <= s[i] <= 'z':  # 소문자 알파벳 범위에 있는지 확인
        index = ord(s[i]) - ord('a')
        if check[index] == -1:
            check[index] = i

for i in range(26):
    print(check[i], end=" ")