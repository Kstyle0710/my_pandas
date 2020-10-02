import pandas as pd
import numpy as np
import matplotlib as mtb

# df = pd.DataFrame(
#     {"a" : [4 ,5, 6],
#      "b" : [7, 8, 9],
#      "c" : ["aaaaaaaaaaa", "bbbbbbbbbbbbbb", "ccccccccccc"]},
#     index = [1, 2, 3])
# print(df)
# result = df.loc[[1,2], ["a", "c"]]
# print(result)
# df["d"] = df["c"].apply(lambda x : x[:3])
# print(df)



df2 = pd.DataFrame([[np.nan, 2, np.nan, 0], [3, 4, np.nan, 1], [np.nan, np.nan, np.nan, 5]],
                   columns=list('ABCD'))
print(df2)

# df2 = df2.dropna(axis=1, how="any")   ## 열기준으로 하나라도 널값이 있으면 열을 삭제
df2 = df2.fillna("K")
print(df2)



# df = pd.DataFrame(np.random.rand(100,5), columns=['a', 'b', 'c', 'd', 'e'])
# df.plot.hist()


import matplotlib.pyplot as plt

# plt.rc("font", family="Malgun Gothic")
# plt.rc("font", family="AppleGothic")
# plt.rc("axes", unicode_minus=False)
# plt.style.use("fivethirtyeight")

# pd.Series([1, 3, 5, -7, 9]).plot.bar(title="한글 제목")





