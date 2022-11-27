# 22.11.24
# Programmers - Checking Phone number(전화번호 목록)
# https://school.programmers.co.kr/learn/courses/30/lessons/42577

# import re
# def solution(phone_book):
#     phone_books = " " + " ".join(phone_book)
#     for phone_number in phone_book:
#         if len(phone_number) > 19:
#             continue
#         if len(re.findall(" " + phone_number, phone_books)) > 1:
#             return False
#     # for phone_number in phone_book:
#     #     for compare_phone_number in phone_book:
#     #         if len(phone_number) < len(compare_phone_number):
#     #             if compare_phone_number.startswith(phone_number):
#     #                 return False
#     return True

# 채점 결과
# 정확성: 83.3
# 효율성: 12.5
# 합계: 95.8 / 100.0

# 22.11.27

# import re

# def make_new_phone_book(phone_book):
#     new_phone_book = dict()
#     for index in range(20):
#         new_phone_book[index] = list()
#     for phone_number in phone_book:
#         if len(phone_number) not in new_phone_book:
#             new_phone_book[len(phone_number)] = list()
#         new_phone_book[len(phone_number)].append(phone_number)
#     for phone_number_length in new_phone_book.keys():
#         new_phone_book[phone_number_length] = ' '.join(new_phone_book[phone_number_length])
#     return new_phone_book

# def check_phone_number(phone_number: str, phone_books: str):
#     return len(re.findall(" " + phone_number, phone_books)) > 0

# def solution(phone_book):
#     new_phone_book = make_new_phone_book(phone_book)
#     for phone_number in phone_book:
#         if len(phone_number) > 19:
#             continue
#         else:
#             for index in range(len(phone_number) + 1, 20):
#                 if check_phone_number(phone_number, ' ' + new_phone_book[index]):
#                     return False
#     return True

# 채점 결과
# 정확성: 83.3
# 효율성: 12.5
# 합계: 95.8 / 100.0

import re

def make_phone_book_hash(phone_book):
    phone_book_hash = dict()
    for phone_number in phone_book:
        for index in range(1,len(phone_number)+1):
            if phone_number[:index] not in phone_book_hash.keys():
                phone_book_hash[phone_number[:index]] = 1
            else:
                phone_book_hash[phone_number[:index]] += 1
    return phone_book_hash

def check_phone_number(phone_number: str, phone_books: str):
    return len(re.findall(" " + phone_number, phone_books)) > 0

def solution(phone_book):
    phone_book_hash = make_phone_book_hash(phone_book)
    # print(phone_book_hash)
    for phone_number in phone_book:
        if phone_book_hash[phone_number] > 1:
            return False
    return True