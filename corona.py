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
df = pd.read_csv('./data/seoul_covid19_9_24_.csv', encoding="utf-8")


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
# month_case = df["월"].value_counts().sort_index() # sort_index가 없으면, 시간 순서가 아닌 확진자가 많은 순서대로 시각화를 하는 문제 발생
# # print(month_case)
# # print(month_case.iloc[0])    # 특정 인덱스 월별 확진자 인원수
# month_mean = month_case.mean()
# g = month_case.plot.bar(title = "Monthly Seoul Covid19", figsize=(16, 8), rot=0)
# for i in range(len(month_case)):
#      case_count = month_case.iloc[i]
#      if case_count > 20:
#          g.text(x=i-0.1, y=month_case.iloc[i]+50, s=month_case.iloc[i])
# plt.axhline(month_mean, color="red", linestyle=":")
#
# plt.show()

## 주단위 확진자에 대한 빈도수 시각회
# weekly_case = df["주"].value_counts().sort_index() # sort_index가 없으면, 시간 순서가 아닌 확진자가 많은 순서대로 시각화를 하는 문제 발생
# print(weekly_case)
# # # print(weekly_case.iloc[0])    # 특정 인덱스 월별 확진자 인원수
# weekly_mean = weekly_case.mean()
# g = weekly_case.plot.bar(title = "Weekly Seoul Covid19", figsize=(12, 5), rot=0)
# for i in range(len(weekly_case)):
#      case_count = weekly_case.iloc[i]
#      if case_count > 20:
#          g.text(x=i-0.1, y=weekly_case.iloc[i]+50, s=weekly_case.iloc[i])
# plt.axhline(weekly_mean, color="red", linestyle=":")
#
# plt.show()

## 월가 주를 함께 그룹화하여 빈도수 구하고 시각화 하기
## value_counts는 시리즈에서만 사용 가능, 데이터프레임에서는 불가능 그래서 그룹바이 사용

# month_week_case = df.groupby(["월", "주"])["연번"].count()
# # print(month_week_case)
#
# month_week_case.plot.bar(title = "Monthly + Weekly Seoul Covid19", figsize=(16, 7), rot=30)
# plt.show()

## 확진자가 발생하지 않은 날도 포함하여 시각화
# print(day_count)
# print(df.iloc[-1])  # 리스트의 맨 첫번째 날짜 전체 정보
# print(df.iloc[-1, 7])   # 리스트의 맨 마지막 날짜의 날짜 정보(7행)
first_day = df.iloc[-1, 7]

# print(df.iloc[0])  # 리스트의 맨 마지막 날짜 전체 정보
last_day = df.iloc[0, 7]

days = pd.date_range(first_day, last_day)
# print(days)   # 시리즈 형태
# print(pd.DataFrame({"확진일자" : days}))    # 데이터프레임 형태
df_days = pd.DataFrame({"확진일자" : days})

daily_case = df["확진일자"].value_counts()   # 확진일자별 빈도수
df_daily_case = pd.DataFrame(daily_case)
df_daily_case.columns = ["확진수"]   # 컬럼명 바꾸기

all_day = df_days.merge(df_daily_case, left_on="확진일자", right_on=df_daily_case.index, how="left")
# print(all_day)

## 누적 확진자수 구하기
# accum_sum = all_day["확진수"].sum()   # 총 누적 확진수
# print(accum_sum)
# accum_sum = all_day["확진수"].fillna(0)  # NaN을 0으로 변경
# print(accum_sum)
# accum_sum = all_day["확진수"].fillna(0).cumsum()  # 누적해서 더해주기
# print(accum_sum)

all_day["누적확진"] = all_day["확진수"].fillna(0).cumsum()  # all_day 에 칼럼으로 추가하기
# print(all_day)

## 연도 제외하기
all_day["일자"] = all_day["확진일자"].astype(str).map(lambda x : x[-5:])
# print(all_day)

## 확진수, 누적확진 칼럼을 갖는 데이터프레임 만들기
cum_day = all_day[["일자", "확진수", "누적확진"]]
cum_day = cum_day.set_index("일자")
# print(cum_day)

# cum_day.plot(title = "Accumulated Seoul Covid19", figsize=(16, 7))
# plt.show()

## 시리즈로 2개 그래프 그리기

# cum_day["확진수"].plot.bar(figsize=(16, 7))
# cum_day["누적확진"].plot(figsize=(16, 7), rot=30)
# plt.show()

## 로그 스케일 적용하기
# np.log(cum_day["누적확진"]).plot(figsize=(16, 7))
# np.log(cum_day["확진수"]).plot.bar()
#
# plt.show()

## 확진월과 요일 구하기

# print(all_day["확진일자"].dt.month)
all_day["확진월"] = all_day["확진일자"].dt.month
all_day["확진요일"] =  all_day["확진일자"].dt.dayofweek    ## 0은 월요일
# print(all_day)

## 요일별 확진수 groupby로 구하기

# print(all_day.groupby(["확진월", "확진요일"])["확진수"].sum())  ## 월별 요일별 확진수에 대한 확진자 수

all_day_week = all_day.groupby(["확진월", "확진요일"])["확진수"].sum()
# print(all_day_week)
# print(all_day_week.index)
# print(all_day_week.unstack().astype(int))   ## 멀티인덱스의 마지막 값을 칼럼명으로 바꿔준다.
all_day_week = all_day_week.unstack().astype(int)
## split으로 요일을 문자로 바꿔주기
dayofweek = "월 화 수 목 금 토 일"
dayofweek = dayofweek.split()
all_day_week.columns = dayofweek
# print(all_day_week)
## style.background_gradient로 색상을 표현
new = all_day_week.style.background_gradient(cmap="Blues")
# print(new)

