from discord.ext import commands
import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import random
import requests
from discord.ext.commands import clean_content

class fun(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="coinflip",
        description="Flips a coin for heads or tails.",
        usage='`a!coinflip`'
    )
    async def coinflip(self,ctx):
        sides = ['heads','tails']
        side = random.choice(sides)
        await ctx.send(f"*Coin landed on: {side}, {ctx.author.mention}*")

    @commands.command(
        name="gayrate",
        description="Gayrates mentioned user.",
        usage="`a!gayrate (@user)`"
    )
    async def gayrate(self, ctx,member: discord.Member):
        percentage = random.randint(1,100)
        await ctx.send(f"*{member.mention} is {percentage}% gay.*")

    @commands.command(
        name="simprate",
        description="Simprates mentioned user.",
        usage="`a!simprate (@user)`"
    )
    async def simprate(self, ctx,member: discord.Member):
        percentage = random.randint(1,100)
        await ctx.send(f"*{member.mention} is {percentage}% simp.*")

    @commands.command(
        name="hotrate",
        description="Hotrates mentioned user.",
        usage="`a!hotrate (@user)`"
    )
    async def hotrate(self, ctx,member: discord.Member):
        percentage = random.randint(1,100)
        await ctx.send(f"*{member.mention} is {percentage}% hot.*")

    @commands.command(
        name="compatible",
        description="Checks compatibilty between you and a user.",
        usage="`a!compatible [@user]`"
    )
    async def compatible(self,ctx,member: discord.Member):
        percentage = random.randint(1,100)
        await ctx.send(f"*You and {member.mention} are {percentage}% compatible.*")

    @commands.command(
        name="cat",
        description="Gets a random picture of a cat.",
        usage="`a!cat`"
    )
    async def cat(self,ctx):
        r = requests.get("https://some-random-api.ml/img/cat").json()
        embed = discord.Embed(colour=discord.Colour.from_rgb(255,192,203)) 
        embed.set_image(url=str(r["link"]))
        embed.set_footer(text=f"requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(
        name="dog",
        description="Gets a random picture of a dog.",
        usage="`a!dog`"
    )
    async def dog(self,ctx):
        r = requests.get("https://some-random-api.ml/img/dog").json()
        embed = discord.Embed(colour=discord.Colour.from_rgb(255,192,203)) 
        embed.set_image(url=str(r["link"]))
        embed.set_footer(text=f"requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(
        name="eightball",
        description="Ask 8ball a question.",
        usage="`a!8ball [question]`"
    )
    async def eightball(self,ctx, *, question):
        responses = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it.'
        ]
        answer = random.choice(responses)
        await ctx.send(f"*{answer} {ctx.author.mention}*")

    @compatible.error
    async def compatible_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"**Please mention a user.**")

    @hotrate.error
    async def hotrate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            percentage = random.randint(1,100)
            await ctx.send(f"*You are {percentage}% hot.*")

    @gayrate.error
    async def gayrate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            percentage = random.randint(1,100)
            await ctx.send(f"*You are {percentage}% gay.*")

    @simprate.error
    async def simprate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            percentage = random.randint(1,100)
            await ctx.send(f"*You are {percentage}% simp.*")
        
def setup(client):
    client.add_cog(fun(client))
