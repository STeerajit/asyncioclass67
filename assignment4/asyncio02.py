import asyncio

# Coroutine for a task
async def task_coroutine(value):
    # Report a message
    print(f'task{value} is running')
    # Block for a moment
    await asyncio.sleep(1)

# Define the main coroutine
async def main():
    # Report a message
    print('main coroutine started')
    
    # Start many tasks
    started_tasks = [asyncio.create_task(task_coroutine(i), name=f'task{i}') for i in range(10)]
    
    # Allow some of the tasks time to start
    await asyncio.sleep(0.1)
    
    # Get all tasks
    tasks = asyncio.all_tasks()
    
    # Report all tasks
    for task in tasks:
        print(f'>{task.get_name()}, {task.get_coro()}')
    
    # Wait for all tasks to complete
    for task in started_tasks:
        await task

# Start the asyncio program
asyncio.run(main())
