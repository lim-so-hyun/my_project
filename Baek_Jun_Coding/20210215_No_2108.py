N = int(input())
list = []
for _ in range(N):
    list.append(int(input()))
list.sort()

sum = 0
for i in list:
    sum += i
mean = round(sum / N)
print(mean)

memo = []
for i in list:
    if i in memo: pass
    else:
        memo.append(i)

mid = 0
if len(memo) % 2 == 0:
    mid = (memo[len(memo) // 2 - 1] + memo[len(memo) // 2]) / 2
else:
    mid = memo[len(memo) // 2]
print(mid)

count = [0] * len(memo)
for i in range(len(memo)):
    for j in list:
        if memo[i] == j:
            count[i] += 1

max_index = 0
for i in range(len(memo)):
    if count[i] > count[max_index]:
        max_index = i
max_count = count[max_index]
max_num_count = 0
for i in range(len(count)):
    if count[i] == max_count:
        max_num_count += 1
        if max_num_count == 2:
            real_max_index = i
            print(memo[real_max_index])
            break
if max_num_count == 1:
    print(memo[max_index])

list_range = memo[-1] - memo[0]
print(list_range)
