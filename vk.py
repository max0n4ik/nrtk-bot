from operator import imod
from tkinter import PhotoImage
from vkbottle.bot import Bot, Message
# from tess import listpng
bot=Bot(token="779f454843f3d00257a308abe169a6d6a7140b2e7f4ae04fe98c952f1d0a1b154eac2ff4fa10e71267e10")
from vkbottle import PhotoMessageUploader


@bot.on.message(text="гет")
async def message_handler(message: Message):
    photo_upd=PhotoMessageUploader(bot.api)
    photo = await photo_upd.upload("page-0.png")
    await message.answer(attachment=photo)
 
bot.run_forever()