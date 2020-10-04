import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('./data/seoul_covid19_10_03_.csv', encoding = 'utf-8')

temp = df["확진일"].value_counts().sort_index()
print(temp)
temp.plot(figsize=(15, 5))
plt.show()


