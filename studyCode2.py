import requests

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