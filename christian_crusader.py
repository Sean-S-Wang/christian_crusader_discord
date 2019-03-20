from discord.ext.commands import Bot
from discord import Game
import random
from BotToken import BotToken

BOT_PREFIX = "+"
TOKEN = BotToken().token


client = Bot(command_prefix=BOT_PREFIX)


@client.command(name= "smite_user",
                description="Smites a user with holy words",
                brief="Holy Smites",
                aliases=['smite', 'smite-user'],
                pass_context=True)
async def smite_user(context, *arg):
    possible_responses = [
        'That is unholy',
        'I smite thee',
        'BZZZZZZZZT',
        'tsk tsk'
    ]
    if arg.__len__() == 0:
        smite_target = context.message.author.mention
    else:
        smite_target = arg[0]
    await client.say(random.choice(possible_responses) + ", " +
                     smite_target + "!")


@client.command(name="praise_user",
                description="Praises the user with holy words",
                brief="Praise the sun!",
                aliases=['praise', 'praiseuser'],
                pass_context=True)
async def praise_user(context, *arg):
    possible_responses = [
        'is the best!',
        'is awesome!',
        '... so christian right now',
        'is going to heaven!'
    ]
    if arg.__len__() == 0:
        praise_target = context.message.author.mention
    else:
        praise_target = arg[0]
    await client.say(praise_target + " " +
                     random.choice(possible_responses))


@client.command(name="cleanse",
                description="Changes who the crusader is playing with",
                brief="Who should the crusader play with?",
                aliases=['changepresence', 'change-presence', 'change_presence'],
                pass_context=True)
async def change_presence(context, *arg):
    if arg.__len__() == 0:
        target = 'sinners'
    else:
        target = arg[0]
    await client.say("Seems that " + context.message.author.mention + " wants to cleanse the " + target + ". So be it!")
    await client.change_presence(game=Game(name="with " + target))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with sinners"))
    print(client.user.name + " ready for crusading!")


@client.event
async def on_message(message):
    bad_words = {
        'fuck': 'frick',
        'fucker': 'fricker',
        'fucking': 'fricking',
        'dick': 'duck',
        'bitching': 'blipping',
        'lmao': 'lmbo',
        'motherfucker': 'motherfricker',
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
    bad_word_count = 0
    words_in_message = message.content.split()
    words_in_message = [word.lower() for word in words_in_message]
    if message.author.bot:
        return
    for key in bad_words.keys():
        if key in words_in_message:
            bad_word_count = bad_word_count + 1
            await client.send_message(message.channel, 'That is unholy! I suggest you change ' + key + ' to ' +
                                      bad_words[key])
    if bad_word_count > 2:
        await client.send_message(message.channel, 'So much sin! You cretin!')

    await client.process_commands(message)

client.run(TOKEN)
