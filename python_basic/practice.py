### 제목 ###
## 설명

### 숫자 자료형 ###
# print(5) 
# print(-10)
# print(3.14)
# print(100000000000)
# print(5+3)
# print(2*8)
# print(3*(3+1))


### 문자형 ###
# print('풍선')
# print("나비")
# print("ㅋ"*9)


### boolean ###
## 참과 거짓
# print(5>10)
# print(5<10)
# print(not True)

### 변수 ###
## 애완동물을 소개해 주세요
## 변수는 값을 저장하는 것
# animal = "강아지"
# name = "이름"
# age = 4
# hobby = "walk alone near by park"
# is_adult = age >= 3

# print("우리집 "+ animal + "의 "+name+"은 뭘까요")
# # 정수형을 print 할 때 str로 감싸 줘야 한다
# print("이거 이름을 한글로 치려니까 불편하네"+str(age))
# # , 를 이용해서 붙일 수 있고 이럴때는 str로 바꿔줄 필요가 없다/ 그리고 , 는 한칸 띄우는걸 포함한다
# print("이거 이름을 한글로 치려니까 불편하네",(age))
# # boolean 형태도 print 할 때 str 로 감싸 줘야 한다
# print("이름 부분을 바꿔야 한다면?" +str(is_adult))
# print("My hobby is "+hobby)

### Quiz 1 ###

# station = "사당"
# print(station,"행 열차가 들어오고 있습니다")
# station = "신도림"
# print(station+"행 열차가 들어오고 있습니다")

### 연산자 ###

# print(1+1)
# print(6/4)

# print(2**3)# 2^3
# print(5%3) #5mod3
# print(5//3) #몫
# print(5/3)

# print(3==3)
# print(4==2)

# print(1 != 3)
# print(not(1 != 3))

# print ((3>0)and (3<5))
# print((3>0)&(3<5))
# print((3>0) or (3>5))
# print((3>0)|(3>5))
# print(5>4>3)
# print(5>4>6)

### 간단한 수식 ###

# print(2 + 3 *4)
# print((2 + 3)* 4)
# number = 2+3*4
# print(number)
# number += 2
# print(number)

### 숫자 처리 함수 ###

##절댓값 abs
##제곱 pow
##최댓값 max
# print(abs(-5))
# print(pow(4,2))
# print(max(5, 12))
# print(min(5, 12))
# print(round(3.14))##반올림

# from math import *
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))

### 랜덤함수 ###

# from random import *

# print(random())# 0.0 ~ 1.0 미만의 임의의 값 생성
# print(random() * 10)
# print((int)(random() * 10))#0~9
# print(int(random()*10+1))#1~10

# print(int(random() * 45) +1)

# print(randrange(1, 46)) # 1~45

# print(randint(1,45)) # 1~45

### Quiz 2 ###

# from random import *

# num = randint(4,28)

# print("오프라인 스터디 모임 날짜는 매월 "+str(num)+"일로 선정 되었습니다")

### 문자열 ###

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "python is EZ"
# print(sentence2)
# sentence3 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence3)

### 슬라이싱 ###

# jumin = "990123-1234567"

# print("sex : "+jumin[7])
# print("yr : "+jumin[0:2])
# print("month : "+jumin[2:4])
# print("day : "+jumin[4:6])

# print("birth : " + jumin[:6]) #처음 부터 5 까지
# print("back 7th : "+jumin[7:])
# print("backward 6th : "+jumin[-6:])

### 문자열 처리 함수 ###

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index +1)
# print(index)

# print(python.find("n"))
# print(python.find("Java")) ## find 에서 원하는 값이 없으면 -1 반환
# #print(python.index("Java")) ## index 에서는 에러로 반환

# print(python.count("n"))

### 문자열 포멧 ###

# print("a" + "b")
# print("a","b")

# print("i am %d years old" %20)
# print("i am %s like"%"python")
# print("Apple is start with %c" %"A")
# # %s 는 전부 다 소화 가능

