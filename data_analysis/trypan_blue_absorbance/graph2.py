import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('pipetting_practice.csv')
data.index = ['5%_1', '5%_2', '4%_1', '4%_2', '2%_1', '2%_2', '1%_1', '1%_2']
data = data.transpose()
