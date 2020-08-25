#!/usr/bin/python3
import discord as d
from discord.ext import commands as com
import googletrans as g

bot= com.Bot(prefix="translate",description="翻訳者ボットは素晴らしいですね。, Use 'translator text <text>' to translate.")


@bot.event
async def on_ready():
  print(">>> Logged in as "+bot.user.name)

@bot.command()
aysnc def no_command(ctx):
  
