import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('customer.csv', encoding='cp949')

customer_num = df.iloc[27:,13:]
customer_num.columns = ['1인', '2~5인', '6인 이상']
customer_num.index = ['5천만원 미만', '5천만원~1억원', '1억원~5억원', '5억원 이상']
customer_num = customer_num.astype('float')

plt.rc('font', family='Malgun Gothic')
plot = customer_num.plot(kind='bar', title='식당 매출액 규모에 따른 주요 유입고객')
for p in plot.patches:
    left, bottom, width, height = p.get_bbox().bounds
    plot.annotate("%.1f "%(height)   # 높이에 해당하는 값을
                  , (left+width/2, height*1.01)  # 이 좌표에
                  , ha='center')  # 중심축 가운데로 해서 찍어줘라

plt.show()