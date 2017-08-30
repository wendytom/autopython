#-*- coding:utf-8 -*-

import threading
import time

#def test(p):
    #time.sleep(0.01)
    #print p

#lis1 = []
#for i in xrange(0,15):
    #a = threading.Thread(target=test,args=[i])
    #a.start()
    #lis1.append(a)

#for i in lis1:
    #i.join()
    
#print "ending ..."

mlock = threading.Lock()
def a():
    for i in range(10):
        mlock.acquire()
        print i
        time.sleep(2)
        print i
        mlock.release()
    
def b():
    print "b begin"
    time.sleep(2)
    print "b end"
    
b_time = time.time()
_a = threading.Thread(target=a)
_b = threading.Thread(target=b)
_a.start()
_b.start()
_a.join()
_b.join()
print time.time() - b_time