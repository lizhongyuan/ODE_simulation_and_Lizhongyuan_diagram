import pandas as pd
import dataframe_image as dfi


df = pd.DataFrame({'Reference': ['40%','30%'],
                  'colA': ['30% (20%)','25% (14%)'],
                  'colB': ['45% (20%)','25% (30%)'],
                  'colC': ['25% (30%)','35% (30%)']})


def highlight(x, color1, color2):
    ref = x[0]
    ans = [None]
    for y in x[1:]:
        c = color1 if y < ref else color2
        ans.append(f"color: {c};")
    return ans

def _color_red_or_green(val):
    # color = 'red' if val < 0 else 'green'
    # return 'color: %s' % color
    return 'color: red'

# df.style.apply(highlight, color1='green', color2='red', axis=1)
# df.style.applymap(_color_red_or_green)
df.style.set_properties(**{'background-color': 'black',
                           'color': 'green'})

dfi.export(df, filename='table2.jpg', fontsize=20, max_cols=-1, max_rows=-1)
# dfi.export(df, filename='table2.xlsx', fontsize=20, max_cols=-1, max_rows=-1)
