A,B,C,D = map(int,input().split())
W = C - A
H = D - B
list = [A,B,W,H]
min = A
for i in list:
    if i < min:
        min = i
print(min)
