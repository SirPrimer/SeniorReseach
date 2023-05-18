import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_excel('JobTypesFinal.xlsx')


df = df.sort_values(by='Female to Male', ascending=True)


y_labels = df['JobTypes']
x_values = df['Female to Male']


colors = ['blue' if x < 1 else 'pink' for x in x_values]


plt.barh(y_labels, x_values, color=colors)


plt.ylabel('Industry', rotation=0)
plt.xlabel('Ratio')
plt.title('Female to Male ratio')

for i, v in enumerate(x_values):
    plt.text(v, i, str(v), ha='left', va='center')

plt.show()
