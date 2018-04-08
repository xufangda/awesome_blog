# import orm, asyncio
# from models import User, Blog, Comment

# loop=asyncio.get_event_loop()
# async def test():
#     await orm.create_pool(loop, user='root', password='buzhidao', database='awesome')

#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

#     await u.save()

# loop.run_until_complete(test())
# loop.close()
import asyncio


async def my_sleeping_task(name, secs):
    print('Starting {}'.format(name))
    await asyncio.sleep(secs)
    print('Finished {}'.format(name))
    return name


async def main():
    tasks = [
        my_sleeping_task('one', 3),
        my_sleeping_task('two', 2),
        my_sleeping_task('three', 1),
    ]

    while len(tasks):
        done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
        for task in done:
            print(task, task.result())


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(main())
    finally:
        loop.close()