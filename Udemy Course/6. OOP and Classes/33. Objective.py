# Создайте класс банковского счета, который имеет атрибуты:
# owner - владелец
# balance - баланс
# и два метода:
# deposit - внести седства
# withdraw - снять средства
# Сумма снятия не должна превышать доступный баланс
class Account:
    def __init__(self, owner, value):
        self.owner = owner
        self.value = value
    
    def __str__(self):
        return f"{self.owner}: {self.value}"
    
    def get_owner(self):
        return f"Владелец счета: {self.owner}"

    def add_funds(self, amount):
        self.value += amount
        print (self.value)

    def withdraw (self,amount):
        if self.value > amount:
            self.value -= amount
            print (self.value)
        else:
            print("На счете недостаточно средств")

    def get_balance(self):
        return f"На счете доступно: {self.value}"

account1 = Account ('Владислав', 100)
print(account1) #Данные владельца
print(account1.get_owner())
print(account1.get_balance()) #Общий баланс
account1.add_funds(50) #Ввод 50
account1.withdraw(75) #Вывод 75
account1.withdraw(500) #На счете недостаточно средств