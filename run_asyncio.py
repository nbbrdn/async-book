import asyncio, time


async def one():
    print("Start one")
    await asyncio.sleep(1)
    print("Stop one")


async def two():
    print("Start two")
    await asyncio.sleep(2)
    # time.sleep(5)
    print("Stop two")


async def three():
    print("Start three")
    await asyncio.sleep(3)
    print("Stop three")


async def main():
    # asyncio.create_task(one())
    # asyncio.create_task(two())
    # await asyncio.create_task(three())
    await asyncio.gather(two(), one(), three())


if __name__ == "__main__":
    start = time.time()
    asyncio.run(main())
    print(time.time() - start)
