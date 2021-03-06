import pandas as pd

## 한글 폰트 설정
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic")
## 숫자 마이너스 값 깨짐 현장 해결
plt.rc("axes", unicode_minus=False)
plt.style.use("fivethirtyeight")


# url = "http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=14&ncvContSeq=&contSeq=&board_id=&gubun="
# table = pd.read_html(url, encoding="utf-8")
# print(table[1])
# df = table[1]
# file_name = f"./data/world_covid19.csv"
# df.to_csv(file_name, index=False)



df = pd.read_csv('./data/world_covid19.csv', encoding="utf-8")
# df1 = df['09.16'].str.strip("명")
df = df.apply(lambda x: x.str.strip('명'), axis = 1)
nation = df['국가/일']
df = df[['09.16', '09.17', '09.18', '09.19', '09.20', '09.21', '09.22']]
# df = df['09.16'].astype(str).astype(int)

df = df.apply(pd.to_numeric, errors='ignore')   # convert all columns of DataFrame
print(df)

# df.plot()
# plt.show()