# print("i love %s and %s" %("blue","red"))

# print("i am {} yrs old" .format(20))

# print("i love {} and {}" .format("blue","red"))
# print("i love {1} and {0}" .format("blue","red"))

# print("i am {age} yrs old and i love {color}" .format(age = 20, color = "red"))

# # python 3.6 
# age = 20
# color = "red"
# print(f"i am {age} yrs old and i love {color}")

### 탈출 문자 ###

# print("백문이 불여일견 \n 백견이 불여일타")
# print("i am \"nado coding\" hello")
# print("C:\\users\\inwon")
# print("Red Apple\rPine")
# print("Redd\bApple")
# print("red\tApple")

### quiz 2 ###

# st = "http://naver.com"
# print(st[-9:])
# print(st[-9:-4])
# print(st[-9:-6]+str(len(st[-9:-4]))+str(st.count("e"))+"!")

# st = st.replace("http://","")
# print(st)
# st = st[:st.index(".")]
# print(st)

### List ###

# subway = [10, 20, 30]
# print(subway)

# subway = ["yu", "jo", "park"]
# print(subway)

# print(subway.index("jo"))

# subway.append("haha")
# print(subway)

# subway.insert(1,"jung")
# print(subway)

# subway.pop()
# print(subway)

# subway.append("yu")
# print(subway)
# print(subway.count("yu"))

# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# num_list.reverse()
# print(num_list)

# num_list.clear()
# print(num_list)

# mix_list = ["jo", 10, True]
# print(mix_list)

# num_list.extend(mix_list)
# print(num_list)

### dictionary ###

# cabinet = {3:"yu", 100:"inwon"}
# print(cabinet[3]) 
# print(cabinet[100])

# print(cabinet.get(3))
# print(cabinet.get(5))
# print(cabinet.get(5, "사용가능"))

# print(3 in cabinet)
# print(5 in cabinet)

# cabinet = {"A-3":"yu", "B-100":"inwon"}
# print(cabinet["A-3"])

# print(cabinet)
# cabinet["A-3"] = "subin"
# cabinet["C-20"] = "jo"
# print(cabinet)

# del cabinet["A-3"]
# print(cabinet)

# print(cabinet.keys())
# print(cabinet.values())

# print(cabinet.items())

# cabinet.clear()
# print(cabinet)

### tuple ###

## 값 추가 변경 불가능

# menu = ("don", "chi")
# print(menu[0])
# print(menu[1])

#menu.add("seng")

# name = "kim"
# age = 20
# hobby = "coding"
# print(name, age, hobby)

# (name, age, hobby) = ("kim", 20, "coding")
# print(name, age, hobby)

### set ###

## 중복이 안되고 순서가 없다

# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"yu", "kim", "yang"}
# python = set(["yu", "park"])

# print(java & python)
# print(java.intersection(python))

# print(java | python)
# print(java.union(python))

# print(java - python)
# print(java.difference(python))

# python.add("kim")
# print(python)

# java.remove("kim")
# print(java)

### 자료구조의 변경 ###

# menu = {"coffe", "milk", "juice"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

### quiz 4 ###

# from random import *
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

# id_lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(id_lst)
# print("chicken : "+str(sample(id_lst,1)))
# print("coffee : "+str(sample(id_lst,3)))

# users = range(1,21)
# users = list(users)

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users, 4)

# print("chi : {0}".format(winners[0]))
# print("coffe : {0}".format(winners[1:]))

### if ###

# weather = input("how is the weather today?")

# if weather == "rain" or weather == "snow":
#     print("take your umbrella")
# elif weather == "mm":
#     print("take your masks")
# else:
#     print("take nothing")

# temp = int(input("how is the temp today?"))
# if 30 <= temp:
#     print("it's too hot")
# elif 10 <= temp and temp < 30:
#     print("it's good")
# elif 0 <= temp and temp < 10:
#     print("take your coat")
# else:
#     print("it's too cold")

