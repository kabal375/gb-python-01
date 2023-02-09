from bot_create import dp
from aiogram import types
from aiogram.dispatcher.filters.builtin import Command, Text
from keyboards import kb_main_menu
from play import Play


@dp.message_handler(Command(['start']))
async def com_start(message: types.Message):
    await message.answer(f'Привет тебе, {message.from_user.full_name}! Сыграем в конфеты? Введи /help для справки',
                        reply_markup=kb_main_menu)


@dp.message_handler(Command(['help']))
async def com_help(message: types.Message):
    await message.answer('Игра заключается в том, что ты и я будем по очереди брать конфеты из кучи.' + \
        ' Кто взял последнюю, тот победил \n')
    await message.answer('/play - запуск игры в конфеты')
    await message.answer('/info (после запуска игры) - информация о текущем размере кучи и количестве конфет,' + \
        ' которое можно взять за ход')
    await message.answer('/stop - досрочное завершение игры')


@dp.message_handler(Command(['play']))
async def com_play(message: types.Message):
    game = Play.get_instance(Play, message.from_id)
    if game:
        await message.answer('Игра уже запущена!')
    else:
        game = Play.start_game(Play, message.from_user.first_name, message.from_id)
        await message.answer(f' Игра началась')
        await message.answer(f' Конфет в куче - {game.total}')
        await message.answer(f' Вводи количество конфет, которые хочешь взять из кучи. Но не больше, чем {game.max_n}')
        if game.is_players_turn:
            await message.answer('Твой ход первый')
        else:
            await message.answer(f'Я хожу первым! Забрал {game.bot_turn()}. В куче осталось {game.total}')
    print(message.from_user.full_name + ' joined')


@dp.message_handler(Command(['stop']))
async def com_stop(message: types.Message):
    game = Play.get_instance(Play, message.from_id)
    if game:
        Play.stop_game(Play, message.from_id)
        await message.answer('Игра прервана. Очень жаль :(')
    else:
        await message.answer('Игра не запущена. Нажмите /play для начала')


@dp.message_handler(Command(['info']))
async def com_info(message: types.Message):
    game = Play.get_instance(Play, message.from_id)
    if game:
        await message.answer(game.get_info())
    else:
        await message.answer('Игра не запущена. Нажмите /play для начала')


@dp.message_handler()
async def com_any_other(message: types.Message):
    game = Play.get_instance(Play, message.from_id)
    if message.text.isdigit() and game:
        if game.player_turn(int(message.text)):
            if game.check_win():
                await message.answer('Конфеты кончились. Ты победил!')
                Play.stop_game(Play, message.from_id)
            else:
                await message.answer(f'Забрал {game.bot_turn()}. В куче осталось {game.total}')
                if game.check_win():
                    await message.answer('Конфеты кончились. Моя победа!')
                    Play.stop_game(Play, message.from_id)
        else:
            await message.answer(f'Нельзя столько взять. Максимум: {min(game.max_n, game.total)} конфет')

    else:
        await message.answer('Что-то пошло не так. 🤷‍♂️ Попробуйте ещё раз')
