from discord.ext import commands
import discord
import os
import json
import time
import asyncio

intents=discord.Intents.all()

def get_prefix(client,message):
    with open("cogs/prefixes.json","r") as f:
        prefixes = json.load(f)

    return prefixes[str(message.guild.id)] 

client = commands.Bot(command_prefix=get_prefix,intents=intents,owner_ids=[798325945463078952,746051373753171978])
client.remove_command(name="help")

def read_json(filename):
    with open(f"{filename}.json","r") as file:
        data = json.load(file)
    return data

@client.event
async def on_ready():

    data = read_json("cogs/blacklist")
    client.blacklisted_users = data["blacklistedUsers"]

    print("Bot is ready.")

    while True: 
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{len(client.guilds)} Servers {len(client.users)} Members!"))
        await asyncio.sleep(4)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"a!help"))
        await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.author.id in client.blacklisted_users:
        return

    with open("cogs/antispam.json") as f:
        config = json.load(f)

    antispamm = config.get(f"{message.guild.id}")

    if antispamm == "True":
        if message.author.id == 798325945463078952 or message.author.id == 746051373753171978 or message.author.id == client.user.id:
            pass
        else:
            counter = 0
            with open("cogs/spam_detect.txt","r+") as file:
                for lines in file:
                    if lines.strip("\n") == str(message.author.id):
                        counter+=1

                file.writelines(f"{str(message.author.id)}\n")
                if counter > 5:
                    await message.channel.purge(limit=counter)
                    muted = discord.utils.get(message.guild.roles, name="Muted")
                    await message.author.add_roles(muted)

                    with open("cogs/logs.json") as f:
                        config = json.load(f)

                    log_channel = config.get(f"{message.guild.id}")
                    logs = client.get_channel(log_channel)

                    if log_channel != "None":
                        embed=discord.Embed(title=f"{message.author}",description=f"**{message.author.mention} has been muted by {client.user} **\n{message.content}\n\n **Reason**\n Spamming",colour=discord.Colour.from_rgb(255,192,203),timestamp=message.created_at)
                        embed.set_footer(text=f"ID: {message.author.id}")
                        embed.set_thumbnail(url=message.author.avatar_url)

                        await logs.send(embed=embed)
                    else:
                        pass
    else:
        pass

    await client.process_commands(message)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run("token-here")
