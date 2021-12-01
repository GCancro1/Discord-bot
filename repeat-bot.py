import os
import discord
import yaml


with open("discord_config.yml", "r") as ymlfile:
    configs = yaml.safe_load(ymlfile)

print(configs)


TOKEN = configs["token"]
GUILD = configs["guild"]
CHANNEL_ID = configs["channel"]
MESSAGE_FILES = configs["message_files"]

intents = discord.Intents.default()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f"{client.user} is connected to the following guild:\n"
        f"{guild.name}(id: {guild.id})"
        f"{guild.channels}"
    )

    channel = client.get_channel(CHANNEL_ID)
    for file in MESSAGE_FILES:
        with open(file, "r") as f:
            message = f.read()
            print(f"Sending message: \n{message} to channel: {channel}\n")
            await channel.send(message)
    print("logging out")
    await client.close()

# basic repeat message
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     await message.channel.send(message)

client.run(TOKEN)

