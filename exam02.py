import re

text = "상품 코드: 7, 가격: 15000원, 재고: 102개."

# 하나 이상의 숫자를 찾는 패턴 (\d+)
pattern = r'\d+'

# 패턴과 일치하는 모든 부분을 찾아서 리스트로 반환
numbers = re.findall(pattern, text)

print("찾은 숫자 목록:", numbers)

# 실행 결과:
# 찾은 숫자 목록: ['7', '15000', '102']