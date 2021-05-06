# 원하는 형태로 데이터프레임 수정, 저장하기
import pandas as pd
df = pd.read_csv('life style.txt', sep="\t",  index_col = 1, header = 1)
df = df.loc[:,'분류':]

# 무엇을 분석할지 몰라서 일단 카테고리별로 DF 따로 저장해두기
gender_df1 = df.loc['성별']   # 또는 gender_df2 = df.iloc[1:3]로 직접 index번호로도 슬라이싱 가능
age_df = df.loc['연령별']
degree_df = df.loc['학력별']
income_df = df.loc['소득별']
marriage_df = df.loc['혼인상태별']
region_df = df.loc[df['분류'].str.contains('구')]

# '성별'에 따른 행복지수 분석 코드
gender_df = df.loc['성별']
# 남자가 여자에 비해 더 높은 행복지수를 갖는 column들만 인덱싱하고 싶은데 두 행 비교하는 방법 모르겠어서
# 행, 열 변환해서 column 기준으로 indexing 하고, 남자, 여자로 column 이름 바꿔주자
new_df = gender_df.transpose()
new_df.columns = ['남자', '여자']
new_df = new_df.loc['행복지수 종합':]
condition =  new_df['남자'] - new_df['여자'] > 0
new_df.loc[condition]

print(new_df)