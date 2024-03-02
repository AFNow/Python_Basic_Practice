board = ['0','1','2','3','4','5','6','7','8','9']
def x_or_o():
    slotted = []
    player1 = ''
    player2 = ''
    step = 0 # Если равно 0 игра окончена
    def marker_selection(): # выбор маркера игрока
        nonlocal player1
        nonlocal player2
        marker = ''
        while marker != 'x' and marker != 'o':
            marker = input('1й игрок - выберите символ x или о: ')
        player1 = marker
        if player1 == 'x':
            player2 = 'o'
        else:
            player2 = 'x'
    marker_selection()
    print(f"1й игрок: {player1}, 2й игрок: {player2}")
    print (step)
    def board_print(): # распечатка игрового поля
        print (board[7]+' | '+board[8]+' | '+board[9])
        print (board[4]+' | '+board[5]+' | '+board[6])
        print (board[1]+' | '+board[2]+' | '+board[3])
        print (step)
    board_print()
    def winner_check():
        nonlocal step
        # pl1 rows
        if (board[1] == board[2] == board[3] == player1) or (board[4] == board[5] == board[6] == player1) or (board[7] == board[8] == board[9] == player1):
                step = -2
                print('Победа за ',player1)
                return player1 
        # pl1 columns
        elif (board[1] == board[4] == board[7] == player1) or (board[2] == board[5] == board[8] == player1) or (board[3] == board[6] == board[9] == player1):
                step = -2
                print('Победа за ',player1)
                return player1 
        # pl1 slashes
        elif (board[1] == board[5] == board[9] == player1) or (board[7] == board[5] == board[3] == player1):
                step = -2
                print('Победа за ',player1)
                return player1 
        # pl2 rows
        if (board[1] == board[2] == board[3] == player2) or (board[4] == board[5] == board[6] == player2) or (board[7] == board[8] == board[9] == player2):
                step = -2
                print('Победа за ',player2)
                return player2
        # pl2 columns
        elif (board[1] == board[4] == board[7] == player2) or (board[2] == board[5] == board[8] == player2) or (board[3] == board[6] == board[9] == player2):
                step = -2
                print('Победа за ',player2)
                return player2
        # pl2 slashes
        elif (board[1] == board[5] == board[9] == player2) or (board[7] == board[5] == board[3] == player2):
                step = -2
                print('Победа за ',player2)
                return player2
        elif step  == 9:
                step = -2
                print('Ничья')
    def order(): # порядок хода и запись занятых ячеек
        nonlocal slotted 
        nonlocal step
        while step >= 0:
            number = int(input('Введите ячейку: '))
            if number not in slotted:
                if step %2 == 0: # Ход второго игрока
                    step += 1
                    board[number] = player1
                    board_print()
                    winner_check()
                else:
                    step += 1
                    board[number] = player2 # Ход первого игрока
                    board_print()
                    winner_check()
                slotted.append (number)
            else:
                print ('Ячейка занята')
                step -= 1
        else:
            print ('Игра окончена')
    order()
x_or_o()


#Отобразить доску (игровое поле).----

#Получить ввод от игрока. ----

#Поместить этот ввод на доске. ---

#Проверить, получился ли в игре выигрыш, проигрыш, ничья, или игра продолжается.-----

#Повторить шаги 3 и 4 до тех пор, пока не получим выигрыш или ничью.-----
