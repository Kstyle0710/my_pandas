## WHO 데이터를 파일 다운로드 없이 사이트 링크로 바로 가져오기

import urllib.request

# source = urllib.request.urlopen('https://covid19.who.int/WHO-COVID-19-global-data.csv').readlines()
# print(source[:10])


from urllib.request import urlretrieve
url = 'https://covid19.who.int/WHO-COVID-19-global-data.csv'

urlretrieve(url, './data/WHO-COVID-19-global-data.csv')