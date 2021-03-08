def loggu(n):
    if n == 1:
        return 0
    elif n == 0:
        return 1

# 남자는 배수 스위치를 로꾸꺼
def boy(sw):
    for i in range(N):
        if (i + 1) % sw == 0:
            switchs[i] = loggu(switchs[i])

# 여자는 좌우 대칭 가장 먼것 로꾸꺼
def girl(sw):
    q = sw - 1
    idx = 0
    max_idx = 0
    # 양 옆에 같은게 없다면 하나만 바뀜
    if q - 1 >= 0 and q + 1 < N and switchs[q - 1] != switchs[q + 1]:
        switchs[q] = loggu(switchs[q])
    else:
        while True:
            idx += 1
            # 벗어나면 그만!
            if q - idx < 0 or q + idx >= N:
                break
            # 최대 범위를 구하자
            if switchs[q-idx] == switchs[q+idx]:
                if max_idx < idx:
                    max_idx = idx
        # 구한 최대 범위를 모두 로꾸꺼
        for i in range(q - max_idx, q + max_idx + 1):
            switchs[i] = loggu(switchs[i])

# 입력들
N = int(input())
switchs = list(map(int, input().split()))
students_num = int(input())
students = [list(map(int, input().split())) for _ in range(students_num)]

for i in range(students_num):
    if students[i][0] == 1:
        boy(students[i][1])
    else:
        girl(students[i][1])

for i in range(len(switchs)):
    if i % 20 == 0:
        print()
    print(switchs[i], end=' ')