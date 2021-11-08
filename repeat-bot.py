import os
import discord
import yaml


with open("discord_config.yml", "r") as ymlfile:
    configs = yaml.safe_load(ymlfile)

print(configs)

token = configs["token"]
my_guild = configs["guild"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)



@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == my_guild:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    await message.channel.send(message)

client.run(token)

