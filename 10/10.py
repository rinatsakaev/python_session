from concurrent.futures import ThreadPoolExecutor
from asyncio import sleep as asleep


def return_after_5_secs(message):
    sleep(5)
    return message


pool = ThreadPoolExecutor(3)

future = pool.submit(return_after_5_secs, ("hello"))
print(future.done())
print(future.done())
print(future.result())