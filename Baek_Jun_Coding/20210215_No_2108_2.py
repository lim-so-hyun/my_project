import sys
from collections import Counter
N = int(sys.stdin.readline())
list = []
for i in range(N):
    list.append(int(sys.stdin.readline()))
list.sort()
list_s = Counter(list).most_common()  # Counter의 most_common()은 빈도수 높은 순으로 리스트 안의 튜플 형태로 반환!
                                      # [(-2, 2), (-1, 2), (-3, 1)]이런식으로 각 요소 몇개인지!
print(round(sum(list)/N))  # 평균값 한줄로 표현가능. sum은 내장함수!
print(list[N//2])   # 중앙값 한줄로 표현하기

if len(list_s) == 1:
    print(list_s[0][0])
else:
    if list_s[0][1] == list_s[1][1]:  # 최빈값이 두개 이상 존재할 경우 list_s의 앞의 두개로 확인
        print(list_s[1][0])   # 두번째로 작은 원소 print
    else:
        print(list_s[0][0])  # 최빈값 하나일 경우 바로 첫번째 원소 print

print(list[-1] - list[0]) # 범위 한줄로 표현하기