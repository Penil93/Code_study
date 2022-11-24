# 22.11.24
# Programmers - Checking Phone number(전화번호 목록)
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

import re
def solution(phone_book):
    phone_books = " " + " ".join(phone_book)
    for phone_number in phone_book:
        if len(phone_number) > 19:
            continue
        if len(re.findall(" " + phone_number, phone_books)) > 1:
            return False
    # for phone_number in phone_book:
    #     for compare_phone_number in phone_book:
    #         if len(phone_number) < len(compare_phone_number):
    #             if compare_phone_number.startswith(phone_number):
    #                 return False
    return True

# 채점 결과
# 정확성: 83.3
# 효율성: 12.5
# 합계: 95.8 / 100.0