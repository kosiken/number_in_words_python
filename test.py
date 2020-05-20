from time import sleep
from to_words import name_long_number

n = 0
while True:

    print(name_long_number(n))
    sleep(2)
    n+=1
