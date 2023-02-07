from bot_create import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command


@dp.message_handler(Command(['start']))
async def com_start(message: types.Message):
    await message.answer('Привет тебе!')


@dp.message_handler(Command(['help']))
async def com_help(message: types.Message):
    await message.answer('Здесь могла бы быть справка')


@dp.message_handler()
async def com_any_other(message: types.Message):
    await message.answer(f'{message.from_user.full_name}, смотри, что я поймал - {message.text}')
