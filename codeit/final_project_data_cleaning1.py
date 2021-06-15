import pandas as pd
import matplotlib as plt

df1 = pd.read_csv('client.csv', encoding='cp949')
df2 = pd.read_csv('campaign_etc.csv', encoding='cp949')
df = pd.merge(df1, df2, on='index', how='inner')
df.drop(['index'], axis='columns', inplace=True)
df.insert(5, 'housing', '')
df.loc[:25131, 'housing'] = 'yes'
df.loc[25131:, 'housing'] = 'No'
df.rename(columns={'y':'deposit'},inplace=True)
df.replace({'yes': 1, 'yes': 1, 'No': 0, 'no':0},inplace=True)

# 결측치, 이상치, 중복치 찾기 위해서 다양하게 시행해본 코드들

# 결측치 있는 column 찾으려고
df.isnull().sum()

# 분포 보고 싶어서 통계치 보여주는 describe() 써봄.
df['balance'].describe()

# boxplot으로 분포 확인해보려고 시행.
plt.rcParams['figure.figsize'] = [10, 10]
df.plot(kind='box', y='duration')

df['pdays'].plot(kind='box')

# 연속형 변수는 float 이라고 되어있으려나 싶어서 시행해봤던 코드
df.dtypes

# 중복되는 column 찾으려고 시행한 코드 -> 중복 column 있길래 drop
df.T.duplicated()
df = df.T.drop_duplicates().T

