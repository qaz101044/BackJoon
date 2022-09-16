A = []
N = int(input())

for i in range(N) :
    element = int(input())
    A.append(element)
A.sort(reverse = False) # 오름차순 정렬
for i in range(N) :
    print(A[i])