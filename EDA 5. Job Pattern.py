import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('JobTypesFinal.xlsx')

data = data[['JobTypes', 'jobWorkPattern_สหกิจศึกษา_Mean', 'jobWorkPattern_งานนอกเวลา_Mean', 'jobWorkPattern_งานอิสระ_Mean', 'jobWorkPattern_สัญญาจ้าง_Mean', 'jobWorkPattern_งานประจำ_Mean']]

data.to_excel('EDAEduheatmap.xlsx', index=False)


data = pd.read_excel('EDAEduheatmap.xlsx', index_col='JobTypes')

columns = ['jobWorkPattern_สหกิจศึกษา_Mean', 'jobWorkPattern_งานนอกเวลา_Mean', 'jobWorkPattern_งานอิสระ_Mean', 'jobWorkPattern_สัญญาจ้าง_Mean', 'jobWorkPattern_งานประจำ_Mean']

plt.rcParams['font.family']='Tahoma'

fig, ax = plt.subplots()


heatmap = ax.matshow(data, cmap=plt.cm.RdYlGn, vmin=0, vmax=1)


ax.set_xticks(range(len(columns)))
ax.set_yticks(range(len(data.index)))


ax.set_xticklabels(columns, rotation=90)
ax.set_yticklabels(data.index)

cbar = plt.colorbar(heatmap)

plt.title('Job Work Pattern Heatmap')


plt.show()
