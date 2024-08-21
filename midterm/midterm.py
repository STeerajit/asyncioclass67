# import asyncio

# async def fibonacii(n):
#     await asyncio.sleep(1)
#     a, b = 0, 1
#     if n <= 1:
#         return n
#     else:
#         for i in range(1, n):
#             c = a + b 
#             a = b
#             b = c
#         return b
# async def main():
#     n = 10
#     coros = [asyncio.create_task(fibonacii(i)) for i in range(n)]
#     results = await asyncio.gather(*coros)
#     print(results)
# asyncio.run(main())

import asyncio

async def fibonacii(n):
    await asyncio.sleep(1)
    a, b = 0, 1
    if n <= 1:
        return n
    else:
        for i in range(1, n):
            c = a + b 
            a = b
            b = c
        return b

async def main():
    n = 10
    coros = [asyncio.create_task(fibonacii(i)) for i in range(n)]
    
    # รัน tasks ทั้งหมดและรอให้เสร็จสิ้นด้วย asyncio.wait
    done, pending = await asyncio.wait(coros)

    # ดึงผลลัพธ์จาก tasks ที่เสร็จสิ้นแล้ว
    results = [task.result() for task in done]
    print(results)

asyncio.run(main())
