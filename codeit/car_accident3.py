import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('car_accident.txt', sep="\t", engine = 'python', encoding = 'utf8', index_col = 0, header=1, thousands = ',')
df.replace('-', 0, inplace=True)
승용차 = df[['구분', '승용차']]
승용차1 = 승용차.loc[승용차['구분']=='발생건수']
승용차2 = 승용차.loc[승용차['구분']=='사망자수']
승용차3 = 승용차.loc[승용차['구분']=='부상자수']
final승용차 = pd.concat([승용차1, 승용차2, 승용차3], axis=1)
final승용차.drop('구분', axis='columns', inplace=True)
final승용차.columns = ['발생건수', '사망자수', '부상자수']
final승용차 = final승용차.astype('float')

# graph 1
final승용차.plot(kind='box', y='발생건수')
final승용차 = final승용차.reset_index()

outlier1 = final승용차['발생건수'] > 10000
final승용차.drop(final승용차[outlier1].index, axis='index', inplace=True)
final승용차['size'] = final승용차['발생건수'].apply(np.sqrt)
final승용차['size'] = final승용차['size'] * 4

# graph 2
final승용차.plot(kind='scatter', x='부상자수', y='사망자수', s='size', c='size', cmap='gnuplot2', alpha=0.5)
plt.title('승용차 교통사고의 부상자수와 사망자수의 비율')
plt.colorbar

# correlation 출력
final승용차['부상자수'].corr(final승용차['사망자수'])

