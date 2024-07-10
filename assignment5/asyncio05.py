import asyncio
import random

async def make_rice():
    prep_time = 1 + random.random()
    print(f'Rice: Preparing... (will take {prep_time:.2f} seconds)')
    await asyncio.sleep(prep_time)
    print('Rice is ready!')
    return 'Rice'

async def make_noodle():
    prep_time = 1 + random.random()
    print(f'Noodle: Preparing... (will take {prep_time:.2f} seconds)')
    await asyncio.sleep(prep_time)
    print('Noodle is ready!')
    return 'Noodle'

async def make_curry():
    prep_time = 1 + random.random()
    print(f'Curry: Preparing... (will take {prep_time:.2f} seconds)')
    await asyncio.sleep(prep_time)
    print('Curry is ready!')
    return 'Curry'

async def main():
    tasks = [
        asyncio.create_task(make_rice()),
        asyncio.create_task(make_noodle()),
        asyncio.create_task(make_curry())
    ]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    
    for task in done:
        print(f'{task.result()} was the first to be ready!')

    for task in pending:
        task.cancel()

# Run the asyncio program
asyncio.run(main())