### for ###

# for waiting_no in [0,1,2,3,4]:
#     print("waiting : {0}".format(waiting_no))

# for waiting_no in range(5): #0,1,2,3,4
#     print("waiting : {}".format(waiting_no))

# for waiting_no in range(1,6): #1,2,3,4,5
#     print("waiting : {}".format(waiting_no))

# starbucks = {"ironmen", "thor", "groot"}
# for customer in starbucks:
#     print("{0}, ready for your coffee".format(customer))

### while ###

# customer = "thor"
# index = 5
# while index >=1:
#     print("{0},cust ready for your coffee. {1} remain".format(customer,index))
#     index -= 1
#     if index == 0:
#         print("coffee is gone")

# customer = "ironmen"
# index = 1
# while True:
#     print("{0}, coffee is ready, calling {1}".format(customer,index))
#     index+=1

# customer = "thor"
# person = "Unknown"

# while person != customer:
#     print("{0}, coffee is ready".format(customer))
#     person = input("what's your name?")

### continue, break ###

# absent = [2,5]
# no_book = [7]
# for student in range(1, 11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print("today class is over. {0} follow me".format(no_book))
#         break
#     print("{0}, read the book plz".format(student))

### 1 line for ###

# students = [1,2,3,4,5]
# print(students)
# students = [i+100 for i in students]
# print(students)

# students = ["ironman", "thor", "groot"]
# students = [len(i) for i in students]
# print(students)

### Quiz 5 ###
# from random import *

# customer = [randint(5,51) for i in range(50)]
# print(customer)
# index = 1
# co = 0
# for i in customer:
#     if i <= 15:
#         print("[O] {0} customer (spend time : {1})".format(index,i))
#         co+=1
#     else:
#         print("[ ] {0} customer (spend time : {1})".format(index,i))
#     index += 1
# print("total cust : {0} person".format(co))

# from random import *
# cnt = 0
# for i in range(1, 51):
#     time = randrange(5, 51) # 5~ 50
#     if 5 <= time <= 15:
#         print("[0] {0} customer (spend time : {1})".format(i, time))
#         cnt+=1
#     else:
#         print("[ ] {0} customer (spend time : {1})".format(i, time))
# print("total : {0}".format(cnt))

### Function ###

# def open_account():
#     print("new account making")

# open_account()

### 전달값과 반환값 ###

# def deposit(balance, money):
#     print("입금 완료 : 잔액은 {0} 입니다".format(balance+money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금 완료 : 잔액은 {0} 입니다".format(balance-money))
#         return balance - money
#     else:
#         print("출금 불가 : 잔액은 {0} 입니다".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance-money-commission ## tuple 형식으로 반환

# balance = 0
# balance = deposit(balance, 1000)
# print(balance)
# balance = withdraw(balance, 500)
# print(balance)
# commission, balance = withdraw_night(balance, 500)
# print("commision {0}, remaining {1}".format(commission, balance))

### 기본값 ###

# def profile(name, age, main_lang):
#     print("name : {0}\tage : {1}\tmain lang : {2}" \
#         .format(name,age,main_lang))

# profile("you", 20, "python")
# profile("kim", 25, "java")

# def profile(name, age=17, main_lang="python"):
#     print("name : {0}\tage : {1}\tmain lang : {2}" \
#         .format(name,age,main_lang))

# profile("you")
# profile("kim")

### 키워드 값 ###

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "you", main_lang= "python", age = 20)

### 가변 인자 ###

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     ## end = " " ==> 줄바꿈 하지 않음
#     print("name : {0}\tage : {1}\t".format(name,age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     ## end = " " ==> 줄바꿈 하지 않음
#     print("name : {0}\tage : {1}\t".format(name,age), end = " ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("you", 20, "python", "java", "c", "c++", "c#", "javascript")
# profile("kim", 25, "kotlin", "swift")

### 지역변수와 전역변수 ###

# gun = 10

