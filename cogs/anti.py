from discord.ext import commands
import discord
import json
import asyncio

class anti(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        while True:
            await asyncio.sleep(5)
            with open("cogs/spam_detect.txt","r+") as file:
                file.truncate(0)

    @commands.Cog.listener()
    async def on_member_join(self,member):

        with open("cogs/antibot.json") as f:
            config = json.load(f)

        if member.bot == True:
            antibott = config.get(f"{member.guild.id}")
            if antibott == "True":

                with open("cogs/logs.json") as f:
                    config = json.load(f)

                log_channel = config.get(f"{member.guild.id}")
                logs = self.client.get_channel(log_channel)

                if log_channel != "None":
                    embed=discord.Embed(title=f"Bot Banned",description=f"**{member.mention} has been banned by {self.client.user.mention}**\n\n**Reason**\n Anti Bot",timestamp=member.joined_at,colour=discord.Colour.from_rgb(255,192,203))
                    embed.set_footer(text=f"ID: {member.id}")
                    embed.set_thumbnail(url=self.client.user.avatar_url)

                    await logs.send(embed=embed)
                else:
                    pass

                await member.ban(reason="Anti Bot")
            else:
                pass

    @commands.Cog.listener()
    async def on_guild_join(self,guild): 
        #anti-bot
        with open('cogs/antibot.json', 'r') as f: 
            antibot = json.load(f) 

        antibot[str(guild.id)] = "True"

        with open('cogs/antibot.json', 'w') as f: 
            json.dump(antibot, f, indent=4)

        #anti-spam
        with open('cogs/antispam.json', 'r') as f: 
            antibot = json.load(f) 

        antibot[str(guild.id)] = "True"

        with open('cogs/antispam.json', 'w') as f: 
            json.dump(antibot, f, indent=4)

    @commands.Cog.listener()
    async def on_guild_remove(self,guild): 
        #anti-bot
        with open('cogs/antibot.json', 'r') as f: 
            antibot = json.load(f)

        antibot.pop(str(guild.id))

        with open('cogs/antibot.json', 'w') as f:
            json.dump(antibot, f, indent=4)

        #anti-spam
        with open('cogs/antispam.json', 'r') as f: 
            antibot = json.load(f)

        antibot.pop(str(guild.id))

        with open('cogs/antispam.json', 'w') as f:
            json.dump(antibot, f, indent=4)

    @commands.command(
        name="antispam",
        description="Turns anti spam on or off.",
        usage="`a!antispam [on/off]`"
    )
    async def antispam(self,ctx,category = None):
        
        if category == None:
            await ctx.send("**Please specify either on or off.**")

        elif category == "on" or category == "On":
            with open("cogs/antispam.json") as f:
                config = json.load(f)

            antispamm = config.get(f"{ctx.guild.id}")
            if ctx.author != ctx.guild.owner:
                await ctx.send('**Only server owner can use this command.**')
            elif antispamm == "True":
                await ctx.send('**Anti spam is already enabled.**')
            else:
                with open('cogs/antispam.json', 'r') as f:
                    antibot = json.load(f)

                antibot[str(ctx.guild.id)] = "True"

                with open('cogs/antispam.json', 'w') as f: 
                    json.dump(antibot, f, indent=4)

                await ctx.send('*Anti spam is now enabled.*')

        elif category == "off" or category == "Off":
            with open("cogs/antispam.json") as f:
                config = json.load(f)

            antispamm = config.get(f"{ctx.guild.id}")
            if ctx.author != ctx.guild.owner:
                await ctx.send('**Only server owner can use this command.**')
            elif antispamm == "False":
                await ctx.send('**Anti spam is already disabled.**')
            else:
                with open('cogs/antispam.json', 'r') as f:
                    antispam = json.load(f)

                antispam[str(ctx.guild.id)] = "False"

                with open('cogs/antispam.json', 'w') as f: 
                    json.dump(antispam, f, indent=4)

                await ctx.send('*Anti spam is now disabled.*')

    @commands.command(
        name="antibot",
        description="Turns anti bot on or off.",
        usage="`a!antibot [on/off]`"
    )
    async def antibot(self,ctx,category = None):
        
        if category == None:
            await ctx.send("**Please specify either on or off.**")

        elif category == "on" or category == "On":
            with open("cogs/antibot.json") as f:
                config = json.load(f)

            antibott = config.get(f"{ctx.guild.id}")
            if ctx.author != ctx.guild.owner:
                await ctx.send('**Only server owner can use this command.**')
            elif antibott == "True":
                await ctx.send('**Anti bot is already enabled.**')
            else:
                with open('cogs/antibot.json', 'r') as f:
                    antibot = json.load(f)

                antibot[str(ctx.guild.id)] = "True"

                with open('cogs/antibot.json', 'w') as f: 
                    json.dump(antibot, f, indent=4)

                await ctx.send('*Anti bot is now enabled.*')

        elif category == "off" or category == "Off":
            with open("cogs/antibot.json") as f:
                config = json.load(f)

            antibott = config.get(f"{ctx.guild.id}")
            if ctx.author != ctx.guild.owner:
                await ctx.send('**Only server owner can use this command.**')
            elif antibott == "False":
                await ctx.send('**Anti bot is already disabled.**')
            else:
                with open('cogs/antibot.json', 'r') as f:
                    antibot = json.load(f)

                antibot[str(ctx.guild.id)] = "False"

                with open('cogs/antibot.json', 'w') as f: 
                    json.dump(antibot, f, indent=4)

                await ctx.send('*Anti bot is now disabled.*')
 
def setup(client):
    client.add_cog(anti(client))
