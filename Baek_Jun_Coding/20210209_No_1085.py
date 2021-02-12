A,B,C,D = map(int,input().split())
W = 0
H = 0
if A < (C-A) :
    W = A
else:
    W = C-A
if B < (D-B) :
    H = B
else:
    H = D-B
if W < H:
    print (W)
else:
    print (H)
