from aiogram import Router, F, types
from aiogram.filters import Command


group_router = Router()
group_router.message.filter(F.chat.type != 'private')

BAD_WORDS = ("дурак", "тупой", "изгой")


@group_router.message(Command("ban", prefix="/!"))
async def ban_user_handler(message: types.Message):
    print(message.reply_to_message)
    if message.reply_to_message:
        author_id = message.reply_to_message.from_user.id
        await message.chat.ban(author_id)


@group_router.message(F.text)
async def echo_handler(message: types.Message):
    for word in BAD_WORDS:
        print(word)
        if word in message.text:
            await message.answer("Такое слово нельзя использовать")
            await message.delete()
    

