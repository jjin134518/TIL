for tc in range(1, int(input())+1):
    n = int(input())
    arr = list(map(int, input().split()))
    end = arr[-1]      #끝에서부터 보기 (끝에서 부터 전에 샀으면 이익 누적 구하기) => 중간에 조금 큰값이 있어도 파는 것을 방지
    purchased = 0
    for i in range(n-1, -1, -1):
        if end > arr[i]:                #전날들 값이 끝값보다 작으면 샀을태니까 이익값 누적
            purchased += end - arr[i]
        else:
            end = arr[i]                #만약 중간에 더 큰 값이 있으면 그날 한번 팔았을태니까 그게 끝값이 된다
    print("#{} {}".format(tc, purchased))

