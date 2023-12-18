
import asyncio
import random
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters, Client
from AnonX import app
from strings.filters import command

@app.on_message(command(['نداء','ن']))
def call_random_member(client, message):
    chat_id = message.chat.id
    members = [
        member for member in client.iter_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"وين خاتل تعال هنا يمعود  😾 {random_member_mention}",
        f"• يـا قمـري ❤️‍🔥 {random_member_mention}",
        f"حبي عوف الخاض وتعال نتونس 🌚 🤔 {random_member_mention}",
        f"• يـا راس السطل تعال {random_member_mention}",
        f"• انتة ليش هيج كمر  🌚♥ {random_member_mention}"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')



@app.on_message(command(['زوجني','ز']))
def call_random_member(client, message):
    chat_id = message.chat.id
    members = [
        member for member in client.iter_chat_members(chat_id)
        if not member.user.is_bot
    ]
    random_member = random.choice(members)
    random_member_mention = f"[{random_member.user.first_name}](tg://user?id={random_member.user.id})"
    random_message = random.choice([
        f"**• اخترت لك هذا الشخص** {random_member_mention} \n **🙈♥**",
        f"**• اخترت لك هذا الشخص** \n {random_member_mention} \n **"
    ])
    client.send_message(chat_id, random_message, reply_to_message_id=message.message_id, parse_mode='markdown')




