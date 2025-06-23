def BigNUm(number):
    max = number[0]
    for i in range(len(number)):
        if number[i] > max:
            max = number[i]
    return max

list2 = [1,532,12,35,1]
print(BigNUm(list2))


def Evennumber(list3):
    list4 =[]
    for i in range(len(list3)):
        if list3[i] % 2 == 0:
            list4.append(list3[i])
    return list4

num =[2,4,9,4,6,8,12,24,39,5]
print(Evennumber(num))


def sortlist(number2):
    for i in range(len(number2)-1):
        if(number2[i]>number2[i+1]):
            return False
    return True

listt =[1,2,30,4,5,67,30]
print(sortlist(listt))


def revars2 (string2):
  string2= string2[-1::-1]
  return string2

string3 ="hello world!"
print(revars2(string3))

def count2(string3):
    count1 =0
    for char in string3:
        if "a" in char or "e" in char or "i" in char or "o" in char or "u" in char:
            count1 =count1 + 1
    return count1

str2 ="abcaaaa"
print(count2(str2))



def palindrom(string4):
   length2 = len(string4)-1
   for chars in string4:
       if chars != string4[length2]:
           return False
       length2 =length2 -1
   return True

 
chars2 ="abca"
print(palindrom(chars2))


def findLongestword(list11):
    maxletter =0
    maxletter2 =0
    count3 =0
    max1 = []
    for item in list11:
        
        for i in range(len(item)):
            maxletter = maxletter +1  
        if maxletter >= maxletter2:
            maxletter2= maxletter
        maxletter=0
            
            
        
    for item2 in list11:
        for ch in range(len(item2)):
            count3 =count3+1
        if count3 == maxletter2:
            max1.append(item2)
        count3 = 0
    return max1


list33 = ["bdd","a","dddddd","ae","2222222222","1222222222"]
print(findLongestword(list33))

def findpolindrom(lis):
    lis22 =[]
    for item in lis:
        if palindrom(item)==True:
            lis22.append(item)
    return lis22




lis34 = ["radar","apple","level","banana","stats","noon"]
print(findpolindrom(lis34))


print(10%16)
