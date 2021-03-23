import csv

f = open('seoul.csv')
data = csv.reader(f)
next(data)
high = []   # 최고기온 담을 list
low = []   # 이번엔 최저기온도 그려보려고 list 따로 만듦.

for row in data:
    if row[2] != '' and row[4] != '':  # 이번에는 최저, 최고 기온 모두 데이터가 제대로 되어있는지 확인 필요
        if 1999 <= int(row[0].split('-')[0]):
            if row[0].split('-')[1] == '05' and row[0].split('-')[-1]=='11':
                high.append(float(row[2]))
                low.append(float(row[4]))
print(high)
print(low)
