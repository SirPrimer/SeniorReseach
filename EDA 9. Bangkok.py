import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('JobTypesFinal.xlsx')

df = df.sort_values(by='province_กรุงเทพมหานคร_Mean', ascending=True)

plt.rcParams['font.family']='Tahoma'

y_labels = df['JobTypes']
x_values = df['province_กรุงเทพมหานคร_Mean']

plt.barh(y_labels, x_values)

plt.ylabel('JobTypes', rotation=0)
plt.xlabel('province_กรุงเทพมหานคร_Mean')
plt.title('Bangkok work Ration')

for i, v in enumerate(x_values):
    plt.text(v, i, str(round(v, 2)), ha='left', va='center')

plt.show()