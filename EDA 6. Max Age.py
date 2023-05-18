import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('JobTypesFinal.xlsx')


data['Range'] = data['MaxAge_Mean'] - data['MinAge_Mean']


data.sort_values(by='MaxAge_Mean', ascending=True, inplace=True)


plt.figure(figsize=(15, 12))

bars1 = plt.barh(data['JobTypes'], data['MaxAge_Mean'], label='MaxAge_Mean')
bars2 = plt.barh(data['JobTypes'], data['Range'], left=data['MinAge_Mean'], label='MinAge_Mean')

for b1, b2 in zip(bars1, bars2):
    plt.text(b1.get_x() + b1.get_width()-0.3, b1.get_y()-0.1 + b1.get_height()/2, round(b1.get_width()), ha='right', va='center', fontsize=8)
    plt.text(b2.get_x() -0.3 , b2.get_y()-0.1 + b2.get_height()/2, round(b2.get_x()), ha='right', va='center', fontsize=8 , color='white')

plt.xlabel('Age')
plt.ylabel('Industry')
plt.title('Age Range for Workers in 49 Industries')
plt.legend()

plt.show()