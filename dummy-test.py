import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style='whitegrid')

iris = sns.load_dataset('iris')

fig, axes = plt.subplots(ncols=2, nrows=2, constrained_layout=True)
axes = axes.flatten()

sns.lineplot(data=iris, x='sepal_width', y='sepal_length', estimator=None, ax=axes[0])
sns.lineplot(data=iris, x='sepal_width', y='sepal_length', estimator='sum', ax=axes[1])
def my_median(nums):
    return np.median(nums)
sns.barplot(data=iris, x='species', y='sepal_length', estimator=my_median, ax=axes[2])
sns.barplot(data=iris, x='species', y='sepal_length', estimator=lambda d: sum(d), ax=axes[3])

plt.show()
plt.gcf().savefig('plot.png')
