# def check()

for i in range(1, int(input())+1):
    n, m = map(int, input().split())
    arr = [[0]*(n+2) for _ in range(n+2)]

    i = int((n+2) / 2)
    arr[i][i], arr[i][i-1], arr[i-1][i],arr[i-1][i-1]  = 2, 1, 1, 2

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1] #12시부터 시계방향
    for j in range(m):
        a, b, c = map(int, input().split())
        arr[b][a] = c
        a,b = i,j
            for d in range(8):
                nr = i + dr[d]
                nc = j + dc[d]
                while True:
                    nr += de[i]
                    nc += dc[i]

                    if nr <= 0 or nr>n or nc<=0 or nc>n: break
                    if arr[nr][nc] == 0: break
                    if arr[nr][nc] == color:
                        while not not (nr == r and nc == c):
                            nr -= dr[i]
                            nc 
                    else:
                        break
    # if c == 2:
        #     for d in range(8):
        #         while 0 <= a < n and 0 <= b <n:
        #             b = b + dr[d]
        #             a = a + dc[d]
        #             if arr[b][a] == 1:
        #                 arr[b][a] = 2
        #
        #             else:
        #                 break

        print(arr)

