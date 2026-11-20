# Asyncio is a Python library that allows you to run multiple tasks efficiently 
# without making your program wait for one task to finish before starting another.
# It is mainly used for asynchronous programming.
# Asyncio allows Python to switch between tasks when one task is waiting.
# For example:
# - Task 1 starts downloading a file.
# - While waiting for the download, Python works on Task 2.
# - While Task 2 is waiting, Python can work on Task 3.
# - When the results are ready, the tasks continue.
# This is called asynchronous programming.
# 3. Important keywords in Asyncio
# There are three important things you should understand.
#1. async: This keyword is used to define a function as asynchronous.This defines a coroutine function.
#2. await: This keyword is used to pause the execution of a function
# until the result of an asynchronous operation is ready.asyncio.sleep(2) waits for two seconds without blocking the entire event loop.
#3. event loop: This is the core of every asyncio application. 
# It runs asynchronous tasks and callbacks, performs network IO operations, and runs subprocesses.
# It is responsible for managing and scheduling all the asynchronous tasks in your program.
# asyncio.run()
# It is used to execute an asynchronous main function.


import asyncio #module

async def task1():
    print("Task 1 started")
    await asyncio.sleep(3)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())   #await main() is used in jupyter notebook instead of asyncio.run(main())

# asyncio.gather() is a function in Python's asyncio library that allows you to run multiple 
# asynchronous tasks concurrently and collect their results together.
# Without gather():
# async def main():
#     await task1()
#     await task2()
#with gather():
# async def main():
    # await asyncio.gather(task1(), task2())


#using create_task() to run multiple tasks concurrently:
import asyncio
async def task1():
    print("Downloading file...")
    await asyncio.sleep(3)
    print("File downloaded!")

async def task2():
    print("Fetching API...")
    await asyncio.sleep(2)
    print("API data fetched!")

async def main():

    t1 = asyncio.create_task(task1())
    t2 = asyncio.create_task(task2())

    await t1
    await t2

asyncio.run(main())