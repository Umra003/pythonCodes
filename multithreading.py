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


# start():Starts the function in a separate thread. 
#join(): Waits for the thread to complete before proceeding with the main program.
# Without join(), the main thread may continue executing without waiting for the worker threads.
import threading

def greet(name):
    print("Hello", name)

t1 = threading.Thread(target=greet, args=("Umra",)) #passing argument to the thread function using args parameter
#args=("Umra",) — the comma is important because it makes this a one-element tuple.

t1.start()
t1.join()



from concurrent.futures import ThreadPoolExecutor  #ThreadPoolExecutor, which makes managing multiple threads easier.
import time

def task(n):
    print("Task", n, "started")
    time.sleep(2)
    print("Task", n, "completed")

with ThreadPoolExecutor(max_workers=3) as executor:
    executor.map(task, [1, 2, 3, 4, 5])

print("All tasks completed")