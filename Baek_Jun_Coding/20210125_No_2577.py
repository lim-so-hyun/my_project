A = 3
B = 3
C = 4
multiple = str(A*B*C)
list = [0]*10
for i in range(len(multiple)):
    list[(int(multiple[i]))] += 1
for element in list:
    print(element)
