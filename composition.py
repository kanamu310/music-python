import random

def composition():
    f = open('music.txt','w')
    f.write(str(random.randint(0,1000)))
    f.close()
    f = open('music.txt','a')
    f.write(',')
    f.close()
    
    for i in range(31) :
        f = open('music.txt','a')
        f.write(str(random.randint(0,1000)))
        f.write(',')

    f.close()

if __name__ == "__main__" :
    composition()
