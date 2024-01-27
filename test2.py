import pandas as pd
import numpy as np
import matplotlib as mpl
import dataframe_image as dfi

df = pd.DataFrame({
    "strings": ["Adam", "Mike"],
    "ints": [1, 3],
    "floats": [1.123, 1000.23]
})


df.style \
 .format(precision=3, thousands=".", decimal=",") \
 .format_index(str.upper, axis=1) \
 .relabel_index(["row 1", "row 2"], axis=0) \

dfi.export(df, filename='table1.jpg', fontsize=20, max_cols=-1, max_rows=-1)
