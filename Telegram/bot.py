from unicodedata import name
import telebot 
from telebot import types
from datetime import date
import emoji
bot = telebot.TeleBot("5522737361:AAHmy2-Ytqeqx8z3Bs6GchBf_88g19pu_IY")

@bot.message_handler(commands=["help","start"])

def start(message):
    
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(text="Cuando arranca?🇶🇦", callback_data="Inicio") 
    button2 = types.InlineKeyboardButton(text="Cuando juega la Seleccion 🇦🇷", callback_data="Argentina")
    button3 =  types.InlineKeyboardButton(text="Fixture", callback_data="fixture")
    button4 =  types.InlineKeyboardButton(text="Fixture Argentina 🇦🇷 ⚽️", callback_data="fix_arg")
    button5 =  types.InlineKeyboardButton(text="Convocados Amistosos ", callback_data="conv_amis")
    button6 =  types.InlineKeyboardButton(text="Amistosos", callback_data="amistosos")
    button7 =  types.InlineKeyboardButton(text="⚽️Finalissima🏆", callback_data="finalisima")
    button8 = types.InlineKeyboardButton(text="Ayuda a los devs", callback_data="donar")
    markup.add(button1, button2,button3,button4,button5,button6,button7,button8)
    bot.send_message(chat_id=message.chat.id, text=" 🇶🇦 Qatar 2022 ⚽️", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    
    mundial = date(2022,11,20)
    argentina = date(2022,11,22)
    hoy = date.today()
    argentina_primer = argentina - hoy
    faltan = mundial - hoy 
    if call.data == "Inicio":
        bot.send_message(call.message.chat.id, 'Faltan %s dias para el mundial ' %faltan.days)
    if call.data == "Argentina":
        bot.send_message(call.message.chat.id,'🇦🇷  Faltan %s dias para que juegue la Seleccion 🇦🇷 ' %(argentina_primer.days))
    if call.data == "fixture":
        fixture = open("test_bot/fixturemundial.png","rb")
        bot.send_photo(call.message.chat.id,fixture,"Andas manija %s. Aca tenes el fixture Mundial " %call.message.chat.first_name )
    if call.data == "fix_arg":
        fixture = open("test_bot/fixarg.jpg","rb")
        bot.send_photo(call.message.chat.id,fixture,"Fixture Argentina")
    if call.data == "conv_amis":
        fixture = open("test_bot/convocados.jpg","rb")
        bot.send_photo(call.message.chat.id,fixture,"Hola %s Convocados Amistosos " %call.message.chat.first_name )
        
    if call.data == "amistosos":
        fixture = open("test_bot/amistoso.png","rb")
        bot.send_photo(call.message.chat.id,fixture,"Amistosos" )
        bot.send_message(call.message.chat.id,"Agendate los partidos!")
        bot.send_message(call.message.chat.id, "https://calendar.google.com/event?action=TEMPLATE&tmeid=MmVjZWFldjNqZTNnMGYwYTVtdXZvamVscWEganVhbmNydXpzMjcyQG0&tmsrc=juancruzs272%40gmail.com")
        bot.send_message(call.message.chat.id, "https://calendar.google.com/event?action=TEMPLATE&tmeid=MmtkZWFldmk0NW5vNG8ycXZwamFyNGo2NDMganVhbmNydXpzMjcyQG0&tmsrc=juancruzs272%40gmail.com")
    
    if call.data == "donar":
        bot.send_message(call.message.chat.id, 'http://mpago.li/2cxGTgo')

    if call.data == 'finalisima':
        bot.send_video(chat_id=call.message.chat.id, video=open('test_bot/finalisima.mp4', 'rb'), supports_streaming=True)
   
@bot.message_handler(content_types=["text"])
def enviar(message):
    mundial = date(2022,11,20)
    hoy = date.today()
    faltan = mundial - hoy 
    papu = open("test_bot/papu.jpg",'rb')
    if message.text.startswith("/"):
        bot.send_message(message.chat.id,'Queres mas datos? /start')
    else:
        bot.send_message(message.chat.id,'Dale que falta solo %s , manija? '%faltan.days)
        bot.send_message(message.chat.id,'Mas info con /start')
        bot.send_photo(message.chat.id, papu,'Ya casi')
bot.polling()

if __name__ == '__main__':
    print('Iniciando bot')
    bot.infinity_polling()
    print('Fin')
    