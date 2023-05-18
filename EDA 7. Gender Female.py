import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('JobTypesFinal.xlsx')


data.sort_values(by='Gender_Female_Mean', ascending=False, inplace=True)


data = data[::-1]
data['Gender_Male_Mean'] = data['Gender_Male_Mean'][::-1]
data['Gender_Female_Mean'] = data['Gender_Female_Mean'][::-1]


plt.figure(figsize=(10, 8))

bars1 = plt.barh(data['JobTypes'], data['Gender_Male_Mean'], label='Male', color='#008DD5' )
bars2 = plt.barh(data['JobTypes'], -data['Gender_Female_Mean'], label='Female', color='#E43F6F')

plt.xlabel('Percentage')
plt.ylabel('Industry')
plt.title('Gender Distribution in 30 Industries')
plt.legend()

for b1, b2 in zip(bars1, bars2):
    plt.text(b1.get_x()+0.02 , b1.get_y()-0.1 + b1.get_height()/2, round(b1.get_width()*100,1), ha='left', va='center', fontsize=8, color='white')
    plt.text(b2.get_x()-0.02 , b2.get_y()-0.1 + b2.get_height()/2, round(-b2.get_width()*100,1), ha='right', va='center', fontsize=8 , color='white')

plt.xlim(-1, 1)

plt.grid(axis='x', linestyle='--', alpha=0.7)

plt.show()
