#승합차

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn

df = pd.read_csv('car_accident.txt', sep="\t", engine = 'python', encoding = 'utf8', index_col = 0, header=1, thousands = ',')
df.replace('-', 0, inplace=True)

승합차 = df[['구분', '승합차']]

승합차1 = 승합차.loc[승합차['구분']=='발생건수']
승합차2 = 승합차.loc[승합차['구분']=='사망자수']
승합차3 = 승합차.loc[승합차['구분']=='부상자수']

final승합차 = pd.concat([승합차1, 승합차2, 승합차3], axis=1)
final승합차.drop('구분', axis='columns', inplace=True)
final승합차.columns = ['발생건수', '사망자수', '부상자수']
final승합차 = final승합차.astype('float')
final승합차.plot(kind='box', y='발생건수')
final승합차 = final승합차.reset_index()

outlier2 = final승합차['발생건수'] > 2000
final승합차.drop(final승합차[outlier2].index, axis='index', inplace=True)
final승합차['size'] = final승합차['발생건수'].apply(np.sqrt)
final승합차['size'] = final승합차['size'] * 10
final승합차

final승합차.plot(kind='scatter', x='부상자수', y='사망자수', s='size', c='size', cmap='gnuplot2', alpha=0.5)
plt.title('승합차 교통사고의 부상자수와 사망자수의 비율')
plt.colorbar

final승합차['부상자수'].corr(final승합차['사망자수'])