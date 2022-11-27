# 22.11.26
# Programmers - Make minimum value(최솟값 만들기)
# https://school.programmers.co.kr/learn/courses/30/lessons/12941

def solution(A,B):
    A.sort()
    B.sort(reverse = True)
    answer = 0
    for a, b in zip(A, B):
        answer += a * b
    return answer