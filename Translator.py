#!/usr/bin/python3
import discord as d
from discord.ext import commands as com
import googletrans as gTrans

bot= com.Bot(command_prefix="translate",description="翻訳者ボットは素晴らしいですね。, Use 'translator text <text>' to translate.")
translator=gTrans.Translator()
langs=gTrans.LANGUAGES
token="NzM2NjA2NDkxMzU1NjQzOTU0.XxxQQQ.JyIDQ3O8uXPkMqiE01GVYN2Cq34"

@bot.event
async def on_ready():
  print(">>> Logged in as "+bot.user.name)

@bot.command()
async def no_command(ctx):
  await bot.say("Feature not made yet.")

@bot.command(" text")
async def on_text(ctx, args):
  tran=trans.translate(text)
  await bot.say(f"From : {langs[tran.src]}\nText : `{tran.text.escape()}`")

bot.run(token)
