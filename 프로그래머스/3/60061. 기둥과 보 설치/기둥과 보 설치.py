def possible(answer):
    for x, y, staff in answer:
        if staff == 0: # 기둥
            # 바닥일 때
            if y == 0:
                continue
            # 바로 밑이 기둥이나 보 일때
            if [x, y - 1, 0] in answer or [x, y, 1] in answer or [x - 1, y, 1] in answer:
                continue
            return False
        elif staff == 1: # 보
            # 밑에 기둥이 있을 때
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer:
                continue
            # 양 옆에 보가 있을 때
            if ([x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    
    return True
                

def solution(n, build_frame):
    answer = []
    for x, y, staff, isInstallOrDelete in build_frame:

        if isInstallOrDelete == 0: # 삭제
            answer.remove([x, y, staff])
            if not possible(answer):
                answer.append([x, y, staff])
        
        elif isInstallOrDelete == 1: # 설치
            answer.append([x, y, staff])
            if not possible(answer):
                answer.remove([x, y, staff])
    
    return sorted(answer)