import multiprocessing
import time


def sing(num,name):
    for i in range(num):
        print(name)
        print('singing...')
        time.sleep(0.5)


def dance(num,name):
    for i in range(num):
        print(name)
        print('dancing...')
        time.sleep(0.5)


if __name__ == '__main__':
    sing_pro = multiprocessing.Process(target=sing, args=(3, 'xnmk'))
    dance_pro = multiprocessing.Process(target=dance, kwargs={'name':'xnhs','num': 2})
    sing_pro.start()
    dance_pro.start()
