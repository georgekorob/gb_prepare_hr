import asyncio
import aiohttp
from urllib.request import urlopen
from bs4 import BeautifulSoup
import aiofiles

url = 'http://127.0.0.1:8000/'
print(f'url: {url}')
data = urlopen(url).read()
soup = BeautifulSoup(data, features="html.parser")
links = soup.findAll('a')
urls = {a.get_text().strip(): url + a.get('href')[1:] for a in links}


async def make_request(session, name_url):
    name, url = name_url
    print(f"making request to {url}")
    async with session.get(url) as resp:
        if resp.status == 200:
            text = await resp.text()
            async with aiofiles.open(f'save_files/{name}.html', mode='w+') as f:
                await f.write(text)


async def main(urls):
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(
            *[make_request(session, name_url) for name_url in urls.items()]
        )


loop = asyncio.get_event_loop()
loop.run_until_complete(main(urls))
