# Пожалуйста, игнорируйте этот файл. Это лишь черновик, в котором я пытался реализовать выбор валют в виде кнопок

import telebot
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

TOKEN = '1923148599:AAG2B5JTFG06mIC-8xPsfwm5FmqkRxM4FOc'

bots = telebot.TeleBot(TOKEN)


# --------------------------
def intro(bot, update):
    bot.message.reply_text(intro_message())


def select_base(bot, update):
    bot.message.reply_text(select_base_message(), reply_markup=select_base_keyboard())


def select_quote(bot, update):
    bot.message.reply_text(select_quote_message(), reply_markup=select_quote_keyboard())


# --------------------------

def select_base_keyboard():
    keyboard = [[InlineKeyboardButton('Dollar', callback_data='m1_1')],
                [InlineKeyboardButton('Euro', callback_data='m1_1')],
                [InlineKeyboardButton('Ruble', callback_data='m1_1')]]
    return InlineKeyboardMarkup(keyboard)


def select_quote_keyboard():
    keyboard = [[InlineKeyboardButton('US Dollar', callback_data='m1_1')],
                [InlineKeyboardButton('Euro', callback_data='m1_1')],
                [InlineKeyboardButton('Russian Ruble', callback_data='m1_1')]]
    return InlineKeyboardMarkup(keyboard)


# --------------------------
def intro_message():
    return 'Добро пожаловать в Currency Converter! Тут будет больше текста /values'


def select_quote_message():
    return 'Выберите из списка валюту, с которой будет производиться конвертация (quote):'


def select_base_message():
    return 'Выберите из списка валюту, в которую будет производиться конвертация (base):'


# --------------------------
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# --------------------------
updater = Updater('1923148599:AAG2B5JTFG06mIC-8xPsfwm5FmqkRxM4FOc', use_context=True)
updater.dispatcher.add_handler(CommandHandler('start', intro))
updater.dispatcher.add_handler(CommandHandler('values', select_quote))

updater.start_polling()
