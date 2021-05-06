# 유기동물의 연령 분포 boxplot으로 표현하기

import csv
import numpy as np

f = open('abandoned_pets_csv.csv')
data = csv.reader(f)
next(data)
age_all = []

for row in data:
    row[9] = int(row[9])
    age = 2021 - row[9]
    age_all.append(age)

for row in data:
    if '개' in row[7]:
        dogs_cats[0] += 1
    if '고양이' in row[7]:
        dogs_cats[1] += 1

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.figure(figsize=(20, 5), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.title('유기동물의 연령 분포', color='darkblue')
plt.boxplot(age_all)
plt.show()

age_array = np.array(age_all)
print('1/4: ' + str(np.percentile(age_all, 25)))
print('1/2: ' + str(np.percentile(age_all, 50)))
print('3/4: ' + str(np.percentile(age_all, 75)))
print('평균: ' + str(round(np.mean(age_all), 2)))