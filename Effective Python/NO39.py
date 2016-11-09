from collections import deque
from threading import Thread
from queue import Queue
from time import sleep


# class MyQueue(object):
#     def __init__(self):
#         self.items = deque()
#         self.lock = Lock()
#
#
# class Worker(Thread):
#     def __init__(self, func, in_queue, out_queue):
#         super().__init__()
#         self.func = func
#         self.in_queue = in_queue
#         self.out_queue = out_queue
#         self.polled_count = 0
#         self.work_done = 0


# queue = Queue()
#
#
# def consumer():
#     print('Consumer waiting')
#     queue.get()
#     print('Consumer done')
#
# thread = Thread(target=consumer)
# thread.start()
#
#
# print('Producer putting')
# queue.put(object())
# thread.join()
# print('Producer done')
#
#
# queue = Queue(1)
#
#
# def consumer():
#     sleep(0.1)
#     queue.get()
#     print('Consumer got 1')
#     queue.get()
#     print('Consumer got 2')
#
# thread = Thread(target=consumer)
# thread.start()


in_queue = Queue()


def consumer():
    print('Consumer waiting')
    work = in_queue.get()
    print('Consumer working')
    print('Consumer done')
    in_queue.task_done()


Thread(target=consumer).start()
in_queue.put(object())
print('Producer waiting')


class ClosableQueue(Queue):
    SENTINEL = object()

    def close(self):
        self.put(self.SENTINEL)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.SENTINEL:
                    return
                yield item
            finally:
                self.task_done()


