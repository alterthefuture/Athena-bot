from discord.ext import commands
import discord
import json

class server(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self,guild): 
        with open('cogs/prefixes.json', 'r') as f: 
            prefixes = json.load(f) 

        prefixes[str(guild.id)] = "a!"

        with open('cogs/prefixes.json', 'w') as f: 
            json.dump(prefixes, f, indent=4)

        with open('cogs/logs.json', 'r') as f: 
            logs = json.load(f) 

        logs[str(guild.id)] = "None"

        with open('cogs/logs.json', 'w') as f: 
            json.dump(logs, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild): 
        with open('cogs/prefixes.json', 'r') as f: 
            prefixes = json.load(f)

        prefixes.pop(str(guild.id))

        with open('cogs/prefixes.json', 'w') as f:
            json.dump(prefixes, f, indent=4)

        with open('cogs/logs.json', 'r') as f: 
            logs = json.load(f)

        logs.pop(str(guild.id))

        with open('cogs/logs.json', 'w') as f:
            json.dump(logs, f, indent=4)

    @commands.command(
        name="setprefix",
        description="Changes server prefix.",
        usage="`a!prefix [prefix]`"
    )
    async def setprefix(self,ctx,prefix):
        if ctx.author != ctx.guild.owner:
            await ctx.send('**Only server owner can use this command.**')
        else:
            try:

                with open('cogs/prefixes.json', 'r') as f:
                            prefixes = json.load(f)

                prefixes[str(ctx.guild.id)] = prefix

                with open('cogs/prefixes.json', 'w') as f: 
                    json.dump(prefixes, f, indent=4)

                await ctx.send(f"*Successfully set prefix to: {prefix}*")
            except:
                await ctx.send("**Failed to set prefix.**")

def setup(client):
    client.add_cog(server(client))
