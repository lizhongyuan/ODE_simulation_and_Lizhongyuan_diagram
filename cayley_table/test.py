import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Create example DataFrame
data = np.random.rand(5, 5)  # 5x5 random
df = pd.DataFrame(data)

# heatmap by imShow
fig, ax = plt.subplots()
im = ax.imshow(df, cmap='viridis')

# Add color bar
cbar = ax.figure.colorbar(im, ax=ax)

# Add edges to each grid
ax.set_xticks(np.arange(df.shape[1] + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(df.shape[0] + 1) - 0.5, minor=True)
#ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
ax.tick_params(which="minor", bottom=False, left=False)

# show results
plt.show()