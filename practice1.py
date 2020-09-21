import pandas as pd
import numpy as np
import matplotlib as mtb

# df = pd.DataFrame(
#     {"a" : [4 ,5, 6],
#      "b" : [7, 8, 9],
#      "c" : [10, 11, 12]},
#     index = [1, 2, 3])
# print(df)


# df = pd.DataFrame(np.random.rand(100,5), columns=['a', 'b', 'c', 'd', 'e'])
# df.plot.hist()


import matplotlib.pyplot as plt

# plt.rc("font", family="Malgun Gothic")
plt.rc("font", family="AppleGothic")
plt.rc("axes", unicode_minus=False)
plt.style.use("fivethirtyeight")

pd.Series([1, 3, 5, -7, 9]).plot.bar(title="한글 제목")



# url = "https://www.seoul.go.kr/coronaV/coronaStatus.do"
# df = pd.read_html(url)
# print(df[0])