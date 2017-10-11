"""
    asyncio 直接内置了对异步IO的支持
    asyncio 的编程模型就是一个消息循环。我们从asyncio模块中直接获取一个EventLoop的引用，
    然后把需要执行的协程扔到EvenLoop中执行，就实现了异步IO

"""
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world!')
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print('Hello world')

# 获取EventLoop
loop = asyncio.get_event_loop()
# 执行coroutine
loop.run_until_complete(hello())
loop.close()


