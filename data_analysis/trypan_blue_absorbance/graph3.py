import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data3 = pd.read_csv('pipetting_practice2.csv')
data3 = data3.transpose()
data3.columns = ['absorption', 'concentration', 'row']
data3[['absorption', 'concentration']] = data3[['absorption', 'concentration']].astype('float')

plt.figure(figsize=(20,15))
sns.scatterplot(data=data3, x='concentration', y='absorption', hue='row', palette=['orange', 'skyblue'], alpha=0.4, s=500)
sns.regplot(x='concentration', y='absorption', data=data3, ci=None)
plt.xlabel('concentration (%)', fontsize=35, labelpad=15)
plt.ylabel('absorbance', fontsize=35, labelpad=20)
plt.xticks(np.arange(1, 5.5, 1), fontsize =25, labels = [1,2, 3, 4,5])
plt.yticks(fontsize=25)
plt.legend(fontsize=30)
plt.show()