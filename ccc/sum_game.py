N = int(input())

swifts = [int(n) for n in input().split(' ')]
semaphores = [int(n) for n in input().split(' ')]

swift_sum = 0
semaphore_sum = 0

largest = 0

for k in range(N):
    swift_sum += swifts[k]
    semaphore_sum += semaphores[k]

    if swift_sum == semaphore_sum:
        largest = k + 1

print(largest)
