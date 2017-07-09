#coding: UTF-8
import re
from slackbot.bot import respond_to
from slackbot.bot import listen_to


@respond_to('@here', re.IGNORECASE)
def at_here_reply(message):
    message.reply('I don\'t like @here')
