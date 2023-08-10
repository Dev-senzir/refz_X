from telethon import functions
from telethon.tl import functions
from telethon.tl.functions.channels import InviteToChannelRequest

from IC_X_K import IC_X_K

from ..core.managers import edit_delete, edit_or_reply

@IC_X_K.on(admin_cmd(pattern="تاك(?: |$)(.*)"))
async def iq(IC_X_K):
    mentions = IC_X_K.text[8:]
    chat = await IC_X_K.get_input_chat()
    async for x in IC_X_K.client.iter_participants(chat, 200):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉"
    await IC_X_K.client.send_message(IC_X_K.chat_id, mentions)
    await IC_X_K.delete()
@IC_X_K.on(admin_cmd(pattern="تاك 150(?: |$)(.*)"))
async def iq(IC_X_K):
    mentions = IC_X_K.text[8:]
    chat = await IC_X_K.get_input_chat()
    async for x in IC_X_K.client.iter_participants(chat, 150):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await IC_X_K.client.send_message(IC_X_K.chat_id, mentions)
    await IC_X_K.delete()
@IC_X_K.on(admin_cmd(pattern="تاك 100(?: |$)(.*)"))
async def iq(IC_X_K):
    mentions = IC_X_K.text[8:]
    chat = await IC_X_K.get_input_chat()
    async for x in IC_X_K.client.iter_participants(chat, 100):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await IC_X_K.client.send_message(IC_X_K.chat_id, mentions)
    await IC_X_K.delete()
@IC_X_K.on(admin_cmd(pattern="تاك 50(?: |$)(.*)"))
async def iq(IC_X_K):
    mentions = IC_X_K.text[8:]
    chat = await IC_X_K.get_input_chat()
    async for x in IC_X_K.client.iter_participants(chat, 50):
        mentions += f" \n🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await IC_X_K.client.send_message(IC_X_K.chat_id, mentions)
    await IC_X_K.delete()
@IC_X_K.on(admin_cmd(pattern="تاك 10(?: |$)(.*)"))
async def iq(IC_X_K):
    mentions = IC_X_K.text[8:]
    chat = await IC_X_K.get_input_chat()
    async for x in IC_X_K.client.iter_participants(chat, 10):
        mentions += f" \n 🝳 ⦙ ⵧ〈[{x.first_name}](tg://user?id={x.id})〉 \n"
    await IC_X_K.client.send_message(IC_X_K.chat_id, mentions)
    await IC_X_K.delete()
