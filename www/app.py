#!/usr/bin/env python
# -*- encoding:utf-8 -*-
# @author: Yasin
# @file: app.py
# @time: 2016/7/11 22:58
import logging;logging.basicConfig(level=logging.INFO)
import asyncio,datetime,os,json,time
from datetime import  datetime
from aiohttp import web
def index(request):
    return web.Response(body=b'<h1>blog</h1>')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET','/',index)
    srv = yield from loop.create_server(app.make_handler(),'127.0.0.1',9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()