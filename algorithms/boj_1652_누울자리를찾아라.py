
n = int(input())
arr = [list(map(str,input())) for _ in range(n)]
garo = 0
saero = 0
# 세로
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        count = 0
        nr, nc = i, j
        while 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
            if arr[nr][nc] == '.':
                count += 1
                visited[nr][nc] = 1
                nr += 1
            else: break
        if count >= 2:
            saero += 1
visitedr = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        count = 0
        nr, nc = i, j
        while 0 <= nr < n and 0 <= nc < n and not visitedr[nr][nc]:
            if arr[nr][nc] == '.':
                count += 1
                visitedr[nr][nc] = 1
                nc += 1
            else: break
        if count >= 2:
            garo += 1

print(garo, saero)




