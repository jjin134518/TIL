n = int(input())
binary = []
if n == 0:
    print(0)
else:
    while n:
        if n%(-2):
            binary.append('1')
            n = n//(-2)+1
        else:
            binary.append('0')
            n //= -2

print(''.join(reversed(binary)))
