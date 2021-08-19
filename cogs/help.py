from discord.ext import commands
import discord
import json

class help(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="help",
        description="Displays a list of athena's command list.",
        usage="`{get_prefix}help`"
    )
    async def help(self,ctx,category=None):

        with open("cogs/prefixes.json") as f:
            config = json.load(f)

        get_prefix = config.get(f"{ctx.guild.id}")

        if category == None:
            embed=discord.Embed(title="Athena Help Menu",description=f"Below are all the commands type `{get_prefix}help [catagory]` to get started.\n\n [Server](https://discord.com/invite/nSF4vQaW35) • [Invite](https://discord.com/api/oauth2/authorize?client_id=862536816531341312&permissions=8&scope=bot) • [Upvote](https://discordbotlist.com/bots/athena-1350/upvote)",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
            embed.add_field(name="Information",value="`Displays Information Commands.`",inline=False)
            embed.add_field(name="Server",value="`Displays Server Commands.`",inline=False)
            embed.add_field(name="Music",value="`Displays Music Commands.`",inline=False)
            embed.add_field(name="Anti",value="`Displays Anti Commands.`",inline=False)
            embed.add_field(name="Love",value="`Displays Love Commands.`",inline=False)
            embed.add_field(name="Fun",value="`Displays Fun Commands.`",inline=False)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
            embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

            await ctx.send(embed=embed)
      
        elif category == "music" or category == "Music":
            cog = self.client.get_cog('music')
            commands = cog.get_commands()
            embed = discord.Embed(title="Athena Music Commands",colour=discord.Colour.from_rgb(255,192,203),description='Commands with () are optional and [] is required.',timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'.'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: {command.usage}\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: {command.usage}',inline=False)

            await ctx.send(embed=embed)
        elif category == "info" or category == "Info" or category == "Information" or category == "information":
            cog = self.client.get_cog('information')
            commands = cog.get_commands()
            embed = discord.Embed(title="Athena Information Commands",colour=discord.Colour.from_rgb(255,192,203),description='Commands with () are optional and [] is required.',timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'.'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: {command.usage}\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: {command.usage}',inline=False)

            await ctx.send(embed=embed)
            
        elif category == "love" or category == "Love":
            cog = self.client.get_cog('love')
            commands = cog.get_commands()
            embed = discord.Embed(title="Athena Love Commands",colour=discord.Colour.from_rgb(255,192,203),description='Commands with () are optional and [] is required.',timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'.'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: {command.usage}\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: {command.usage}',inline=False)

            await ctx.send(embed=embed)

        elif category == "server" or category == "Server":
            cog = self.client.get_cog('server')
            commands = cog.get_commands()
            embed = discord.Embed(title="Athena Server Commands",colour=discord.Colour.from_rgb(255,192,203),description='Commands with () are optional and [] is required.',timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'.'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: {command.usage}\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: {command.usage}',inline=False)

            await ctx.send(embed=embed)

        elif category == "fun" or category == "Fun":
            cog = self.client.get_cog('fun')
            commands = cog.get_commands()
            embed = discord.Embed(title="Athena Fun Commands",colour=discord.Colour.from_rgb(255,192,203),description='Commands with () are optional and [] is required.',timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'.'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: {command.usage}\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: {command.usage}',inline=False)

            await ctx.send(embed=embed)

        elif category == "anti" or category == "Anti":
            cog = self.client.get_cog('anti')
            commands = cog.get_commands()
            embed = discord.Embed(title="Athena Anti Commands",colour=discord.Colour.from_rgb(255,192,203),description='Commands with () are optional and [] is required.',timestamp=ctx.message.created_at)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'.'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: {command.usage}\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: {command.usage}',inline=False)

            await ctx.send(embed=embed)

        elif category == "owner" or category == "Owner":
            if ctx.author.id == your_id_as_a_int:
                cog = self.client.get_cog('owner')
                commands = cog.get_commands()
                embed = discord.Embed(title="Athena Owner Commands",colour=discord.Colour.from_rgb(255,192,203),description='Commands with () are optional and [] is required.',timestamp=ctx.message.created_at)
                embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/863200845688733736/863930582320939029/original.jpg")
                for command in commands:
                    if command.aliases != []:
                        alias_list = command.aliases
                        temp_alias_list = []
                        for i in range(len(alias_list)):
                            temp_alias_list.append(f'.'+alias_list[i])
                        embed.add_field(
                            name=command.qualified_name,
                            value=f'Description: {command.description}\nUsage: {command.usage}\nAliases: `{", ".join(temp_alias_list)}`',
                            inline=False
                        )
                    else:
                        embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: {command.usage}',inline=False)

                await ctx.send(embed=embed)
            else:
                pass


def setup(client):
    client.add_cog(help(client))
