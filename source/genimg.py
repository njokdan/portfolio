import asyncio, os
from playwright.async_api import async_playwright
from content import CASES
U="http://localhost:8765/portfolio/"; G="generated"
async def m():
    os.makedirs(G+"/og",exist_ok=True)
    async with async_playwright() as p:
        b=await p.chromium.launch(); pg=await b.new_page(viewport={"width":1200,"height":630})
        await pg.goto(U); await pg.wait_for_timeout(2200)
        await pg.add_style_tag(content=".top,.intro,.hero-cta,.route-hint,.proof-band,#work,.why,#services,#more,#experience,#goals,#faq,.contact,.foot,.bus{display:none!important}.hero{padding-top:46px;height:630px}.hello{font-size:22px;color:#1C2126;margin-bottom:14px}.route-wrap{margin-top:30px}.route-track{padding-top:0}.hero h1{font-size:66px;max-width:24ch}")
        await pg.wait_for_timeout(300); await pg.screenshot(path=G+"/og.png")
        for c in CASES:
            await pg.goto(U+f"work/{c['id']}/"); await pg.wait_for_timeout(500)
            await pg.add_style_tag(content=".top,.crumb,.case-links,.case-body,.pager,.contact,.foot,.case-meta span:last-child{display:none!important}.case-head{height:630px;padding:70px 0 0;box-sizing:border-box;background:linear-gradient(#F4C20D,#F4C20D) left bottom/100% 26px no-repeat,linear-gradient(#1C2126,#1C2126) left calc(100% - 34px)/100% 8px no-repeat,#F3F4F1}.case-head h1{margin-top:0;font-size:120px}.case-line{font-size:30px;max-width:40ch}.case-meta{font-size:20px}.case-head .wrap::before{content:'Case study by Daniel Njoku';display:block;font:650 22px/1 Archivo,sans-serif;color:#535C65;margin-bottom:22px}")
            await pg.screenshot(path=f"{G}/og/{c['id']}.png")
        svg=open("dist/portfolio/favicon.svg").read()
        for size,name in [(512,"icon-512.png"),(180,"apple-touch-icon.png")]:
            ic=await b.new_page(viewport={"width":size,"height":size})
            await ic.set_content(f"<style>body{{margin:0}}svg{{width:{size}px;height:{size}px;display:block}}</style>{svg}")
            await ic.screenshot(path=f"{G}/{name}"); await ic.close()
        await b.close()
asyncio.run(m())
