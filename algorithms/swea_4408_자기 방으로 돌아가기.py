for tc in range(1, int(input())+1):
    n = int(input())
    path = [0] * 201

    for i in range(n):
        a,b = map(int, input().split())
        if a > b:
            a,b = b,a
        a = (a+1) // 2
        b = (b+1) // 2

        for j in range(a, b+1):
            path[j] += 1

    print("#{} {}".format(tc,max(path)))

