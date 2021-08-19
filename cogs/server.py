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
        name="setlogchannel",
        description="Sets log channel to mentioned channel.",
        usage="`a!setlogchannel [#channel]`"
    )
    async def setlogchannel(self,ctx,channel: discord.TextChannel):
        if ctx.author != ctx.guild.owner:
            await ctx.send('**Only server owner can use this command.**')
        else:
            try:
                with open('cogs/logs.json', 'r') as f:
                        log = json.load(f)

                log[str(ctx.guild.id)] = channel.id

                with open('cogs/logs.json', 'w') as f: 
                    json.dump(log, f, indent=4)
                
                await ctx.send(f"*Successfully set log channel to: {channel.mention}*")

                with open("cogs/logs.json") as f:
                    config = json.load(f)

                log_channel = config.get(f"{ctx.guild.id}")
                logs = self.client.get_channel(log_channel)

                if log_channel != "None":
                    embed=discord.Embed(title=f"New Log Channel",description=f"**{ctx.author.mention} has set the log channel to {channel.mention}**",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                    embed.set_footer(text=f"ID: {ctx.author.id}")
                    embed.set_thumbnail(url=ctx.author.avatar_url)

                    await logs.send(embed=embed)
                else:
                    pass
            except:
                await ctx.send("**Failed to set log channel.**")

    @commands.command(
        name="disablelogchannel",
        description="Disables log channel.",
        usage="`a!disablelogchannel`"
    )
    async def disablelogchannel(self,ctx):
        if ctx.author != ctx.guild.owner:
            await ctx.send('**Only server owner can use this command.**')
        else:
            try:
                with open('cogs/logs.json', 'r') as f:
                        log = json.load(f)

                log[str(ctx.guild.id)] = "None"

                with open('cogs/logs.json', 'w') as f: 
                    json.dump(log, f, indent=4)
                
                await ctx.send(f"*Successfully disabled log channel.*")

            except:
                await ctx.send("**Failed to disable log channel.**")

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
