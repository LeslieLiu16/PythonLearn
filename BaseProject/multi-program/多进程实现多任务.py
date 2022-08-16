import multiprocessing
import time

def sing():
    for i in range(3):
        print('singing...')
        time.sleep(0.5)

def dance():
    for i in range(3):
        print('dancing...')
        time.sleep(0.5)  


if __name__ == '__main__':
    sing_pro = multiprocessing.Process(target=sing)
    dance_pro = multiprocessing.Process(target=dance)
    sing_pro.start()
    dance_pro.start()
