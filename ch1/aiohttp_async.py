from aiohttp import web
import time

#비동기 함수를 코루틴으로 다루는 async
async def handle(request):
    return web.json_response({'time':time.time()})

if __name__ == '__main__':
    app=web.Application()
    app.router.add_get('/',handle)
    web.run_app(app)

    