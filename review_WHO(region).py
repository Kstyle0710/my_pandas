import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rc("font", family="Malgun Gothic")
## 숫자 마이너스 값 깨짐 현장 해결
plt.rc("axes", unicode_minus=False)
plt.style.use("fivethirtyeight")


## 파일 읽어오기
df = pd.read_csv('./data/WHO-COVID-19-global-data.csv')
# print(df.shape)
# print(df.info())
# print(df.head())

## 칼럼명의 공란 지우기
df.columns = df.columns.str.replace(' ', '')


## 검토 대상 설정
review_target = 'New_cases'
# review_target = 'Cumulative_cases'
# review_target = 'New_deaths'
# review_target = 'Cumulative_deaths'

start_point = -100   ## 최종에서 역으로 00일치


target_area = 'EURO'              ### EURO (유럽), WPRO(극동아시아)   AMRO (북남미), EMRO (중동) SEARO (중앙아시아) , WPRO(호주 등)
columns1 = ['Date_reported', 'Country', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']  ## 출력 대상 칼럼
target_df1 = df.loc[df["WHO_region"] == target_area, columns1]
# print(target_df1)
target_df1 = target_df1.set_index('Date_reported')
# print(target_df1)

## 검토
case_df1 = target_df1[review_target].sort_index()
mean3= case_df1[start_point:].mean()
# print(mean3)   ## 0명 포함 평균
for_mean_df1 = case_df1[case_df1 > 0]
mean4 = for_mean_df1[start_point:].mean()
print("지역별 평균값(0제외) : {} / {}".format(mean4, target_area, start_point*-1))   ## 0명 제외 평균


## 시각화 분석
g = case_df1[start_point:].plot(title = "{0} ({1}) - 평균값 : {2}".format(target_area,review_target, int(mean4)), figsize=(15,8))

if start_point == 0:
    for i in range(len(case_df1)):
        case_count = case_df1[start_point:].iloc[i]
        if case_count > mean4:
            g.text(x=i, y=case_count, s=case_count)
else:
    for i in range(start_point*-1):
        case_count = case_df1[start_point:].iloc[i]
        if case_count > mean4:
            g.text(x=i, y=case_count, s=case_count)

plt.axhline(mean4, color="red", linestyle=":")
plt.show()


