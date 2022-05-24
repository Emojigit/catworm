# -*- coding: utf-8 -*-

__author__ = "Emoji"
__version__ = "1.0.0"
__url__ = "https://github.com/Emojigit/catworm"
__description__ = "Catworm by Yan"
__dname__ = "catworm"

from telethon import events
from asyncio import sleep
from time import time
cats = [
    "CAADBQADOgQAAgGegFYOH_O1Sy_hJgI",
    "CAADBQADcAMAApDLgVac4W-yRc548QI",
    "CAADBQADMQQAAn0ZgFY0TkXJmOwNlwI"
]
def setup(bot,storage):
    @bot.on(events.NewMessage(pattern='/catworm'))
    async def catworm(event):
        chatid = event.chat_id
        last_exec = storage.get("catworm_lastexec_" + str(chatid),0)
        now = int(time())
        if now - last_exec < 5:
            await event.reply("太快了喵，貓貓蟲不喜歡你啊喵！")
        else:
            storage.set("catworm_lastexec_" + str(chatid),now,autosave=False)
            for x in cats:
                await bot.send_file(event.chat,file=x,silent=True)
            storage.save()
        raise events.StopPropagation
    @bot.on(events.NewMessage())
    async def catworm_hug(event):
        # 摸摸猫猫虫
        text = event.message.text
        if "摸摸猫猫虫" in text or "摸摸貓貓蟲" in text or "抱抱猫猫虫" in text or "抱抱貓貓蟲" in text:
            await event.reply("摸摸喵～")
