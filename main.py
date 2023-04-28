import asyncio
from pyrogram import Client, filters

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



    
bot.run()
