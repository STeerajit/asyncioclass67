# example of waiting for all tasks to complete
from random import random
import asyncio

#coroutine to execute in a new task
async def task_coro(arg):
    #generate a ramdom value between 0 and 1
    value = random()
    #block for a moment
    await asyncio.sleep(value)
    #report the value
    print(f'>task{arg} done with {value}')
    
#main coroutine
async def main():
    #create many task
    tasks = [asyncio.create_task(task_coro(i))for i in range(10)]
    #wait for all task to complete
    done, pedding = await asyncio.wait(tasks)
    #report results
    print('all done')

#start the asyncio program
asyncio.run(main())
