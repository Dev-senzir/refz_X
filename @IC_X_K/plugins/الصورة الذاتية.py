from IC_X_K import *
from IC_X_K import IC_X_K 
from ..sql_helper.globals import gvarstatus

@IC_X_K.on(admin_cmd(pattern="(ذاتية|ذاتيه)"))
async def dato(event):
    if not event.is_reply:
        return await event.edit("..")
    IC_X_K = await event.get_reply_message()
    pic = await IC_X_K.download_media()
    await bot.send_file(
        "me",
        pic,
        caption=f"""
- تـم جـلب الصـورة بنجـاح ✓ 
- غير مبري الذمه اذا استخدمت الامر للابتزاز
- CH: @def_Zoka 
- Dev: @IC_X_K 
  """,
    )
    await event.edit(" 🙂❤️ ")
