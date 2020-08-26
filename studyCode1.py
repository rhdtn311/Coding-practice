# 딕셔너리와 함수를 이용하여 기본값에 대해 배웠다.
# 기본값이 있는 파라미터와 기본값이 없는 파라미터의 경우 기본값이 없는 함수가 순서 상 기본값이 있는 함수 앞에 위치해야한다.
# 기본값을 이용하여 인수값을 조건으로 사용하는 법을 배웠다.
# is, in, not in 을 사용하는 법을 배웠다.

my_english_dict = {}

def add_to_dict(dic = {}, key = "", value = "") :
    if type(dic) is not dict: 
        print("You need to send a dictionary. You sent : <class 'str'>")
    elif value is ""  :
        print("You need to send a word and a definition.")
    elif key in dic.keys() : 
        print(f"{key} is already on the dictionary. Won't add.")
    else :
        dic[key] = value
        print(f"{key} has been added")

def get_from_dict(dic = {}, key = "") : 
    if type(dic) is not dict : 
        print("You need to send a dictionary. You sent : < class 'str'> " )
    elif key is "" :
        print("You need to send a word to search for.")
    elif key not in dic.keys() : 
        print(f"{key} was not found in this dict.")
    else :
        print(f"{key} :" + dic[key])

def update_word(dic = {}, key = "", value = "") : 
    if type(dic) is not dict : 
        print("You need to send a dictionary. You sent : <class 'str'>")
    elif value is "" : 
        print("You need to send a word and a definition to update.")
    elif key not in dic.keys() : 
        print(f"{key} is not on the dict. Can't update non-existing word.")
    else : 
        dic[key] = value
        print(f"{key} has been updated to : " + value)

def delete_from_dict(dic = {}, key = "") :
    if type(dic) is not dict :
        print("You need to send a dictionary. You sent : <class 'str'>")
    elif key is "" : 
        print("You need to specify a word to delete.")
    elif key not in dic.keys() :
        print("{0} is not in this dict. Won't delete.".format(key))
    else :
        del dic[key] 
        print("{0} has been deleted.".format(key))