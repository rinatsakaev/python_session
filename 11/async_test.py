import asyncio
import inspect
import socket


async def hello_planet():
    for i in range(15):
        print("hello")
        await asyncio.sleep(1)
        print("planet")

async def bye_world():
    for i in range(20):
        print("bye")
        await asyncio.sleep(0.5)
        print("world")
async def main1():
    #await hello_planet()
    #await bye_world()
    task1 = asyncio.create_task(hello_planet())
    task2 = asyncio.create_task(bye_world())

    await task1
    await task2

async def main2():
    g = asyncio.gather(hello_planet(), bye_world())
    await g

async def main3():
    done, pending = await asyncio.wait([hello_planet(), bye_world()], return_when="FIRST_COMPLETED")
    pass

async def main4():
    fut1 = asyncio.ensure_future(hello_planet())
    task1 = asyncio.create_task(bye_world())
    g = asyncio.gather(fut1, task1)
    await g

if __name__ == '__main__':

    # loop = asyncio.get_event_loop()
    # loop.create_task(hello_planet())
    # loop.create_task(bye_world())
    # loop.run_forever()

    #asyncio.run(main1())

    #asyncio.run(main2())

    #asyncio.run(main3())
    print(inspect.getsourcelines(main4))
    # loop = asyncio.get_event_loop()
    # t = loop.create_task(main4())
    # loop.run_until_complete(t)
 #   asyncio.run(main4())
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.SO_REUSEADDR)
    pass