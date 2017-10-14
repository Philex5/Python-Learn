# 异步编程的一个原则：一旦决定使用异步，则系统的每一层都必须是异步，“开动没有回头箭”
# aiomysql为MySQL数据库提供了异步IO的驱动

# 创建连接池
# 创建一个全局的连接池，每一HTTP请求都可以从连接池中直接获取数据库连接
# 使用连接池的好处是不必频繁地打开和关闭数据库连接，而是能复用就尽量复用
import asyncio
import logging
import aiomysql


def log(sql, args=()):
    logging.info('SQL: %s' % sql )


@asyncio.coroutine
def create_pool(loop, **kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        port=kw.get('port', 3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset', 'utf8'),
        autocommit=kw.get('autocommit', True),
        maxsize=kw.get('maxsize', 10),
        minsize=kw.get('minsize', 1),
        loop=loop
    )

# 首先把常用的SELECT、INSERT、UPDATE和DELETE操作用函数封装起来


@asyncio.coroutine
def select(sql, args, size=None):
    log(sql, args)
    global __pool
    with (yield from __pool) as conn:
        cur = yield from conn.cursor(aiomysql.DictCursor)
        yield from cur.execute(sql.replace('?', '%s'), args or ())  # 将SQL语句中的占位符(?)替换为MySQL中的占位符(%s)
        if size:
            rs = yield from cur.fetchmany(size)  # 获取最多指定数量的记录
        else:
            rs = yield from cur.fetchall()
        yield from cur.close()
        logging.info('rows returned: %s' % len(rs))
        return rs
# 每一个需要等待的操作都要加上yield from


@asyncio.coroutine
def execute(sql, args):
    log(sql)
    with (yield from __pool) as conn:
        try:
            cur = yield from conn.cursor()
            yield from cur.execute(sql.replace('?', '%s'), args)
            affected = cur.rowcount
            yield from cur.close()
        except BaseException as e:
            raise
        return affected

# ORM
# 设计ORM需要从上层调用者角度来设计
# 先考虑如何定义一个user对象， 然后把数据库user和它关联起来

from orm import Model, StringField, IntegerField


class User(Model):
    _table_ = 'users'

    id = IntegerField(primary_key=True)
    name = StringField()
