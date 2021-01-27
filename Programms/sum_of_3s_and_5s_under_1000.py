# sum_or_3s_and_5s

sum = 0
for n in range(1,1000):
    if n%3==0 or n%5==0:
        sum += n
print(sum)
        
