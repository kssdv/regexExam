import re

phone_number = "010-1234-5678"

# 하이픈(-)을 찾는 패턴
pattern = r'-'

# 패턴에 해당하는 부분을 빈 문자열("")로 교체
new_number = re.sub(pattern, "", phone_number)

print("기존 번호:", phone_number)
print("변경된 번호:", new_number)

# 실행 결과:
# 기존 번호: 010-1234-5678
# 변경된 번호: 01012345678

# 자주 쓰이는 정규표현식 메타문자 (규칙)
# 문자	의미	예시
# .	줄바꿈 문자를 제외한 모든 문자 1개	a.b -> "acb", "a_b", "a8b"
# \d	숫자(Digit) [0-9]	\d\d -> "12", "99"
# \w	문자, 숫자, 밑줄(Word) [a-zA-Z0-9_]	\w\w -> "ab", "a1", "_c"
# \s	공백(Space) (스페이스, 탭, 줄바꿈 등)	hello\sworld -> "hello world"
# *	0회 이상 반복	a*b -> "b", "ab", "aaab"
# +	1회 이상 반복	a+b -> "ab", "aaab"
# ?	0회 또는 1회	a?b -> "b", "ab"
# []	대괄호 안의 문자 중 하나	[abc] -> "a", "b", "c"
# ^	문자열의 시작	^Hello -> "Hello world" (O), "Say Hello" (X)
# $	문자열의 끝	world$ -> "Hello world" (O), "world is..." (X)
