import pandas as pd
import matplotlib.pyplot as plt

leisure_2019 = pd.read_csv('leisure.txt', sep="\t", encoding = 'utf8', index_col = 1)
leisure_2019.drop('기간', axis='columns', inplace=True)
leisure_2019.replace('(.*):(.*)', r'\1.\2', regex=True, inplace=True)  # Dataframe 전체에 있던 : 를 .로 변경하기 위한 정규표현식. 그래야 숫자로 취급가능할 것 같아서.

leisure_2019_day = leisure_2019.loc['교제 및 참여활동', ['평일', '토요일', '일요일']]
leisure_2019_day = leisure_2019_day.astype('float')
leisure_2019_day.index=['소계', '교제활동', '참여활동', '종교활동', '의례활동']

plt.rcParams['font.family']='Malgun Gothic'
graph = leisure_2019_day.loc['교제활동':, :].plot(kind='bar', title='요일별 교제 및 참여활동 세부 항목 여가시간')
for p in graph.patches:
    left, bottom, width, height = p.get_bbox().bounds
    graph.annotate("%.2f"%(height), xy=(left+width/2, height+0.01), ha='center', va='center')
plt.show()
