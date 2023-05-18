import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('.\\test\\11. Construction\\EDAFinal.xlsx')

data = df['qualiExperience']
num_bins = 20

n, bins, patches = plt.hist(data, num_bins, density=False, alpha=0.75)

plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: '{:.1%}'.format(x/len(df))))

mean = data.mean()
plt.axvline(mean, color='red', linestyle='dashed', linewidth=1)

plt.xlabel('Avg. Minimum Experience')
plt.ylabel('Frequency (normalized)')
plt.title('Histogram of Minimum Experience for Construction Industry')
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
