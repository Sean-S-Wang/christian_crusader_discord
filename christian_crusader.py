from discord.ext.commands import Bot
from discord import Game
import random
from pathlib import Path
import re


BOT_PREFIX = "+"
token_config = open(str(Path("BotToken.config").absolute()))
TOKEN = token_config.readline().split()[0]


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
    smite_target = ''
    arg_count = 0
    if arg.__len__() == 0:
        smite_target = context.message.author.mention
        await client.say(random.choice(possible_responses) + ", " +
                         smite_target + "!")
    elif arg.__len__() == 1:
        smite_target = arg[0]
        await client.say(random.choice(possible_responses) + ", " +
                         smite_target + "!")
    else:
        for current_target in arg:
            arg_count = arg_count + 1
            if arg_count == arg.__len__():
                smite_target = smite_target + 'and ' + current_target
            else:
                smite_target = smite_target + current_target + ', '
        await client.say(random.choice(possible_responses) + ", " +
                         smite_target + "!")


@client.command(name="praise_user",
                description="Praises the user with holy words",
                brief="Praise the sun!",
                aliases=['praise', 'praiseuser'],
                pass_context=True)
async def praise_user(context, *arg):
    possible_responses = [
        'the best!',
        'awesome!',
        '... so christian right now',
        'going to heaven!'
    ]
    praise_target = ''
    arg_count = 0
    if arg.__len__() == 0:
        praise_target = context.message.author.mention
        await client.say(praise_target + " is " +
                         random.choice(possible_responses))
    elif arg.__len__() == 1:
        praise_target = arg[0]
        await client.say(praise_target + " is " +
                         random.choice(possible_responses))
    else:
        for current_target in arg:
            arg_count = arg_count + 1
            if arg_count == arg.__len__():
                praise_target = praise_target + 'and ' + current_target
            else:
                praise_target = praise_target + current_target + ', '
        await client.say(praise_target + " are " +
                         random.choice(possible_responses))


@client.command(name="cleanse",
                description="Changes who the crusader is playing with",
                brief="Who should the crusader play with?",
                aliases=['changepresence', 'change-presence', 'change_presence'],
                pass_context=True)
async def change_presence(context, *arg):
    target = ''
    if arg.__len__() == 0:
        target = 'sinners'
    else:
        for current_word in arg:
            target = target + ' ' + current_word
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
        'fück': 'frick',
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
        'damnit': 'dangit',
        'cunt': 'punt',
        'biatch': 'bleach',
        'smd': 'smp',
        'bitches': 'beaches',
        'tit': 'bit',
        'tits': 'bits',
        'lmfao': 'lmfba',
        'whore': 'princess',
        'slut': 'butt'
    }
    possible_retorts = [
        ', you vile creature....',
        ', you forget your place!',
        ', disgusting...',
        ', do you kiss your mother with that mouth?',
        ', may you rot in heck!',
        ', may Gosh have mercy on your soul...'
    ]
    message_string = message.content
    # regex pattern for stripping out non-alphanumeric and non-spaces
    pattern = re.compile(r"([^\s\w]|_)+")
    # Initialize bad word count
    bad_word_count = 0
    # Take out everything except alpha-numeric and spaces
    message_string = pattern.sub('', message_string)
    # Split string into individual words
    words_in_message = message_string.split()
    # Set to lowercase
    words_in_message = [word.lower() for word in words_in_message]
    # Don't respond to yourself
    if message.author.bot:
        return
    for key in bad_words.keys():
        if key in words_in_message:
            bad_word_count = bad_word_count + 1
            await client.send_message(message.channel, message.author.mention + random.choice(possible_retorts) +
                                      ' I suggest you change ' + key + ' to ' +
                                      bad_words[key])
    if bad_word_count > 2:
        await client.send_message(message.channel, 'So much sin! You cretin!')

    await client.process_commands(message)

client.run(TOKEN)
