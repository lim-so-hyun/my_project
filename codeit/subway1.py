import pandas as pd
subway = pd.read_csv('subway.csv', encoding='cp949')  # UnicodeDecode Error 떠서 encoding 방식 추가.
subway.drop('작업일자', axis='columns', inplace=True)
statistics = subway.describe()
statistics

# 시간대별 전역의 승차 및 하차 인원 평균
on_mean = statistics.iloc[1, 1::2]
off_mean = statistics.iloc[1, 2::2]
pd.options.display.float_format = '{:.2f}'.format  # 소숫점 둘째 자리까지만 보이게 하는 코드 추가
time = ['04시', '05시', '06시', '07시', '08시', '09시', '10시', '11시', '12시', '13시', '14시', '15시'
        , '16시', '17시', '18시', '19시', '20시', '21시', '22시', '23시', '00시', '01시', '02시', '03시']
on_mean.index = time # 승차인원 평균
off_mean.index = time # 하차인원 평균

mean = pd.concat([on_mean, off_mean], axis=1) #승하차 같이 보기 위해 합침
mean.columns = ['승차인원 평균', '하차인원 평균']
mean = mean.transpose()
print(mean)