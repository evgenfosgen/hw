import asyncio
import aiohttp           # асинхронные HTTP-запросы
import aiofiles          # асинхронная запись файлов
import sys


async def dw_one(session, url, filename):
    async with session.get(url) as response:
        # ждём пока сайт вернёт нам картинку (не блокируем луп)
        content = await response.read()
        # асинхронно сохраняем байты картинки в файл
        async with aiofiles.open(filename, "wb") as f:
            await f.write(content)


async def dw_all(how_many):
    url = "https://picsum.photos/200"

    async with aiohttp.ClientSession() as session:
        tasks = []

        for i in range(how_many):
            filename = f"images/image_{i+1:03}.jpg"
            task = dw_one(session, url, filename)  # cоздаём задачу
            tasks.append(task)

        results = await asyncio.gather(*tasks)  # ждем завершения всех задач


async def main():
    arg = int(sys.argv[1])
    await dw_all(arg)


if __name__ == "__main__":
    asyncio.run(main())


# python3 5.1.py 10
