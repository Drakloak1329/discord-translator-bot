#!/usr/bin/python3
import discord as d
from discord.ext import commands as com
import googletrans as g

bot= com.Bot(command_prefix="translate",description="翻訳者ボットは素晴らしいですね。, Use 'translator text <text>' to translate.")
trn=g.Translator()
lng=g.LANGUAGES
tok="9kcIecZajPE_VJJ9zgNRPTtMN0N21Pew"

@bot.event
async def on_ready():
  print(">>> Logged in as "+bot.user.name)

@bot.command()
aysnc def no_command(ctx):
  await bot.say("Feature not made yet.")

@bot.command(" text")
async def on_text(ctx, args):
  tran=trn.translate(text)
  await bot.say(f"From : {lang[tran.src]}\nText : `{tran.text.escape()}`")

bot.run(tok)
