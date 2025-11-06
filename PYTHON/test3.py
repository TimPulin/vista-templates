# coding=utf-8
import json
import os
from aiohttp import ClientSession
import requests
import asyncio

BASE_URL = "http://192.168.78.88:8002/print/html/client"


class SendBody:
    def __init__(self, template_id, event_id=None,client_id = None, action_id=None, repeat=False):
        self.event_id = event_id
        self.template_id = template_id
        self.action_id = action_id
        self.repeat = repeat
        self.client_id = client_id

    def get_body(self):
        body = {"repeat": self.repeat, "template_id": self.template_id, 'client_id': self.client_id}


        return body

    def get_url(self):
        url = BASE_URL

        return url


async def get_html(send_template):
    send_body = send_template.get_body()
    url = send_template.get_url()
    data = {json.dumps(send_body): "без разницы что"}
    async with ClientSession() as session:
        async with session.post(
            url,
            data=data,
        ) as response:
            html_text = await response.text()
            html_content = json.loads(html_text)

            meta_tag = '<meta charset="UTF-8">\n'
            html_content = meta_tag + html_content
    return html_content


async def main():
    import webbrowser

    send_body = SendBody(client_id=1, template_id=6666855)
    html = await get_html(send_body)
    from time import sleep
    sleep(1)
    with open("test.html", "w", encoding="utf-8") as f:
        f.write(html)
    webbrowser.open("test.html")





if __name__ == "__main__":

    asyncio.run(main())



