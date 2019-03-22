# christian_crusader_discord
Discord bot that replaces bad words with wholesome ones

Click this link to add this bot to your server:
[Christian Crusader](https://discordapp.com/api/oauth2/authorize?client_id=557729286048710669&permissions=0&scope=bot)

Bot Prefix is +, because crosses

# Setting up python environment
I use [anaconda](https://www.anaconda.com/distribution/#download-section) to set up my environments. You can do:
`conda env create -f environment.yml`

You can also set up the environment via pip:
`pip install -r requirements.txt`

# Running the bot
* Create a text file called BotToken.config: (i.e. `vim BotToken.config`)
* Copy/Paste your bot private bot token into this file. You can follow [this](https://discordpy.readthedocs.io/en/rewrite/discord.html) tutorial if you don't know how to find your bot token
* If you've set up your python environment correctly, running the bot should be as simple as:  
`python christian_crusader.py`
* You should see `crusader now ready for crusading!` display in the terminal if your bot is running successfully.
