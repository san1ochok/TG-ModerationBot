from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from handlers import client_system, admin_system

from configure.database import *
from configure.config import *

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)

client_system.register_handlers_client_system(dp)
admin_system.register_handlers_admin_system(dp)


@dp.message_handler(content_types=['new_chat_members'])
async def start(message):
    cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if cursor.fetchone() is None:
        InsertValue(message.from_user.first_name, message.from_user.id,
                    datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        for row in cursor.execute(f"SELECT joiningDate FROM users where id={message.from_user.id}"):
            print('New user:', message.from_user.id, '|', row[0])
        for tmStamp in cursor.execute(f"SELECT joiningDate FROM users where id={message.from_user.id}"):
            for plRep in cursor.execute(f"SELECT plRep FROM users where id={message.from_user.id}"):
                for mnRep in cursor.execute(f"SELECT mnRep FROM users where id={message.from_user.id}"):
                    await message.answer(
                        "⚡ *Новый пользователь в нашем чате:* [{username}](tg://user?id={userid})\n🕐 *В моей базе с:* `{timeStamp}`\n🔥 *Глобальная репутация:*  `{plRep} 🟢 / {mnRep} 🔴`"
                            .format(username=message.from_user.full_name, userid=message.from_user.id,
                                    timeStamp=tmStamp[0], plRep=plRep[0], mnRep=mnRep[0]),
                        parse_mode='MarkdownV2', disable_web_page_preview=True)


@dp.message_handler(text=['iam', 'я', '??'])
async def iam(message):
    for tmStamp in cursor.execute(f"SELECT joiningDate FROM users where id={message.from_user.id}"):
        for plRep in cursor.execute(f"SELECT plRep FROM users where id={message.from_user.id}"):
            for mnRep in cursor.execute(f"SELECT mnRep FROM users where id={message.from_user.id}"):
                await message.answer(
                    "⚡ *Ваш никнейм:* [{username}](tg://user?id={userid})\n🕐 *В моей базе с:* `{timeStamp}`\n🔥 *Глобальная репутация:*  `{plRep} 🟢 / {mnRep} 🔴`"
                        .format(username=message.from_user.full_name, userid=message.from_user.id,
                                timeStamp=tmStamp[0], plRep=plRep[0], mnRep=mnRep[0]),
                    parse_mode='MarkdownV2', disable_web_page_preview=True)


@dp.message_handler(text=['who', 'кто'])
async def iam(message):
    if not message.reply_to_message:
        pass
    else:
        for tmStamp in cursor.execute(
                f"SELECT joiningDate FROM users where id={message.reply_to_message.from_user.id}"):
            for plRep in cursor.execute(f"SELECT plRep FROM users where id={message.reply_to_message.from_user.id}"):
                for mnRep in cursor.execute(
                        f"SELECT mnRep FROM users where id={message.reply_to_message.from_user.id}"):
                    await message.reply(
                        "⚡ *Никнейм:* [{username}](tg://user?id={userid})\n🕐 *В моей базе с:* `{timeStamp}`\n🔥 *Глобальная репутация:*  `{plRep} 🟢 / {mnRep} 🔴`"
                            .format(username=message.reply_to_message.from_user.full_name,
                                    userid=message.reply_to_message.from_user.id,
                                    timeStamp=tmStamp[0], plRep=plRep[0], mnRep=mnRep[0]),
                        parse_mode='MarkdownV2', disable_web_page_preview=True)


thank_words = ['спасибо', 'спс', 'дякую', 'сенкс', 'фенк', 'спасибі', 'thx', 'thanks', 'thank']


@dp.message_handler()
async def start(message):
    cursor.execute(f"SELECT name FROM users where id = {message.from_user.id}")
    if cursor.fetchone() is None:
        InsertValue(message.from_user.first_name, message.from_user.id,
                    datetime.now().strftime('%Y/%m/%d %H:%M:%S'))
        for row in cursor.execute(f"SELECT joiningDate FROM users where id={message.from_user.id}"):
            print('New user:', message.from_user.id, '|', row[0])
        for tmStamp in cursor.execute(f"SELECT joiningDate FROM users where id={message.from_user.id}"):
            for plRep in cursor.execute(f"SELECT plRep FROM users where id={message.from_user.id}"):
                for mnRep in cursor.execute(f"SELECT mnRep FROM users where id={message.from_user.id}"):
                    await message.answer(
                        "⚡ *Новый пользователь в нашем чате:* [{username}](tg://user?id={userid})\n🕐 *В моей базе с:* `{timeStamp}`\n🔥 *Глобальная репутация:*  `{plRep} 🟢 / {mnRep} 🔴`"
                            .format(username=message.from_user.full_name, userid=message.from_user.id,
                                    timeStamp=tmStamp[0], plRep=plRep[0], mnRep=mnRep[0]),
                        parse_mode='MarkdownV2', disable_web_page_preview=True)
        if any(word in message.text.lower() for word in thank_words):
            await message.reply(
                "Если тебе кто-то помог, можешь прописать `+r`, ответив на сообщение, что б добавить ему репутацию, или `-r` что б убавить её.\n\n_Так ты помогаешь нам, сделать наш чат лучше 😉_")


if __name__ == '__main__':
    try:
        CreateDB()
        executor.start_polling(dp, on_startup=on_startup, on_shutdown=on_shutdown)
    except BaseException as _ex:
        print('\n\033[31mAn error was detected : ', _ex, '\033[39m')
        print('- - - - - - - - - - - - - -')
