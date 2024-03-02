# Наследование классов позволяет экономить силы при написании кода путем переноса операций из одного (в частности головного класса) в другой,
# что позволяет второму получать функции первого.
class Animal():# Класс при своем исполнении может исполнить три функции:
    def __init__(self):# Первая функция исполняется сразу при вызове класса
        print ("Animal was created")
    def who_am_i(self):
        print ("I'm an animal")
    def eat(self):
        print ("I'm eating")

class Dog(Animal):# Класс Dog ссылается на предыдущий класс Animal и получает его функции, но переписывает часть их под себя
    def __init__(self):
        Animal.__init__(self)# Функция вызывается сразу же при обращении к классу Dog
        print ("Dog was created")
    def who_am_i(self):# Функция переписывает значение, заимствованное из класса Animal
        print ("I'm a dog")
    def bark(self):# Новая функция, которая свойственна только классу Dog
        print("Woof!")
        
my_animal = Animal()
my_animal.who_am_i()
my_animal.eat()

my_dog = Dog()
my_dog.who_am_i()
my_dog.eat()
my_dog.bark()