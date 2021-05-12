import pandas as pd
import matplotlib.pyplot as plt

#데이터 불러오기
df = pd.read_csv('customer.csv', encoding='cp949',header=2,index_col=2)
#필요없는 열 제거 후 다른 데이터셋에 저장
fna=df.drop(['특성별(1)','특성별(2)','특성별(4)','남성','여성','1인','2~5인','6인 이상'],axis='columns') #연령 열만 남기기
gf=fna.iloc[1:7,:] #일반음식점
#음식점 특성별을 기준으로 선그래프 그리기 위해 transpose해주기
gft=gf.transpose()
gft.plot(kind='line', title='연령대별 일반음식점 고객 비율')
plt.rc('font', family='Malgun Gothic') # 한글 폰트 안깨지게 하기 위해서 폰트 설정
plt.rcParams['figure.figsize'] = [15, 7]
plt.rc('font', family='Malgun Gothic')
plt.legend(bbox_to_anchor=(1,1))
plt.show()