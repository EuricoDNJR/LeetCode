def isvalid(s):
    s = list(s)
    print(s)
    tam = len(s)
    flag = 0
    for i in range(tam):
        if s[i] == '(':
            for j in range(i + 1, tam):
                if s[j] == ')':
                    flag = 1
                    s[i] = '_'
                    s[j] = '_'
                    break
            if flag == 0:
                return False
            else:
                flag = 0
        elif s[i] == '[':
            for j in range(i + 1, tam):
                if s[j] == ']':
                    flag = 1
                    s[i] = '_'
                    s[j] = '_'
                    break
            if flag == 0:
                return False
            else:
                flag = 0
        elif s[i] == '{':
            for j in range(i + 1, tam):
                if s[j] == '}':
                    flag = 1
                    s[i] = '_'
                    s[j] = '_'
                    break
            if flag == 0:
                return False
            else:
                flag = 0
        elif s[i] == '_':
            pass
        else:
            return False
    return True
    #Open brackets must be closed by the same type of brackets.
    #Open brackets must be closed in the correct order.
    #Every close bracket has a corresponding open bracket of the same type.
s = "{[]}"
print(isvalid(s))