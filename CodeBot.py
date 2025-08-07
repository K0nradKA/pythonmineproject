import discord
from discord.ext import commands
discord.ext.commands.Bot

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready!")
    print("-------------------------")

channel_id =1402960125559570455 
channelbot = bot.get_channel(channel_id)


@bot.event
async def on_ready():
    print("Bot is ready!")
    print("-------------------------")


@bot.command()
async def hallo(ctx):
    await ctx.send('Hello!')
@bot.command()













