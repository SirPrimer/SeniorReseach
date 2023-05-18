import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('JobTypesFinal.xlsx')


plt.figure(figsize=(10, 8))


plt.scatter(data['qualiExperience_Mean'], data['AverageSalary'])


plt.xlabel('AVG_Experience_Yr')
plt.ylabel('AVG_Salary')
plt.title('Average Salary vs. Average Job Experience by Industry')


for i, row in data.iterrows():
    plt.text(row['qualiExperience_Mean']+0.015, row['AverageSalary'] , row['JobTypes'])


plt.show()