A="so good"
if A == ' ' or A == " ":
    print(0)
else:
    word_count = 1
    for i in range(1,len(A)-1):
        if A[i]==' ':
            word_count += 1
    print(word_count)