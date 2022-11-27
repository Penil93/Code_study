# 22.11.24
# Programmers - Checking punctuation(괄호 확인하기)
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    PUNCTUATION_List = list()
    for index, text in enumerate(s):
        if text == "(": PUNCTUATION_List.append(index)
        elif text == ")":
            if len(PUNCTUATION_List) == 0: return False
            else: PUNCTUATION_List.pop(-1)
        else: continue
    if len(PUNCTUATION_List) == 0: return True
    else: return False