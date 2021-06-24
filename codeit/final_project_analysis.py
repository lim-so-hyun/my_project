import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

# 최종적으로 7718개의 데이터가 남았음. 이를 가지고 분석 진행하기로 함.

# age 분석
df = df.astype({'age':float})
age = plt.subplots(figsize=(12, 10))
age = sns.violinplot(data=df, y='age')
age.set_title("고객층의 age 분포", size=20)

age1 = plt.subplots(figsize=(12, 10))
plt.rcParams['font.family'] = 'Malgun Gothic'
age1 = sns.distplot(df['age'], bins=15)
age1.set_title("고객층의 age 분포", size=20)

# marital 분석
marital = df['marital'].value_counts()
plt.rc('font', family='Malgun Gothic')
plt.rcParams['font.size'] = 15
plt.pie(marital, labels=['married', 'single', 'divorced'], colors=['lightblue', 'darksalmon', 'mediumpurple']
        , autopct='%.1f%%', explode=(0.05, 0, 0.03))
plt.legend()
plt.show()

# job 분석
job = df['job'].value_counts()
plt.rcParams['font.size'] = 15
plt.pie(job, labels=['management', 'blue-collar', 'technician', 'admin', 'services', 'retired', 'student', 'self-employed', 'entrepreneur', 'unemployed', 'housemaid', 'unknown']
        , autopct='%.1f%%', explode=(0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01))
plt.legend(loc='center left', bbox_to_anchor=(1.1, 0.5))
plt.show()

# pdays 분석
pdays = plt.subplots(figsize=(12, 10))
pdays = df['pdays'].plot(kind='box')
pdays.set_title("마지막 contact 으로부터 지난 날의 수")
df['pdays'].quantile(0.25), df['pdays'].quantile(0.5), df['pdays'].quantile(0.75), df['pdays'].mean()

# duration 분석
duration1 = plt.subplots(figsize=(12, 10))
plt.rcParams['font.family'] = 'Malgun Gothic'
duration = sns.distplot(df['duration'], bins=15)
duration.set_title("duration 분포", size=20)

# age와 duration 관계
import numpy as np

sns.set(rc = {'figure.figsize':(12,10)})
age_duration = sns.stripplot(x='age', y='duration', hue="deposit", palette=["green", "red"], data=df, alpha=0.5)
plt.title("customer's age and duration", size=20)
plt.xticks(rotation=45)
plt.xticks(np.arange(0, 95, 5))
plt.yticks(np.arange(0, 2500, 500))
plt.legend(loc='center right')
age_duration

## deposit 성사된 데이터들만 가지고 age와 duration 관계 다시 확인
sns.set(rc = {'figure.figsize':(12,10)})
age_duration = sns.stripplot(x='age', y='duration',palette=["mediumpurple"], data=df.loc[df['deposit']==1], alpha=0.5)
plt.title("Yes deposit customer's age and duration", size=20)
plt.xticks(rotation=45)
plt.xticks(np.arange(0, 95, 5))
plt.yticks(np.arange(0, 2500, 500))
plt.legend(loc='center right')
age_duration

# balance와 duration 의 관계
sns.set(rc = {'figure.figsize':(12,10)})
balance_duration = sns.stripplot(x='balance', y='duration', hue="deposit", palette=["lightblue", "salmon"], data=df, alpha=0.5)
plt.title("customer's balance and duration", size=20)
plt.xticks(rotation=90)
#balance_duration.set_xticks(range(0,40000, 5000))
plt.legend(loc='center right')
balance_duration

# job에 따른 deposit 성사율
deposit_true = df['deposit'] == 1
deposit_false = df['deposit'] == 0
true = df.loc[deposit_true]
true_job_groups = true.groupby("job")
true_series = true_job_groups['deposit'].count()  # 모든 column에서 데이터 수는 동일하기는 한데 굳이 dataframe으로 같은 값 여러개 띄울 필요 없어서 한 column 지정해서 호출한 것
false = df.loc[deposit_false]
false_job_groups = false.groupby("job")
false_series = false_job_groups['deposit'].count()

df_concat = pd.concat([true_series, false_series], axis=1)
df_concat.columns = ['true', 'false']
df_concat['ratio'] = df_concat['true']/(df_concat['true']+df_concat['false'])

plt.rcParams['font.family'] = 'Malgun Gothic'
job_concat = df_concat.plot(kind='bar', y='ratio')
job_concat.set_title("직업군에 따른 적금 개설 성사 비율")

# marital에 따른 deposit 성사율
deposit_true = df['deposit'] == 1
deposit_false = df['deposit'] == 0
true = df.loc[deposit_true]
true_marital_groups = true.groupby("marital")
true_series1 = true_marital_groups['deposit'].count()  # 모든 column에서 데이터 수는 동일하기는 한데 굳이 dataframe으로 같은 값 여러개 띄울 필요 없어서 한 column 지정해서 호출한 것
false = df.loc[deposit_false]
false_marital_groups = false.groupby("marital")
false_series1 = false_marital_groups['deposit'].count()

df_concat = pd.concat([true_series1, false_series1], axis=1)
df_concat.columns = ['true', 'false']
df_concat['ratio'] = df_concat['true']/(df_concat['true']+df_concat['false'])

plt.rcParams['font.family'] = 'Malgun Gothic'
marital_concat = df_concat.plot(kind='bar', y='ratio', color='salmon')
marital_concat.set_title("결혼 상태에 따른 적금 개설 성사 비율")

# 그 외 요소들의 상관계수 확인
df= df.astype({'default':'int','loan':'int','day':'int','campaign':'int','pdays':'int','previous':'int','deposit':'int','housing':'int', 'age':'float', 'balance':'float','duration':'float'})
sns.heatmap(df.corr(), annot=True)

# 상관관계 clustermap으로 확인
corr = df.corr()
sns.clustermap(corr)

# deposit 과의 상관계수 내림차순 정렬
df.corr()['deposit'].sort_values(ascending=False)