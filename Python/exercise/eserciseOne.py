# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 06:59:28 2017

@author: Isola
"""


#eserciseOne
def sum_three(x,y,z):
    return x+y+z


def ave_three(x,y,z):
    return sum_three(x,y,z)/3


def print_line(a = 20):
    print('——'*a)


def factorical():   #还可以加循环 能连续交互
    x = input("please input a unsign int number less than ten!\n")
    fac_x = 1
    try: 
        if  int(x) > 10 and int(x) < 0:
            print("number donot less than ten and more than zero.please try again!\n")
            fac_x = -1
        else:
            for a in range(1,int(x)+1):
                fac_x *= a
        return fac_x
    except ValueError:
        print("number in not int.please try again!\n")
        
          
#esercisetwo
def bekFile():
    esercise = open("..//python_day1_exercise.txt","rb")
    bek = open("..//bek.txt", "wb")
    
    try: 
        for line in esercise.readlines():
            #print(line)
            #print(type(line))
            bek.write(line) #.encode("utf-8")
            bek.write(b"\n")
    except IOError:
        print("Error: can\'t write file or read data\n")
    finally:
        esercise.close()
        bek.close()
        
        
#esercisethree
def inpt():
    #dataset = {'names':['H'],'class':['2'],'id':['3']} #可以实现  不过比较麻烦
    dataset = {'names':'','clas':'','numbers':''}
    #defaultCharacter = "-"
    xname = input("please input your name. \n")
    xclas = input("please input your class. \n")
    xnumber = input("please input your number. \n")
    if  len(xname)>1 and len(xname) <5:    #判断是不是多字符 
        dataset['names'] = xname
    else:
        print("name must be 2~4 characters. please try again!\n")
        return -1 #错误数据
        
    #不嵌套也可以  代码更清晰
    if len(xclas)>0 and len(xclas) <10:   #必须要有字符 也不能太多
        dataset['clas'] = xclas
    else:
        print("class must be 1~10 characters. please try again!\n")
        #clas.append(defaultCharacter)
        #number.append(defaultCharacter)
        return -1 #错误数据
    
    if len(xnumber)> 0 and len(xnumber) <15:
        dataset['numbers']  = xnumber
    else:
        print("number must be 1~15 characters. please try again!\n")
        #number.append(defaultCharacter)
        return -1
    #print(dataset)    
    return dataset  #传回数据集之后 进行存储


def record():
    #假设之前的数据集 是 
    dataSet = {'names':['Hs'],'clas':['2'],'numbers':['31']}
    newData = inpt()  #调方法给用户取数据
    while(newData == -1):
        print("user input error this times")
        newData = inpt() #调方法给用户取数据
    dataSet['names'].append(newData['names'])
    dataSet['clas'].append(newData['clas'])
    dataSet['numbers'].append(newData['numbers'])
    print(dataSet)
    

#eserciseFour
def login():
    id_x = "root"
    password = '123456'
    id_y = input("please input your id!\n")
    passy = input("please input your password!\n")
    if id_y == id_x and password == passy :
        print("wclcome to my world!\n")
        return 1
    else:
        print('incorrectness. please input again!\n')
        return 0
        
    
#eserciseFive
import re
def printstar():
    for x in range(5):
        print('*'*(5-x))
    for x in range(1,6):
        print('{:>5}'.format('*'*x))   #右对齐   五个字符  自动补空
    for x in range(1,6):
        sstr='*'*x
        pattern = re.compile('.{1,1}') # 拆成一个一个的字符
        ss = ' '.join(pattern.findall(sstr))  #每个字符由空格连起来
        print('{:^9}'.format(ss))  #中间对齐  9个字符  自动补空
        
             
#esercisesix
import random
def roshambo():
    while(True):
        x = random.randrange(1, 4)
        a = input('please input your number,0 signty rock,1 signty paper,2 signty scissors\n')
        if int(a)>0 and int(a)<4:
            if int(a) == x :
                print('Tie,one more time!\n')
            elif int(a) > x:
                print("Congratulations!you win!\n")
            else:
                print("Unfortunately,you lose,Next refueling!\n")
        else:
            print('Not naughty!\n')
            
            
#eserciseseven
def whoElse():
    users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0}
        }
    if 1 == login():
        print("now you can query record information!\n")
    else :
        print('give you three chances prove yourself\n ')
        for a in range(3):
            if 1 == login():
                print("now you can query record information!\n")
                break
            elif a == 2 :
                print('The destruction procedure has been started, the base explodes one minute later!\n')
            else:
                print("You have only %s chances" %(2-a))
                
    konw = input("what do you want to konw?\n")
    if konw in users:
        print(users[konw])
    else:
        print("There's no one you want to look for \n")
        
    
    
#eserciseeight

class StudentMageSys(object):
    stuCount = 0
    name = []
    numbers = []
    age = []
    datdeflt = "-"
    
    def __init__(self, name, number, age):
      self.name.append(name)
      self.numbers.append(number)
      self.age.append(age)
      StudentMageSys.stuCount += 1
      
    
    def count(self):
        return self.stuCount
    
    
    def add(self, name, number,age):
        self.name.append(name)          
        self.numbers.append(number)  #录入系统吧  就不自动加1了
        self.age.append(age)
        StudentMageSys.stuCount += 1
        return 
    
    
    def delName(self,name):
        if name in self.name:
            indx = self.name.index(name)
            self.name.remove(name)
            del self.numbers[indx]   #删除indx那条数据
            del self.age[indx]   #删除indx那条数据
            StudentMageSys.stuCount -= 1
            ret = 1
        else:
            ret = 0
        return ret
    
    
    def edit(self,name,number,age):
        if name in self.name:
            indx = self.name.index(name)
            if not len(number) == 0:
                self.numbers[indx] = number  #修改indx那条数据
            if not len(age) == 0:
                self.age[indx] = age  #修改indx那条数据
            print('edit success!')
            ret = 1  #成功
        else:
            print("There's no one you want to edit \n")
            ret = 0  # 失败
        return ret
    
    
    def query(self,name):
        if name in self.name:
            indx = self.name.index(name)
            print("Name : ", self.name[indx],  ", number: ", self.numbers[indx], ", age: ", self.age[indx])
        else:
            print("There's no one you want to look for \n")
        return 
    
    
    def quit(self):  #不明所以
        return
    
    
        
    