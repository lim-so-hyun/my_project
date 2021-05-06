# 연령대별 유기동물의 수 막대그래프로 표현하기

import csv

f = open('abandoned_pets_csv.csv')
data = csv.reader(f)
next(data)
total_num = 0
age_list = [0]*18

for row in data:
    total_num += 1
    row[9] = int(row[9])
    age = 2021-row[9]
    age_list[age] += 1

import matplotlib.pyplot as plt
plt.style.use('ggplot')
plt.rc('font',family='Malgun Gothic')
plt.title('연령대별 유기동물의 수')
plt.bar(range(18),age_list,color='slategray')
plt.show()