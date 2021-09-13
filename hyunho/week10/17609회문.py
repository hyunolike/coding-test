import sys

input = lambda : sys.stdin.readline().rstrip()

def pseudo(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

def is_palindrome(s, left, right):
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            res1 = pseudo(s, left+1, right)
            res2 = pseudo(s, left, right-1)
            if res1 or res2:
                return 1
            else:
                return 2
    return 0


for _ in range(int(input())):
    string = input()
    res = is_palindrome(string, 0 , len(string) - 1)
    print(res)
