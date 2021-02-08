for t in range(1, 11):
    e = int(input())
    arr = list(map(int, input().split()))
    total = 0
    for i in range(2, e-1):                         #the question stated that the first and the last two numbers are 0. so those can be eliminated
        if max(arr[i-2:i+3]) == arr[i]:             #to have visibility it has to be the tallest with in 4 surrounding buildings
            total += (arr[i] - (max(arr[i-2],arr[i-1], arr[i+1], arr[i+2])))    #add total 

    print( "#{} {}".format(t,total))        #if testing environment has older version of python (3.5), f string will not work**

    # what other ways can i solve?? (result: memory-60,976 kb | running time-169ms | code-length: 282)


