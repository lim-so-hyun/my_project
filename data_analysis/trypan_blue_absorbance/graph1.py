import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pipetting_practice.csv')
data.index = ['5%_1', '5%_2', '4%_1', '4%_2', '2%_1', '2%_2', '1%_1', '1%_2']
data = data.transpose()

plt.rc('font', family='Malgun Gothic')
data.plot(kind='box',  y=['5%_1', '5%_2', '4%_1', '4%_2', '2%_1', '2%_2', '1%_1', '1%_2'], figsize=(30, 20))
#plt.title('concentration에 따른 trypan blue absorbance', fontsize=35, pad=15)
plt.style.use('ggplot')
plt.xlabel('concentration', fontsize=35, labelpad=15)
plt.ylabel('absorbance', fontsize=35, labelpad=20)
plt.xticks(fontsize =30)
plt.yticks(fontsize=30)
plt.show()