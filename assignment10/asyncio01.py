from random import random
import asyncio

# Coroutine to generate work 
async def producer(queue):
    print('Producer: Running')
    # Generate work
    for i in range(10):
        # Generate value
        value = i
        # Block to simulate work
        await asyncio.sleep(random())
        # Add to queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # Send an all-done signal
    await queue.put(None)
    print('Producer: Done')

# Coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    # Consume work
    while True:
        # Get a unit of work
        item = await queue.get()
        # Check for stop signal
        if item is None:
            break
        # Report
        print(f'\t> Consumer got {item}')
    # All done
    print('Consumer: Done')

# Entry point coroutine
async def main():
    # Create the shared queue
    queue = asyncio.Queue()
    # Run the producer and consumer
    await asyncio.gather(producer(queue), consumer(queue))

# Start the asyncio program
asyncio.run(main())
