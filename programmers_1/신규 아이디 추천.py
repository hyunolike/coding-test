# 문자열 처리: https://han-py.tistory.com/331

# 정규식 사용하기
import re
def inPalindrome(str):
    str=str.lower()

    # 정규식 사용: re.sub(패턴, 바꿀문자열, 적용할문자열)
    # 한 문자씩 검사할 때는 []안에 넣어 줄 것
    str = re.sub('[^a-z0-9]', '', str)
    if str==str[::-1]:
        print('회문입니다')
    else:
        print('회문이 아닙니다.')

# 문자열 대체 replace
# https://ponyozzang.tistory.com/334
# 문자열.replace(검색문자, 치환문자, 치환횟수)
text='일본의 부가세는 8% 입니다.'
text_mod = text.replace("8","10")

# 제일 처음 일치하는 문자만 치환하고 싶을 때
text="orange, orange, melon"
text_mod=text.replace("orange", "apple", 1)
print(text_mod) # apple, orange, melon

