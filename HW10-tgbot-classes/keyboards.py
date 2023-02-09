from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_main_menu = ReplyKeyboardMarkup(resize_keyboard=True)

btn_start = KeyboardButton('/start')
btn_help = KeyboardButton('/help')
btn_play = KeyboardButton('/play')
btn_info = KeyboardButton('/info')
btn_stop = KeyboardButton('/stop')

kb_main_menu.add(btn_start, btn_help)
kb_main_menu.add(btn_play, btn_info, btn_stop)