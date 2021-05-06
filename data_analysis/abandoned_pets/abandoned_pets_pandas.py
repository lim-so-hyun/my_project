import pandas as pd

pets_df = pd.read_csv('abandoned_pets.csv', encoding='cp949')
# 처음에 여기서 encoding 부분 추가 안했을 때 Unicode decoding error인가 그거 또 떴는데 이번에는 'utf8'뭐시기로 error가 떠서 'cp949'로 encoding 추가해서 해결!

print(pets_df)