from telethon import events, Button
from ..Config import Config
from ..sql_helper.globals import gvarstatus
from SPIDER.razan.resources.mybot import *

ROZ_PIC = "https://graph.org/file/6e4359dc87a11152d5951.jpg"

if Config.TG_BOT_USERNAME is not None and tgbot is not None:
    @tgbot.on(events.InlineQuery)
    async def inline_handler(event):
        builder = event.builder
        result = None
        query = event.text
        await bot.get_me()
        if query.startswith("التنصيب") and event.query.user_id == bot.uid:
            buttons = [[Button.url("① قناة السورس", "https://t.me/def_Zoka"), Button.url("② استخراج ايبيات", "https://my.telegram.org/"),],[Button.url("③ استخراج الجلسة", "https://t.me/SESION_REFZ_BOT"), Button.url("④ بوت فاذر", "http://t.me/BotFather"),],[Button.url("⑤ رابط التنصيب", "https://dashboard.heroku.com/new?template=https://github.com/SOURCE-SPIDER/TELEHON"),],[Button.url("المطـور 👨🏼‍💻", "https://t.me/
IC_X_K"),]]
            if ROZ_PIC and ROZ_PIC.endswith((".jpg", ".png", "gif", "mp4")):
                result = builder.photo(ROZ_PIC, text=ROZ, buttons=buttons, link_preview=False)
            elif ROZ_PIC:
                result = builder.document(ROZ_PIC,title="
IC_X_K",text=ROZ,buttons=buttons,link_preview=False)
            else:
                result = builder.article(title="
IC_X_K",text=ROZ,buttons=buttons,link_preview=False)
            await event.answer([result] if result else None)
@bot.on(admin_cmd(outgoing=True, pattern="التنصيب"))
async def repo(event):
    if event.fwd_from:
        return
    TG_BOT = Config.TG_BOT_USERNAME
    if event.reply_to_msg_id:
        await event.get_reply_message()
    response = await bot.inline_query(TG_BOT, "التنصيب")
    await response[0].click(event.chat_id)
    await event.delete()

# edit by ~ @IC_X_K
