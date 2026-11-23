# A thread is the smallest unit of execution within a process.
# Multithreading means executing multiple threads within the same process so that different tasks can make progress concurrently.
# Python provides a built-in module called threading
# key functions : start(), join(), thread(),etc
import threading
import time

def task():
    print("Task started")
    time.sleep(3)
    print("Task completed")

t1 = threading.Thread(target=task)

t1.start()
t1.join()

print("Main program completed")