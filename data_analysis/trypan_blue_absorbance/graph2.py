import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data2 = pd.read_csv('pipetting_practice.csv')
data2['concentration'] = [5,5,4,4,2,2,1,1]
data2['row'] = [1, 2, 1, 2, 1, 2, 1, 2]

plt.figure(figsize=(20,15))
plt.plot(data2.iloc[:, :12].T, 'o-')
plt.ylabel('absorbance', fontsize=35, labelpad=20)
plt.xticks(np.arange(0, 12, 1), fontsize =20, labels = ['#1','#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#10', '#11', '#12'])
plt.yticks(fontsize=20)
plt.legend(['5%_1', '5%_2', '4%_1', '4%_2', '2%_1', '2%_2', '1%_1', '1%_2'], fontsize=17)