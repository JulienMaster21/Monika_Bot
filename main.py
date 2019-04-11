import discord
import os
import re
import sys
import random
import asyncio
from datetime import datetime, timedelta
from configparser import ConfigParser

client = discord.Client()
path = os.path.dirname(os.path.realpath(__file__))

config = ConfigParser()
config.read("{}/config.ini".format(path))

# lists = ConfigParser()
# lists.read("{}/lists.ini".format(path))

prefix = config.get("DEFAULT", "prefix")
# command_list = lists.get("DEFAULT", "command_list")
# woutmees_list = lists.get("DEFAULT", "woutmees_list")

def randomNum (min, max):
    return random.randint(min, max)

def start ():
    loop = asyncio.get_event_loop()
    # client.start(config.get("DEFAULT", "token"), loop=loop)
    client.run(config.get("DEFAULT", "token"), loop=loop)
    with open("{}/config.ini".format(path), "w") as cfg_file:
        config.write(cfg_file)

command_list =  [
                    {
                        "name" : "hello monika",
                        "description" : "-greet me"
                    },
                    {
                        "name" : "i love you monika",
                        "description" : "-tell me you love me"
                    },
                    {
                        "name" : "just monika",
                        "description" : "-tell me you only need me"
                    },
                    {
                        "name" : "monika is best girl",
                        "description" : "-tell me i'm the best girl"
                    },
                    {
                        "name" : "DDLC injection",
                        "description" : "-get a quick, but concentrated dose of DDLC"
                    },
                    {
                        "name" : "roll <number>",
                        "description" : "-Roll a dice"
                    },
                    {
                        "name" : "mention <member>",
                        "description" : "-mention someone in the server"
                    },
                    {
                        "name" : "kick <member>",
                        "description" : "-kick someone from the server"
                    },
                    {
                        "name" : "ban <member>",
                        "description" : "-ban someone from the server"
                    },
                    {
                        "name" : "unban <user>",
                        "description" : "-unban someone from the server"
                    },
                    {
                        "name" : "prefix",
                        "description" : "-show what the prefix is for commands"
                    },
                    {
                        "name" : "change prefix <value>",
                        "description" : "-change what prefix is used for commands"
                    },
                    {
                        "name" : "clear",
                        "description" : "-delete all messages"
                    },
                    {
                        "name" : "restart",
                        "description" : "-tell monika to restart"
                    },
                    {
                        "name" : "exit",
                        "description" : "-tell monika to go offline"
                    },
                ]

