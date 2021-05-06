import pandas as pd
import numpy as np

# 데이터셋 불러오기 및 다듬기
df = pd.read_csv('life style.txt', sep="\t",  index_col = 1, header = 1) # index_col, header 지정
df = df.loc[:,'분류':] # 기간은 모두 2020으로 동일하므로 제외시키고 데이터셋 저장

# 분석하고자 하는 부분 인덱싱 이용하여 따로 저장 및 분석

# 성별 DataFrame 저장 및 분석

gender_df = df.loc['성별']
new_df = gender_df.transpose()
new_df.columns = ['남자', '여자']  # column 이름 변경
new_df = new_df.loc['행복지수 종합':]

# 질문 1. 남자가 여자보다 높은 행복지수를 보이는 행복지수는 무엇일까?
condition =  new_df['남자'] - new_df['여자'] > 0  # 남자의 행복지수에서 여자의 행복지수를 뺀 값이 0 보다 큰 경우만 인덱싱
print(new_df.loc[condition])


# 연령대별 DataFrame 저장 및 분석

age_df = df.loc['연령별']  # '대분류'가 '연령별'인 데이터만 인덱싱해서 age_df에 저장
x = age_df.transpose()   # 연령대가 column으로 들어가고, 행복지수가 row로 들어가도록, 행/열 변환
x.columns = x.loc['분류']  # columns 이름을 '연령대'가 아닌 '10대', '20대' ... 이 있는 '분류' 목록으로 대체
x = x.iloc[1:]  # '연령대' column은 불필요하므로 슬라이싱해서 저장
x = x.astype('float')

# 질문 1. 각 행복지수에 대해, 가장 높은 행복지수를 보이는 연령대와, 해당 연령대의 행복지수는 몇일까?
result = pd.concat([x.idxmax(axis=1), x.max(axis=1), x.idxmin(axis=1), x.min(axis=1)], axis=1)
result.columns = ['행복지수가 가장 높은 연령대', '해당 연령대의 행복지수'
                  , '행복지수가 가장 낮은 연령대', '해당 연령대의 행복지수']
print(result)

# 질문 2. 각 연령대에 대해, 가장 높은 행복지수를 보이는 영역과, 해당 영역의 행복지수는 몇일까?
result2 = pd.concat([x.idxmax(axis=0), x.max(axis=0), x.idxmin(axis=0), x.min(axis=0)], axis=1)
result2.columns = ['행복지수가 가장 높은 영역', '해당 영역의 행복지수'
                  , '행복지수가 가장 낮은 영역', '해당 영역의 행복지수']
print(result2)

# 질문 3. '행복지수 종합'과 가장 근사한 행복지수 수치를 보이는 영역은 무엇일까?
sub = x.sub(x.iloc[0],axis=1)  # x 데이터프레임의 전체 값을 '행복지수 종합' 값으로 뺀 값으로 데이터프레임 생성 (편차 계산)
sub['sum'] = np.abs(sub).sum(axis=1)  # sub 데이터프레임의 맨 오른쪽에 'sum' 컬럼 추가하자. 편차에 절댓값 씌운 것들의 합을 계산
print(sub)