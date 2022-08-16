import os
import multiprocessing
import time


def sing(num,name):
    print("唱歌进程的pid：",os.getpid())
    print("父进程的pid：",os.getppid())
    for i in range(num):
        print(name)
        print('singing...')
        time.sleep(0.5)


def dance(num,name):
    print("跳舞进程的pid：",os.getpid())
    for i in range(num):
        print(name)
        print('dancing...')
        time.sleep(0.5)


if __name__ == '__main__':
    print("主进程的pid:",os.getpid())
    sing_pro = multiprocessing.Process(target=sing, args=(3, '小明'))
    dance_pro = multiprocessing.Process(target=dance, kwargs={'name':'小红','num': 2})
    dance_pro.daemon = True # 设置子进程守护
    sing_pro.start()
    dance_pro.start()
