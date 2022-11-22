# 22.11.22
# Programmers - Parking fees(주차 요금 계산)
# https://school.programmers.co.kr/learn/courses/30/lessons/92341?language=python3

import math

IN_DIC = dict()
RECORD_DIC = dict()

def record_times(record_time, record_car_no, record_type):
    if record_type == "IN":
        IN_DIC[record_car_no] = record_time
    elif record_type == "OUT":
        if record_car_no not in RECORD_DIC.keys():
            Intime = IN_DIC.pop(record_car_no)
            Intime = int(Intime[:2]) * 60 + int(Intime[-2:])
            Outtime = int(record_time[:2]) * 60 + int(record_time[-2:])
            RECORD_DIC[record_car_no] = Outtime - Intime
            
        else:
            Intime = IN_DIC.pop(record_car_no)
            Intime = int(Intime[:2]) * 60 + int(Intime[-2:])
            Outtime = int(record_time[:2]) * 60 + int(record_time[-2:])
            RECORD_DIC[record_car_no] += Outtime - Intime

def cal_fee(fees, record_times):
    if record_times - fees[0] > 0:
        result = fees[1] + math.ceil((record_times - fees[0]) / fees[2]) * fees[3]
    else:
        result = fees[1]
    return result

def solution(fees, records):
    for record in records:
        record_time, record_car_no, record_type = record.split(' ')
        record_times(record_time, record_car_no, record_type)
    answer = list()
    
    Last_record_list = list(IN_DIC.keys())
    for Last_record in Last_record_list:
        record_times("23:59", Last_record, "OUT")
    print("Record dictionary : {}".format(RECORD_DIC))
    RECORD_LIST = list(RECORD_DIC.keys())
    RECORD_LIST.sort()
    for RECORD in RECORD_LIST:
        result = cal_fee(fees, RECORD_DIC[RECORD])
        answer.append(result)
    return answer
