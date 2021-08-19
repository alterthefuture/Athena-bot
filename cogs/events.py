from discord.ext import commands
import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp
import asyncio
import json
from discord.ext.commands import CommandNotFound

intents=discord.Intents.all()

client = commands.Bot(command_prefix="a!",intents=intents,owner_id=798325945463078952)

class events(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_guild_join(self,guild):

        if guild.member_count <= 1:
            await guild.leave()
        else:
            try:
                to_send = sorted([chan for chan in guild.channels if chan.permissions_for(guild.me).send_messages and isinstance(chan, discord.TextChannel)], key=lambda x: x.position)[0]
            except IndexError:
                pass
            embed = discord.Embed(title="Athena Moderation Bot", description="Hey, thanks for inviting athena! type `a!help` to get started.",colour=discord.Colour.from_rgb(255,192,203))
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
            embed.set_footer(text='Developed By lxy#5676') 
            await to_send.send(embed=embed)

            async with aiohttp.ClientSession() as session:
                webhook = Webhook.from_url('https://discord.com/api/webhooks/862539160824709153/36kgL7eJzDx7tJv04ejM7LwXS_ADXI8Alpye5e9bx-bOVCumTHrt_TNkV5sQbg_UGubu', adapter=AsyncWebhookAdapter(session))

                invite = await guild.text_channels[0].create_invite()
                embed=discord.Embed(title="I have joined a server!",colour=discord.Colour.from_rgb(255,192,203))
                embed.add_field(name="`Server Name`",value=guild.name,inline=False)
                embed.add_field(name="`Server Owner`",value=guild.owner,inline=False)
                embed.add_field(name="`Members`",value=len(guild.members),inline=False)
                embed.add_field(name="`Invite`",value=invite)
                embed.set_footer(text=f"ID: {guild.id}")
                embed.set_thumbnail(url=guild.icon_url)

                await webhook.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, CommandNotFound):
            with open("cogs/prefixes.json") as f:
                config = json.load(f)

            get_prefix = config.get(f"{ctx.guild.id}")

            await ctx.send(f"**Command Not Found. Please Type** `{get_prefix}help` **For A List Of Commands.**")
        else:
            pass

    
def setup(client):
    client.add_cog(events(client))