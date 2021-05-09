import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('customer.csv', encoding='cp949')

# 성별에 따른 외식업체 이용 비율
total_gender = df.iloc[1:3,11:13]
total_gender = total_gender.transpose()
total_gender.columns = ['성별', '비율']
total_gender.index = total_gender['성별']
total_gender.drop('성별', axis='columns', inplace=True)
total_gender = total_gender.astype('float')

plt.rc('font', family='Malgun Gothic')
total_gender.plot(kind='pie', y='비율', title='성별에 따른 외식업체 이용자 비율'
               , autopct='%.1f%%', startangle=90, counterclock=False)
plt.show()