import asyncio

import os
import time
import requests
from config import OWNER_ID, USER_OWNER
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from AnonX import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from AnonX import app
from random import  choice, randint

                
@app.on_message(
    command(["مطورين spark","المطور ","مطورين","مطورين الفراعنة "])
    & ~filters.edited
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/9e90986cd4964303776a8.jpg",
        caption=f"""**⩹━★⊷━⌞ ميوزك الفراعنة  ⌝━⊶★━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم مطورين الفراعنة  ميوزك\nللتحدث مع مطورين اضغط علي الازرار بالاسفل👇\n**⩹━★⊷━⌞ ميوزك الفراعنة  ⌝━⊶★━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩علي | 🇮🇶 ˹َّّ ", url=f"https://t.me/co_od"), 
                 ],[
                    
                
                    InlineKeyboardButton(
                        "★⌞  ميوزك الفراعنة  ⌝⚡", url=f"https://t.me/wasit_go"),
                
        ],

            ]

        ),

    )








@app.on_message(
    command(["علي","مبرمج السورس","علي","علي"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("co_od")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞ميوزك الفراعنة  ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞ميوزك الفراعنة  ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["قناة السورس"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("wasit_go")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  ميوزك الفراعنة  ⌝━⊶★━⩺\n\n¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  ميوزك الفراعنة  ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )


@app.on_message(
    command(["مطورك","علي","ali"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    usr = await client.get_chat("co_od")
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**⩹━★⊷━⌞  ميوزك الفراعنة  ⌝━⊶★━⩺\n\n‍ ¦ᦔꫀꪜ :{name}مطوري\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}\n\n**⩹━★⊷━⌞  ميوزك الفراعنة  ⌝━⊶★━⩺**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{usr.username}")
                ],
            ]
        ),
    )
    

@app.on_message(
    command(["المطور"])
    & filters.group
    & ~filters.edited
)
async def yas(client, message):
    
    usr = await client.get_chat(USER_OWNER)
    name = usr.first_name
    photo = await app.download_media(usr.photo.big_file_id)
    await message.reply_photo(photo,       caption=f"**معلومات المطور الاساسي \n\n ¦ᦔꫀꪜ :{name}\n ¦ꪊ𝘴ꫀ𝘳 :@{usr.username}\n ¦Ꭵժ :`{usr.id}`\n ¦ႦᎥ᥆ :{usr.bio}**", 
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                       "مطور البوت", url=f"https://t.me/{usr.username}")
                ],   [
                    InlineKeyboardButton(
                        "قناة السورس", url=f"https://t.me/wasit_go"),                        
                 ],
            ]
        ),
    )
    


@app.on_message(
    command(["ذكاء حياه"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/9e90986cd4964303776a8.jpg",
        caption=f"""**⩹⊷━⌞  ميوزك الفراعنة  ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم الذكاء الاصتناعي الخاص بسورس سبارك\nلتتمكن من استخدام اوامر الذكاء الاصتناعي اكتب \n /gpt + السؤال بالاسفل👇\n**⩹━━⌞  ميوزك الفراعنة  ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩علي | 🇮🇶 ˹َّّ", url=f"https://t.me/co_od"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  ميوزك الفراعنة  ⌝⚡", url=f"https://t.me/wasit_go"),
                ],

            ]

        ),

    )



@app.on_message(
    command(["قرأن"])
    & ~filters.edited
    
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/9e90986cd4964303776a8.jpg",
        caption=f"""**⩹⊷━⌞  ميوزك الفراعنة  ⌝━━⩺**\nمرحبا بك عزيزي {message.from_user.mention} في قسم تشغيل القرأن الخاص بسورس سبارك\nلتتمكن من استخدام اوامر القرأن اكتب \n سورة + اسم السورة بالاسفل👇\n**⩹━━⌞  ميوزك الفراعنة  ⌝━━⩺**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "᳒ᯓ𓆩علي | 🇮🇶 ˹َّّ", url=f"https://t.me/co_od"), 
                 ],[
                
                    InlineKeyboardButton(
                        "★⌞  ميوزك الفراعنة  ⌝⚡", url=f"https://t.me/wasit_go"),
                ],

            ]

        ),

    )



    
