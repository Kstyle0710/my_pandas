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
df = pd.read_csv('./data/seoul_covid19_9_21_.csv', encoding="utf-8")


## 한글 폰트 설정
import matplotlib.pyplot as plt
plt.rc("font", family="Malgun Gothic")
## 숫자 마이너스 값 깨짐 현장 해결
plt.rc("axes", unicode_minus=False)
plt.style.use("fivethirtyeight")

## 시각화를 더 선명하게 설정
# from IPython.display import set_matplotlib_formats
# set_matplotlib_formats("retina")

# 날짜 데이터 전처리

df['확진일자'] = pd.to_datetime("2020-"+ df["확진일"].str.replace(".","-"))
# print(df[["확진일", "확진일자"]].head(10))
df["월"] = df["확진일자"].dt.month
df["주"] = df["확진일자"].dt.isocalendar().week
# print(df[["확진일", "확진일자", "월", "주"]].head(10))


## 시각화
## sort_index의 의미: 시간 순으로 정렬 (데이트타임 타입이면 자동 적용됨)
# df["확진일자"].value_counts().sort_index().plot(title="Daily Seoul Covid19", figsize=(10, 5))
# plt.axhline(30, color="red", linestyle=":")


## 레이블 표시 (x축에 연도 없이 월-일로 표시하기 - 뒤에서 다섯 글자까지 잘라오기)
df['월일'] = df["확진일자"].astype(str).map(lambda x : x[-5:])
# print(df['월일'])
## 월일은 데이트타임 형식이 아니기 때문에 자동으로 시간 순서로 시각화 안됨

day_count = df['월일'].value_counts().sort_index()
# print(day_count)
# day_count.iloc[2]  # x 축의 두번째 값


## 일반 플롯 차트
# g= day_count.plot(title="Daily Seoul Covid19", figsize=(16, 8))
#
# # g.text(x=2, y=3, s=3)   # 좌표 2, 3에 레이블 3을 표시 (for문으로 돌리면서 전부 표시 가능)
# for i in range(len(day_count)):
#     case_count = day_count.iloc[i]
#     if case_count > 100:
#         g.text(x=i, y=case_count+1, s=case_count)
#
# plt.axhline(100, color="red", linestyle=":")
# plt.axhline(50, color="blue", linestyle=":")
### plt.show()


## 특정 데이터 찾아가기.. 최대값
# print(day_count.describe())
# print(day_count.max())   # 확진자 최대값
# print(day_count[day_count == day_count.max()]) ## 확진지가 제일 많은 날
# max_day = day_count[day_count == day_count.max()] ## 확진자가 제일 많았던 날의 발생이력 조회
# print(df[df["월일"] == "08-29"])  ## 확진자가 제일 많은 날의 상세 데이터 df
# filtered_df = df[df["월일"] == "08-29"]
# print(filtered_df["접촉력"].describe())

## 슬라이싱 바 차트
# start_point = -50    # 최종에서 역으로 50일치...
# total_mean = day_count.mean()
# partial_mean = day_count[start_point:].mean()
# # print(mean_value)
#
# g = day_count[start_point :].plot.bar(title="Daily Seoul Covid19", figsize=(16, 8))
#
# for i in range(start_point*-1):
#     case_count = day_count[start_point :].iloc[i]
#     if case_count > 20:
#         g.text(x=i-0.5, y=case_count+1, s=case_count)
#
# plt.axhline(total_mean, color="red", linestyle=":")
# plt.axhline(partial_mean, color="blue", linestyle=":")
#
# plt.show()

## 월별 확진자수에 대한 빈도수 시각화

month_case = df["월"].value_counts().sort_index() # sort_index가 없으면, 시간 순서가 아닌 확진자가 많은 순서대로 시각화를 하는 문제 발생
# print(month_case)
# print(month_case.iloc[0])    # 특정 인덱스 월별 확진자 인원수
month_mean = month_case.mean()
g = month_case.plot.bar(title = "Monthly Seoul Covid19", figsize=(16, 8), rot=0)
for i in range(len(month_case)):
     case_count = month_case.iloc[i]
     if case_count > 20:
         g.text(x=i-0.1, y=month_case.iloc[i]+50, s=month_case.iloc[i])
plt.axhline(month_mean, color="red", linestyle=":")

plt.show()