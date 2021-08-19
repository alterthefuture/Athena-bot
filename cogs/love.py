from discord.ext import commands
import discord
import requests

class love(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="hug",
        description="Hugs mentioned user.",
        usage="`a!hug [@user]`"
    )
    async def hug(self,ctx, user: discord.Member):
        if user == ctx.author:
            r = requests.get("https://nekos.life/api/v2/img/hug")
            res = r.json()
            embed = discord.Embed(description=f"{ctx.author.mention} hugs themselves",colour=discord.Colour.from_rgb(255,192,203))
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            r = requests.get("https://nekos.life/api/v2/img/hug")
            res = r.json()
            embed = discord.Embed(description=f"{ctx.author.mention} hugs {user.mention}",colour=discord.Colour.from_rgb(255,192,203))
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)

    @commands.command(
        name="kiss",
        description="Kisses mentioned user.",
        usage="`a!kiss [@user]`"
    )
    async def kiss(self,ctx, user: discord.Member):
        if user == ctx.author:
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()
            embed = discord.Embed(description=f"{ctx.author.mention} kisses themselves",colour=discord.Colour.from_rgb(255,192,203))
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            r = requests.get("https://nekos.life/api/v2/img/kiss")
            res = r.json()
            embed = discord.Embed(description=f"{ctx.author.mention} kisses {user.mention}",colour=discord.Colour.from_rgb(255,192,203))
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)

    @commands.command(
        name="cuddle",
        description="Cuddles mentioned user.",
        usage="`a!cuddle [@user]`"
    )
    async def cuddle(self,ctx, user: discord.Member):
        if user == ctx.author:
            r = requests.get("https://nekos.life/api/v2/img/cuddle")
            res = r.json()
            embed = discord.Embed(description=f"{ctx.author.mention} cuddles themselves",colour=discord.Colour.from_rgb(255,192,203))
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)
        else:
            r = requests.get("https://nekos.life/api/v2/img/cuddle")
            res = r.json()
            embed = discord.Embed(description=f"{ctx.author.mention} cuddles {user.mention}",colour=discord.Colour.from_rgb(255,192,203))
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
            embed.set_image(url=res["url"])
            await ctx.send(embed=embed)

    @cuddle.error
    async def cuddle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"**Please mention a user.**")

    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"**Please mention a user.**")

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"**Please mention a user.**")

def setup(client):
    client.add_cog(love(client))
