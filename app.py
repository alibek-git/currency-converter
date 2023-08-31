import telebot
from config import TOKEN, keys
from extensions import CryptoConverter, ConversionException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'To start, please enter the command in the following format\n<base currency> \
<currency to convert to> \
<the amount>\n To see the list of available currencies please run /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Currencies Available:'
    for key in keys.keys():
        text = '\n'.join((text, key, ))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConversionException('Wrong number of parameters')

        quote, base, amount = values
        total_base = CryptoConverter.get_price(quote, base, amount)
    except ConversionException as e:
        bot.reply_to(message, f'User Error \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Could not handle the command \n{e}')

    else:
        text = f'{amount} of {quote} in {base} equals {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
