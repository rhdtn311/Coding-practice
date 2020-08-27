import requests
# requests 모듈에 대해 알았다. (배우진 않았다.)
# while문의 활용
# strip() 의 사용법과 약간의 응용법을 터득했다.
# try, catch문을 활용했다.
# 반복문에 대해 조금은 더 안 것 같다.
# is 와 == 의 차이점에 대해 학습할 것이다. (is 는 객체가 같을 때 True, ==는 값이 같을 때 True)
while True :
  urlResult = input("Please write a URL or URLs you want to check. (seperated by comma)\n").split(",") 

  starting = len(urlResult)

  for j in urlResult :
    j = j.strip()
    if j[-4:] != ".com" : 
      print("{} is not a valid answer.".format(j))
      starting = 0 
  
  while starting > 0 :
    for i in urlResult :  
      starting -= 1    
        
      i = i.strip()
      if i.lstrip("http://") == i : 
        i = "http://" + i.lstrip("http://") 
      try :      
        r = requests.get(i)  
        if r.status_code == 200 : 
          print("{} is up!".format(i))
        elif r.status_code != 200 : 
          print("{} is down!".format(i))  
      except : print("{} is down!".format(i))    

  count = 1
  while count > 0 :
    answer = input("Do you want start over ? y/n\n") 

    if answer == "y" : 
      count -= 1
    elif answer == "n" :
      print("Ok. Bye.")
      exit()
    else : 
      print("That's not a valid answer.")