# Discord bot for messaging

Python 3.10 code that successfully uses a Discord Bot to periodically post to a specified server.

## Getting started:

### Setting up environment

1. Make sure python3.10 and python3.10-venv are installed 
2. Run setup.sh 
3. Ask me for the discord_config.yml file which contains the bot and guild token keys

### Discord_config

token: your discord api token

guild: this is the server you want to access

channel: this is the channel you want to message in

message_files: list of txt files to read and send in the text channel specified


### Sending messages
Once the message_files are written to, calling repeat_bot.run() will write all the message_files to the channel

The repeat bot is set when ready to send the messages and close the client. If you would like to keep the bot in the channel get rid of the client.close. 
(Note the repeat function I have demonstrates how the bot can be active in channel)
