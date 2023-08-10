#تعريب وتتطوير السيد يوسف @IC_X_K
import os

from telethon import events

from ..sql_helper.globals import addgvar, delgvar, gvarstatus

os.system("pip install googletrans")
from googletrans import Translator

from 
IC_X_K import 
IC_X_K

translator = Translator()


@
IC_X_K.ar_cmd(pattern="تفعيل الترجمة")
async def traenjm(event):
    if gvarstatus("translateen"):
        await edit_delete(event, "⎊ **الترجمة التلقائية مفعلة بالأصل ✅**")
        return
    if not gvarstatus("translateen"):
        addgvar("translateen", "Done")
        await edit_delete(
            event, "⎊ **تم بنجاح تفعيل الترجمة التلقائية ✅**"
        )
        return


@
IC_X_K.ar_cmd(pattern="تعطيل الترجمة")
async def stoptraenjm(event):
    if not gvarstatus("translateen"):
        await edit_delete(event, "⎊ **الترجمة التلقائية غير مفعلة بالأصل ❌**")
        return
    if gvarstatus("translateen"):
        delgvar("translateen")
        await edit_delete(event, "⎊ **تم تعطيل الترجمة التلقائية ❌**")
        return


@
IC_X_K.on(events.NewMessage(outgoing=True))
async def translateen(event):
    if gvarstatus("translateen"):
        if event.message.message.startswith(("!", ".", "/", "http", "@")):
            return
        try:
            translation = translator.translate(
                event.message.message, src="ar", dest="en"
            )
            if translation.text != event.message.message:
                await 
IC_X_K.edit_message(event.message, translation.text)
        except:
            pass
