import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('car_accident.txt', sep="\t", engine = 'python', encoding = 'utf8', index_col = 0, header=1, thousands = ',')
df.replace('-', 0, inplace=True)

total = df.loc[df['자치구'] == '합계'].copy()
total.drop('자치구', axis='columns', inplace=True)

total_sum = total.loc[:,:'합계']
df2015 = total_sum.loc['2015', :]
df2015.index=df2015['구분']
df2015.drop('구분', axis='columns', inplace=True)

df2016 = total_sum.loc['2016', :]
df2016.index=df2016['구분']
df2016.drop('구분', axis='columns', inplace=True)

df2017 = total_sum.loc['2017', :]
df2017.index=df2017['구분']
df2017.drop('구분', axis='columns', inplace=True)

df2018 = total_sum.loc['2018', :]
df2018.index=df2018['구분']
df2018.drop('구분', axis='columns', inplace=True)

df2019 = total_sum.loc['2019', :]
df2019.index=df2019['구분']
df2019.drop('구분', axis='columns', inplace=True)

df_concat = pd.concat([df2015, df2016, df2017, df2018, df2019], axis=1)
df_concat.columns=['2015', '2016', '2017', '2018', '2019']
df_concat = df_concat.transpose()
df_concat['발생건수에 대한 사망자수의 비율'] = df_concat['사망자수']/df_concat['발생건수']
df_concat['발생건수에 대한 부상자수의 비율'] = df_concat['부상자수']/df_concat['발생건수']

plt.rc('font', family='Malgun Gothic')

y1 = df_concat['발생건수에 대한 사망자수의 비율']
y2 = df_concat['발생건수에 대한 부상자수의 비율']

plt.style.use('ggplot')

fig, ax1 = plt.subplots()
ax1.set_xlabel('년도')
ax1.plot(df_concat.index, y1, 'g--', label='발생건수에 대한 사망자수 비율')
ax1.tick_params(axis='y')
plt.legend()

ax2 = ax1.twinx()
ax2.plot(df_concat.index, y2, 'b-', label='발생건수에 대한 부상자수 비율')
ax2.tick_params(axis='y')
plt.legend()

plt.title('년도별 교통사고 발생건수에 대한 사망자수와 부상자수의 비율')
fig.tight_layout()
plt.show()