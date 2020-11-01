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

## 국가 종류 식별하기
country = df["Country"].unique()
# print(country)

'''
['Afghanistan' 'Albania' 'Algeria' 'American Samoa' 'Andorra' 'Angola'
 'Anguilla' 'Antigua and Barbuda' 'Argentina' 'Armenia' 'Aruba'
 'Australia' 'Austria' 'Azerbaijan' 'Bahamas' 'Bahrain' 'Bangladesh'
 'Barbados' 'Belarus' 'Belgium' 'Belize' 'Benin' 'Bermuda' 'Bhutan'
 'Bolivia (Plurinational State of)' 'Bonaire, Sint Eustatius and Saba'
 'Bosnia and Herzegovina' 'Botswana' 'Brazil' 'British Virgin Islands'
 'Brunei Darussalam' 'Bulgaria' 'Burkina Faso' 'Burundi' 'Cabo Verde'
 'Cambodia' 'Cameroon' 'Canada' 'Cayman Islands'
 'Central African Republic' 'Chad' 'Chile' 'China' 'Colombia' 'Comoros'
 'Congo' 'Cook Islands' 'Costa Rica' 'Côte d’Ivoire' 'Croatia' 'Cuba'
 'Curaçao' 'Cyprus' 'Czechia' "Democratic People's Republic of Korea"
 'Democratic Republic of the Congo' 'Denmark' 'Djibouti' 'Dominica'
 'Dominican Republic' 'Ecuador' 'Egypt' 'El Salvador' 'Equatorial Guinea'
 'Eritrea' 'Estonia' 'Eswatini' 'Ethiopia' 'Falkland Islands (Malvinas)'
 'Faroe Islands' 'Fiji' 'Finland' 'France' 'French Guiana'
 'French Polynesia' 'Gabon' 'Gambia' 'Georgia' 'Germany' 'Ghana'
 'Gibraltar' 'Greece' 'Greenland' 'Grenada' 'Guadeloupe' 'Guam'
 'Guatemala' 'Guernsey' 'Guinea' 'Guinea-Bissau' 'Guyana' 'Haiti'
 'Holy See' 'Honduras' 'Hungary' 'Iceland' 'India' 'Indonesia'
 'Iran (Islamic Republic of)' 'Iraq' 'Ireland' 'Isle of Man' 'Israel'
 'Italy' 'Jamaica' 'Japan' 'Jersey' 'Jordan' 'Kazakhstan' 'Kenya'
 'Kiribati' 'Kosovo[1]' 'Kuwait' 'Kyrgyzstan'
 "Lao People's Democratic Republic" 'Latvia' 'Lebanon' 'Lesotho' 'Liberia'
 'Libya' 'Liechtenstein' 'Lithuania' 'Luxembourg' 'Madagascar' 'Malawi'
 'Malaysia' 'Maldives' 'Mali' 'Malta' 'Marshall Islands' 'Martinique'
 'Mauritania' 'Mauritius' 'Mayotte' 'Mexico'
 'Micronesia (Federated States of)' 'Monaco' 'Mongolia' 'Montenegro'
 'Montserrat' 'Morocco' 'Mozambique' 'Myanmar' 'Namibia' 'Nauru' 'Nepal'
 'Netherlands' 'New Caledonia' 'New Zealand' 'Nicaragua' 'Niger' 'Nigeria'
 'Niue' 'North Macedonia' 'Northern Mariana Islands (Commonwealth of the)'
 'Norway' 'occupied Palestinian territory, including east Jerusalem'
 'Oman' 'Other' 'Pakistan' 'Palau' 'Panama' 'Papua New Guinea' 'Paraguay'
 'Peru' 'Philippines' 'Pitcairn Islands' 'Poland' 'Portugal' 'Puerto Rico'
 'Qatar' 'Republic of Korea' 'Republic of Moldova' 'Réunion' 'Romania'
 'Russian Federation' 'Rwanda' 'Saint Barthélemy' 'Saint Helena'
 'Saint Kitts and Nevis' 'Saint Lucia' 'Saint Martin'
 'Saint Pierre and Miquelon' 'Saint Vincent and the Grenadines' 'Samoa'
 'San Marino' 'Sao Tome and Principe' 'Saudi Arabia' 'Senegal' 'Serbia'
 'Seychelles' 'Sierra Leone' 'Singapore' 'Sint Maarten' 'Slovakia'
 'Slovenia' 'Solomon Islands' 'Somalia' 'South Africa' 'South Sudan'
 'Spain' 'Sri Lanka' 'Sudan' 'Suriname' 'Sweden' 'Switzerland'
 'Syrian Arab Republic' 'Tajikistan' 'Thailand' 'The United Kingdom'
 'Timor-Leste' 'Togo' 'Tokelau' 'Tonga' 'Trinidad and Tobago' 'Tunisia'
 'Turkey' 'Turkmenistan' 'Turks and Caicos Islands' 'Tuvalu' 'Uganda'
 'Ukraine' 'United Arab Emirates' 'United Republic of Tanzania'
 'United States of America' 'United States Virgin Islands' 'Uruguay'
 'Uzbekistan' 'Vanuatu' 'Venezuela (Bolivarian Republic of)' 'Viet Nam'
 'Wallis and Futuna' 'Yemen' 'Zambia' 'Zimbabwe']

'''

## 검토 대상 설정
target = 'Republic of Korea'         ## 'Republic of Korea'  Germany    Sweden   France   Saudi Arabia   Japan   China  Brazil   India   United States of America
columns = ['Date_reported', 'Country', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']   ## 출력 대상 칼럼
target_df = df.loc[df["Country"] == target, columns]
print(target_df.tail())
# date_list = df.values.tolist()
# print(date_list)
# print(target_df)
target_df = target_df.set_index('Date_reported')
# print(target_df)


review_target = 'New_cases'
# review_target = 'Cumulative_cases'
# review_target = 'New_deaths'
# review_target = 'Cumulative_deaths'

start_point = -100   ## 최종에서 역으로 00일치


## 검토
case_df = target_df[review_target].sort_index()
# print(case_df.mean())



mean1= case_df[start_point:].mean()
# print(mean1)   ## 0명 포함 평균
for_mean_df = case_df[case_df > 0]
# print(for_mean_df)
mean2 = for_mean_df[start_point:].mean()  # 지정구간 평균값 구하기 (0값 제외후)
mean3 = for_mean_df.mean()  # 전체구간 평균값 구하기 (0값 제외후)
print("국가별 평균값(0제외) : {} / {}".format(mean2, target))   ## 0명 제외 평균


## 시각화 분석
g = case_df[start_point:].plot(title = "{0} ({1}) - 구간평균 : {2}, 총평균 : {3}".format(target,review_target, int(mean2), int(mean3)), figsize=(15,8))

if start_point == 0:
    for i in range(len(case_df)):
        case_count = case_df[start_point:].iloc[i]
        if case_count > mean2:
            g.text(x=i, y=case_count, s=case_count)
else:
    for i in range(start_point*-1):
        case_count = case_df[start_point:].iloc[i]
        if case_count > mean2:
            g.text(x=i, y=case_count, s=case_count)

plt.axhline(mean2, color="red", linestyle=":")
plt.axhline(mean3, color="blue", linestyle=":")
plt.show()

