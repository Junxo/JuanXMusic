import random
from asyncio import sleep

import asyncio

from pyrogram import filters
from JuanXMusic import AdminActual
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait, UserNotParticipant
from JuanXMusic.utils.decorators import AdminRightsCheck

from JuanXMusic import *


spam_chats = []


def get_arg(message: Message, _):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])



@app.on_message(filters.command(["tol"]) & filters.private & ~BANNED_USERS)
AdminRightsCheck
async def tagall(cli, message: Message, _, chat_id):
    await message.delete()
    chat_id = message.chat.id
    args = get_arg(message)
    if not args:
        args = "Hi!"
    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    m = client.get_chat_members(chat_id)
    async for usr in m:
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f"(tg://user?id={usr.user.id}) "
        if usrnum == 5:
            txt = f"**{args}**\n\n{usrtxt}"
            try:
                await client.send_message(chat_id, txt)
            except FloodWait as e:
                await sleep(e.value)
                await client.send_message(chat_id, txt)

            await sleep(2)
            usrnum = 0
            usrtxt = ""
    try:
        await client.send_message(chat_id, "**Proses Tag All selesai.")
        spam_chats.remove(chat_id)
    except:
        pass

@app.on_message(filters.command(["cancel"]) & filters.private & ~BANNED_USERS)
AdminRightsCheck
async def untag(cli, message: Message, _, chat_id):
    if not message.chat.id in spam_chats:
        return await message.reply("**Sepertinya tidak ada tagall disini.**")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("**Proses Tag All berhenti..**")
