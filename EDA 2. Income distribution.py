import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_excel('JobTypesFinal.xlsx')

data = data[['JobTypes', '0-10000', '10000-20000', '20000-30000', '30000-40000', '40000-50000', '50000-60000', '60000-70000']]

data.to_excel('EDAheatmap.xlsx', index=False)


data = pd.read_excel('EDAheatmap.xlsx', index_col='JobTypes').transpose()

columns = data.columns


fig, ax = plt.subplots()

heatmap = ax.matshow(data, cmap=plt.cm.RdYlGn, vmin=0, vmax=1, origin='lower')

ax.set_xticks(range(len(columns)))
ax.set_yticks(range(len(data.index)))

ax.set_xticklabels(columns, rotation=90)
ax.set_yticklabels(data.index)

ax.tick_params(axis='both', which='major', labelsize=14)

cbar = plt.colorbar(heatmap)

plt.title('Job Types Heatmap')

plt.show()
