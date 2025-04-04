import asyncio
from asyncio import Future


def make_request() -> Future:
    future = Future()
    asyncio.create_task(set_future_value(future))
    return future


async def set_future_value(future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)


async def main():
    future = make_request()
    print(f"Is the future done? {future.done()}")  # False
    value = await future
    print(f"Is the future done? {future.done()}")  # True
    print(value)


asyncio.run(main())