woutmees_list = [
                    {
                        "name" : "Sayori discovers Cookie Clicker",
                        "url" : "https://www.youtube.com/watch?v=fpkvZhX_djg",
                        "image" : "https://i.ytimg.com/vi/fpkvZhX_djg/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLA-6L8j5VSrXEs3wEIZYHL--_LJnA"
                    },
                    {
                        "name" : "Vista",
                        "url" : "https://www.youtube.com/watch?v=YuCuM5p1m2Q",
                        "image" : "https://i.ytimg.com/vi/YuCuM5p1m2Q/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAQq3SGtiZiQt16Bg_ZtQH1DIVNNg"
                    },
                    {
                        "name" : "HHHNNNNGGGGGGGGGGG",
                        "url" : "https://www.youtube.com/watch?v=0g1AlShR0XY",
                        "image" : "https://i.ytimg.com/vi/0g1AlShR0XY/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBxZTfLqn_n9EexN8zIYvwa4YdeGg"
                    },
                    {
                        "name" : "Doki Doki Chibi Soldiers 2: Ȩl͟ec҉tr̢i͢c ͏Bo͠òp-a͡l̢o̵o",
                        "url" : "https://www.youtube.com/watch?v=qNvLlrGti5Q",
                        "image" : "https://i.ytimg.com/vi/qNvLlrGti5Q/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBOoJoHgmWcej7C1bAL2xefSCUFkw"
                    },
                    {
                        "name" : "THE CAKE!! IT BURNS BURNS BURNS!!",
                        "url" : "https://www.youtube.com/watch?v=5B_WcjmfPQw",
                        "image" : "https://i.ytimg.com/vi/5B_WcjmfPQw/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCW70slSK9ztDoOHThuCKoHrN2j9g"
                    },
                    {
                        "name" : "DON'T PLAY A GAME CALLED DOKI DOKI",
                        "url" : "https://www.youtube.com/watch?v=h1_36S38sVE",
                        "image" : "https://i.ytimg.com/vi/h1_36S38sVE/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCK-p2AoUb587yLcHTEdtUV-2TcIg"
                    },
                    {
                        "name" : "DEPRESSION :the game:",
                        "url" : "https://www.youtube.com/watch?v=mILZQDSpT8w",
                        "image" : "https://i.ytimg.com/vi/mILZQDSpT8w/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLATVm3l1TK_7mm6Bj5YleVB8j217w"
                    },
                    {
                        "name" : "Yuri meets a new friend",
                        "url" : "https://www.youtube.com/watch?v=Xqhl5xiFdi8",
                        "image" : "https://i.ytimg.com/vi/Xqhl5xiFdi8/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLB8Oo_HKpdeAathuEImmujAF0MIzg"
                    },
                    {
                        "name" : "Monika Snaps",
                        "url" : "https://www.youtube.com/watch?v=FxfHHsrzHfo",
                        "image" : "https://i.ytimg.com/vi/FxfHHsrzHfo/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLC1BdB7pqn2kgXdVFMC5Dzutaq3DQ"
                    },
                    {
                        "name" : "Sayori Walks Home",
                        "url" : "https://www.youtube.com/watch?v=re8kUBC4CTA",
                        "image" : "https://i.ytimg.com/vi/re8kUBC4CTA/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAViesNpG65EC3A2tOZEsBrp1cC-Q"
                    },
                    {
                        "name" : "MONIKA CAN'T DECIDE",
                        "url" : "https://www.youtube.com/watch?v=MTWLaRwT_14",
                        "image" : "https://i.ytimg.com/vi/MTWLaRwT_14/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBmMZb-NpiwXXP0cNZ_Y0QG29p02Q"
                    },
                    {
                        "name" : "Monika's Beach Ball Story",
                        "url" : "https://www.youtube.com/watch?v=zdNzooDXQes",
                        "image" : "https://i.ytimg.com/vi/zdNzooDXQes/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAQVyRzRsHwwG-epjgjC3pAmUYACA"
                    },
                    {
                        "name" : "Clocki Clocki Cliterature Club",
                        "url" : "https://www.youtube.com/watch?v=8E_1OTNid2M",
                        "image" : "https://i.ytimg.com/vi/8E_1OTNid2M/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCfwsKv7THa3RhIlQYQaoTH4lkn1Q"
                    },
                    {
                        "name" : "test video please do not doki",
                        "url" : "https://www.youtube.com/watch?v=Q0M5gf1r_Ik",
                        "image" : "https://i.ytimg.com/vi/Q0M5gf1r_Ik/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCtDsPXk7bHPV4fC-EKd6p7xXrggg"
                    },
                    {
                        "name" : "DON'T STOP HER NOW",
                        "url" : "https://www.youtube.com/watch?v=Ibpohmt9TwI",
                        "image" : "https://i.ytimg.com/vi/Ibpohmt9TwI/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBHbz7Cnn2wlurnJtywjoVYZuA_BA"
                    },
                    {
                        "name" : "The Ballad of Natsuki's Dad",
                        "url" : "https://www.youtube.com/watch?v=d4AYObbFTu4",
                        "image" : "https://i.ytimg.com/vi/d4AYObbFTu4/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLD3iOrdHU84R3RQz1TrxGKvOi-JDg"
                    },
                    {
                        "name" : "Sayori's Bow Explodes and then She Honks like a Goose",
                        "url" : "https://www.youtube.com/watch?v=QHqbyrsMv9w",
                        "image" : "https://i.ytimg.com/vi/QHqbyrsMv9w/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAfLSuNym_7b0a3OvLKGlLXIwELhA"
                    },
                    {
                        "name" : "THIS SMILE",
                        "url" : "https://www.youtube.com/watch?v=T6KGjLts_vU",
                        "image" : "https://i.ytimg.com/vi/T6KGjLts_vU/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAbewt7MUYNdkkR6t8nBWx1euEzjw"
                    },
                    {
                        "name" : "Doki Doki Chibi Soldiers",
                        "url" : "https://www.youtube.com/watch?v=MKNGYPGoNdw",
                        "image" : "https://i.ytimg.com/vi/MKNGYPGoNdw/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLA3rXYqDYrDW-FrJxN60kolDhLO_g"
                    },
                    {
                        "name" : ":D",
                        "url" : "https://www.youtube.com/watch?v=nWPbzOOOz6w",
                        "image" : "https://i.ytimg.com/vi/nWPbzOOOz6w/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBbyCLEvXvCwuB7_AQQb423NXXmQQ"
                    },
                    {
                        "name" : "Dawn of Doki",
                        "url" : "https://www.youtube.com/watch?v=0cw6y_274Tw",
                        "image" : "https://i.ytimg.com/vi/0cw6y_274Tw/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAmw9njuTv7g3BtWH_2l-9I7yvYzw"
                    },
                    {
                        "name" : "JUMP IN THE CAAC",
                        "url" : "https://www.youtube.com/watch?v=Jv6m8xCd0jQ",
                        "image" : "https://i.ytimg.com/vi/Jv6m8xCd0jQ/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCmZktTeen7sWR5KtgQQbFzSWbaDA"
                    },
                    {
                        "name" : "DOKIS COMBINE!!",
                        "url" : "https://www.youtube.com/watch?v=9Tnu3vNi5ZY",
                        "image" : "https://i.ytimg.com/vi/9Tnu3vNi5ZY/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLDI4IEOsjlc80dEHUo0grjDCo4jlQ"
                    },
                    {
                        "name" : "Just a Bit Doki",
                        "url" : "https://www.youtube.com/watch?v=I3dQpzCO-Lo",
                        "image" : "https://i.ytimg.com/vi/I3dQpzCO-Lo/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLB3aWT77_SBKPr7GS77y3M_nx5vLw"
                    },
                    {
                        "name" : "DOKIDO [Popipo x Doki Doki Literature Club crossover]",
                        "url" : "https://www.youtube.com/watch?v=BbHQ33ZZSV8",
                        "image" : "https://i.ytimg.com/vi/BbHQ33ZZSV8/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLCS_IaXHpsE657jSVyQdm3ccZqnjg"
                    },
                    {
                        "name" : "SAYORIQUEST",
                        "url" : "https://www.youtube.com/watch?v=XDNpufX5e_Q",
                        "image" : "https://i.ytimg.com/vi/XDNpufX5e_Q/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLBImqJDxpR9LJLk4PSVf8TVaoW7Rg"
                    },
                    {
                        "name" : "Monika is Coming to Town - A DDLC Christmas Song",
                        "url" : "https://www.youtube.com/watch?v=62O-mdyNlYo",
                        "image" : "https://i.ytimg.com/vi/62O-mdyNlYo/hqdefault.jpg?sqp=-oaymwEZCNACELwBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLDtxS9N3XilDQkAs4ptvdpPaa5leQ"
                    },
                    {
                        "name" : "Monika Eats Waffles",
                        "url" : "https://www.youtube.com/watch?v=VNK55bjfl08",
                        "image" : "https://i.ytimg.com/vi/VNK55bjfl08/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLAxHGGuczJR2Z2ysa6b9rDnzXSjpg"
                    },
                    {
                        "name" : "Rhythm Heaven Club - Yandere Slice",
                        "url" : "https://www.youtube.com/watch?v=om1plRja-vg",
                        "image" : "https://i.ytimg.com/vi/om1plRja-vg/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLB94BttOntrguTLs9y5w7vFktLyNA"
                    },
                    {
                        "name" : "Sayoriquest Mashup Megamix (April Fools)",
                        "url" : "https://www.youtube.com/watch?v=P7nEiJ4UhYY",
                        "image" : "https://i.ytimg.com/vi/P7nEiJ4UhYY/hqdefault.jpg?sqp=-oaymwEZCPYBEIoBSFXyq4qpAwsIARUAAIhCGAFwAQ==&rs=AOn4CLD5oquk-_tOjvqm1v_NkKqYkL4z8Q"
                    },
                ]

