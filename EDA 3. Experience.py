import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('JobTypesFinal.xlsx')

df = df.sort_values(by='qualiExperience_Mean', ascending=True)

y_labels = df['JobTypes']
x_values = df['qualiExperience_Mean']

x_values = [round(x, 3) for x in x_values]

plt.barh(y_labels, x_values)

plt.ylabel('JobTypes', rotation=0)
plt.xlabel('Avg. Minimum Experience')
plt.title('Avg. Minimum Experience for Each Industry')

for i, v in enumerate(x_values):
    plt.text(v, i, str(v), ha='left', va='center')

plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
