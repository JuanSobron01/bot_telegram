from unicodedata import name
import telebot 
from telebot import types
from datetime import date
from datetime import datetime
bot = telebot.TeleBot("5522737361:AAHmy2-Ytqeqx8z3Bs6GchBf_88g19pu_IY")

@bot.message_handler(commands=["help","start"])

def start(message):
    #import pdb ; pdb.set_trace()
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Inicio", callback_data="Inicio") 
    button2 = types.InlineKeyboardButton(text="Argentina", callback_data="Argentina")
    button3 =  types.InlineKeyboardButton(text="Fixture", callback_data="fixture")
    button4 =  types.InlineKeyboardButton(text="Fixture Argentina", callback_data="fix_arg")
    button5 =  types.InlineKeyboardButton(text="Convocados Amistosos ", callback_data="conv_amis")
    button6 =  types.InlineKeyboardButton(text="Amistosos", callback_data="amistosos")

    markup.add(button1, button2,button3,button4,button5,button6)
    bot.send_message(chat_id=message.chat.id, text="Qatar 2022 ", reply_markup=markup)



@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    mundial = date(2022,11,20)
    argentina = date(2022,11,22)
    hoy = date.today()
    argentina_primer = argentina - hoy
    faltan = mundial - hoy 
    if call.data == "Inicio":
        bot.send_message(call.message.chat.id, 'Faltan %s dias para el mundial :soccer_ball:' %faltan.days)
    if call.data == "Argentina":
        bot.send_message(call.message.chat.id,'Faltan %s dias para que juegue la Seleccion %s' %(argentina_primer.days, '\U0001F1E6'))
    if call.data == "fixture":
        fixture = open("test_bot/fixturemundial.png","rb")
        bot.send_photo(call.message.chat.id,fixture,"Andas manija %s Fixture Mundial :soccer_ball:" %call.message.chat.first_name )
    if call.data == "fix_arg":
        fixture = open("test_bot/fixarg.jpg","rb")
        bot.send_photo(call.message.chat.id,fixture,"Fixture Argentina")
    if call.data == "conv_amis":
        fixture = open("test_bot/convocados.jpg","rb")
        bot.send_photo(call.message.chat.id,fixture,"Hola %s Convocados Amistosos :soccer_ball:" %call.message.chat.first_name )
    if call.data == "amistosos":
        fixture = open("test_bot/amistoso.png","rb")
        bot.send_photo(call.message.chat.id,fixture,"Amistosos" )

def enviar(mensaje):
    bot.reply_to(mensaje,'Buenos dias! ') #repite y responde /start

@bot.message_handler(content_types=["text"])
def mensaje_texto(message):
    mundial = date(2022,11,20)
    hoy = date.today()
    faltan = mundial - hoy 
    print(faltan)
    if message.text.startswith("/"):
        bot.send_message(message.chat.id,'Comando no disponible')
    else:
        bot.send_message(message.chat.id,'Faltan %s dias para el mundial ' %faltan.days)




bot.polling()

if __name__ == '__main__':
    print('Iniciando bot')
    bot.infinity_polling()
    print('Fin')