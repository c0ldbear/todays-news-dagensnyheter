import aiohttp
import asyncio
from bs4 import BeautifulSoup

async def fetchNews():
    url = "https://www.dn.se/nyhetsdygnet"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            rText = await response.text()
            #print(await response.text())

async def main():
    await fetchNews()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())