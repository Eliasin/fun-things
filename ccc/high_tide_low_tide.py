from math import ceil

N = int(input())

tides = [int(n) for n in input().split()]
tides.sort()

low_tides = tides[0:ceil(len(tides) / 2)]
low_tides.reverse()

high_tides = tides[ceil(len(tides) / 2): len(tides)]

result = []
for i in range(int(ceil(N / 2))):
    if i < len(low_tides):
        result.append(low_tides[i])
    if i < len(high_tides):
        result.append(high_tides[i])

for t in result:
    print(str(t) + " ", end="")
