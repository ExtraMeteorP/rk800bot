import discord

TOKEN = 'NTI1Mjk4Mzk5MzMxODc2ODg1.DxtzlA._7BTbNo_lWIa-SiGI1rirCbdNFY'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!updateebt'):
        str = message.content.split(" ");
        embed=discord.Embed(title="ExtraBotany Update", description="An Addon that expands your Botania experience and adds to more fun", color=0x00ff00, url = "https://minecraft.curseforge.com/projects/extrabotany")
        embed.set_thumbnail(url="https://media.forgecdn.net/avatars/163/934/636684452988167490.png")
        embed.set_footer(text="ExtraMeteorP", icon_url="https://i.loli.net/2018/12/20/5c1b8970ee6f8.jpg")

        embed.add_field(name="Minecraft Versions", value=str[1])
        embed.add_field(name="Mod Version", value=str[2])
        embed.add_field(name="Type", value=str[3])
        embed.add_field(name="Download", value="[CurseForge](https://minecraft.curseforge.com/projects/extrabotany/files/"+str[4]+"/download)")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!updatedr'):
        str = message.content.split(" ");
        embed=discord.Embed(title="CustomDailyReward Update", description="Giving highly customable daily rewards to dedicated players.", color=0x00ff00, url = "https://minecraft.curseforge.com/projects/custom-daily-reward")
        embed.set_thumbnail(url="https://media.forgecdn.net/avatars/176/834/636766679773826331.png")
        embed.set_footer(text="ExtraMeteorP", icon_url="https://i.loli.net/2018/12/20/5c1b8970ee6f8.jpg")

        embed.add_field(name="Minecraft Versions", value=str[1])
        embed.add_field(name="Mod Version", value=str[2])
        embed.add_field(name="Type", value=str[3])
        embed.add_field(name="Download", value="[CurseForge](https://minecraft.curseforge.com/projects/custom-daily-reward/files/"+str[4]+"/download)")
        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!Hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)


        @client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
