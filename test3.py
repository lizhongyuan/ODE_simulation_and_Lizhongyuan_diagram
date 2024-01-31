import pandas as pd
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 1)
data = [[1, 2, 3],
        [9, 1, 8],
        [6, 5, 4]]
cell_colors = [['#56b5fd', 'w', 'w'],
               ['w', '#1ac3f5', 'w'],
               ['w', 'w', '#1ac3f5']]
column_labels = ["Col 1", "Col 2", "Col 3"]
indexes = ["Row 1", "Row 2", "Row 3"]

# creating a 2-dimensional dataframe out of the given data
# df = pd.DataFrame(data, columns = column_labels)
df = pd.DataFrame(data, columns=column_labels, index=indexes)

print(df)

ax.axis('tight')  # turns off the axis lines and labels
ax.axis('off')  # changes x and y axis limits such that all data is shown

# plotting data
table = ax.table(cellText=df.values,
                 colLabels=df.columns,
                 rowLabels=df.index,
                 cellColours=cell_colors,
                 rowColours=["yellow"] * 3,
                 colColours=["red"] * 3,
                 loc="center")
table.set_fontsize(14)
table.scale(1, 2)

table.get_celld()[(1, 0)].set_facecolor('#56b5fd')
table.get_celld()[(2, 0)].set_facecolor("#1ac3f5")
table.get_celld()[(2, 1)].set_facecolor("#808080")

plt.show()