# all_day_week.plot.bar(title = "월별 요일별 Seoul Covid19", figsize=(16, 7), rot=0)
# plt.show()

## 거주지별 확진자
# print(df["거주지"].value_counts())
gu_count = df["거주지"].value_counts()
# gu_count.plot.barh(figsize=(10, 15))   ## 위에가 적은 순
# gu_count.sort_values().plot.barh(figsize=(10, 15))   ## 위에가 많은 순
# plt.show()

## 서울 구만 추출
# print(gu_count[0:27])   ## 상위권 지역 조회 (기타가 포함되어 있음)
gu_index = gu_count[0:27]
gu_index = gu_index.index.tolist()
gu_index.remove("기타")
gu_index.remove("타시도")
# print(gu_index)

## 거주지가 서울이 아닌 지역을 따로 추출
not_seoul = set(gu_count.index) - set(gu_index)
# print(not_seoul)

## reset_index로 데이터 프레임으로 변환
df_gu = gu_count.reset_index()
df_gu.columns = ["구", "확진수"]
# print(df_gu)

## 지역이라는 새로운 칼럼을 만들어 서울이 아닌 타지역 값을 넣어주기
# print(df_gu[df_gu["구"].isin(gu_index)])  ## 서울 지역만 보기
# print(df_gu[~df_gu["구"].isin(gu_index)])  ## 서울 외 지역만 보기(물결 표시)

# print(df[df["거주지"].isin(gu_index)])
# print(df.loc[df["거주지"].isin(gu_index)])
df.loc[df["거주지"].isin(gu_index), "지역"] = df["거주지"]
# print(df)
df["지역"] = df["지역"].fillna("타지역")
# print(df)
# print(df["지역"].unique())
# df["지역"].value_counts().plot.barh()
# plt.show()


## 접촉력 분석
## 접촉력 빈도수
# print(df["접촉력"].value_counts().head(20))

## 접촉력 유니크
# print(df["접촉력"].unique())

##확인이 들어가 있는 접촉력만 찾기
# print(df[df["접촉력"].str.contains("확인")])
# print(df.loc[df["접촉력"].str.contains("확인"), "접촉력"].unique())

##확인중을 확인 중으로 변경
df.loc[df["접촉력"].str.contains("확인"), "접촉력"] = "확인 중"
# print(df.loc[df["접촉력"].str.contains("확인"), "접촉력"].unique())
# print(df["접촉력"].value_counts())

## 접촉력 빈도수 시각화
contact_count = df["접촉력"].value_counts()
contact_count_top = contact_count.sort_values().tail(30)
# contact_count_top.plot.barh(figsize=(15, 7))
# plt.show()

## 상위 15개만 구하기
top_contact = contact_count_top.tail(15)
## 접촉력 빈도수가 높은 목록에 대한 index 값 구하기
top_contact.index
##위에서 구한 top_contact에 해당하는 데이터만 isin으로 가져오기
# print(df[df["접촉력"].isin(top_contact.index)])
top_group = df[df["접촉력"].isin(top_contact.index)]
## 접촉력, 월별 빈도수를 groupby로 구하기
# top_group.groupby(["접촉력", "월"])["연번"].count()
result = top_group.groupby(["접촉력", "월"])["연번"].count().unstack().fillna(0).astype(int)
# print(result)

## 이태원이 들어간 접촉력 보기
# print(df[df["접촉력"].str.contains("이태원")])
## 이태원 + 6월 접촉력 보기
# print(df[df["접촉력"].str.contains("이태원") & (df["월"]==6)])   ## 두번째 조건은 괄호로 묶어준다.

## 감염경로 불명.. 접촉력이 확인중인 데이터만 구하기
# print(df[df["접촉력"].str.contains("확인")])
# print(df[df["접촉력"] == "확인 중"])
df_unknown = df[df["접촉력"] == "확인 중"]
unknown_weekly_case = df_unknown.groupby(["월", "주"])["연번"].count()
# print(unknown_weekly_case)
# unknown_weekly_case.plot.bar(figsize=(15,7))
# plt.show()

## 다시 주별 전체 확진수 데이터 프레임으로 구하기
# all_weekly_case = df["주"].value_counts()
all_weekly_case = df["주"].value_counts().to_frame()
all_weekly_case.columns = ["전체확진수"]
# print(all_weekly_case)

## 주별 확인중 데이터 구하기
# print(df_unknown["주"])
unknown_weekly_case2 = df_unknown["주"].value_counts().to_frame()
unknown_weekly_case2.columns = ["불명확진수"]

## 전체와 확인중 데이터 비교
unknown_case = all_weekly_case.merge(unknown_weekly_case2, left_index=True, right_index=True)
# print(unknown_case)
unknown_case = unknown_case.sort_index()
# print(unknown_case)
# unknown_case.plot(figsize=(15, 4))
# plt.show()

## 감염경로 확인중의 주별 비율 구하기
unknown_case["불명비율"] = unknown_case["불명확진수"]/unknown_case["전체확진수"]*100
# print(unknown_case)
unknown_case["불명비율"].plot.bar(figsize=(15, 4))
plt.show()









