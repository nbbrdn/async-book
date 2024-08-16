import asyncio


async def add_one(number: int) -> int:
    return number + 1


result = asyncio.run(add_one(1))

print(result)
