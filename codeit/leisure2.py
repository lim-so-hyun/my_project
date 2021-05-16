import pandas as pd
import matplotlib.pyplot as plt

leisure_2019 = pd.read_csv('leisure.txt', sep="\t", encoding = 'utf8', index_col = 1)
leisure_2019.drop('기간', axis='columns', inplace=True)
leisure_2019.replace('(.*):(.*)', r'\1.\2', regex=True, inplace=True)  # Dataframe 전체에 있던 : 를 .로 변경하기 위한 정규표현식. 그래야 숫자로 취급가능할 것 같아서.

preference_2019 = pd.read_csv('leisure preference 2019.txt', sep='\t', encoding='utf8', index_col=1)
preference_2019.drop('기간', axis='columns', inplace=True)

# 성별에 따른 여가활동 시간
leisure_2019_gender = leisure_2019.loc[leisure_2019['행동분류별']=='소계', ['요일평균', '요일평균.1', '요일평균.2']]
leisure_2019_gender = leisure_2019_gender.astype('float')
leisure_2019_gender = leisure_2019_gender.transpose()
leisure_2019_gender.index=['평균', '남자', '여자']

plt.rcParams['font.family']='Malgun Gothic'
graph = leisure_2019_gender['남자':].plot(kind='bar', title='성별별 여가활동 시간', stacked=True)
for p in graph.patches:
    left, bottom, width, height = p.get_bbox().bounds
    graph.annotate("%.2f"%(height), xy=(left+width/2, bottom+height/2), ha='center', va='center')
