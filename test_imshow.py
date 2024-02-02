import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpl

# sphinx_gallery_thumbnail_number = 2

vegetables = ["cucumber", "tomato", "lettuce", "asparagus",
              "potato", "wheat", "barley"]
farmers = ["Farmer Joe", "Upland Bros.", "Smith Gardening",
           "Agrifun", "Organiculture", "BioGoods Ltd.", "Cornylee Corp."]

harvest = np.array([[0, 7.5, 2, 2.5, 3, 3.5, 4, 0, 7.5, 2, 2.5, 3, 3.5, 4],
                    [4.5, 5, 5.5, 6, 6.5, 7, 7.5, 0, 7.5, 2, 2.5, 3, 3.5, 4],
                    [8, 8.5, 9, 9.5, 10, 10.5, 11, 0, 7.5, 2, 2.5, 3, 3.5, 4],
                    [11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.7, 1.7, 0.6, 2.6, 2.2, 6.2, 0.0, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 2, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 2, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [1.3, 1.2, 0.0, 0.0, 0.0, 3.2, 5.1, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    [0.1, 2.0, 0.0, 1.4, 0.0, 1.9, 2, 11.5, 12, 0.3, 0.0, 3.1, 0.0, 0.0],
                    ])


fig, ax = plt.subplots()
im = ax.imshow(X=harvest, cmap=plt.cm.get_cmap('gist_heat'))

ax.set_xticks(np.arange(len(farmers)), labels=farmers)
ax.set_yticks(np.arange(len(vegetables)), labels=vegetables)

fig.tight_layout()
plt.show()