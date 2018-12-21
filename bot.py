import discord

TOKEN = 'NTI1Mjk4Mzk5MzMxODc2ODg1.Dv531g.Z-uebPyLFQmPHgDOlzIaK9clHfk'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        embed = discord.Embed(title="[ExtraBotany Update]", colour=discord.Colour(0x18f64f), url="(https://minecraft.curseforge.com/projects/extrabotany)", description="An Addon that expands your Botania experience and adds to more fun", timestamp=datetime.datetime.utcfromtimestamp(1545221595))

        embed.set_thumbnail(url="https://media.forgecdn.net/avatars/163/934/636684452988167490.png")
        embed.set_footer(text="ExtraMeteorP", icon_url="https://i.loli.net/2018/12/20/5c1b8970ee6f8.jpg")

        embed.add_field(name="Minecraft Versions", value="1.12.2")
        embed.add_field(name="Mod Version", value="ExtraBotany-r1.1-49")
        embed.add_field(name="Type", value="Release")
        embed.add_field(name="Download", value="[CurseForge](https://minecraft.curseforge.com/projects/extrabotany/files/2650122/download)")
        await client.send_message(message.channel, embed=embed)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
