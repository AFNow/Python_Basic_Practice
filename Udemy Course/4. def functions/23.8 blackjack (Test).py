# На входе три числа от 1 до 11
# Если их сумма меньше или равна 21, то вернуть их сумму.
# Если сумма больше 21 и среди чисел присутствует 11, то уменьшить общую сумму на 10
# Если сумма, в том числе после уменьшения, равна 21, вернуть 'BUST'
def blackjack(nums):
    for item in nums:
        if sum(nums)-10 == 21:
            print('BUST')
            return ('BUST')
        elif 11 in nums:
            print (sum(nums)-10)
            return (sum(nums)-10)
        elif sum(nums) <= 21:
            print (sum(nums))
            return (sum(nums))
nums = (10,10,11)
blackjack(nums)


# blackjack(5,6,7) > 18
# blackjack(9,9,11) > 'BUST'
# blackjack(9,9,11) > 19