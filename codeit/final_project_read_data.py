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
