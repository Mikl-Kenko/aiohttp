from aiohttp import web
import aiohttp_jinja2
import jinja2


router = web.RouteTableDef()

@router.get('/')
@aiohttp_jinja2.template("index_start.html")
async def hi_aiohttp(request):
    context = {
        'message': 'Hello Aiohttp !!!'
    }
    return context

async def set_app():
    app = web.Application()
    app.add_routes(router)
    aiohttp_jinja2.setup(
    app, loader=jinja2.FileSystemLoader("templates")
    )
    return app

web.run_app(set_app())
