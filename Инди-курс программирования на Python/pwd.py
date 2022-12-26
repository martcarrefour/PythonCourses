from string import printable
import time
timing = time.time()

pwd = '//dsa'
exitFlag = False

tic = time.perf_counter()
for b1 in printable:
    for b2 in printable:
        for b3 in printable:
            pwd_try = b1+b2+b3
            if pwd_try == pwd:
                print(f'Correct password is {pwd_try}')
                exitFlag = True

    if exitFlag:
        break

toc = time.perf_counter()
print(f"Вычисление заняло {toc - tic:0.4f} секунд")