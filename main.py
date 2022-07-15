import os
import nextcord
from nextcord.ext import commands
import wavelink
from pyfiglet import figlet_format
from music import *

intents = nextcord.Intents.default()
intents.message_content = True

bot = nextcord.Client()
bot = commands.Bot(command_prefix="o!", intents = intents)

@bot.event
async def on_ready():
  print(figlet_format("Orange - gbaaxza"))
  bot.loop.create_task(node_connect())

async def node_connect():
  await bot.wait_until_ready()
  await wavelink.NodePool.create_node(bot=bot, host="lavalinkinc.ml", port=443, password="incognito", https=True)

play(bot)
pause(bot)
resume(bot)
disconnect(bot)
stop(bot)





bot.run(os.getenv("Token"))
