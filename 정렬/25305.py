N,k = map(int,input().split())
score_list = list(map(int,input().split()))

score_list.sort(reverse = True)
# 리스트명.sort(reverse=false) : 오름차순 1,2,3,4,5
# 리스트명.sort(reverse=True) : 내림차순 5,4,3,2,1

print(int(score_list[k-1]))