# def checkpoint(soldiers): #경계근무
#     global gun # 전역 공간에 있는 gun 사용
#     gun = gun - soldiers
#     print("remain : {0}".format(gun))

# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("remain : {0}".format(gun))
#     return gun

# print("totla gun : {0}".format(gun))
# gun = checkpoint_ret(gun, 2)
# print("remain gun : {0}".format(gun))

### quiz 6 ###

# def std_weight(height, gender):
#     if gender == 1:
#         return height*height*22/10000
#     else:
#         return height*height*21/10000
    

# stdw = std_weight(175,1)
# stdw = round(stdw,2)
# print("height is {0} std_weight is {1}".format(175, stdw))

### 표준 입출력 ###

# print("python", "java", sep=",", end="?")
# print("funny?")

# import sys
# print("python", "java", file=sys.stdout)
# print("python", "java", file=sys.stderr)

# scores = {"math":0, "english":50, "coding":100}
# for subject, score in scores.items():
#     # print(subject, score)
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for num in range(1, 21):
#     print("waiting num : " + str(num).zfill(3))

# answer = input("input anything : ")
# print(type(answer))
# print("input value is " + answer + "..")

### 다양한 출력 포멧 ###

# print("{0: >10}".format(500))

# print("{0: >+10}".format(500))
# print("{0: >+10}".format(-500))

# print("{0:_<10}".format(500))

# print("{0:,}".format(100000000000))

# print("{0:+,}".format(-1000000000000))

# print("{0:^<+30,}".format(1000000000000))

# print("{0:f}".format(5/3))

# print("{0:.2f}".format(5/3))

### 파일 입출력 ###

# score_file = open("score.txt", "w", encoding="utf8")
# print("math : 0", file=score_file)
# print("english : 50", file=score_file)
# score_file.close()

# score_file = open("score.txt", "a", encoding="utf8")
# score_file.write("science : 80")
# score_file.write("\ncoding : 100")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt","r", encoding="utf8")
# print(score_file.readline(), end="")
# print(score_file.readline(), end = "")
# print(score_file.readline(), end = "") 
# print(score_file.readline(), end = "")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# while True:
#     line = score_file.readline()
#     if not line :
#         break
#     print(line, end="")
# score_file.close()

# score_file = open("score.txt", "r", encoding="utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end = "")
# score_file.close()

### pickle ###

# import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"name":"park", "age":30, "hobby":["soccer","golf","coding"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile 에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

### with ###

# import pickle

# with open("profile.pickle","rb") as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt","w",encoding = "utf8") as study_file:
#     study_file.write("hi my name is H")

# with open("study.txt","r",encoding = "utf8") as study_file:
#     print(study_file.read())

### quiz 7 ###

# for i in range(1,51):
#     name = "./test_file/"+str(i)+"주차"
#     with open(name, "w", encoding = "utf8") as study_file:
#         tmp = str(i) + "주차 주간보고\n부서 :\n이름 :\n업무 요약 :"
#         study_file.write(tmp)

### class ###

# #marin
# name = "marin"
# hp = 40
# damage = 5

# print("{} unit is made".format(name))
# print("hp {0}, attack {1}\n".format(hp,damage))

# #tank
# tank_name = "tank"
# tank_hp = 150
# tank_damage = 35

# tank2_name = "tank2"
# tank2_hp = 150
# tank2_damage = 35

# print("{} unit made".format(tank_name))
# print("hp {0}, attack {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격. [공격력 {2}]".format(name, location, damage))

# attack(name, "1", damage)
# attack(tank_name, "1", tank_damage)
# attack(tank2_name, "1", tank2_damage)

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.damage = damage
#         self.hp = hp
#         print("{0} unit is making".format(self.name))
#         print("hp {0}, attack {1}".format(self.hp, self.damage))

# marin1 = Unit("marin", 40, 5)
# marin2 = Unit("marin", 40, 5)
# tank = Unit("tank", 150, 35)

### __init__ ###

