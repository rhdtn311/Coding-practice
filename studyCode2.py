import requests
# requests 모듈에 대해 알았다. (배우진 않았다.)
# while문의 활용
# strip() 의 사용법과 약간의 응용법을 터득했다.
# try, catch문을 활용했다.
# 반복문에 대해 조금은 더 안 것 같다.
# is 와 == 의 차이점에 대해 학습할 것이다. (is 는 객체가 같을 때 True, ==는 값이 같을 때 True)

# 훨씬 더 깔끔한 코드가 있다. if문과 함수를 적절히 잘 이용했다. 많이 배워야겠다.
import os
import requests

def restart():
  answer = str(input("Do you want to start over? y/n ")).lower()
  if answer == "y" or answer =="n":
    if answer == "n":
        print("k. bye!")
        return
    elif answer == "y":
      main()
  else:
    print("That's not a valid answer")
    restart()


def main():
  os.system('clear')
  print("Welcome to IsItDown.py!\nPlease write a URL or URLs you want to check. (separated by comma)")
  urls = str(input()).lower().split(",")
  for url in urls:
    url = url.strip()
    if "." not in url:
      print(url, "is not a valid URL.")
    else:
      if "http" not in url:
        url = f"http://{url}"
      try:
        request = requests.get(url)
        if request.status_code == 200:
          print(url,"is up!")
        else:
          print(url, "is down!")
      except:
          print(url, "is down!")
  restart()


main()