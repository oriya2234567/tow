


class child():
     def __init__(self ,name ,age):
         self.name = name
         self.__age = age

     def print2(self):   
        print(self.name)


def say():
    print("tel")


def decorator(func):
    def wrap():
        print("macabi")
        func()
        print("aviv")
    return wrap

me = decorator(say)
me()



class Person:
    def __init__(self, name):
        self._name = name  # שמרנו במשתנה "פרטי" בשם _name

    @property
    def name(self):
        print("קוראים למשתנה name")
        return self._name
    
    @name.setter
    def name(self,value):
        self._name =value

p = Person("אוריה")
print(p.name)
p.name = "oriya"
print(p.name)





