while True:
    s = input()
    if s == ".":
        break
    stack = []
    balanced = True

    for i in range(len(s)):
        if s[i] == "(" or s[i] == "[":
            stack.append(s[i])
        elif s[i] == ")":
            if len(stack) == 0 or stack[-1] != "(":
                balanced = False
                break
            stack.pop()
        elif s[i] == "]":
            if len(stack) == 0 or stack[-1] != "[":
                balanced = False
                break
            stack.pop()

    # 마지막에는 스택이 비어 있어야 함
    if len(stack) != 0:
        balanced = False

    if balanced: 
        print("yes")
    else:
        print("no")