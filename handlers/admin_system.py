from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from configure.config import *
from configure.database import *
from datetime import datetime
from datetime import timedelta

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(text=['ban', 'бан'], is_chat_admin=True)
async def ban_system(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    comment = " ".join(message.text.split()[1:])
    await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
    await message.reply(f'👮 | <b>Решение было принято:</b> {name1}\n🛑 | <b>Забанил пользователя</b>: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок</b>: навсегда\n📃 | <b>Причина</b>: {comment}',  parse_mode='html')


@dp.message_handler(text=['kick', 'кик'], is_chat_admin=True)
async def kick_system(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    comment = " ".join(message.text.split()[1:])
    await bot.kick_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False))
    await message.reply(f'👮 | <b>Решение было принято:</b> {name1}\n🛑 | <b>/Кикнул пользователя</b>: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок</b>: навсегда\n📃 | <b>Причина</b>: {comment}',  parse_mode='html')


@dp.message_handler(text=['unban', 'анбан'], is_chat_admin=True)
async def unban_system(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
    await message.reply(f'👮 | <b>Решение было принято:</b> {name1}\n✅ | <b>Разбанил пользователя</b>: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>',  parse_mode='html')


@dp.message_handler(commands=['mute'], is_chat_admin=True)
async def mute_system(message):
    if message.from_user.id == 787080961 or 227342603 or 1143859214:
        name1 = message.from_user.get_mention(as_html=True)
        if not message.reply_to_message:
            await message.reply("Эта команда должна быть ответом на сообщение!")
            return
        try:
            muteint = int(message.text.split()[1])
            mutetype = message.text.split()[2]
            comment = " ".join(message.text.split()[3:])
        except IndexError:
            await message.reply('Не хватает аргументов!\nПример:\n`/mute 1 ч причина`')
            return
        if mutetype == "ч" or mutetype == "часов" or mutetype == "час":
            dt = datetime.now() + timedelta(hours=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date=timestamp)
            await message.reply(f'👮 | <b>Решение было принято:</b> {name1}\n🛑 | <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок наказания:</b> {muteint} {mutetype}\n📃 | <b>Причина:</b> {comment}',  parse_mode='html')
        if mutetype == "м" or mutetype == "минут" or mutetype == "минуты":
            dt = datetime.now() + timedelta(minutes=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
            await message.reply(f'👮 | <b>Решение было принято:</b> {name1}\n🛑 | <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок наказания:</b> {muteint} {mutetype}\n📃 | <b>Причина:</b> {comment}',  parse_mode='html')
        if mutetype == "д" or mutetype == "дней" or mutetype == "день":
            dt = datetime.now() + timedelta(days=muteint)
            timestamp = dt.timestamp()
            await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(False), until_date = timestamp)
            await message.reply(f'👮 | <b>Решение было принято:</b> {name1}\n🛑 | <b>Нарушитель:</b> <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>\n⏰ | <b>Срок наказания:</b> {muteint} {mutetype}\n📃 | <b>Причина:</b> {comment}',  parse_mode='html')
    else:
        await message.reply("Ей, ей, ей. Ты походу что-то попутал. Тебе нельзя использовать эту команду 🙊")


@dp.message_handler(text=['unmute', 'анмут'], is_chat_admin=True)
async def unmute_system(message):
    name1 = message.from_user.get_mention(as_html=True)
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    await bot.restrict_chat_member(message.chat.id, message.reply_to_message.from_user.id, types.ChatPermissions(True, True, True, True))
    await message.reply(f'👮 | <b>Решение было принято:</b> {name1}\n🔊 | Размутил пользователя: <a href="tg://user?id={message.reply_to_message.from_user.id}">{message.reply_to_message.from_user.first_name}</a>', parse_mode='html')


def register_handlers_admin_system(dp: Dispatcher):
    dp.register_message_handler(ban_system, text=['ban', 'бан'], is_chat_admin=True)
    dp.register_message_handler(kick_system, text=['kick', 'кик'], is_chat_admin=True)
    dp.register_message_handler(unban_system, text=['unban', 'анбан'], is_chat_admin=True)
    dp.register_message_handler(mute_system, commands=['mute'], is_chat_admin=True)
    dp.register_message_handler(unmute_system, text=['unmute', 'анмут'], is_chat_admin=True)