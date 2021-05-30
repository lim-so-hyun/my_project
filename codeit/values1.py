import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('preference.csv', encoding='cp949')
data_info = data.loc[:, :'특성별(2)']

data2017 = pd.concat([data_info, data.loc[:,'2017':'2017.27']], axis=1)
data2017.index= data2017['특성별(2)']
data2017.columns = data2017.iloc[1,:]
data2017 = data2017.iloc[2:, 2:]
data2017.drop(['만18-19세', '만20-24세', '만25-29세', '만30-34세'], axis='index', inplace=True)

data2018 = pd.concat([data_info, data.loc[:, '2018':'2018.27']], axis=1)
data2018.index= data2018['특성별(2)']
data2018.columns = data2018.iloc[1,:]
data2018 = data2018.iloc[2:, 2:]
data2018.drop(['만18-19세', '만20-24세', '만25-29세', '만30-34세'], axis='index', inplace=True)

data2019 = pd.concat([data_info, data.loc[:, '2019':'2019.27']], axis=1)
data2019.index= data2019['특성별(2)']
data2019.columns = data2019.iloc[1,:]
data2019 = data2019.iloc[2:, 2:]
data2019.drop(['만18-19세', '만20-24세', '만25-29세', '만30-34세'], axis='index', inplace=True)

data2020 = pd.concat([data_info, data.loc[:, '2020':]], axis=1)
data2020.index= data2020['특성별(2)']
data2020.columns = data2020.iloc[1,:]
data2020 = data2020.iloc[2:, 2:]
data2020.drop(['만15-18세', '만19-29세', '만30-39세', '만30-34세', '중·고등학생'], axis='index', inplace=True)

df2019 = data2019.loc['중·고등학생':'대졸이상',:]
df2019 = df2019.transpose()
df2019 = df2019.astype('float')
plt.rc('font', family='Malgun Gothic')

df2019.iloc[:7, :].plot(title='학력별 일 vs 여가 선호도')
plt.style.use('ggplot')
plt.xticks(size=10, rotation=90)
plt.xlabel('학력')

df2019.iloc[7:14, :].plot(title='학력별 현실 vs 이상 중요도')
plt.style.use('ggplot')
plt.xticks(size=10, rotation=90)
plt.xlabel('학력')

df2019 = df2019.astype('float')
plt.rc('font', family='Malgun Gothic')
df2019.iloc[14:21, :].plot(title='학력별 결과 vs 과정 중요도')
plt.style.use('ggplot')
plt.xticks(size=10, rotation=90)
plt.xlabel('학력')

df2019 = df2019.astype('float')
plt.rc('font', family='Malgun Gothic')
df2019.iloc[21:, :].plot(title='학력별 개인 vs 집단 선호도')
plt.style.use('ggplot')
plt.xticks(size=10, rotation=90)
plt.xlabel('학력')