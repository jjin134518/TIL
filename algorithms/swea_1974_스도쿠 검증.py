for tc in range(1, int(input())+1):
    arr = [list(map(int,input().split())) for _ in range(9)]
    ans = 1
    # 가로 세로 체크
    for i in range(9):
        hor = []
        ver = []
        for j in range(9):
            if arr[i][j] in hor:
                ans = 0
                break
            else:
                hor.append(arr[i][j])
            if arr[j][i] in ver:
                ans = 0
                break
            else:
                ver.append(arr[j][i])
    # 3*3 박스 체크
    for i in range(0,9,3):
        for j in range(0,9,3):
            total = 0
            total += sum(arr[i][j:j+3])
            total += sum(arr[i+1][j:j+3])
            total += sum(arr[i+2][j:j+3])
            if total != 45:
                ans = 0
                break

    print("#{} {}".format(tc, ans))

