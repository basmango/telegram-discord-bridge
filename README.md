# telegram-discord-bridge 🌉
A Telegram Discord bridge made using Zero MQ and managed with Systemd

## Instructions
1. Clone this respository.
2. Create a discord bot with the necessary permissions, viewing channels, reading messages etc.
3. Make a telegram bot, and disable the privacy mode.
4. Invite the telegram bot to your group
5. Acquire the group id of your telegram group by inviting @RawDataBot to your group ( you must have a telegram username for this) alteratively get it via your bot itself (message.chat_id)
6. Make a `.env` file similar to the `.env.demo` file and enter all the required credentials.
7. Use the command ``pipenv shell`` , it should install the dependencies automatically.
8. Run the bot python scripts. (`telegram_bot.py`,`discord_bot.py`)

## TODO
1. Use Message embeds for discord.
2. Implement cross platform replies.
3. ~~Make systemd .service file for running scripts.~~
4. Improve configuration.
