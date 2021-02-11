N = int(input())
weight = []
height = []
for _ in range(N):
    A,B = map(int,input().split())
    weight.append(A)
    height.append(B)
print (weight)
print (height)

rank = [1] * N
for i in range(N):
    for j in range(N):
        if weight[i] < weight[j] and height[i] < height[j]:
            rank[i] += 1
for num in rank:
    print (num)
            
