# 22.11.27
# Programmers - Product matrices(행렬의 곱셈)
# https://school.programmers.co.kr/learn/courses/30/lessons/12949

import numpy

def solution(arr1, arr2):
    return numpy.dot(numpy.array(arr1), numpy.array(arr2)).tolist()