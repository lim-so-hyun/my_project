import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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

df2018 = data2018.loc['중·고등학생':'대졸이상',:]
df2018 = df2018.astype('float')

df2018['work'] = df2018['일을 매우 더 중시함']*0.5+df2018['일을 더 중시함']*0.3+df2018['일을 약간 더 중시함']*0.2
df2018['leisure'] = df2018['여가를 매우 더 중시함']*0.5+df2018['여가를 더 중시함']*0.3+df2018['여가를 약간 더 중시함']*0.2
df2018['reality'] = df2018['현실을 매우 더 중시함']*0.5+df2018['현실을 더 중시함']*0.3+df2018['현실을 약간 더 중시함']*0.2
df2018['ideal'] = df2018['이상을 매우 더 중시함']*0.5+df2018['이상을 더 중시함']*0.3+df2018['이상을 약간 더 중시함']*0.2
df2018['result'] = df2018['결과를 매우 더 중시함']*0.5+df2018['결과를 더 중시함']*0.3+df2018['결과를 약간 더 중시함']*0.2
df2018['process'] = df2018['과정을 매우 더 중시함']*0.5+df2018['과정을 더 중시함']*0.3+df2018['과정을 약간 더 중시함']*0.2
df2018['individual'] = df2018['개인을 매우 더 중시함']*0.5+df2018['개인을 더 중시함']*0.3+df2018['개인을 약간 더 중시함']*0.2
df2018['group'] = df2018['집단을 매우 더 중시함']*0.5+df2018['집단을 더 중시함']*0.3+df2018['집단을 약간 더 중시함']*0.2
new_df2018 = df2018.loc[:, 'work':'group']
sns.heatmap(new_df2018.corr())
plt.rcParams['axes.unicode_minus'] = False
plt.title("가치별 상관관계")
plt.xlabel("values")
plt.ylabel("values")