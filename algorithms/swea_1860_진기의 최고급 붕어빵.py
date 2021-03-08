for tc in range(1, int(input())+1):
    n, m, k = map(int, input().split())
    time = list(map(int, input().split()))
    count = 0
    ans = 'Possible'
    for i in range(0, max(time)+1):
        if i != 0 and i % m == 0:
            count += k
        if i in time:
            a = time.count(i)
            count -= a
        if count < 0:
            ans = 'Impossible'
            break

    print("#{} {} {} {} {}".format(tc, n, m, k, ans))

