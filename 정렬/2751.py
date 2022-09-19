import sys

A = []
N = int(input())

for i in range(N) :
    element = int(sys.stdin.readline())
    A.append(element)
A.sort(reverse = False) # 오름차순 정렬
for i in range(N) :
    print(A[i])