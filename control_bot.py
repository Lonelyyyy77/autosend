from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from db import get_status, set_status, init_db
import asyncio

BOT_TOKEN = "ВАШ_BOT_TOKEN"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

init_db()

def get_keyboard():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Включить", callback_data="on")
    kb.add(InlineKeyboardButton(text="Выключить", callback_data="off"))

   return kb.as_markup()

@dp.message(CommandStart())
async def start(message: types.Message):
    status = get_status()
    await message.answer(
        f"Автоответчик сейчас: {'🟢 ВКЛ' if status else '🔴 ВЫКЛ'}",
        reply_markup=get_keyboard()
    )

@dp.callback_query()
async def toggle(callback: types.CallbackQuery):
    if callback.data == "on":
        set_status(True)
        text = "✅ Автоответчик включен."
    else:
        set_status(False)
        text = "⛔ Автоответчик выключен."

    await callback.message.edit_text(
        text,
        reply_markup=get_keyboard()
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())