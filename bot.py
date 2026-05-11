import discord
from discord.ext import commands
import requests
import os

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

API_URL = "https://asset-manager--354242789.replit.app"

@bot.event
async def on_ready():
    print(f"Bot online as {bot.user}")

@bot.command()
async def validate(ctx, key: str):
    response = requests.post(f"{API_URL}/validate", json={"key": key})
    data = response.json()
    await ctx.send("✅ Valid" if data.get("success") else "❌ Invalid")

TOKEN = os.environ.get("DISCORD_TOKEN")
bot.run(TOKEN)