@client.event
async def on_ready():
    print("Woke up Monika.")
    await client.send_message(client.get_channel("543053709786087454"), "Hello everybody.")
    await client.change_presence(game=discord.Game(name="Hosting the literature club."))

@client.event
async def on_message(message):
    global prefix
    # Prevent Monika from reacting to bots
    if message.author.bot:
        return
    message_arguments = re.findall(r'(?:[^\s"]|"(?:\\.|[^"])*")+', message.content[len(prefix):])
    # Show Menu
    if message.content == "{}menu".format(prefix) or message.content == "{}help".format(prefix):
        menu = discord.Embed(
            title = "Menu",
            colour = 0x50C878
        )
        for i in range(0, len(command_list)):
            menu.add_field( name = "{}{}".format(prefix, command_list[i]["name"]),
                            value = command_list[i]["description"],
                            inline = False)
        await client.send_message(message.channel, embed=menu)
    # React to hello
    elif message.content == "{}hello monika".format(prefix):
        await client.send_message(message.channel, "Hello {}.".format(message.author.name))
    # React to I love you
    elif message.content == "{}i love you monika".format(prefix):
        await client.add_reaction(message, "❤")
        await client.send_message(message.channel, "I love you too, {}.".format(message.author.name))
    # React to Just Monika
    elif message.content == "{}just monika".format(prefix):
        await client.add_reaction(message, "❤")
        await client.send_message(message.channel, "Just me.")
    # React to best girl
    elif message.content == "{}monika is best girl".format(prefix):
        await client.add_reaction(message, "❤")
    # Show a short DDLC video
    elif message.content == "{}DDLC injection".format(prefix):
        selection = randomNum(0, len(woutmees_list) - 1)
        #woutmees_video = discord.Embed(
            #title = woutmees_list[selection]["name"],
            #description = woutmees_list[selection]["url"],
            #url = woutmees_list[selection]["url"],
            #colour = 0xFFC0CB
        #)
        #woutmees_video.set_image(url = woutmees_list[selection]["image"])
        #await client.send_message(message.channel, embed=woutmees_video)
        await client.send_message(message.channel, woutmees_list[selection]["url"])
    elif message.content.startswith("{}roll".format(prefix)):
        input = message_arguments[1]
        await client.send_message(message.channel, "You rolled a {}.".format(randomNum(1, int(input))))
    # Mention someone on the server
    elif message.content.startswith("{}mention".format(prefix)):
        input = message_arguments[1]
        try:
            if (int(input)):
                if (input in (o.id for o in message.server.members)):
                    await client.send_message(message.channel, "<@{}>".format(input))
                else:
                    await client.send_message(message.channel, "That user is not on the server.")
        except ValueError:
            for o in message.server.members:
                if (input == o.name):
                    await client.send_message(message.channel, "<@{}>".format(o.id))
                    break
            else:
                await client.send_message(message.channel, "That user is not on the server.")
    # Kick someone from the server
    elif message.content.startswith("{}kick".format(prefix)):
        input = message_arguments[1]
        try:
            if (int(input)):
                for o in message.server.members:
                    if (input == o.id):
                        await client.kick(message.server.get_member(o.id))
                        await client.send_message(message.channel, "{} has been kicked out of the literature club.".format(o.name))
                        break
                else:
                    await client.send_message(message.channel, "That user is not on the server.")
        except ValueError:
            for o in message.server.members:
                if (input == o.name):
                    await client.kick(message.server.get_member(o.id))
                    await client.send_message(message.channel, "{} has been kicked out of the literature club.".format(o.name))
                    break
            else:
                await client.send_message(message.channel, "That user is not on the server.")
    # Ban someone from the server
    elif message.content.startswith("{}ban".format(prefix)):
        input = message_arguments[1]
        try:
            if (int(input)):
                for o in message.server.members:
                    if (input == o.id):
                        await client.ban(message.server.get_member(o.id), 0)
                        await client.send_message(message.channel, "{}.chr has been deleted.".format(o.name))
                        break
                else:
                    await client.send_message(message.channel, "That user is not on the server.")
        except ValueError:
            for o in message.server.members:
                if (input == o.name):
                    await client.ban(message.server.get_member(o.id), 0)
                    await client.send_message(message.channel, "{}.chr has been deleted.".format(o.name))
                    break
            else:
                await client.send_message(message.channel, "That user is not on the server.")
    # Unban someone from the server
    elif message.content.startswith("{}unban".format(prefix)):
        input = message_arguments[1]
        try:
            if (client.get_user_info(input)):
                await client.unban(message.server, await client.get_user_info(input))
                await client.send_message(message.channel, "{}.chr has been restored.".format(await client.get_user_info(input)))
            else:
                await client.send_message(message.channel, "That user is not on the server.")
        except:
            await client.send_message(message.channel, "That is not a valid input.")
    # Show what prefix the bot uses
    elif message.content == "{}prefix".format(prefix):
        await client.send_message(message.channel, "The prefix for commands is `{}`.".format(prefix))
    # Change wat prefix the bot uses
    elif message.content.startswith("{}change prefix".format(prefix)):
        config.set("DEFAULT", "prefix", message_arguments[2])
        prefix = config.get("DEFAULT", "prefix")
        await client.send_message(message.channel, "The prefix is now `{}`.".format(prefix))
    # Clear all messages
    elif message.content == "{}clear".format(prefix):
        await client.purge_from(message.channel, limit=100, after=datetime.today() - timedelta(days=14))
    # Restart Monika
    elif message.content == "{}restart".format(prefix):
        await client.send_message(message.channel, "Goodbye everybody.")
        #await client.close()
        #start()
    # Close Monika
    elif message.content == "{}exit".format(prefix):
        await client.send_message(message.channel, "Goodbye everybody.")
        await client.close()

start()
