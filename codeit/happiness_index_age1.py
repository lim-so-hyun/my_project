# 연령대별 행복지수 DF 분석

import pandas as pd
df = pd.read_csv('life style.txt', sep="\t",  index_col = 1, header = 1)
df = df.loc[:,'분류':]
age_df = df.loc['연령별']
x = age_df.transpose()
x.columns = x.loc['분류']
x.iloc[1:]
print(x)

# 각 행복지수마다, 연령대 중에서 가장 행복 지수 높은 연령대와, 해당 행복지수를 한눈에 볼 수 있게 하고 싶음
x['max'] = x.max(axis=1) # 행 축을 따라 최댓값을 찾는 DataFrame.max() 메서드
x['min'] = x.min(axis=1)
x.loc['max'] = x.max(axis=0) # 열 축을 따라 최댓값을 찾는 DataFrame.max() 메서드
x.loc['min'] = x.min(axis=0)
print(x)
