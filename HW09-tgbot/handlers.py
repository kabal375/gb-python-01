from bot_create import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
import game


@dp.message_handler(Command(['start']))
async def com_start(message: types.Message):
    await message.answer(f'Привет тебе, {message.from_user.full_name}! Сыграем в конфеты? Введи /help для справки')


@dp.message_handler(Command(['help']))
async def com_help(message: types.Message):
    await message.answer('Игра заключается в том, что ты и я будем по очереди брать конфеты из кучи. \
        Кто взял последнюю, тот победил \n')
    await message.answer(f'/total <число> - установка исходного количества конфет. По умолчанию: {game.default_total}')
    await message.answer(f'/max <число> - установка максимального количества конфет, \
        которое можно взять за ход. По умолчанию: {game.default_max_n}')
    await message.answer('/play - запуск игры в конфеты')
    await message.answer('/stop - досрочное завершение игры')


@dp.message_handler(Command(['total']))
async def com_total(message: types.Message):
    if game.is_started:
        await message.answer('Нельзя менять параметры во время игры')
    else:
        if game.set_total(message.text.split()[1]):
            await message.answer(f'Исходное количество конфет установлено - {game.total}')
        else:
            await message.answer(f'Указано некорректное значение. Введи число больше {game.min_total}')


@dp.message_handler(Command(['max']))
async def com_max(message: types.Message):
    if game.is_started:
        await message.answer('Нельзя менять параметры во время игры')
    else:   
        if game.set_max_n(message.text.split()[1]):
            await message.answer(f'Максимальное количество конфет, доступное за ход - {game.max_n}')
        else:
            await message.answer(f'Указано некорректное значение. Введи число больше {game.min_n}')


@dp.message_handler(Command(['play']))
async def com_play(message: types.Message):
    if game.is_started:
        await message.answer('Игра уже запущена!')
    else:
        game.start_game()
        await message.answer(f' Игра началась')
        await message.answer(f' Вводи количество конфет, которые хочешь взять из кучи. Но не больше, чем {game.max_n}')
        if game.is_players_turn:
            await message.answer('Твой ход первый')
        else:
            await message.answer('Первым ходит бот')

@dp.message_handler(Command(['stop']))
async def com_play(message: types.Message):
    game.end_game()
    await message.answer(f' Игра закончилась')
    await message.answer(f' Значения размера кучи конфет и количества за ход сброшены, но могут быть заданы снова')



@dp.message_handler()
async def com_any_other(message: types.Message):
    if message.text.isdigit() and game.is_started:
        if game.check_turn(int(message.text)):
            if game.total == 0:
                await message.answer('Конфеты кончились. Ты победил!')
                game.end_game()
                await message.answer(f' Значения размера кучи конфет и количества за ход сброшены, но могут быть заданы снова')
            else:
                game.bot_turn()
                if game.total == 0:
                    await message.answer('Конфеты кончились. Моя победа!')
                    game.end_game()
                    await message.answer(f' Значения размера кучи конфет и количества за ход сброшены, но могут быть заданы снова')
                else:
                    await message.answer(f'В куче осталось {game.total} конфет')
        else:
            await message.answer(f'Нельзя столько взять. Максимум: {min(game.max_n, game.total)} конфет')


    else: 
        await message.answer(f'{message.from_user.first_name}, смотри, что я поймал - {message.text}')
