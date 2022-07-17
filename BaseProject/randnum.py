import random
import string

words = ['A','C','D','F','G','H','Q','R','S','T','V','W','X','Y']

for i in range(100):

    first = random.randint(0,9)
    sec = random.randint(0,9)
    w = random.choice(words)
    thir = random.randint(0,9)
    four = random.randint(0,9)

    if first != 4 and sec != 4 and thir != 4:
        
        print('第'+str(i+1)+'个'+' '+str(first) + str(sec) + str(w) + str(thir) + str(6))
