# 22.11.26
# Programmers - Maximum and minimum (최댓값과 최솟값)
# https://school.programmers.co.kr/learn/courses/30/lessons/12939

def solution(s):
    s_list = [int(i) for i in s.split(" ")]
    return " ".join([str(min(s_list)), str(max(s_list))])