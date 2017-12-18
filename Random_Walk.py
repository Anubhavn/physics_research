import random

def calc_pi(n):
    counter = 0
    for i in range(n):
        x,y = random.random(),random.random()
        dist = abs(x-.5)**2+abs(y-.5)**2
        if dist<= 0.25:
            counter +=1
    print (4*counter/n)


for i in range (3):
    calc_pi(10000000)







