def flip_a_coin(n):# *Эмуляция подбрасывания монеты** - Напишите программу, которая эмулирует подбрасывание одной монеты столько раз, сколько решит пользователь. Подсчитайте, сколько раз выпали орёл и решка.
    import random
    count = 0
    heads = 0
    tails = 0
    while count < n:
        flip = random.randint(1,2)
        count += 1
        if flip % 2 == 0:
            heads += 1
        else:
            tails += 1
    print (f"Выпало {heads} орлов и {tails} решек")
flip_a_coin(10000)