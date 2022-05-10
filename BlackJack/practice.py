# pop -wyciąga z listy
# shuffle - tasowanie
# metoda - funkcja w klasie
# metody statyczne  -> @staticmethod - nie potrzebuje self
# metoda specjalna __str__  / zamienia na str, wywołu się  przy str(barbara)
# metoda specjalna __repr__ / do np listy obiektów, pozwala je wyświetlać
# metoda specjalna __eq__ / 
# enkapsulacja/metoda prywatna !!! def _promote() !!! (można je używać w klasie) --> gentelmeńska umowa
# wyjątki -> obsługa zdarzenia, które wiąże się z błędem, wyświetla tekst zamiast crashowania ekranu
# dziedziczenie -> super wskazuje na klasę z której się dziedziczy, dane sie nie duplikują
# własne typy wyjątków !


class Person:
    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name=last_name

    def say_hello(self):
        print(f'Hi I am {self.first_name} {self.last_name}')




class Student(Person):
    def __init__(self,first_name,last_name,semester):
        super().__init__(first_name,last_name)
        self.semester=semester

    def promote(self):
        self.semester+=1

    
    def __str__(self):
        return f'My name is {self.first_name} and I am a student'

    def __repr__(self):
        return f'Student#{self.first_name}'

    def __eq__(self, other):
        return all([self.first_name==other.first_name,self.semester==other.semester])


class Worker(Person):
    def __init__(self,first_name,last_name,hour_rate):
        super().__init__(first_name,last_name)
        self.hour_rate=hour_rate
        self.time=0



    def register_time(self,time):
        self.time+=time

    def get_paid(self):
        time=self.time
        self.time=0
        return time*self.hour_rate



# ------------------------------
john = Student('John','Fifi',1)
john.say_hello()

barbara = Student('Barbara','Sisi',3)
barbara.promote()
barbara.say_hello()

print(barbara)

students = [barbara,john]
print(students)


baska = Student('Barbara','Sisi',4)
print(baska==barbara)

# -------------------------

adam = Worker('Adam','Kowalski',100)
print(adam.say_hello())
adam.register_time(10)
print(adam.get_paid())

#-------------------------

# Kompozycja: 

class Car:
    def __init__(self,brand,capacity):
        self.brand=brand
        self.engine=Engine(capacity) #!!!! 
    
class Engine:
    def __init__(self,capacity):
        self.capacity=capacity


car = Car('Chrysler',3.6)
print(car.engine.capacity)


# wyjątki / finally

a=input('Podaj lizcbe A: ')
b=input('Podaj lizcbe B: ')

try:
    result = int(a)/int(b)
    print(f'Wynik dzielenia {result}')
except ValueError:
    print('Błąd, nie podałeś prawidłowej liczby!')
except ZeroDivisionError:
    print(f'Błąd, podzieliłeś przez 0')
            
a=[]
b={}

try:
    print(a[3])
    print(b['dwa'])
except (KeyError,IndexError):
    print('Tala wartość nie istnieje!')

#******************************************

try:
    print("In try block")
    #raise ValueError
    #print("In try block 2")   #nie wykona się2
finally:
    print("In finally block") 
    # wykonuje się zawsze, dobrze mieć np czyszenie zasobów, czyszczenie plikow


# własne wyjątki

class InvalidSemestr(Exception):
    pass


class Studenciak:
    def __init__(self,first_name):
        self.first_name=first_name
        self.semestr=1

    def degrade(self):
        if self.semestr==1:
            raise InvalidSemestr('Student jest na 1 semestrze!')

        self.semestr-=1


try:
    antek = Studenciak('Anthony')
    antek.degrade()
    antek.degrade()
    print(antek.semestr)
except InvalidSemestr as exception:
    print(exception)