"""管理python子进程:subprocess模块,I just need a really simple win32 example of communicate() between
a parent.py and child.py.A string sent from parent.py to child.py, altered by child.py and sent back
to parent.py for print() from parent.py"""
import os
import sys
from time import time
import subprocess


# proc = subprocess.Popen(['echo', 'Hello from the child!'], stdout=subprocess.PIPE)  # 用Popen构造器来启动进程
# out, err = proc.communicate()
# print(out.decode('utf-8'))

# proc = subprocess.Popen(['sleep', '0.3'])
# while proc.poll() is None:
#     print('Working...')
# print('Exit status', proc.poll())

# def run_sleep(period):
#     proc = subprocess.Popen(['sleep', str(period)])
#     return proc
#
# start = time()
# procs = []
# for _ in range(10):
#     proc = run_sleep(0.1)
#     procs.append(proc)
#
# for proc in procs:
#     proc.communicate()
# end = time()
# print('Finished in %.3f seconds' % (end - start))

def run_md5(input_stdin):
    proc = subprocess.Popen(['md5'], stdin=input_stdin, stdout=subprocess.PIPE)
    return proc

