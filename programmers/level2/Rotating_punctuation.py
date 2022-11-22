# 22.11.22
# Programmers - Rotating punctuation(괄호 회전하기)
# https://school.programmers.co.kr/learn/courses/30/lessons/76502#

OPEN_PUNCTUATION = ["(", "[", "{"]
CLOSE_PUNCTUATION = [")", "]", "}"]

def check_logic(s: str):
    check_pos_dict = dict()
    for index, text in enumerate(s):
        if text in OPEN_PUNCTUATION:
            check_pos_dict[index] = OPEN_PUNCTUATION.index(text)
        elif text in CLOSE_PUNCTUATION:
            tmp_pos_list = list(check_pos_dict.keys())
            if len(tmp_pos_list) < 1:
                return 0
            if check_pos_dict[tmp_pos_list[-1]] == CLOSE_PUNCTUATION.index(text):
                check_pos_dict.pop(tmp_pos_list[-1])
            else:
                return 0
        else:
            return 0
    if len(check_pos_dict) > 0:
        return 0
    return 1
    
def solution(s: str):
    answer = 0
    if s is None or len(s) < 1:
        return answer
    for i in range(len(s)):
        s = s[1:] + s[0]
        result = check_logic(s)
        answer += result
    return answer