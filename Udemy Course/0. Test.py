import time
def count1m (num):
    start = time.time()
    while num < 1_000_000_000:
        num += 1
    end = time.time()
    print (num)
    print (f"Время выполнения :{end - start}")
count1m (0)