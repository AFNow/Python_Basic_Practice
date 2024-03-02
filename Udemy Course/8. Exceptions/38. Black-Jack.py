player_chips = 50 # Банк фишек у игрока
player_bet = 0 # Текущая ставка
def black_jack():
    print ('Начало игры black-jack,')
    # Основные переменные:
    game = True # Статус игры
    suits = ('♠','♥','♦','♣')
    ranks = ('Двойка','Тройка','Четверка','Пятерка','Шестерка','Семерка','Восьмерка','Девятка','Десятка','Jack','Queen','King','Ace')
    #values = {'Двойка':2,'Тройка':3,'Четверка':4,'Пятерка':5,'Шестерка':6,'Семерка':7,'Восьмерка':8,'Девятка':9,'Десятка':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

    class Deck: # pool Хранит в себе весь список из 52 карт, а также перемешивает их. 
            def __init__(self): # Вся пачка из 52 карт
                self.deck = [] 
                for suit in suits:
                    for rank in ranks:
                        self.deck.append(Card(suit,rank))

            def __str__(self): # Текстовое описание всей деки, список из всех карт в ней.
                deck_comparison = ''
                for card in self.deck:
                    deck_comparison += '\n' + card.__str__()
                return 'В колоде:' + deck_comparison
            
            def shuffle(self): # Метод перемешивания колоды
                import random
                random.shuffle(self.deck)

    class Card: # Класс только единичной карты, формирует ранг и масть
                def __init__(self,suit,rank): # При запуске класса Card создаются функции масти и ранга карты, которые используются в классе Deck
                    self.suit = suit
                    self.rank = rank
                
                def __str__(self): # Текстовое описание карты
                    return self.rank  +' '+ self.suit

    class Hand: # player_arm
            def __init__(self, pool):
                self.hand1 = [] # Изначально пустая первая рука игрока
                #self.hand2 = [] - заготовка для игры со сплитом
                self.pool = pool # Временное хранилище взятой карты
                self.value = 0 # Значение карт в руке
                self.values = {'Двойка':2,'Тройка':3,'Четверка':4,'Пятерка':5,'Шестерка':6,'Семерка':7,'Восьмерка':8,'Девятка':9,'Десятка':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
            
            def __str__(self): # Описание карт для отображения в меню
                return 'Мои карты: ' + ', '.join(str(card) for card in self.hand1)
            
            def cards(self): # Отладка - проверка карт в руке без лишних символов
                    print (self.hand1)

            def cards2(self): # Отладка - проверка карт в руке без лишних символов
                    print (self.hand2)

            def player_pass(self): # Извлечение первой карты из общей колоды и перенесение в руку
                card = self.pool.deck.pop(0)
                self.hand1.append(card)

            def calculate_card_value(self): # Подсчет суммарного значения карт в руке
                for card in self.hand1:
                    if card.rank in self.values:
                        self.value += self.values[card.rank]
                        if card.rank == 'Туз' and self.value > 21:
                            self.value -= 10
                    
    class Dealer:# dealer_arm
            def __init__(self, pool): 
                self.hand = []  # Изначально пустая рука дилера
                self.pool = pool # Временное хранилище взятой карты
                self.value = 0 # Значение карт в руке
                self.values = {'Двойка':2,'Тройка':3,'Четверка':4,'Пятерка':5,'Шестерка':6,'Семерка':7,'Восьмерка':8,'Девятка':9,'Десятка':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
            
            def __str__(self): # Показать все карты дилера
                return f"Карты дилера: {self.hand[0]}, XX" # {self.hand[1]
            
            def cards(self): # Отладка - проверка карт в руке без лишних символов
                    print ("Карты дилера: ", self.hand[0], self.hand[1])

            def dealer_pass(self): # Извлекаем первую карту из колоды
                card = self.pool.deck.pop(0)
                self.hand.append(card)  # Добавляем извлеченную карту в руку игрока
            
            def calculate_card_value(self): # Подсчет суммарного значения карт в руке
                for card in self.hand:
                    if card.rank in self.values:
                        self.value += self.values[card.rank]
                        if card.rank == 'Туз' and self.value > 21:
                            self.value -= 10

    def bet(): # Ставка игрока и начало игры
        global player_chips
        global player_bet
        while True:
                try:
                    value = input('введите ставку:')
                    if value.isdigit():
                        player_bet = int(value)
                        if player_bet <= player_chips:
                            print ('Ставка принята')
                            player_chips = player_chips - player_bet
                            print (f"Остаток в банке: {player_chips}")
                            gameplay()
                            break
                        else:
                            print (f"Ставка должна быть меньше имеющегося состояния в {player_chips} фишек")
                            continue
                    else:
                        print('Это не число,')
                        continue
                except ValueError:
                    print('Это не число,')
                    player_bet = int(input('введите ставку:'))
                    continue

    def gameplay():
        def first_cards(): # Первая раздача карт
            global player_chips
            global player_bet
            pool = Deck() # Указание значения для класса
            pool.shuffle() # Перемешивание карт
            player_arm = Hand(pool) # Создание объекта Hand с переданным доступом к pool
            dealer_arm = Dealer(pool) # Создание объекта Hand с переданным доступом к pool
            player_arm.player_pass() 
            dealer_arm.dealer_pass()
            player_arm.player_pass()
            dealer_arm.dealer_pass()
            print (player_arm)
            player_arm.calculate_card_value()
            print (dealer_arm)
            dealer_arm.calculate_card_value()
            #print (player_arm.value) # Отладка
            #print (dealer_arm.value)  # Отладка
            
            if dealer_arm.value == player_arm.value: # Условие PUSH (Ничья)
                print ('Очки равны, PUSH')
                print ('Ничья')
                player_chips += player_bet
                print (f"Остаток в банке: {player_chips}")
                try:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
                    else:
                        print ('Игра окончена')
                except TypeError:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()

            elif player_arm.value == 21: # Условие BlackJack
                print ('Победа, Black-Jack')
                print (f"Куш равен: {player_bet*1.5}")
                player_chips += player_bet * 1.5
                print (f"Остаток в банке: {player_chips}")
                try:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
                    else:
                        print ('Игра окончена')
                except TypeError:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
            else:
                next_card(player_arm, dealer_arm)

        def check(player_arm, dealer_arm): #Проверка значений карт у дилера и игрока
            if player_arm.value < dealer_arm.value:
                #print (player_arm.value) # Отладка
                #print (dealer_arm.value)  # Отладка
                print('Раскрываем карты')
                print (player_arm)
                dealer_arm.cards()
                print('Проигрыш, ставка потеряна')
                print (f"Остаток в банке: {player_chips}")
                try:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
                    else:
                        print ('Игра окончена')
                except TypeError:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
            elif player_arm.value >  dealer_arm.value and player_arm.value < 21:
                #print (player_arm.value) # Отладка
                #print (dealer_arm.value)  # Отладка
                print('Раскрываем карты')
                print (player_arm)
                dealer_arm.cards()
                print ('Выигрыш')
                try:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
                    else:
                        print ('Игра окончена')
                except TypeError:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
            elif player_arm.value >= 22: # Условие > 21 - BUST
                #print (player_arm.value) # Отладка
                #print (dealer_arm.value)  # Отладка
                print (player_arm)
                dealer_arm.cards()
                print ('Проигрыш, BUST')
                print (f"Остаток в банке: {player_chips}")
                try:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
                    else:
                        print ('Игра окончена')
                except TypeError:
                    answer = str(input('Продолжить? Да/Нет '))
                    if answer == str('Да'):
                        bet()
            else:
                next_card(player_arm, dealer_arm)

            #print (dealer_arm.value)
            #dealer_arm.cards() # Отладка - печать всех карт дилера
            #player_arm.cards() # Отладка - печать всех карт игрока
            #print(pool) # Отладка - печать всего пула карт
        
        def next_card(player_arm, dealer_arm): # Вторая раздача
            global player_chips
            answer = str(input('Взять карту? Да/Нет '))
            if answer == str('Да'):
                player_arm.player_pass()
                player_arm.calculate_card_value()
                dealer_arm.calculate_card_value()
                #print (player_arm.value) # Отладка
                #print (dealer_arm.value)  # Отладка
                check(player_arm,dealer_arm)
                if dealer_arm.value < 17:
                    dealer_arm.dealer_pass()
                    dealer_arm.calculate_card_value()
                    print(dealer_arm)
                    #print (player_arm.value) # Отладка
                    #print (dealer_arm.value)  # Отладка
                else:
                    pass
            elif answer == str('Нет'):
                if player_arm.value < dealer_arm.value:
                    print('Раскрываем карты')
                    print(player_arm)
                    dealer_arm.cards()
                    #print (player_arm.value) # Отладка
                    #print (dealer_arm.value)  # Отладка
                    print('Проигрыш, ставка потеряна')
                    print (f"Остаток в банке: {player_chips}")
                    answer = str(input('Новая ставка? '))
                    if answer == 'Да':
                        bet()
                else:
                    check(player_arm, dealer_arm)
            elif player_arm.value > dealer_arm.value:
                player_arm.calculate_card_value()
                dealer_arm.calculate_card_value()
                #print (player_arm.value) # Отладка
                #print (dealer_arm.value)  # Отладка
                check(player_arm,dealer_arm)
            else:
                if player_arm.value < dealer_arm.value:
                    print('Раскрываем карты')
                    print(player_arm)
                    dealer_arm.cards()
                    #print (player_arm.value) # Отладка
                    #print (dealer_arm.value)  # Отладка
                    print('Проигрыш, ставка потеряна')
                    print (f"Остаток в банке: {player_chips}")
                    answer = str(input('Новая ставка? '))
                    if answer == 'Да':
                        bet()
        first_cards()
             
    bet()
black_jack()
# Рандомный пул из 52 карт с 4 мастями и вариантами из 2, 3, 4, 5, 6, 7, 8, 9, Jack, Jueen, King, Ace -----
# Скрипт ставки на новую игру ----
# После ставки начинается игра, в ходе которой раздаются по 2 карты, обоим сторонам, но у дилера открыта только одна карта. ----
# Если у игрока 21 - победа с кушем в 3к2, если меньше 21, то предлагается взять карту. ----
# Если у игрока наберется более 21, то игра окончена (bust). ----
# Если у игрока две одинаковые по достоинству карты, можно сделать сплит и играть в две руки.
# Если у игрока суммарно 10 или 11, то можно удвоить ставку, но взять только одну карту. 
# Если у дилера менее 17 очков, то он берет третью карту. ------
# Если у дилера открыта 10 или 11, то вторая карта проверяется и при наличии 21 игра окончится с проигрышем ставки. ----
