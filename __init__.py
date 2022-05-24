# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/catworm"
__description__ = "Catworm by Yan"
__dname__ = "catworm"

from telethon import events
from asyncio import sleep
cats = [
    "CAADBQADOgQAAgGegFYOH_O1Sy_hJgI",
    "CAADBQADcAMAApDLgVac4W-yRc548QI",
    "CAADBQADMQQAAn0ZgFY0TkXJmOwNlwI"
]
def setup(bot):
    @bot.on(events.NewMessage(pattern='/catworm'))
    async def catworm(event):
        for x in cats:
            await bot.send_file(event.chat,file=x,silent=True)
        raise events.StopPropagation
