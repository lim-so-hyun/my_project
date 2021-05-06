# 유기견과 유기묘의 비율

import csv

f = open('abandoned_pets_csv.csv')
data = csv.reader(f)
next(data)  # header 넘기자
total_num = 0
dogs_cats = [0]*2

for row in data:
    if '개' in row[7]:
        dogs_cats[0] += 1
    if '고양이'in row[7]:
        dogs_cats[1] += 1
    total_num += 1

import matplotlib.pyplot as plt
plt.rc('font',family='Malgun Gothic')
plt.title('유기동물 중 개와 고양이의 비율')
plt.pie(dogs_cats, labels=['개','고양이'],colors=['lightblue','darksalmon'],startangle=90,autopct='%.1f%%',explode=(0,0.1))
plt.axis('equal')
plt.legend()
plt.show()