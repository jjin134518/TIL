for tc in range(1, int(input())+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    col_min = (n//2)
    col_max = (n//2)+1
    price = 0

    for i in range(n):
        if i < (n//2):
            price += sum(arr[i][col_min:col_max])
            col_min -= 1
            col_max += 1
        else:
            price += sum(arr[i][col_min:col_max])
            col_min += 1
            col_max -= 1
    print("#{} {}".format(tc,price))


