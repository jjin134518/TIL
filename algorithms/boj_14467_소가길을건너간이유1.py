import sys
input = sys.stdin.readline

n = int(input())

arr = [0]*10

visited = [0]*10

for i in range(n):
    a, b = map(int, input().split())
    a = a-1
    if visited[a] == 0:
        arr[a] = b
        visited[a] += 1
    elif visited[a] and arr[a] != b:
        arr[a] = b
        visited[a] +=1

print(sum(visited) - (10-visited.count(0)))

