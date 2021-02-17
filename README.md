# Sci-Hub parser bot
Sci-Hub parser bot for Telegram, using PyTelegramBotApi

This bot can be used to getting documents from Sci-HUB using *DOI* for Telegram. 

### Installation and run
Using console:
```
git clone https://github.com/Antcating/Sci-Hub_parser_bot.git
cd Sci-Hub_parser_bot
python3 main.py
```

### Config

#### Initial Config
On the first run of the bot you will be asked to input Bot Token of your bot, that you can get from [@BotFather](t.me/BotFather). The token will be saved to config file and after that you won't be asked to input it again. Initial configuration is over. 
Addiction information about Bot API and etc. can be found on the main page of the [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI). 

### Usage

*/start* - start the program.\
After applying  */start* bot will show the keyboard with *Get Document* button. You should simply press this button and input DOI of the searching document. Bot will return the document.

Also can be used commands with same names.

For each user can be created own config. 
All configs are saving, so after reboot the settings will not be reset.


### Related projects and thanks 
- [PyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) – telegram bot interaction.