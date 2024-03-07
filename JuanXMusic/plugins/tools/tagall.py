from JuanXMusic import app 
import asyncio
import random
from pyrogram import Client, filters
from pyrogram.errors import UserNotParticipant
from pyrogram.types import ChatPermissions

spam_chats = []


def get_arg(message: Message):
    msg = message.text
    msg = msg.replace(" ", "", 1) if msg[1] == " " else msg
    split = msg[1:].replace("\n", " \n").split(" ")
    if " ".join(split[1:]).strip() == "":
        return ""
    return " ".join(split[1:])

async def isAdmin(filter, client, update):
    try:
        member = await client.get_chat_member(chat_id=update.chat.id, user_id=update.from_user.id)
    except FloodWait as wait_err:
        await sleep(wait_err.value)
    except UserNotParticipant:
        return False
    except:
        return False

    return member.status in [STATUS.OWNER, STATUS.ADMINISTRATOR]

Admin = filters.create(isAdmin)

@app.on_message(filters.command(["tol"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def tagall(client, message: Message):
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
            txt = f"{args}**\n\n{usrtxt}"
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
@LanguageStart
async def untag(client, message: Message):
    if not message.chat.id in spam_chats:
        return await message.reply("**Sepertinya tidak ada tagall disini.")
    else:
        try:
            spam_chats.remove(message.chat.id)
        except:
            pass
        return await message.reply("Proses Tag All berhenti..")
