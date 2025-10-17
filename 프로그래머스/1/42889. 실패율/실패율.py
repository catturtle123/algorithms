def result_sort(result):
    return -result[0], result[1]

def solution(N, stages):
    stage_person = {}
    for i in stages:
        if i in stage_person:
            stage_person[i] += 1
        else:
            stage_person[i] = 1

    person_num = len(stages)
    result = []
    for i in range(1, N + 1): # 스테이지
        if i in stage_person:
            result.append((stage_person[i] / person_num, i))
            person_num -= stage_person[i]
        else:
            result.append((0, i))
    
    result = sorted(result, key=result_sort)

    answer = []
    for i in result:
        answer.append(i[1])

    return answer