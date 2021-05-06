# 연령대별 행복지수 DF 분석

import pandas as pd
import pandas as pd
df = pd.read_csv('life style.txt', sep="\t",  index_col = 1, header = 1)
df = df.loc[:,'분류':]
age_df = df.loc['연령별']
x = age_df.transpose()
x.columns = x.loc['분류']
x = x.iloc[1:]

x = x.astype('float')
result = pd.concat([x.idxmax(axis=1), x.max(axis=1), x.idxmin(axis=1), x.min(axis=1)], axis=1)
result.columns = ['행복지수가 가장 높은 연령대', '해당 연령대의 행복지수'
                  , '행복지수가 가장 낮은 연령대', '해당 연령대의 행복지수']

result2 = pd.concat([x.idxmax(axis=0), x.max(axis=0), x.idxmin(axis=0), x.min(axis=0)], axis=1)
result2.columns = ['행복지수가 가장 높은 영역', '해당 영역의 행복지수'
                  , '행복지수가 가장 낮은 영역', '해당 영역의 행복지수']

print(result)
print(result2)
