import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('customer.csv', encoding='cp949')

# 연령대별 외식업체 이용 비율

total_age = df.iloc[1:3,4:11]
total_age = total_age.transpose()
total_age.columns = ['연령대', '비율']
total_age.index = total_age['연령대']
total_age.drop('연령대', axis='columns', inplace=True)
total_age = total_age.astype('float')

plt.rc('font', family='Malgun Gothic') # 한글 폰트 안깨지게 하기 위해서 폰트 설정
total_age.plot(kind='pie', y='비율', title='연령대에 따른 외식업체 이용자 비율'
               , explode=(0,0.1,0,0,0,0,0) # 우리가 속한 20대에 돌출효과
               , autopct='%.1f%%'  # 비율값 표현되게 하기 위함(소숫점 둘째자리에서 반올림)
               , startangle=90, counterclock=False # 90도에서 시작해서 시계방향으로 돌아가며 나오게 하기 위함.
               , colors = sns.color_palette('hls'))  # 다음 시간에 배울 seaborn 라이브러리에서 색상 가져올 수 있음.
plt.legend(bbox_to_anchor=(1.6,1))  # 범례가 그래프랑 겹쳐보여서 위치 그래프 밖으로 설정
plt.show()
