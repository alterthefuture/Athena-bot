import discord
from discord.ext import commands
from datetime import datetime
import platform

dpyVersion = discord.__version__
pythonVersion = platform.python_version() 
intents=discord.Intents.all()

client = commands.Bot(command_prefix="a!",intents=intents)

class information(commands.Cog):
    def __init__(self, client):
        self.client = client
                  
    @commands.command(
        name='userinfo',
        description='Shows information about the mentioned user.',
        usage='`a!userinfo (@user)`'
    )
    async def userinfo(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        roles = [role for role in member.roles]

        embed = discord.Embed(timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
        embed.set_author(name=f"{member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        embed.add_field(name="`ID`", value=f"{member.id}",inline=False)
        embed.add_field(name="`Status`", value=f"{member.status}",inline=False)
        embed.add_field(name="`Creation Date`",value=member.created_at.strftime("%a, %#d %B, %Y, %I:%M %p "),inline=False)
        embed.add_field(name="`Guild Join Date`",value=member.joined_at.strftime("%a, %#d %B, %Y, %I:%M %p "),inline=False)
        embed.add_field(name=f"`Roles ({len(roles)})`",value=" ".join([role.mention for role in roles]),inline=False)
        embed.add_field(name="`Highest Role`", value=member.top_role.mention,inline=False)

        await ctx.send(embed=embed)
     
    @commands.command(
        name='avatar',
        description='Shows the mentioned users avatar.',
        usage='`a!avatar (@member)`'
    )
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            member = ctx.author
        embed = discord.Embed(title=f"**{member.display_name}'s Avatar**",timestamp=ctx.message.created_at)
        embed.set_image(url='{}'.format(member.avatar_url))
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(
        name='serverinfo',
        description='Shows information about the server.',
        usage='`a!serverinfo`',
    )
    async def serverinfo(self, ctx):
        guild = ctx.guild 

        embed = discord.Embed(timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
        embed.set_author(name=f"{guild}")
        embed.add_field(name="`Channel count`", value=len(guild.channels),inline=False)
        embed.add_field(name="`Role count`", value=len(guild.roles),inline=False)
        embed.add_field(name="`Boost count`", value=guild.premium_subscription_count,inline=False)
        embed.add_field(name="`Member count`", value=guild.member_count,inline=False)
        embed.add_field(name="`Server created on`", value=guild.created_at.strftime("%a, %#d %B, %Y, %I:%M %p "),inline=False)
        embed.add_field(name="`ID`", value=guild.id,inline=False)
        embed.set_thumbnail(url=guild.icon_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)
    
    @commands.command(
        name="botinfo",
        description="Shows information about the bot.",
        usage="`a!botinfo`"
    )
    async def botinfo(self,ctx):
        embed = discord.Embed(title="Athena Bot Information",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
        embed.add_field(name="`Developer`", value="xqi#1400, myst#0001", inline=False)
        embed.add_field(name="`Date of Creation`", value="7/06/2021", inline=False)
        embed.add_field(name="`Language`", value=f"Python {pythonVersion}", inline=False)
        embed.add_field(name="`Discord.py version`", value=f"discord {dpyVersion}", inline=False)
        embed.add_field(name="`Bots ping`", value=f"{round(self.client.latency * 1000)}", inline=False)
        embed.add_field(name="`Servers`",value=f"{len(self.client.guilds)}")
        embed.add_field(name="`Members`",value=f"{len(self.client.users)}")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(information(client))


