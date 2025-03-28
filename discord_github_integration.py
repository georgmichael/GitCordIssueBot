import discord
from discord.ext import commands
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GITHUB_REPO = "Jobinthomas123/Virtual-songbook"
GITHUB_TOKEN = os.getenv("GH_TOKEN")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Define bot prefix and intents
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def create_issue(ctx, title: str, *, description: str):
    """Creates a GitHub issue with the given title and description."""
    url = f"https://api.github.com/repos/{GITHUB_REPO}/issues"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    data = {"title": title, "body": description}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 201:
        issue = response.json()
        await ctx.send(f'Issue created: {issue["html_url"]}')
    else:
        await ctx.send(f'Failed to create issue: {response.content}')

bot.run(DISCORD_TOKEN)
