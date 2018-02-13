q = int(input())
N = int(input())

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

a.sort()
b.sort()

if q == 2:
    a.reverse()

total_speed = 0

for i in range(N):
    total_speed += max(a[i], b[i])

print(total_speed)
