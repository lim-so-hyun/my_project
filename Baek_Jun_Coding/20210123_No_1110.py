N = input()
count = 0
if len(N)<2:
    first = 0
    second = N
    compare_num = N + N
while N is True:
    first = N//10
    second = N-(10*first)
    new_first = (first+second)-(10*((first+second)//10))
    compare_num = 10*second + (new_first)
    count += 1
    if compare_num != N:
        N = compare_num
        continue
    else : break

print(count)