from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
import yaml
import re

tk = yaml.load(open('bot_token.yaml', 'r'))
updater = Updater(token=tk['token'])
dispatcher = updater.dispatcher


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hey Roman send me your expenses in format '^-?\d+\s.+[01]$")


def process_string(bot, update):
    msg = update.message.text
    date_ = update.message.date
    if re.match('^-?\d+\s.+[01]$', msg):
        process_msg(msg, date_)
        bot.send_message(chat_id=update.message.chat_id, text='Message has been processed')
    else:
        bot.send_message(chat_id=update.message.chat_id, text='Wrong message format, try again')


def process_msg(msg, date_):
    res = [date_.strftime('%d/%m/%Y')]
    value, category = msg.split(' ')
    category, is_cash = category[:-1].title(), category[-1]
    res.append('Expense') if float(value) < 0 else res.append('Income')
    res.append(value)
    res.append('-') if category != 'Cashed' else res.append('Cashed')
    res.append(category), res.append('Me'), res.append('-'), res.append(is_cash)
    with open('bot.txt', 'a') as f:
        f.write('\t'.join(res) + '\n')
        if category == 'Cashed':
            res_cash = res.copy()
            res_cash[1], res_cash[2], res_cash[-1] = 'Income', str(abs(int(res_cash[2]))), '1'
            f.write('\t'.join(res_cash) + '\n')


echo_handler = MessageHandler(Filters.text, process_string)
start_handler = CommandHandler('start', start)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(start_handler)
updater.start_polling()
