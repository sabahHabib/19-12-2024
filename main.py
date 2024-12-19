from datetime import date
class Person:
    def __init__(self,name,country,date_of_birth):
        self.name=name
        self.country=country
        self.date_of_birth=date_of_birth
    def calculate_age(self):
        today=date.today()
        age=today.year-self.date_of_birth.year
        if (today.month ,today.day)<(self.date_of_birth.month,self.date_of_birth.day):
            age-=1
        return age

person1=Person("Emma","US",date(1999,5,15))
age=person1.calculate_age()
print(f"Name is:{person1.name} from {person1.country} is {age} years old.")

from abc import ABC ,abstractmethod
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        return "Bark"
class Cat(Animal):
    def sound(self):
        return "Meow"
a1=Dog()
print(a1.sound())
a2=Cat()
print(a2.sound())

class Employee(ABC):
    @abstractmethod
    def work(self):
        pass
class Designer(Employee):
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        return "Draw"
class SoftwareEngineer(Employee):
    def work(self):
        return "Code"
e1=Designer("Emma",30,15000)
e2=SoftwareEngineer()
print(f"{e1.name},{e1.age},{e1.salary},{e1.work()}")

class Student:
    def __init__(self,name,age,subject):
        self.name=name
        self.age=age
        self.__subject=subject
    def set_subject(self,subject):
        self.__subject=subject

    def get_subject(self):
        return self.__subject

s1=Student("abc",16,"Math")
print("subject is",s1.get_subject())


#Polymorphism
#Polymorphism with Methods(overloading)
class Dog():
    def speak(self):
        return "Woof"

class Cat():
    def speak(self):
        return "Meow"
animals=[Dog(),Cat()]
for animal in animals:
    print(animal.speak())

# encapsulation
class BankAccount:
    def __init__(self,account_holder,balance=0):
        self.__account_holder=account_holder
        self.__balance=balance
    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount
            return f"Amount deposit ${amount} new balance is:{self.__balance}"
        return "Invalid deposit"
    def withdraw(self,amount):
        if amount>0 and self.__balance>=amount:
            self.__balance-=amount
            return f"Amount withdraw ${amount} remaining balance is:{self.__balance}"
        return "insufficient balance"
    def get_balance(self):
        return f"Account holder is:{self.__account_holder} balance is:{self.__balance}"


account=BankAccount("john",500)
print(account.deposit(500))
print(account.withdraw(500))
print(account.get_balance())










