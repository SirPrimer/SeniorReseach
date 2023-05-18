import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('JobTypesFinal.xlsx')

data = data[['JobTypes', 'eduLevel_ไม่ระบุ_Mean', 'eduLevel_ไม่มีวุฒิการศึกษา_Mean', 'eduLevel_ต่ำกว่าม6_Mean', 'eduLevel_ปวช._Mean', 'eduLevel_ม.6_Mean', 'eduLevel_ปวส._Mean', 'eduLevel_ปริญญาตรี_Mean', 'eduLevel_ปริญญาโท_Mean']]

data.to_excel('EDAEduheatmap.xlsx', index=False)


data = pd.read_excel('EDAEduheatmap.xlsx', index_col='JobTypes').transpose()

columns = data.columns


plt.rcParams['font.family']='Tahoma'


fig, ax = plt.subplots()

heatmap = ax.matshow(data, cmap=plt.cm.RdYlGn, vmin=0, vmax=1, origin='lower')

ax.set_xticks(range(len(columns)))
ax.set_yticks(range(len(data.index)))

ax.set_xticklabels(columns, rotation=90)
ax.set_yticklabels(data.index)

cbar = plt.colorbar(heatmap)
plt.tick_params(axis='both', which='major', labelsize=14)

plt.title('Education Requirement Heatmap')

plt.show()
