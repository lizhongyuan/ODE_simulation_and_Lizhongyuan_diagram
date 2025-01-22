import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 创建一个示例 DataFrame
data = np.random.rand(5, 5)  # 5x5 的随机数据
df = pd.DataFrame(data)

# 使用 imshow 绘制热图
fig, ax = plt.subplots()
im = ax.imshow(df, cmap='viridis')

# 添加颜色条
cbar = ax.figure.colorbar(im, ax=ax)

# 为每个方格添加边缘线
ax.set_xticks(np.arange(df.shape[1] + 1) - 0.5, minor=True)
ax.set_yticks(np.arange(df.shape[0] + 1) - 0.5, minor=True)
#ax.grid(which="minor", color="gray", linestyle='-', linewidth=0.5)
ax.tick_params(which="minor", bottom=False, left=False)

# 显示图形
plt.show()