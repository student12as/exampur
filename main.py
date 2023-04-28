import asyncio
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
import time
from pyrogram.types import User, Message
from subprocess import getstatusoutput
import logging
import os
import sys
import re
from pyrogram import Client as bot
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode
from pyromod import listen

bot = Client("bot",
             bot_token= "5509916510:AAHroyKDRf7HaKq4Z79X3AhzoYXMefk6BpA",
             api_id= 27495136,
             api_hash= "4ccc4865eec4d8fde7530e71948b3424")


@bot.on_message(filters.command(["start"]))

async def start(bot, update):

       await update.reply_text("Hi i am **PYRO BOT**.\n\n"

                              "**NOW:-** "

                                       

                                       "Press **/help** to continue..\n\n"

                                     "Bot made by ** AYUSH **" )





@bot.on_message(filters.command(["exampur"]) & ~filters.edited)
async def account_login(bot: Client, m: Message):
    global cancel
    cancel = False
    editable = await m.reply_text(
        "Send **ID & Password** in this manner otherwise bot will not respond.\n\nSend like this:-  **ID*Password**")
    rwa_url = "https://auth.exampurcache.xyz/auth/login"
    
    hdr = {
           "appauthtoken": "no_token",
           "User-Agent": "Dart/2.15(dart:io)",
           "content-type": "application/json; charset=UTF-8",       
           "Accept-Encoding": "gzip",
           "content-length": "94",
           "host": "auth.exampurcache.xyz" 
          }
    info={"phone_ext": "91", "phone": "", "email": "", "password": ""}
    #7355971781*73559717
    input1: Message = await bot.listen(editable.chat.id)
    raw_text = input1.text
    info["email"] = raw_text.split("*")[0]
    info["password"] = raw_text.split("*")[1]
    await input1.delete(True)
    scraper = cloudscraper.create_scraper()
    res = scraper.post(rwa_url, data=info).content
    output = json.loads(res)
    #print(output)
    token = output["data"]["authToken"]
    hdr1 = {
            "appauthtoken": token,
            "User-Agent": "Dart/2.15(dart:io)",
            "Accept-Encoding": "gzip",
            "host": "auth.exampurcache.xyz"
            }
    await editable.edit("**login Successful**")

    res1 = requests.get("https://auth.exampurcache.xyz/mycourses", headers=hdr1)
    b_data = res1.json()['data']
    cool = ""
    for data in b_data:
        FFF = "**BATCH-ID - BATCH NAME - INSTRUCTOR**"
        aa = f" ```{data['_id']}```      - **{data['title']}**\n\n"
        # aa=f"**Batch Name -** {data['batchName']}\n**Batch ID -** ```{data['id']}```\n**By -** {data['instructorName']}\n\n"
        if len(f'{cool}{aa}') > 4096:
            print(aa)
            cool = ""
        cool += aa
    await editable.edit(f'{"**You have these batches :-**"}\n\n{FFF}\n\n{cool}')
    editable1 = await m.reply_text("**Now send the Batch ID to Download**")
    input2 = message = await bot.listen(editable.chat.id)
    raw_text2 = input2.text

    scraper = cloudscraper.create_scraper()
    html = scraper.get("https://auth.exampurcache.xyz/course_subject/" + raw_text2,headers=hdr1).content
    output0 = json.loads(html)
    subjID = output0["data"]
    vj = ""
    for data in subjID:
       tids = (data["_id"])
       b = (data["title"])
       idid = f"{tids}&"
       if len(f"{vj}{idid}") > 4096:
          vj = ""
       vj += idid
    raw=vj
    await m.reply_text(raw)

    editable= await m.reply_text(f"Now send the **Topic IDs** to Download\n\nSend like this **1&2&3&4** so on\nor copy paste or edit **below ids** according to you :\n\n**Enter this to download full batch :-**\n```{raw}```")
    input4 = message = await bot.listen(editable.chat.id)
    raw_text4 = input4.text
    try:
        xv = raw_text4.split('&')
        for y in range(0,len(xv)):
            t =xv[y]

            res4 = requests.get("https://auth.exampurcache.xyz/course_material/chapter/"+t+"/" + raw_text2,headers=hdr1)
            b_data2 = res4.json()['data']
            
            vj = ""
            for i in range(0, len(b_data2)):
               tids = (b_data2[i])
               idid = f"{tids}"
               if len(f"{vj}{idid}") > 4096:
                  vj = ""
               encoded_URL = urllib.parse.quote(idid, safe="")
               chapter = encoded_URL.replace("%28", "(").replace("%29", ")").replace("%26", "&")
               vj += chapter
               res5 = requests.get("https://auth.exampurcache.xyz/course_material/material/"+t+"/"+raw_text2+"/"+chapter,headers=hdr1)
               b_data3 = res5.json()['data']
               vk = ""
               for data in b_data3:
                  tids = (data["video_link"])
                  b = (data["title"])
                  idid = f"{tids}&"
                  if len(f"{vk}{idid}") > 4096:
                       vk = ""
                  vk += idid
                  cc = (f"{b}:{tids}")
                  mm = "Exampur"
                  with open(f'{mm}.txt', 'a') as f:
                      f.write(f"{b}:{tids}\n")
            await m.reply_document(f"{mm}.txt")
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done")

@bot.on_message(filters.command("forward"))
async def forward(bot: Client , m: Message):
    msg = await bot.ask(m.chat.id, "**Forward any message from the Target channel\nBot should be admin at both the Channels**")
    t_chat = msg.forward_from_chat.id
    msg1 = await bot.ask(m.chat.id, "**Send Starting Message From Where you want to Start forwarding**")
    msg2 = await bot.ask(m.chat.id, "**Send Ending Message from same chat**")
   # print(msg1.forward_from_message_id, msg1.forward_from_chat.id, msg1.forward_from_message_id)
    i_chat = msg1.forward_from_chat.id
    s_msg = int(msg1.forward_from_message_id)
    f_msg = int(msg2.forward_from_message_id)+1
    await m.reply_text('**Forwarding Started**\n\nPress /restart to Stop and /log to get log TXT file')
    try:
        for i in range(s_msg, f_msg):
            try:
                await bot.copy_message(
                    chat_id= t_chat,
                    from_chat_id= i_chat,
                    message_id= i
                )
                
            except Exception:
                continue
    except Exception as e:
        await m.reply_text(str(e))
    await m.reply_text("Done Forwarding")



    
bot.run()
