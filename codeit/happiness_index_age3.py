import pandas as pd
import numpy as np

df = pd.read_csv('life style.txt', sep="\t",  index_col = 1, header = 1)
df = df.loc[:,'분류':]
age_df = df.loc['연령별']
x = age_df.transpose()
x.columns = x.loc['분류']
x = x.iloc[1:]

sub = x.sub(x.iloc[0],axis=1)
# sub = sub.iloc[:6,:6]
sub['sum'] = np.abs(sub).sum(axis=1)
print(sub)