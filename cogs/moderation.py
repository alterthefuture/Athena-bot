from discord.ext.commands import has_permissions, MissingPermissions, BotMissingPermissions
from discord.ext import commands
import discord
import json

class moderation(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="kick",
        description="Kicks mentioned user.",
        usage="`a!kick [@user] (reason)`"
    )
    @commands.bot_has_guild_permissions(kick_members=True)
    @commands.has_permissions(kick_members=True)
    async def kick(self,ctx,member:discord.Member,*,reason=None):
        guild = ctx.guild
        if ctx.author == member:
            await ctx.send('**You cant kick yourself**')
        elif ctx.author.top_role < member.top_role:
            await ctx.send(f"**You can't kick a member above you.**")
        elif ctx.guild.owner == member:
            await ctx.send('**You cant kick the server owner**')
        else:
            if reason == None:
                try:
                    try:
                        with open("cogs/logs.json") as f:
                            config = json.load(f)

                        log_channel = config.get(f"{ctx.guild.id}")
                        logs = self.client.get_channel(log_channel)

                        if log_channel != "None":
                            embed=discord.Embed(title=f"Member Kicked",description=f"**{ctx.author.mention} has been kicked by{ctx.channel.mention}**\n\n **Reason**\n {reason}",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                            embed.set_footer(text=f"ID: {ctx.author.id}")
                            embed.set_thumbnail(url=ctx.author.avatar_url)

                            await logs.send(embed=embed)
                        else:
                            pass

                        await member.kick()
                        await ctx.send(f'*{member} was kicked | Reason: {reason} *')
                    except:
                        with open("cogs/logs.json") as f:
                            config = json.load(f)

                        log_channel = config.get(f"{ctx.guild.id}")
                        logs = self.client.get_channel(log_channel)

                        if log_channel != "None":
                            embed=discord.Embed(title=f"Member Kicked",description=f"**{ctx.author.mention} has been kicked by{ctx.channel.mention}**\n\n **Reason**\n {reason}",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                            embed.set_footer(text=f"ID: {ctx.author.id}")
                            embed.set_thumbnail(url=ctx.author.avatar_url)

                            await logs.send(embed=embed)
                        else:
                            pass

                        await member.kick()
                        await ctx.send(f'*{member} was kicked| Reason: {reason} *')
                except:
                    await ctx.send(f"**Couldn't kick that user.**")
            else:
                try:
                    with open("cogs/logs.json") as f:
                        config = json.load(f)

                    log_channel = config.get(f"{ctx.guild.id}")
                    logs = self.client.get_channel(log_channel)

                    if log_channel != "None":
                        embed=discord.Embed(title=f"Member Kicked",description=f"**{ctx.author.mention} has been kicked by{ctx.channel.mention}**\n\n **Reason**\n {reason}",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                        embed.set_footer(text=f"ID: {ctx.author.id}")
                        embed.set_thumbnail(url=ctx.author.avatar_url)

                        await logs.send(embed=embed)
                    else:
                        pass

                    await member.kick(reason=reason)
                    await ctx.send(f'*{member} was kicked | Reason: {reason}*')
                except:
                    await ctx.send(f"**Couldn't kick that user.**")

    @commands.command(
        name="ban",
        description="Bans mentioned user.",
        usage="`a!ban [@user] (reason)`"
    )
    @commands.bot_has_guild_permissions(ban_members=True)
    @commands.has_permissions(ban_members=True)
    async def ban(self,ctx,member:discord.Member,*,reason=None):
        guild = ctx.guild
        if ctx.author == member:
            await ctx.send('**You cant ban yourself**')
        elif ctx.author.top_role < member.top_role:
            await ctx.send(f"**You can't ban a member above you.**")
        elif ctx.guild.owner == member:
            await ctx.send('**You cant ban the server owner**')
        else:
            if reason == None:
                try:
                    try:
                        with open("cogs/logs.json") as f:
                            config = json.load(f)

                        log_channel = config.get(f"{ctx.guild.id}")
                        logs = self.client.get_channel(log_channel)

                        if log_channel != "None":
                            embed=discord.Embed(title=f"Member Banned",description=f"**{ctx.author.mention} has been banned by{ctx.channel.mention}**\n\n **Reason**\n {reason}",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                            embed.set_footer(text=f"ID: {ctx.author.id}")
                            embed.set_thumbnail(url=ctx.author.avatar_url)

                            await logs.send(embed=embed)
                        else:
                            pass

                        await member.ban()
                        await ctx.send(f'*{member} was banned | Reason: {reason}*')
                    except:
                        with open("cogs/logs.json") as f:
                            config = json.load(f)

                        log_channel = config.get(f"{ctx.guild.id}")
                        logs = self.client.get_channel(log_channel)

                        if log_channel != "None":
                            embed=discord.Embed(title=f"Member Banned",description=f"**{ctx.author.mention} has been banned by{ctx.channel.mention}**\n\n **Reason**\n {reason}",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                            embed.set_footer(text=f"ID: {ctx.author.id}")
                            embed.set_thumbnail(url=ctx.author.avatar_url)

                            await logs.send(embed=embed)
                        else:
                            pass

                        await member.ban()
                        await ctx.send(f'*{member} was banned | Reason: {reason}*')
                except:
                    await ctx.send(f"**Couldn't ban that user.**")
            else:
                try:
                    with open("cogs/logs.json") as f:
                        config = json.load(f)

                    log_channel = config.get(f"{ctx.guild.id}")
                    logs = self.client.get_channel(log_channel)

                    if log_channel != "None":
                        embed=discord.Embed(title=f"Member Banned",description=f"**{ctx.author.mention} has been banned by{ctx.channel.mention}**\n\n **Reason**\n {reason}",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                        embed.set_footer(text=f"ID: {ctx.author.id}")
                        embed.set_thumbnail(url=ctx.author.avatar_url)

                        await logs.send(embed=embed)
                    else:
                        pass

                    await member.ban(reason=reason)
                    await ctx.send(f'*{member} was banned | Reason: {reason}*')
                except:
                    await ctx.send(f"**Couldn't ban that user.**")

    @commands.command(
        name="lock",
        description="Locks mentioned channel.",
        usage="`a!lock (channel) (reason)`"
    )
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.has_permissions(manage_channels=True)
    async def lock(self,ctx,channel: discord.TextChannel = None,*,reason=None):
        if channel is None: channel = ctx.channel
        try:
            await channel.set_permissions(ctx.guild.default_role, overwrite=discord.PermissionOverwrite(send_messages = False), reason=reason)
            await ctx.send(f"*{ctx.channel.mention} has been locked. | Reason: {reason}*")
            
            with open("cogs/logs.json") as f:
                config = json.load(f)

            log_channel = config.get(f"{ctx.guild.id}")
            logs = self.client.get_channel(log_channel)

            if log_channel != "None":
                embed=discord.Embed(title=f"Channel Locked",description=f"**{channel.mention} has been locked by {ctx.author.mention}**\n\n **Reason**\n {reason}",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                embed.set_footer(text=f"ID: {ctx.author.id}")
                embed.set_thumbnail(url=ctx.author.avatar_url)

                await logs.send(embed=embed)
            else:
                pass

        except:
            await ctx.send(f"**{ctx.channel.mention} couldn't be locked.**")
        else:
            pass

    @commands.command(
        name="unlock",
        description="Unlocks mentioned channel.",
        usage="`a!unlock (channel) (reason)`"
    )
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.has_permissions(manage_channels=True)
    async def unlock(self,ctx,channel: discord.TextChannel=None,*,reason=None):
        if channel is None: channel = ctx.channel
        try:
            await channel.set_permissions(ctx.guild.default_role, overwrite=discord.PermissionOverwrite(send_messages = True), reason=reason)
            await ctx.send(f"*{ctx.channel.mention} has been unlocked. | Reason: {reason}*")

            with open("cogs/logs.json") as f:
                config = json.load(f)

            log_channel = config.get(f"{ctx.guild.id}")
            logs = self.client.get_channel(log_channel)

            if log_channel != "None":
                embed=discord.Embed(title=f"Channel Unlocked",description=f"**{channel.mention} has been unlocked by {ctx.author.mention}**\n\n **Reason**\n {reason}",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
                embed.set_footer(text=f"ID: {ctx.author.id}")
                embed.set_thumbnail(url=ctx.author.avatar_url)

                await logs.send(embed=embed)
            else:
                pass

        except:
            await ctx.send(f"**{ctx.channel.mention} couldn't be unlocked.**")
        else:
            pass

    @commands.command(
        name="purge",
        description="Purges entered amount of messages.",
        usage="`a!purge [amount]`"
    )
    @commands.bot_has_guild_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self,ctx, amount=5,reason=None):
        await ctx.channel.purge(limit=amount+1)

        with open("cogs/logs.json") as f:
            config = json.load(f)

        log_channel = config.get(f"{ctx.guild.id}")
        logs = self.client.get_channel(log_channel)

        if log_channel != "None":
            embed=discord.Embed(title=f"Messages Purged",description=f"**{ctx.author.mention} has purged {amount} messages in {ctx.channel.mention}**",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
            embed.set_footer(text=f"ID: {ctx.author.id}")
            embed.set_thumbnail(url=ctx.author.avatar_url)

            await logs.send(embed=embed)
        else:
            pass
            
    @commands.command(
        name="nuke",
        description="Deletes channel and clones it.",
        usage="`a!nuke`"
    )
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.has_permissions(manage_channels=True)
    async def nuke(self,ctx):
        with open("cogs/logs.json") as f:
            config = json.load(f)

        log_channel = config.get(f"{ctx.guild.id}")
        logs = self.client.get_channel(log_channel)

        if log_channel != "None":
            embed=discord.Embed(title=f"Channel Nuked",description=f"**{ctx.channel.name} has been nuked by {ctx.author.mention}**",timestamp=ctx.message.created_at,colour=discord.Colour.from_rgb(255,192,203))
            embed.set_footer(text=f"ID: {ctx.author.id}")
            embed.set_thumbnail(url=ctx.author.avatar_url)

            await logs.send(embed=embed)
        else:
            pass

        counter = 0
        await ctx.send(f"*Nuking {ctx.channel.name}...*")
        channel_info = [ctx.channel.category,
        ctx.channel.position]
        channel_id = ctx.channel.id
        await ctx.channel.clone()
        await ctx.channel.delete()
        new_channel = channel_info[0].text_channels[-1]
        await new_channel.edit(position=channel_info[1])
        embed = discord.Embed(colour=discord.Colour.from_rgb(255,192,203))
        embed.set_author(name=f"Successfully Nuked")
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_image(url="https://media.discordapp.net/attachments/720812237794574347/765218830418182204/200.gif?width=269&height=150")
        await new_channel.send(embed=embed)

        

    @commands.command(
        name="mute",
        description="Mutes mentioned user.",
        usage="`a!mute [@user] (reason)`"
    )
    @commands.bot_has_guild_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def mute(self,ctx, member: discord.Member, *, reason=None):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")

        if not muted:
            return await ctx.send("**Can't Find the Muted role.**")
        else:
            try:
                try:
                    await member.add_roles(muted)
                    await ctx.send(f'*{member.mention} has been muted. | Reason: {reason}*')

                    with open("cogs/logs.json") as f:
                        config = json.load(f)

                    log_channel = config.get(f"{ctx.guild.id}")
                    logs = self.client.get_channel(log_channel)

                    if log_channel != "None":
                        embed=discord.Embed(title=f"Member Muted",description=f"**{member.mention} has been muted by {ctx.author.mention}** \n\n **Reason**\n {reason}",colour=discord.Colour.from_rgb(255,192,203),timestamp=ctx.message.created_at)
                        embed.set_footer(text=f"ID: {ctx.message.author.id}")
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)

                        await logs.send(embed=embed)
                    else:
                        pass
                except:
                    await member.add_roles(muted)
                    await ctx.send(f'*{member.mention} has been muted. | Reason: {reason}*')

                    with open("cogs/logs.json") as f:
                        config = json.load(f)

                    log_channel = config.get(f"{ctx.guild.id}")
                    logs = self.client.get_channel(log_channel)

                    if log_channel != "None":
                        embed=discord.Embed(title=f"Member Muted",description=f"**{member.mention} has been muted by {ctx.author.mention}** \n\n **Reason**\n {reason}",colour=discord.Colour.from_rgb(255,192,203),timestamp=ctx.message.created_at)
                        embed.set_footer(text=f"ID: {ctx.message.author.id}")
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)

                        await logs.send(embed=embed)
                    else:
                        pass
            except:
                await ctx.send(f"**Cant Mute {member.mention}**")

    @commands.command(
        name="unmute",
        description="Umutes mentioned user.",
        usage="`a!unmute [@user] (reason)`"
    )
    @commands.bot_has_guild_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def unmute(self,ctx, member: discord.Member, *, reason=None):
        muted = discord.utils.get(ctx.guild.roles, name="Muted")

        if not muted:
            return await ctx.send(f"**{member.mention} is not muted.**")
        else:
            try:
                try:
                    await member.remove_roles(muted)
                    await ctx.send(f'*{member.mention} has been unmuted. | Reason: {reason}*')

                    with open("cogs/logs.json") as f:
                        config = json.load(f)

                    log_channel = config.get(f"{ctx.guild.id}")
                    logs = self.client.get_channel(log_channel)

                    if log_channel != "None":
                        embed=discord.Embed(title=f"Member Unmuted",description=f"**{member.mention} has been unmuted by {ctx.author.mention}** \n\n **Reason**\n {reason}",colour=discord.Colour.from_rgb(255,192,203),timestamp=ctx.message.created_at)
                        embed.set_footer(text=f"ID: {ctx.message.author.id}")
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)

                        await logs.send(embed=embed)
                    else:
                        pass
                except:
                    await member.remove_roles(muted)
                    await ctx.send(f'*{member.mention} has been unmuted. | Reason: {reason}*')

                    with open("cogs/logs.json") as f:
                        config = json.load(f)

                    log_channel = config.get(f"{ctx.guild.id}")
                    logs = self.client.get_channel(log_channel)

                    if log_channel != "None":
                        embed=discord.Embed(title=f"Member Unmuted",description=f"**{member.mention} has been unmuted by {ctx.author.mention}** \n\n **Reason**\n {reason}",colour=discord.Colour.from_rgb(255,192,203),timestamp=ctx.message.created_at)
                        embed.set_footer(text=f"ID: {ctx.message.author.id}")
                        embed.set_thumbnail(url=ctx.message.author.avatar_url)

                        await logs.send(embed=embed)
                    else:
                        pass
            except:
                await ctx.send(f"**Cant unmute that user.**")

    @commands.command(
        name="setup",
        description="Creates and setups mute role across all channels.",
        usage="`a!setup`"
    )
    @commands.bot_has_guild_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def setup(self,ctx):
        role = discord.utils.get(ctx.guild.roles, name="Muted") 
        if not role:
            try:
                muted = await ctx.guild.create_role(name="Muted", reason="To use for muting")
                for channel in ctx.guild.channels:
                    overwrite = channel.overwrites_for(ctx.guild.default_role)
                    if overwrite.view_channel == False:
                        pass
                    else:
                        await channel.set_permissions(muted, send_messages=False, read_message_history=True,read_messages=True)
            except:
                pass

            await ctx.send("*Succesfully setup Muted Role*")
    
    @commands.command(
        name="role",
        description="Add roles to mentioned user.",
        usage="`a!role [@user] [role]`"
    )
    @commands.bot_has_guild_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, user : discord.Member, *, role : discord.Role):
        if ctx.author.top_role < role:
            await ctx.send("**Can't add roles higher than you.**")
        elif ctx.author.top_role < user.top_role and ctx.author != ctx.guild.owner:
            await ctx.send(f"**Can't add roles to a member higher than you.**")
        else:
            try:
                await user.add_roles(role)
                await ctx.send(f"*Successfully given {user.mention} the role: {role}*")

                with open("cogs/logs.json") as f:
                    config = json.load(f)

                log_channel = config.get(f"{ctx.guild.id}")
                logs = self.client.get_channel(log_channel)

                if log_channel != "None":
                    embed=discord.Embed(title=f"Role Given",description=f"**{user.mention} was given the role {role.mention} by {ctx.author.mention}**",colour=discord.Colour.from_rgb(255,192,203),timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"ID: {ctx.message.author.id}")
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)

                    await logs.send(embed=embed)
                else:
                    pass
            except:
                await ctx.send(f"**Couldn't add roles to that user.**")

    @commands.command(
        name="drole",
        description="Removes roles from mentioned user.",
        usage="`a!drole [@user] [role]`"
    )
    @commands.bot_has_guild_permissions(manage_roles=True)
    @commands.has_permissions(manage_roles=True)
    async def drole(self, ctx, user : discord.Member, *, role : discord.Role):
        if ctx.author.top_role < role:
            await ctx.send("**Can't remove roles higher than you.**")
        elif ctx.author.top_role < user.top_role and ctx.author != ctx.guild.owner:
            await ctx.send(f"**Can't remove roles to a member higher than you.**")
        else:
            try:
                await user.remove_roles(role)
                await ctx.send(f"*Successfully Removed {user.mention} from: {role}*")

                with open("cogs/logs.json") as f:
                    config = json.load(f)

                log_channel = config.get(f"{ctx.guild.id}")
                logs = self.client.get_channel(log_channel)

                if log_channel != "None":
                    embed=discord.Embed(title=f"Role Removed",description=f"**{user.mention} was removed from the role {role.mention} by {ctx.author.mention}**",colour=discord.Colour.from_rgb(255,192,203),timestamp=ctx.message.created_at)
                    embed.set_footer(text=f"ID: {ctx.message.author.id}")
                    embed.set_thumbnail(url=ctx.message.author.avatar_url)

                    await logs.send(embed=embed)
                else:
                    pass
            except:
                await ctx.send(f"**Couldn't remove roles to that user.**")

    @commands.command(
        name="slowmode",
        description="Sets a slowmode for the channel.",
        usage="`a!slowmode [seconds]`",
    )
    @commands.bot_has_guild_permissions(manage_messages=True)
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds: int=0):
        if seconds > 120:
            return await ctx.send("**Amount can't be over 120 seconds.**")
        if seconds == 0:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send("*I have turned slowmode off.*")

            with open("cogs/logs.json") as f:
                config = json.load(f)

            log_channel = config.get(f"{ctx.guild.id}")
            logs = self.client.get_channel(log_channel)

            if log_channel != "None":
                embed=discord.Embed(title=f"Slowmode Disabled",description=f"**{ctx.author.mention} disabled slowmode for {ctx.channel.mention}**",colour=discord.Colour.from_rgb(255,192,203),timestamp=ctx.message.created_at)
                embed.set_footer(text=f"ID: {ctx.message.author.id}")
                embed.set_thumbnail(url=ctx.message.author.avatar_url)

                await logs.send(embed=embed)
            else:
                pass
        else:
            if seconds == 1:
                numofsecs = "second"
            else:    
                numofsecs = "seconds"
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"*Set channel delay to {seconds} {numofsecs}.*")

            with open("cogs/logs.json") as f:
                config = json.load(f)

            log_channel = config.get(f"{ctx.guild.id}")
            logs = self.client.get_channel(log_channel)

            if log_channel != "None":
                embed=discord.Embed(title=f"Slowmode Enabled",description=f"**{ctx.author.mention} enabled {seconds} {numofsecs} slowmode for {ctx.channel.mention}**",colour=discord.Colour.from_rgb(255,192,203),timestamp=ctx.message.created_at)
                embed.set_footer(text=f"ID: {ctx.message.author.id}")
                embed.set_thumbnail(url=ctx.message.author.avatar_url)

                await logs.send(embed=embed)
            else:
                pass

    @slowmode.error
    async def slowmode_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please enter a amount of seconds.**')

    @drole.error
    async def drole_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please specify a role.**')

    @role.error
    async def role_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please specify a role.**')
            
    @setup.error
    async def setup_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')

    @unmute.error
    async def unmute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')

    @mute.error
    async def mute_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')

    @nuke.error
    async def nuke_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')

    @lock.error
    async def lock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')

    @unlock.error
    async def unlock_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please mention a user to ban.**')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'**You are missing the permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f'**Bot missing permission: `{"".join(error.missing_perms)}`**')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**Please mention a user to kick.**')
        
def setup(client):
    client.add_cog(moderation(client))
