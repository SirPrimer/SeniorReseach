import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('JobTypesFinalOG.xlsx')

df = df.sort_values(by='Instances', ascending=True)

y_labels = df['JobTypes']
x_values = df['Instances']

plt.barh(y_labels, x_values)

plt.ylabel('Industry', rotation=0)
plt.xlabel('Count')
plt.title('Industry Job count')

for i, v in enumerate(x_values):
    plt.text(v, i, str(v), ha='left', va='center')

plt.show()
