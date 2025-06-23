class chaild:
    def __init__(self,name,age):
        self._name =name
        self._age =age
    @property
    def name(self):
     return self._name

    @name.setter
    def name(self,value):
        self._name = value


r =chaild("or" ,15)
print(r.name)
r.name = "mark" 
print(r.name)




class dogs():
   def __init__(self,numofdogs,listname):
      self._num = numofdogs
      self._list = listname
   @property
   def num(self):
      return self._num
   
   @num.setter
   def num (self,num2):
      self._num =num2

listname =["oo","dd","omer"]
num=10
r = dogs(num,listname)
print(r.num)

r.num ="oriya"  
print(r.num)


   



class Person():
   def __init__(self,name,lastname):
      self._name =name
      self._lastname =lastname
   def __str__(self):
      return "your name is " + self._name +" and your last name is "+ self._lastname
   def GetAll(self):
      print("name  is " + self._name ,"last name is " , self._lastname) 
      
   
oriya = Person("oriya","rabani")
print(oriya)

oriya.GetAll()


listname = [ "david" ,"nataly" ,"yhaly","oriya"]
for item in listname:
   print("hello" , item)