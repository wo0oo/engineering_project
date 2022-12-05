import requests
#res = requests.get("http://naver.com")
res = requests.get("https://www.lost112.go.kr/")
res.raise_for_status() #문제가 있으면 바로 종료 문제 없으면 진행
print("응답코드 :", res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else:
#     print("문제가 생겼습니다. [에러코드 ",res.status_code,"]")

print(len(res.text)) #홈페이지의 글자 수
print(res.text)

#파일로 만들기
with open("mylost112.html","w",encoding="utf8") as f:
    f.write(res.text)    