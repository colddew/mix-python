# -*- coding:utf-8 -*-

from multiprocessing import Process, Lock, Pool
import time


# def process(num):
#     time.sleep(num)
#     print 'Process:', num
#
# if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=process, args=(i,))
#         p.start()
#
#     print('CPU number:' + str(multiprocessing.cpu_count()))
#     for p in multiprocessing.active_children():
#         print('Child process name: ' + p.name + ' id: ' + str(p.pid))
#
#     print('Process Ended')


def function(index):
    print 'Start process: ', index
    time.sleep(3)
    print 'End process', index


if __name__ == '__main__':
    pool = Pool(processes=3)
    for i in xrange(4):
        pool.apply_async(function, (i,))
        # pool.apply(function, (i,))

    print "Started processes"
    pool.close()
    pool.join()
    print "Subprocess done."


# class MyProcess(Process):
#     def __init__(self, loop, lock):
#         Process.__init__(self)
#         self.loop = loop
#         self.lock = lock
#
#     def run(self):
#         for count in range(self.loop):
#             time.sleep(0.1)
#             self.lock.acquire()
#             print('Pid: ' + str(self.pid) + ' LoopCount: ' + str(count))
#             self.lock.release()
#
# if __name__ == '__main__':
#
#     lock = Lock()
#     for i in range(10, 15):
#         p = MyProcess(i, lock)
#         p.start()
#         # p.join()
#
#     print 'Main process Ended!'
