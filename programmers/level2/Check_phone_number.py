# 22.11.24
# Programmers - Checking Phone number(전화번호 목록)
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

import re
def solution(phone_book):
    phone_books = " " + " ".join(phone_book)
    for phone_number in phone_book:
        if len(re.findall(" " + phone_number, phone_books)) > 1:
            return False
    return True

# 채점 결과
# 정확성: 83.3
# 효율성: 8.3
# 합계: 91.7 / 100.0