# На входе список чисел, вернуть True если массив где-либо содержит рядом стоящие 3 и 3
def has_33(n):
    for item in range(0,len(n)-1):
        if n[item] == 3 and n[item+1] == 3:
            print ('True')
            return True
    print ('False')
    return False
n = [3,11,3,3,11,1,3,3]
has_33(n)


# has_33 ([1,3,3])
# has_33 ([1,3,1,3])
# has_33 ([3,1,3])