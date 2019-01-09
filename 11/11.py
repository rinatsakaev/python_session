import asyncio
import aiohttp
async def fetch(session, url):
    async with session.get(url) as response:
        data = await response.read()
        print(data)
async def get_tasks():
    urls = ["https://aiohttp.readthedocs.io/en/stable/",
            "https://vk.com",
            "https://www.youtube.com/watch?v=LO61F07s7gw"]
    tasks = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = get_tasks()
    asyncio.run(tasks)
