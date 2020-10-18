import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


## 파일 읽어오기
df = pd.read_csv('./data/WHO-COVID-19-global-data.csv')
# print(df.shape)
# print(df.info())
# print(df.head())

plt.rc("font", family="Malgun Gothic")
## 숫자 마이너스 값 깨짐 현장 해결
plt.rc("axes", unicode_minus=False)
plt.style.use("fivethirtyeight")


## 칼럼명의 공란 지우기
df.columns = df.columns.str.replace(' ', '')

## 국가 종류 식별하기
country = df["Country"].unique()
# print(country)

## 타겟 국가 정보만 가져오기
target = 'Republic of Korea'
columns = ['Date_reported', 'Country', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']
target_df = df.loc[df["Country"] == target, columns]
# print(target_df)
target_df = target_df.set_index('Date_reported')
print(target_df)

## 신규 확진자
# new_case_df = target_df[['New_cases']]
# print(new_case_df)
# new_case_df.plot(title = target, figsize=(20,5))
# plt.show()

## 누적 확진자
# new_case_df = target_df[['Cumulative_cases']]
# print(new_case_df)
# new_case_df.plot(title = target, figsize=(20,5))
# plt.show()

## 신규 사망자
# new_case_df = target_df[['New_deaths']]
# print(new_case_df)
# new_case_df.plot(title = target, figsize=(20,5))
# plt.show()

## 누적 사망자
new_case_df = target_df[['Cumulative_deaths']]
print(new_case_df)
new_case_df.plot(title = target, figsize=(20,5))
plt.show()