### 멤버변수 ###

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.damage = damage
#         self.hp = hp
#         print("{0} unit is making".format(self.name))
#         print("hp {0}, attack {1}".format(self.hp, self.damage))

# #레이스
# wraith1 = Unit("wraith", 80, 5)
# print("unit name : {0}, attack : {1}".format(wraith1.name, wraith1.damage))

# #mind control
# wraith2 = Unit("wraith2", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태 입니다".format(wraith2.name))

### method ###

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.damage = damage
#         self.hp = hp
#         print("{0} unit is making".format(self.name))
#         print("hp {0}, attack {1}".format(self.hp, self.damage))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat = AttackUnit("firebat",50,16)
# firebat.attack("5시")

# firebat.damaged(25)
# firebat.damaged(25)

### 상속 ###

# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         #self.damage = damage
#         self.hp = hp
#         #print("{0} unit is making".format(self.name))
#         #print("hp {0}, attack {1}".format(self.hp, self.damage))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         #self.name = name
#         #self.hp = hp
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# firebat = AttackUnit("firebat",50,16)
# firebat.attack("5시")

# firebat.damaged(25)
# firebat.damaged(25)

### 다중 상속 ###

# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         #self.damage = damage
#         self.hp = hp
#         #print("{0} unit is making".format(self.name))
#         #print("hp {0}, attack {1}".format(self.hp, self.damage))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         #self.name = name
#         #self.hp = hp
#         Unit.__init__(self, name, hp)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, damage)
#         Flyable.__init__(self, flying_speed)

# valkyrie = FlyableAttackUnit("valkyrie", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

### 연산자 오버로딩 ###

# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         #self.damage = damage
#         self.hp = hp
#         self.speed = speed
#         #print("{0} unit is making".format(self.name))
#         #print("hp {0}, attack {1}".format(self.hp, self.damage))
#     def move(self, location):
#         print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))

# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         #self.name = name
#         #self.hp = hp
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1}입니다.".format(self.name, self.hp))
#         if self.hp<=0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))

# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) ##지상 스피드 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# vulture = AttackUnit("벌쳐", 80, 10, 20)

# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# #battlecruiser.fly("배틀크루저","9시")
# battlecruiser.move("9시")

### pass ###

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass

# supply_depot = BuildingUnit("서플라이", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

### super ###

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         #Unit.__init__(self,name, hp, 0)
#         super().__init__(name,hp,0)
#         self.location = location

### starcraft ###
#일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))

#     def move(self, location):
#         # print("[지상 유닛 이동]")
#         print("{0} : {1} 방향으로 이동합니다. [speed {2}]".format(self.name, location, self.speed))

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#         self.hp -= damage
#         print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#         if self.hp <= 0:
#             print("{0} : 파괴되었습니다.".format(self.name))

# #공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage

#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
#             .format(self.name, location, self.damage))
            
#     # def damaged(self, damage):
#     #     print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
#     #     self.hp -= damage
#     #     print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
#     #     if self.hp <= 0:
#     #         print("{0} : 파괴되었습니다.".format(self.name))

# #마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "marine", 40, 1, 5)

#     #stimpack
#     def stimpack(self):
#         if self.hp>10:
#             self.hp -= 10
#             print("{0} : 스팀팩을 사용합니다. (HP 10 감소)".format(self.name))
#         else:
#             print("{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))
    
# #tank
# class Tank(AttackUnit):
#     #siege mode
#     seize_developed = False

#     def __init__(self):
#         AttackUnit.__init__(self, "tank", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return
        
#         if self.seize_mode == False:
#             print("{0} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True
#         else:
#             print("{0} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False

# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]".format(name, location, self.flying_speed))


# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage)
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         # print("[공중 유닛 이동]")
#         self.fly(self.name, location)

# class Wraith(FlyableAttackUnit):
    
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "wraith",80, 20, 5)
#         self.clocked = False
    
