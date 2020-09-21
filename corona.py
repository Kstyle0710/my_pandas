import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

## 별도의 로그인이 필요없는 사이트에서 table tag를 크롤링하기
## 서울 코로나 발생자 현황 크롤링 with pandas

# url = 'https://www.seoul.go.kr/coronaV/coronaStatus.do'
# table = pd.read_html(url)
# print(table[3])
# print("--------------------")
# df = table[3]
# last_day = df.loc[0, "확진일"]
# last_day = last_day.replace(".", "_")
# file_name = f"./data/seoul_covid19_{last_day}.csv"
# df.to_csv(file_name, index=False)
# print("-------------------")

## 저장한 CSV로 분석 개시
df = pd.read_csv('./data/seoul_covid19_9_20_.csv', encoding="utf-8")
df['확진일자'] = pd.to_datetime("2020-"+ df["확진일"].str.replace(".","-"))
# print(df[["확진일", "확진일자"]].head(10))
df["월"] = df["확진일자"].dt.month
df["주"] = df["확진일자"].dt.week
print(df[["확진일", "확진일자", "월", "주"]].head(10))


## 한글 폰트 설정
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic")
## 숫자 마이너스 값 깨짐 현장 해결
plt.rc("axes", unicode_minus=False)

## 시각화를 더 선명하게 설정
from IPython.display import set_matplotlibe_formats
set_matplotlibe_formats("retina")



df["확진일자"].value_counts().sort_index().plot(title="한글 제목", figsize=(10, 5))
plt.axhline(30, color="red", linestyle=":")
plt.show()


