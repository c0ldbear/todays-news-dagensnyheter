import aiohttp
import asyncio

async def main():
    print("Hello!\nWait 1 sec plz...")
    await asyncio.sleep(1)
    print("Now you've waited 1 sec. Congratulations!")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())