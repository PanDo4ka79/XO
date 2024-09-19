import telebot
from extensions import CryptoConverter, APIException
from hgjfdk import token



bot=telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать! Чтобы узнать цену валюты, используйте следующий формат:\n"
                          "<base_currency> <quote_currency> <amount>\n\n"
                          "Example: USD EUR 100\n"
                          "Available currencies: USD, EUR, RUB\n"
                          "Use /values to see all available currencies.")


@bot.message_handler(commands=['values'])
def send_values(message):
    bot.reply_to(message, "Available currencies: USD, EUR, RUB")


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    try:
        parts = message.text.split()
        if len(parts) != 3:
            raise APIException('Invalid format. Use <base_currency> <quote_currency> <amount>.')

        base, quote, amount = parts
        amount = float(amount)
        if base not in ['USD', 'EUR', 'RUB'] or quote not in ['USD', 'EUR', 'RUB']:
            raise APIException('Invalid currency. Available currencies: USD, EUR, RUB.')

        price = CryptoConverter.get_price(base, quote, amount)
        bot.reply_to(message, f'{amount} {base} is equal to {price} {quote}.')

    except APIException as e:
        bot.reply_to(message, f'Error: {e}')
    except Exception as e:
        bot.reply_to(message, f'An unexpected error occurred: {e}')


bot.polling()
