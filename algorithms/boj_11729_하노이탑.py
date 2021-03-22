#############
# 이리저리 왔다갔다
# 일단 위에 층은 다 치우고 맨 밑 한놈 옮기기
#############

n = int(input())


def hanoi(n, s, e, m): # n개의 원판이 start에서 end로 middle을 거쳐서 간다
    if n == 1:         # n이 1이면 있는 곳에서 도착지로 옮기면 되니까 시작점과 도착점 프린트
        print(s, e)
        return         # 제귀일때는 다시 불러온 곳으로 돌아가기
    else:
        hanoi(n - 1, s, m, e) # 맨 밑의 가장 큰 원판이 우선 최종 도착지로 가야 되므로 나머지 원판이 다 중간으로 가야됨!
        print(s, e)           # 맨 밑판이 혼자 남으면 시작에서 끝점으로
        hanoi(n - 1, m, e, s) # middle에 있는 원판들이 start를 거쳐서 end로 가면 됨


print((2 ** n) - 1) # 하노이의 탑 공식으로 숫자 구하기
hanoi(n, 1, 3, 2) # n이 1번 에서 2번을 거쳐 3번으로 가기
