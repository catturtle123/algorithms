import sys

def attacked(t, attack, rest):
    cycle = attack + rest
    x = t % cycle
    # "t번째 분이 진행되는 중" -> t가 cycle의 배수면 해당 사이클의 마지막(rest 구간)로 취급
    if x == 0:
        x = cycle
    return 1 if x <= attack else 0

A, B, C, D = map(int, sys.stdin.readline().split())
P, M, N = map(int, sys.stdin.readline().split())

for t in (P, M, N):
    cnt = attacked(t, A, B) + attacked(t, C, D)
    print(cnt)
