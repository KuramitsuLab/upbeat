# -*- coding: utf-8 -*-

from slackbot.bot import respond_to
from slackbot.bot import listen_to
from slackbot.bot import default_reply


#from libs import my_functions





@respond_to('Hey,Siri')
def mention_func(message):
    message.reply('すみません、よく聞き取れませんでした。')

@listen_to('リッスン')
def listen_func(message):
    message.send('リッスンがやられたようだ。')
    message.reply('ふふふ、奴は四天王の中でも最弱。')
