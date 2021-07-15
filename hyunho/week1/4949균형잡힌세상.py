def isVaild(s: str) -> bool:
    stack = []
    table = {
        ')' : '(',
        ']' : '[',
    }

    for char in s:
        # print(stack)
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
            return False
    return len(stack) == 0

while True:
    string = input()
    if string == '.':
        break
    elif string ==' .':
        print('yes')
    else:
        charaters = "()[]"
        join_string = ''.join(x for x in string if x in charaters)

        if isVaild(join_string):
            print('yes')
        else:
            print('no')
