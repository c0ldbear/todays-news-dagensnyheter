import aiohttp
from bs4 import BeautifulSoup
import asyncio

async def fetchNews():
    url = "https://www.dn.se/nyhetsdygnet"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            rText = await response.text()
            #print(await response.text())
    return await findNewsTopics(rText)
    

async def findNewsTopics(responseText):
    soup = BeautifulSoup(responseText, "html.parser")
    news_timeline = soup.find("div", attrs={'class':'timeline-page'})
    news_links = news_timeline.find_all("a", href=True)
    newsUrls = []
    for link in news_links:
        #topic = str(link.find("h3"))
        a_link = link["href"]
        newsUrls += [(a_link)]
    return newsUrls


async def main():
    News = await fetchNews()
    for news in News[:-1]:
        print("https://www.dn.se" + news)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())