#     def clocking(self):
#         if self.clocked == True:
#             print("{0} : 클로킹 모드를 해제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{0} : 클로킹 모드를 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다")

# game_start()

# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# t1 = Tank()
# t2 = Tank()

# w1 = Wraith()

# #유닛 일괄 관리
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# for unit in attack_units:
#     unit.move("1시")

# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료 되었습니다")

# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# for unit in attack_units:
#     unit.attack("1시")

# from random import *

# for unit in attack_units:
#     unit.damaged(randint(5, 21))

# game_over()

### quiz 8 ###

# class House:
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year
    
#     def show_detail(self):
#         print(self.location, self.house_type, self.deal_type\
#             , self.price, self.completion_year)

# print("총 3대의 매물이 있습니다")
# h1 = House("강남","아파트","매매","10억","2010년")
# h1.show_detail()

### 예외처리 ###

# try:
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요 :")))
#     nums.append(int(input("두 번째 숫자를 입력하세요 :")))
#     #nums.append(int(nums[0] / nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except ValueError:
#     print("에러! 잘못된 값을 입력!!")
# except ZeroDivisionError as err:
#     print(err)
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다")
#     print(err)

### 에러 발생시키기 ###
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 :"))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise ValueError
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")

### 사용자 정의 예외처리
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 :"))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("warning!! {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)

### finally ###
# class BigNumberError(Exception):
#     def __init__(self, msg):
#         self.msg = msg

#     def __str__(self):
#         return self.msg

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요 :"))
#     num2 = int(input("두 번째 숫자를 입력하세요 :"))
#     if num1 >= 10 or num2 >= 10:
#         raise BigNumberError("warning!! {0}, {1}".format(num1, num2))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
# except ValueError:
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.")
# except BigNumberError as err:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요.")
#     print(err)
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.")

### 퀴즈 9 ###

# class SoldOutError(Exception):
#     def __init__(self, msg):
#         self.msg = msg
#     def __str__(self):
#         return self.msg

# chicken = 10
# waiting = 1
# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇마리 주문하시겠습니까?"))
#         if order<1:
#             raise ValueError
#         if chicken <= 0:
#             raise SoldOutError("No chicken left")
#         if order > chicken:
#             print("재료가 부족합니다.")
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다."\
#                 .format(waiting, order))
#             waiting += 1
#             chicken -= order
#     except ValueError:
#         print("1이상의 값을 입력해 주세요")
#     except SoldOutError as err:
#         print(err)
#         break

### module ###
# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv
# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price,price_morning
# price(5)
# price_morning(5)

# from theater_module import price_soldier as ps
# ps(5)

### 패키지 ###
# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

### __all__ ###
# from travel import *
# #trip_to = vietnam.VietnamPackage()
# trip_to = thailand.ThailandPackage()
# trip_to.detail()

### 패키지 모듈 위치 ###
# import inspect
# import random
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

### pip install ###
#pypi 홈페이지에 모듈이 많음

# from bs4 import BeautifulSoup
# soup = BeautifulSoup("<p>Some<b>bad<i>HTML")
# print(soup.prettify())

### 내장 함수 ###
# language = input("무슨 언어를 좋아하세요?")
# print("{0}은 아주 좋은 언어입니다".format(language))

# print(dir())
#import random # 외장함수
# print(dir())
# import pickle
# print(dir())

#print(dir(random))
# lst = [1,2,3]
# print(dir(lst))

### 외장 함수 ###

#glob : 경로 내의 폴더/ 파일 목록 조회

# import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능

# import os
# print(os.getcwd())

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더 입니다")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다")
# else:
#     os.makedirs(folder)
#     print(folder, "폴더를 생성하였습니다")

# print(os.listdir())

# import time
# print(time.localtime())
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# import datetime
# print("오늘 날짜는 ", datetime.date.today())

# today = datetime.date.today()
# td = datetime.timedelta(days=100)
# print("우리가 만난지 100일은", today + td)

### 퀴즈 10 ###
# import byme as b
# b.sign()