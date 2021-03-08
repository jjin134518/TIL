n = int(input())
switches = list(map(int,input().split()))
onoff = {0:1, 1:0}

t = int(input())

for i in range(t):
    a,b = map(int,input().split())
    if a == 1:
        for j in range(b-1, n, b):
            switches[j] = onoff[switches[j]]
    else:
        lw = b-2
        hi = b
        while lw >= 0 and hi < n:
            if switches[lw] == switches[hi]:
                lw -= 1
                hi += 1
            else:
                break
        for c in range(lw+1, hi):
            switches[c] = onoff[switches[c]]

for e in range(0, n, 20):
    print(*switches[e:e+20])





