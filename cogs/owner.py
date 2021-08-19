from discord.ext import commands
import discord
import json
import time

def read_json(filename):
    with open(f"{filename}.json","r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

class owner(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):

        data = read_json("cogs/blacklist")
        self.client.blacklisted_users = data["blacklistedUsers"]

    @commands.command(
        name="blacklist",
        description="Blacklist user from bot.",
        usage="`a!blacklist [@user]`"
    )
    @commands.is_owner()
    async def blacklist(self,ctx, user: discord.Member):
        if user == ctx.message.author:
            await ctx.send("**Stupid owner you can't blacklist yourself!**")
        elif user.id in self.client.blacklisted_users:
            await ctx.send("**User is already blacklisted.**")
        elif user == self.client.user:
            await ctx.send("**Stupid owner you can't blacklist the bot!**")
        else:
            try:
                self.client.blacklisted_users.append(user.id)
                data = read_json("cogs/blacklist")
                data["blacklistedUsers"].append(user.id)
                write_json(data, "cogs/blacklist")
                await ctx.send(f"*{user.mention} has been blacklisted.*")
            except:
                await ctx.send("**Can't find mentioned user.**")

    @commands.command(
        name="unblacklist",
        description="Unlacklist user from bot.",
        usage="`a!unblacklist [@user]`"
    )
    @commands.is_owner()
    async def unblacklist(self,ctx, user: discord.Member):
        if user.id in self.client.blacklisted_users:
            self.client.blacklisted_users.remove(user.id)
            data = read_json("cogs/blacklist")
            data["blacklistedUsers"].remove(user.id)
            write_json(data, "cogs/blacklist")
            await ctx.send(f"*{user.mention} has been unblacklisted.*")
        else:
            await ctx.send("**Mentioned user is not blacklisted.**")
    
    @commands.command(
        name="leaves",
        description="Leaves the guild the message was typed in.",
        usage="`a!leave`"
    )
    @commands.is_owner()
    async def leave(self,ctx):
        await ctx.guild.leave()

    @commands.command(
        name="toggle",
        description="Enable or disables a command.",
        usage="`a!toggle [command]`"
    )
    @commands.is_owner()
    async def toggle(self,ctx,*,command):
        command = self.client.get_command(command)

        if command is None:
            await  ctx.send("**This command is not found but you created the bot smh.**")
        
        elif ctx.command == command:
            await ctx.send("**Stupid owner you can't disable this command.**")
        
        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"*{command.qualified_name} has been {ternary}*")

    @commands.command(
        name="load",
        description="Loads a specific cog.",
        usage="`a!load [cog]`"
    )
    @commands.is_owner()
    async def load(self,ctx,extension):
        try:
            self.client.load_extension(f'cogs.{extension}')
            await ctx.send(f"*Successfully loaded the cog: {extension}*")
        except:
            await ctx.send(f"**Failed to load cog: {extension}**")

    @commands.command(
        name="unload",
        description="Unloads a specific cog.",
        usage="`a!unload [cog]`"
    )
    @commands.is_owner()
    async def unload(self,ctx,extension):
        try:
            self.client.unload_extension(f'cogs.{extension}')
            await ctx.send(f"*Successfully unloaded the cog: {extension}*")
        except:
            await ctx.send(f"**Failed to unload cog: {extension}**")

    @commands.command(
        name="reload",
        description="Reloads a specific cog.",
        usage="`a!reload [cog]`"
    )
    @commands.is_owner()
    async def reload(self,ctx,extension):
        try:
            self.client.reload_extension(f'cogs.{extension}')
            await ctx.send(f"*Successfully reloaded the cog: {extension}*")
        except:
            await ctx.send(f"**Failed to reload cog: {extension}**")

    @reload.error    
    async def reload_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("**You must be the owner of the bot to run this command.**")

    @load.error    
    async def load_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("**You must be the owner of the bot to run this command.**")

    @unload.error    
    async def unload_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("**You must be the owner of the bot to run this command.**")

    @toggle.error    
    async def toggle_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("**You must be the owner of the bot to run this command.**")

    @blacklist.error    
    async def blacklist_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("**You must be the owner of the bot to run this command.**")

    @unblacklist.error
    async def unblacklist_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("**You must be the owner of the bot to run this command.**")

    @leave.error
    async def leave_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("**You must be the owner of the bot to run this command.**")

def setup(client):
    client.add_cog(owner(client))
