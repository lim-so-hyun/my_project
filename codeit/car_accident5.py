# 이륜차

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('car_accident.txt', sep="\t", engine = 'python', encoding = 'utf8', index_col = 0, header=1, thousands = ',')
df.replace('-', 0, inplace=True)

이륜차 = df[['구분', '이륜차']]

이륜차1 = 이륜차.loc[이륜차['구분']=='발생건수']
이륜차2 = 이륜차.loc[이륜차['구분']=='사망자수']
이륜차3 = 이륜차.loc[이륜차['구분']=='부상자수']

final이륜차 = pd.concat([이륜차1, 이륜차2, 이륜차3], axis=1)
final이륜차.drop('구분', axis='columns', inplace=True)
final이륜차.columns = ['발생건수', '사망자수', '부상자수']
final이륜차 = final이륜차.astype('float')
final이륜차.plot(kind='box', y='발생건수')
final이륜차 = final이륜차.reset_index()

outlier = final이륜차['발생건수'] > 3000
final이륜차.drop(final이륜차[outlier].index, axis='index', inplace=True)
final이륜차['size'] = final이륜차['발생건수'].apply(np.sqrt)
final이륜차['size'] = final이륜차['size'] * 10
final이륜차

final이륜차.plot(kind='scatter', x='부상자수', y='사망자수', s='size', c='size', cmap='gnuplot2', alpha=0.5)
plt.title('이륜차 교통사고의 부상자수와 사망자수의 비율')
plt.colorbar

final이륜차['부상자수'].corr(final이륜차['사망자수'])