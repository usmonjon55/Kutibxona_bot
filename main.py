import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

API_TOKEN = '6290512650:AAEseEyo-5CEI4cZWspRvrl691n8PsxBJIU'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

bosh_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💿O'zbek adabiyoti💿"),
            KeyboardButton(text="💿Jahon adabiyoti💿")
        ],
        [
            KeyboardButton(text="💿Audio disklar💿")
        ],
        [
            KeyboardButton(text="💿Yangi audio kitoblar💿")
        ],
        [
            KeyboardButton(text="📧Murojaat uchun📧"),
        ]
    ],
    resize_keyboard=True
)

ozbek_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="O'tkan kunlar"),
            KeyboardButton(text="Mehrobdan chayon")
        ],
        [
            KeyboardButton(text="Ufq"),
            KeyboardButton(text="Kecha va kunduz")
        ],
        [
            KeyboardButton(text="Avlodlar dovoni"),
            KeyboardButton(text="Yulduzli tunlar")
        ],
        [
            KeyboardButton(text="Navoiy"),
            KeyboardButton(text="Ulug'bek xazinasi")
        ],
        [
            KeyboardButton(text="Oltin zanglamas"),
            KeyboardButton(text="Jannati odamlar")
        ],
        [
            KeyboardButton(text="Otamdan qolgan dalalar"),
            KeyboardButton(text="Bu dunyoda o'lib bo'lmaydi")
        ],
        [
            KeyboardButton(text="Yulduzlar mangu yonadi"),
            KeyboardButton(text="Ot kishnagan oqshom")
        ],
        [
            KeyboardButton(text="Ikki eshik orasi"),
            KeyboardButton(text="Dunyoning ishlari")
        ],
        [
            KeyboardButton(text="Daftar hoshiyasidagi bitiklar"),
            KeyboardButton(text="bahor qaytmaydi")
        ],
        [
            KeyboardButton(text="Tushda kechgan umrlar"),
            KeyboardButton(text="Nur borki soya bor")
        ],
        [
            KeyboardButton(text="Shum bola"),
            KeyboardButton(text="Bolalik")
        ],
        [
            KeyboardButton(text="Sohibqiron"),
            KeyboardButton(text="Ruhlar isyoni")
        ],
        [
             KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)


jahon_menu_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Choliqushi"),
            KeyboardButton(text="Qon da'vosi")
        ],
        [
            KeyboardButton(text="Martin Iden"),
            KeyboardButton(text="Hikoyalar(Jek London)")
        ],
        [
            KeyboardButton(text="Taras Bulba"),
            KeyboardButton(text="Usta va Margarita")
        ],
        [
            KeyboardButton(text="Sherlok Xolms"),
            KeyboardButton(text="Cho'qintirgan ota")
        ],
        [
            KeyboardButton(text="Alkimyogar"),
            KeyboardButton(text="Kichkina shaxzoda")
        ],
        [
            KeyboardButton(text="Asrga tatigulik kun"),
            KeyboardButton(text="Qiyomat")
        ],
        [
            KeyboardButton(text="Bahorning o'n yetti lahzasi"),
            KeyboardButton(text="Baxtiqaro Kerri")
        ],
        [
            KeyboardButton(text="Besh qavatli uyning oltinchi qavati"),
            KeyboardButton(text="Buzrukning kuzi")
        ],
        [
            KeyboardButton(text="Graf Monte Kristo"),
            KeyboardButton(text="Askanio")
        ],
        [
            KeyboardButton(text="Alvido Gulsari"),
            KeyboardButton(text="Bo'tako'z")
        ],
        [
            KeyboardButton(text="Don Kixot"),
            KeyboardButton(text="Yosh Vertnerning iztiroblari")
        ],
        [
            KeyboardButton(text="Og'ay ona"),
            KeyboardButton(text="Qaynona")
        ],
        [
            KeyboardButton(text="Da Vinchi siri"),
            KeyboardButton(text="Nur va soyalar")
        ],
        [
            KeyboardButton(text="Iqrornoma"),
            KeyboardButton(text="Vijdon azobi")
        ],
        [
            KeyboardButton(text="Ming quyosh shu'lasi"),
            KeyboardButton(text="Shamol ortidan yugurib")
        ],
        [
            KeyboardButton(text="Jamila"),
            KeyboardButton(text="Somon yo'li")
        ],
        [
            KeyboardButton(text="Chingizxonning oq buluti"),
            KeyboardButton(text="Oxirzamon nishonalari")
        ],
        [
            KeyboardButton(text="Menkim, Sohibqiron - Jahongir Temur"),
            KeyboardButton(text="Amir Temur saltanati")
        ],
        [
            KeyboardButton(text="Xazon bo'lgan muhabbat"),
            KeyboardButton(text="Ming bir kecha")
        ],
        [
             KeyboardButton(text="Orqaga")
        ]
    ],
    resize_keyboard=True
)





@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("""Assalomu alaykum! 

Botdan foydalanish uchun ushbu kanalga a'zo bo‘ling:
👉 https://t.me/usmonn_mars_bot

Используйте /off чтобы приостановить подписку.""", reply_markup=bosh_menu_keyboard)



@dp.message_handler(text="💿O'zbek adabiyoti💿")
async def send_welcome(message: types.Message):
    await message.answer("🔘 Tanlang", reply_markup=ozbek_menu_keyboard)

@dp.message_handler(text="💿Jahon adabiyoti💿")
async def send_welcome(message: types.Message):
    await message.answer("🔘 Tanlang", reply_markup=jahon_menu_keyboard)

@dp.message_handler(text="💿Audio disklar💿")
async def send_welcome(message: types.Message):
    await message.answer("Audio darsliklar bu yerda: @audio_darsliklar", reply_markup=bosh_menu_keyboard)


@dp.message_handler(text="💿Yangi audio kitoblar💿")
async def send_welcome(message: types.Message):
    await message.answer("""Yangi audio kitoblarni o‘tkazib yubormaslik uchun kanalimizga obuna bo‘lishni unutmang: 

t.me/audiokitoblar_uz


""", reply_markup=bosh_menu_keyboard)


@dp.message_handler(text="📧Murojaat uchun📧")
async def send_welcome(message: types.Message):
    await message.answer("""Murojaat uchun: 

@audiokitoblar_uzbot""", reply_markup=bosh_menu_keyboard)
    












@dp.message_handler(text="Orqaga")
async def echo(message: types.Message):
    await message.answer("Menu", reply_markup=bosh_menu_keyboard)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)