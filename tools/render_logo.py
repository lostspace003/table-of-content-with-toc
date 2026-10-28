import asyncio
from icons import gennoor_logo_svg
from playwright.async_api import async_playwright
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/opt/pw-browsers/chromium"); pg = await b.new_page(viewport={"width":1200,"height":280}, device_scale_factor=1)
        for dark in (False, True):
            await pg.set_content(f'<html><body style="margin:0;background:transparent">{gennoor_logo_svg(280, dark)}</body></html>')
            await pg.wait_for_timeout(200)
            await pg.screenshot(path=f"logo-{'dark' if dark else 'light'}.png", omit_background=True, clip={"x":0,"y":0,"width":1200,"height":280})
        await b.close()
asyncio.run(main())
