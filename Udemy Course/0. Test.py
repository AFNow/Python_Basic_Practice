
deck = ['Шестерка ♦', 'Queen♣']
values = {'Двойка':2,'Тройка':3,'Четверка':4,'Пятерка':5,'Шестерка':6,'Семерка':7,'Восьмерка':8,'Девятка':9,'Десятка':10,'Валет':10,'Queen':10,'Король':10,'Туз':11}
def calculate_card_value(card):
    for key, value in values.items():
        if key in card:
            return value
    return 0

total_value = sum(calculate_card_value(card) for card in deck)
print(f"Общая стоимость карт в колоде: {total_value}")

