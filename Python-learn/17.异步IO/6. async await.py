"""
   用sayncio提供的@asyncio.coroutine 可以把一个generator标记为coroutine类型，
   然后在coroutine内部用yield from调用另一个coroutine实现异步操作
   为了简化并更好地标记异步IO，从Python3.5开始引入新的语法saync和await,可以让coroutine的代码更简洁易读
   具体规则：
   1. asyncio.coroutine 替换为 async
   2. yield from 替换为 await
"""
# 与sayncio对比
import asyncio

async def hello():
    print('Hello world!')
    r = await asyncio.sleep(1)
    print("hello again")
