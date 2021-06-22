import pandas as pd

df1 = pd.read_csv('client.csv', encoding='cp949')
df2 = pd.read_csv('campaign_etc.csv', encoding='cp949')
df = pd.merge(df1, df2, on='index', how='inner')
df.drop(['index', 'poutcome'], axis='columns', inplace=True)
df.insert(5, 'housing', '')
df.loc[:25131, 'housing'] = 'yes'
df.loc[25131:, 'housing'] = 'No'
df.rename(columns={'y':'deposit'},inplace=True)
df.replace({'yes': 1, 'yes': 1, 'No': 0, 'no':0},inplace=True)


# age 결측치 (12개) 중앙값으로 채우기
age_median = df['age'].median(axis=0)  # age_median = 39
df['age'].fillna(age_median, inplace=True)
df.isnull().sum() # age 결측치 0개 된 것 확인 가능

# duration 결측치 (123개) 중앙값으로 채우기
duration_median = df['duration'].median(axis=0) # duration_median = 181
df['duration'].fillna(duration_median, inplace=True)
df.isnull().sum() # duration 결측치 0개 된 것 확인 가능

# balance 결측치 (16개) 제거
## 남은 결측치가 balance 결측치뿐이라 전체에 대해 dropna 실행가능
df.dropna(inplace=True)
df.isnull().sum() # 모든 결측치 사라짐


# age 는 자를 것 없음. 그대로 유지 (범위 자체가 크지 않고 최댓값이 95세로 오류값이라고 보기 어려우므로)


# balance 이상치 처리
# 음수값 제거
balance_negative = df['balance'] < 0
df.drop(df.loc[balance_negative].index, axis='index', inplace=True)

# IQR 기준 이상치 제거 -> 너무 많이 잘려나가서 기각
#q1, q3 = df['balance'].quantile(0.25), df['balance'].quantile(0.75)
#iqr = q3-q1
#condition = (df['balance'] > q1-1.5*iqr) & (df['balance'] < q3+1.5 *iqr)
#df['balance'][condition].describe()

# 50000 이상인 값 제거 : boxplot 상으로 시각적으로 판단
balance_outlier = df['balance'] > 50000
df.drop(df.loc[balance_outlier].index, axis='index', inplace=True)


# day 이상치 처리
day_outlier = (df['day']<0) | (df['day']>31)
df.drop(df.loc[day_outlier].index, axis='index', inplace=True)


#campaign 는 유지 (25%-1.5IQR, 75%+1.5IQR 기준으로 outlier 확인 했을 때에 3234개가 outlier로 잡히고, 41949개가 남음.상대적으로 outlier 비율 적다고 생각하여 유지)


#duration 이상치 처리
# IQR 기준 이상치 제거
duration_q1, duration_q3 = df['duration'].quantile(0.25), df['duration'].quantile(0.75)
duration_iqr = duration_q3-duration_q1
condition = (df['duration'] > duration_q1-1.5*duration_iqr) & (df['duration'] < duration_q3+1.5 *duration_iqr)
df['duration'][condition].describe()


# pdays 이상치 처리
# 음수값 제거
pdays_negative = df['pdays'] <0
df.drop(df.loc[pdays_negative].index, axis='index', inplace=True)
# 700 이상 제거 : boxplot 상에서 시각적으로 판단
pdays_outlier = df['pdays'] > 700
df.drop(df.loc[pdays_outlier].index, axis='index', inplace=True)


# previous 이상치 처리
# 혼자 동떨어져있는 250 이상 값 제거하기 : 혼자 너무 동떨어져있는데 boxplot 상에서 확인되어서 먼저 제거
previous_outlier = df['previous'] > 250
df.drop(df.loc[previous_outlier].index, axis='index', inplace=True)

# 30 이상 제거: boxplot 상으로 시각적으로 판단
previous_outlier2 = df['previous'] > 30
df.drop(df.loc[previous_outlier2].index, axis='index', inplace=True)

df = df.T.drop_duplicates().T

print(df)
