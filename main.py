import os
import random as rd
os.system("cls")

class login:
  def __init__(self,email,password):
    self.email = email
    self.password = password
# check
def check_login(a:str,b:str)->bool:
  if a =="1234":
    if b =="quang0602":
      return True
    else : return False
  else:
    return False
  
def choose()->int:
  print("[1] . ADD A NEW CLASS ")
  print("[2] . CHECK CLASS")
  print("[3] . DELETE A CLASS")
  print("[0] . EXIT")
  a = int(input("Input your choice : "))
  while a<0 or a>3:
    print("ERROR")
    a = int(input("Input your choice : "))
  return a
# Add subject
class Subject:
  def __init__(self,thu,mon,phong,ma_phong):
    self.thu = thu
    self.mon = mon
    self.phong = phong
    self.ma_phong = ma_phong

def check_room(a:list,b:int)->bool:
    for i in a:
      if b==i:
        return True
    return False
def class_code()->str:
  a = ['1','2','3','4','5','6','7','8','9',
       'Q','E','R','T','Y','U','I','O','P',
       'A','S','D','F','G','H','J','K','L',
       'Z','X','C','V','B','N','M']
  code = ""
  for i in range(6):
    code = code + a[rd.randint(0,len(a))]
  return code
present = 0
# SUBJECT
def add_class() -> Subject:
  print("\t\t\tSUBJECT")
  print("[1] . PROGRAMMING TECHNIQUE")
  print("[2] . CALCULUS")
  print("[3] . PHILOSOPHY")
  print("[4] . COMPUTER ARCHITECT")
  choice = int(input("CHOOSE THE SUITABLE SUBJECT"))
  while choice <=0 or choice >4:
    print("ERROR")
    choice = int(input("CHOOSE THE SUITABLE SUBJECT"))
  subject = ""
  if choice==1:
    subject = "PROGRAMMING TECHNIQUE"
  elif choice==2:
    subject ="CALCULUS"
  elif choice==3:
    subject = "PHILOSOPHY"
  elif choice==4:
    subject = "COMPUTER ARCHITECT"
  #
  # TIME
  os.system("cls")
  time_table = ["MONDAY","TUESDAY","WEDNESDAY","THURSDAY","FRIDAY","SATURDAY"]
  for i in range(1,len(time_table)+1):
    print("[",i,"] . ",time_table[i-1])
  time = int(input("INPUT YOUR SUITABLE TIME : "))
  while time<=0 or time>=7:
    print("ERROR")
    time = int(input("INPUT YOUR SUITABLE TIME : "))


  # ROOM
  os.system("cls")
  print("SUITABLE ROOM LIST")
  room_list = []
  for i in  range(0,10):
    x = rd.randint(1,500)
    room_list.append(x)
    print(x)
  room = int(input("AVAILABLE ROOM : "))
  while check_room(room_list,room) == False:
    print("ERROR")
    room = int(input("AVAILABLE ROOM : "))

  # Class_code
  code = class_code()
  # DONE
  add_class = Subject(time_table[time-1],subject,room,code)
  return add_class


def output(a:list):
  for i in range(0,len(a)):
    print("Subject : ",a[i].mon)
    print("Date : ",a[i].thu)
    print("Class ID : ",a[i].ma_phong)
    print("Room : ",a[i].phong)

def delete_class(a:list):
  c = input("Input the code of your class you want to delete : ")
  for i in range(len(a)):
    if c==a[i].ma_phong:
      a.pop(i)
  
# main
os.system("cls")
user_email = input("Input your email : ")
user_password = input("Input your password : ")
while check_login(user_email,user_password) == False:
  print("Error")
  user_email = input("Input your email : ")
  user_password = input("Input your password : ")
user_obj = login(user_email,user_password)
os.system("cls")
print("========== SUCCESS =========")
a = []
while True:
  choice = choose()
  if choice==1:
    l = add_class()
    a.append(l)
  elif choice==2:
    print("AVAILABLE CLASS ")
    output(a)
  elif choice==3:
    delete_class(a)
    print("List after updated : ")
    output(a)
  elif choice==0:
    break
print("GOOD BYE")