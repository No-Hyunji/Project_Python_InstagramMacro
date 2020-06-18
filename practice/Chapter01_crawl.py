# Chapter01_crawl.py
#  * requests로 크롤링하는 부분을 모듈화 하고,
#  * inport해서 사용하는 코드
#  *
from libs.crawler import crawl

# 수집하고 싶은 인스타그램의 #해스태그 페이지 URL 주소
url = 'https://www.instagram.com/explore/tags/%ED%88%AC%ED%94%BC%EC%97%A0/'

pageString = crawl(url)
print(pageString)