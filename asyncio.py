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