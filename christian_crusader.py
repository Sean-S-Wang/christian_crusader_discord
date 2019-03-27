from discord.ext.commands import Bot
from discord import Game
import random
from pathlib import Path
import re
import json


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
    valid_argument_list = []
    arg_count = 0
    for argument in arg:
        if argument[1] is "@":
            valid_argument_list.append(argument)
    if valid_argument_list.__len__() == 0:
        smite_target = context.message.author.mention
        await client.say(random.choice(possible_responses) + ", " +
                         smite_target + "!")
    elif valid_argument_list.__len__() == 1:
        smite_target = valid_argument_list[0]
        await client.say(random.choice(possible_responses) + ", " +
                         smite_target + "!")
    else:
        for current_target in valid_argument_list:
            arg_count = arg_count + 1
            if arg_count == valid_argument_list.__len__():
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
    valid_argument_list = []
    arg_count = 0
    for argument in arg:
        if argument[1] is "@":
            valid_argument_list.append(argument)
    if valid_argument_list.__len__() == 0:
        praise_target = context.message.author.mention
        await client.say(praise_target + " is " +
                         random.choice(possible_responses))
    elif valid_argument_list.__len__() == 1:
        praise_target = valid_argument_list[0]
        await client.say(praise_target + " is " +
                         random.choice(possible_responses))
    else:
        for current_target in valid_argument_list:
            arg_count = arg_count + 1
            if arg_count == valid_argument_list.__len__():
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
    bad_words = json.load(open("bad_words.txt"))
    if arg.__len__() == 0:
        target = 'sinners'
    else:
        for current_word in arg:
            if current_word in bad_words.keys():
                await client.say(
                    "Do you take me for a fool, " + context.message.author.mention + "?")
                return
            else:
                target = target + ' ' + current_word
    await client.say("Seems that " + context.message.author.mention + " wants to cleanse the " + target +
                     ". So be it!")
    await client.change_presence(game=Game(name="with " + target))


@client.event
async def on_ready():
    await client.change_presence(game=Game(name="with sinners"))
    print(client.user.name + " ready for crusading!")


@client.event
async def on_message(message):
    bad_words = json.load(open("bad_words.txt"))
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
