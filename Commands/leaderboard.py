import discord
from discord.ext import commands
import json
import datetime

class leaderboard:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(pass_context=True)
    async def top(self, ctx, amm):
        channel = ctx.message.channel

        with open('users.json', 'r') as fp:
            users = json.load(fp)

        high_score_list = sorted(users, key=lambda x : users[x].get('xp', 0), reverse=True)

        message = ''

        for number, user in enumerate(high_score_list[:int(amm)]):
            message += '{0}: This is <@{1}> with `{2}` xp\n'.format(number + 1, user, users[user].get('experience', 0))
            
        embed = discord.Embed(title = '', description = '', colour=0xf90000, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text='Made by Coco#6429')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.author.avatar_url)
        embed.add_field(name='Top command was executed', value=message, inline=False)
        
        await self.bot.say(embed=embed)

    @top.error
    async def top_handler(self, error, ctx):
        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(title = '', description = '', colour=0xf90000, timestamp=datetime.datetime.utcnow())
            embed.set_footer(text='Made by Coco#6429')
            embed.set_thumbnail(url=ctx.message.server.icon_url)
            embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.author.avatar_url)
            embed.add_field(name='Top command failed to execute', value='You need to specify how many people should be listed on the LeaderBoard', inline=False)

            await self.bot.say(embed=embed)

    @commands.command(pass_context=True)
    async def xp(self, ctx):
        with open('users.json') as f:
            xpamm = json.load(f)

        embed = discord.Embed(title = '', description = '', colour=0xf90000, timestamp=datetime.datetime.utcnow())
        embed.set_footer(text='Made by Coco#6429')
        embed.set_thumbnail(url=ctx.message.server.icon_url)
        embed.set_author(name=ctx.message.server.name, icon_url=ctx.message.author.avata&r_url)
        embed.add_field(name='Xp command was executed', value="<@{}> you currently have `{}` XP!".format(ctx.message.author.id, xpamm[ctx.message.author.id]['experience']), inline=False)

        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(leaderboard(bot))