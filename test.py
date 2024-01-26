import pandas as pd
import numpy as np
import dataframe_image as dfi
import matplotlib.pyplot as plt
df = pd.DataFrame(np.random.randn(6, 6), columns=list('ABCDEF'))

df_styled = df.style.background_gradient() #adding a gradient based on values in cell
dfi.export(obj=df_styled, filename="mytable.png")