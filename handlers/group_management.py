from aiogram import Router, F, types
from aiogram.filters import Command


group_router = Router()
group_router.message.filter(F.chat.type != 'private')

@group_router.message()
async def echo_handler(message: types.Message):
    print(message.chat.type)
    # print(message.chat)
    await message.answer("Привет")

