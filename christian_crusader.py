from discord.ext.commands import Bot
from discord import Game
import random

BOT_PREFIX = ("+")
TOKEN = "NTU3NzI5Mjg2MDQ4NzEwNjY5.D3MmEw.aYERBIbNoxcwesqF6tTaxcV_ahg"


client = Bot(command_prefix=BOT_PREFIX)


@client.command(name= "smite_user",
                description="Smites a user with holy words",
                brief="Holy Smites",
                aliases=['smite', 'smite-user'],
                pass_context=True)
async def smite_user(context):
    possible_responses = [
        'That is unholy'
    ]
    await client.say(random.choice(possible_responses) + ", " +
                     context.message.author.mention + "!")


@client.command(name="praise_user",
                description="Praises the user with holy words",
                brief="Praise the sun!",
                aliases=['praise', 'praiseuser'],
                pass_context=True)
async def praise_user(context):
    possible_responses = [
        'is the best!',
        'is awesome!',
        '... so christian right now',
        'is going to heaven!'
    ]
    await client.say(context.message.author.mention + " " +
                     random.choice(possible_responses))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with sinners"))
    print(client.user.name + "Ready for crusading")


@client.event
async def on_message(message):
    bad_words = {
        'fuck': 'frick',
        'shit': 'poop',
        'bitch': 'blip',
        'hell': 'heck',
        'ass': 'butt',
        'asshole': 'butthole',
        'bastard': 'custard',
        'damn': 'dang',
        'dammit': 'dangit',
        'damnit': 'dangit'
    }
    if message.author.bot:
        return
    for key in bad_words.keys():
        if key in message.content:
            await client.send_message(message.channel, 'That is unholy! I suggest you change ' + key + ' to ' + bad_words[key])

    await client.process_commands(message)

client.run(TOKEN)
