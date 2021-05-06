# 개와 고양이 나누어서 연령 분포 boxplot으로 표현하기

import csv
import numpy as np

f = open('abandoned_pets_csv.csv')
data = csv.reader(f)
next(data)
dog_ages = []
cat_ages = []

for row in data:
    row[9] = int(row[9])
    age = 2021 - row[9]
    if '개' in row[7]:
        dog_ages.append(age)
    if '고양이' in row[7]:
        cat_ages.append(age)

import matplotlib.pyplot as plt

plt.style.use('ggplot')
plt.figure(figsize=(20, 10), dpi=300)
plt.rc('font', family='Malgun Gothic')
plt.title('유기견과 유기묘의 연령 분포', size=35, color='salmon')
plt.boxplot([dog_ages, cat_ages], labels=['개', '고양이'])
plt.show()