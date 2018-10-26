
# Only runs on 3.6 and above
import asyncio
import datetime

async def display_date():
    loop = asyncio.get_running_loop()
    end_time = loop.time() + 5.0
    while True:
        print(datetime.datetime.now())
        if (loop.time() + 1.0) >= end_time:
            break
        await asyncio.sleep(1)

asyncio.run(display_date())



#
# import random
# from time import sleep
# import asyncio
#
#
# def task(pid):
#     """Synchronous non-deterministic task."""
#     sleep(random.randint(0, 2) * 0.001)
#     print('Task %s done' % pid)
#
#
# async def task_coro(pid):
#     """Coroutine non-deterministic task"""
#     await asyncio.sleep(random.randint(0, 2) * 0.001)
#     print('Task %s done' % pid)
#
#
# def synchronous():
#     for i in range(1, 10):
#         task(i)
#
#
# async def asynchronous():
#     tasks = [task_coro(i) for i in range(1, 10)]
#     await asyncio.gather(*tasks)
#
#
# print('Synchronous:')
# synchronous()
#
# print('Asynchronous:')
# asyncio.run(asynchronous())