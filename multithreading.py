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




#proper example of multi threading with arguments:
import threading
import time

# Function that accepts arguments
def process_result(name, marks):

    print(name, "result processing started")

    time.sleep(2)

    print("Student:", name)
    print("Marks:", marks)

    if marks >= 40:
        print(name, "has passed")
    else:
        print(name, "has failed")

    print("-------------------")


# Create threads and pass arguments

t1 = threading.Thread(
    target=process_result,
    args=("Umra", 85)
)

t2 = threading.Thread(
    target=process_result,
    args=("Ayesha", 32)
)

t3 = threading.Thread(
    target=process_result,
    args=("Rahul", 72)
)


# Start all threads

t1.start()
t2.start()
t3.start()


# Wait for all threads to finish

t1.join()
t2.join()
t3.join()

print("All results processed!")

