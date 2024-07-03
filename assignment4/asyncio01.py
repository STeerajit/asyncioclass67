import asyncio

# Define the main coroutine
async def main():
    # Report a message
    print("main coroutine started")
    
    # Get the current task
    task = asyncio.current_task()
    
    # Report its details
    print(task)

# Start the asyncio program
asyncio.run(main())
