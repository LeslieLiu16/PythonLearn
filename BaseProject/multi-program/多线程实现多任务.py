import threading
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
    sing_thr = threading.Thread(target=sing)
    dance_thr = threading.Thread(target=dance)
    sing_thr.start()
    dance_thr.start()