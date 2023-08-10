#بعد التعديل تبلع بند انت وسورسك🤘
import asyncio
import random
from asyncio.exceptions import TimeoutError

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from IC_X_K import IC_X_K
from ..helpers.utils import reply_id


@IC_X_K.on(admin_cmd(outgoing=True, pattern="ريمكس$"))
async def jepvois(vois):
  rl = random.randint(3,267)
  url = f"https://t.me/REMIXv1/{rl}"
  await vois.client.send_file(vois.chat_id,url,caption="⎊︙ BY : @EE_20 🎧",parse_mode="html")
  await vois.delete()
