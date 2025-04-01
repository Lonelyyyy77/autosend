import random
from telethon import TelegramClient, events
from db import get_status, init_db

api_id = 28429142
api_hash = "0520d9e4327f0efc7801f73c6a4c7e48"

client = TelegramClient('session', api_id, api_hash)

init_db()

busy_responses = [
    "Извини, сейчас не могу говорить.",
    "Я занят, напиши позже.",
    "Отвечу, как только смогу.",
    "Не могу сейчас ответить, извините."
]

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if event.out:
        return

    if get_status():
        reply = random.choice(busy_responses)
        await event.reply(reply)
        print(f"[Userbot] Ответил: {reply}")

def main():
    client.start()
    print("Userbot запущен.")
    client.run_until_disconnected()

if __name__ == '__main__':
    main()