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

## 타겟 국가 정보만 가져오기
target = 'Sweden'         ## 'Republic of Korea
columns = ['Date_reported', 'Country', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']
target_df = df.loc[df["Country"] == target, columns]
# print(target_df)
target_df = target_df.set_index('Date_reported')
# print(target_df)

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
# new_case_df = target_df[['Cumulative_deaths']]
# print(new_case_df)
# new_case_df.plot(title = target, figsize=(20,5))
# plt.show()


## 타겟 지역 정보만 가져오기
target_area = 'EURO'              ### EURO (유럽), WPRO(극동아시아)   AMRO (북남미), EMRO (중동) SEARO (중앙아시아) , WPRO(호주 등)
columns1 = ['Date_reported', 'Country', 'New_cases', 'Cumulative_cases', 'New_deaths', 'Cumulative_deaths']
target_df1 = df.loc[df["WHO_region"] == target_area, columns1]
# print(target_df1)
target_df1 = target_df1.set_index('Date_reported')
# print(target_df1)

## 신규 확진자
case_df1 = target_df1[['New_cases']].sort_index()
# print(case_df1)
case_df1.plot(title = target_area, figsize=(20,5))
plt.show()

## 누적 확진자
case_df1 = target_df1[['Cumulative_cases']].sort_index()
# print(case_df1)
case_df1.plot(title = target_area, figsize=(20,5))
plt.show()