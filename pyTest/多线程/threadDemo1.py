import threading
import time

def loop1():
    while(True):
        print("hello")
        # time.sleep(1)
        l = threading.enumerate()
        print(l)

def loop2():
    while False:
        print("world")
        # time.sleep(1)
        l = threading.enumerate()
        print(l)






if __name__ == '__main__':
   # help(threading)
    t1 = threading.Thread(target=loop1,args=(),name="线程1")
    t2 = threading.Thread(target=loop2,args=(),name="线程2")
    t1.start()
    t2.start()