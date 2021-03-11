arr = [int(input()) for _ in range(9)]
arr.sort()
k, l = 0, 0
for i in range(9):
    for j in range(i+1, 9):
        if sum(arr) - arr[i] - arr[j] == 100:
            k,l = i,j
            break

arr.pop(max(k,l))
arr.pop(min(k,l))

for i in arr:
    print(i)





