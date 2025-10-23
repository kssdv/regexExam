import re

text = "문의사항은 a-rank@google.com 또는 support@example.co.kr 로 연락주세요."

# 이메일 주소를 찾는 정규표현식 패턴
# \w+ : 하나 이상의 문자/숫자
# @   : @ 기호
# \.  : 실제 점(.) 문자
pattern = r'\w+@\w+\.\w+' # raw string을 의미하는 r을 붙이면 \를 이스케이프 문자로 인식하지 않아 편리합니다.

# 문자열에서 패턴 검색
match = re.search(pattern, text)

if match:
    print("이메일을 찾았습니다!")
    print("찾은 이메일:", match.group()) # .group()으로 실제 일치한 문자열을 가져옴
else:
    print("이메일을 찾지 못했습니다.")

# 실행 결과:
# 이메일을 찾았습니다!
# 찾은 이메일: a-rank@google.com