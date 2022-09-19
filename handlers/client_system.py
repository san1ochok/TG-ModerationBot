from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from configure.config import *
from configure.database import *

storage = MemoryStorage()
bot = Bot(token=token, parse_mode=parse_mode)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(text=['rep', 'реп', '+r'])
async def rep_system(message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    if message.reply_to_message.from_user.id != message.from_user.id:
        cursor.execute(f"SELECT name FROM users where id = {message.reply_to_message.from_user.id}")
        plus = 1
        UpdateValue('plRep', plus, message.reply_to_message.from_user.id)
        con.commit()
        for row in cursor.execute(f"SELECT * FROM users where id={message.reply_to_message.from_user.id}"):
            await message.answer('Спасибо за повышение репутации!\n\n*Глобальная репутация пользователя:*  `{plRep} 🟢 / {mnRep} 🔴`'.format(plRep=row[3], mnRep=row[4]))
    else:
        await message.reply('Данное действие не допустимо!')


@dp.message_handler(text=['rep', 'реп', '+r'])
async def derep_system(message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    if message.reply_to_message.from_user.id != message.from_user.id:
        cursor.execute(f"SELECT name FROM users where id = {message.reply_to_message.from_user.id}")
        minus = 1
        UpdateValue('mnRep', minus, message.reply_to_message.from_user.id)
        con.commit()
        for row in cursor.execute(f"SELECT * FROM users where id={message.reply_to_message.from_user.id}"):
            await message.answer('Репутация понижена!\n\n*Глобальная репутация пользователя:*  `{plRep} 🟢 / {mnRep} 🔴`'.format(plRep=row[3], mnRep=row[4]))
    else:
        await message.reply('Данное действие не допустимо!')


@dp.message_handler(text='id')
async def id_system(message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return
    await message.reply(f"ID пользователя: `{message.reply_to_message.from_user.id}`\n")


@dp.message_handler(text=["hug" 'обнять'])
async def hug_system(message):
    await message.reply(f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> обнял <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 🤗", parse_mode = "html")


@dp.message_handler(text=["kiss", 'поцеловать'])
async def kiss_system(message):
    await message.reply(f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> поцеловал <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 💋", parse_mode = "html")


@dp.message_handler(text=["intim", 'интим'])
async def intim_system(message):
    await message.reply(f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> принудил к интиму <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> ❤️‍🔥", parse_mode = "html")


@dp.message_handler(text=["kill", 'убить'])
async def kill_system(message):
    await message.reply(f"<b><a href='tg://user?id={message.from_user.id}'>{message.from_user.first_name}</a></b> убил <b><a href='tg://user?id={message.reply_to_message.from_user.id}'>{message.reply_to_message.from_user.first_name}</a></b> 🔫", parse_mode = "html")


@dp.message_handler(text=["dashboard", 'топ'])
async def dashboard_system(message):
    cursor.execute(f"SELECT id, plRep, mnRep, name FROM users ORDER BY plRep DESC LIMIT 10")
    leadermsg = "<b>Топ експертов чата</b>\n\n"
    fetchleader = cursor.fetchall()
    for i in fetchleader:
        ids = f"<b><a href='tg://user?id={i[0]}'>{i[0]}</a></b>"
        leadermsg += f"{fetchleader.index(i) + 1}| {ids}:  <b>{i[1]}</b> 🟢 / <b>{i[2]}</b> 🔴\n"
        fl3 = leadermsg.replace("3|", "🥉|")
        fl2 = fl3.replace("2|", "🥈|")
        fl = fl2.replace("1|", "🥇|")
    await message.answer(str(fl), parse_mode="html")


def register_handlers_client_system(dp: Dispatcher):
    dp.register_message_handler(rep_system, text=['rep', 'реп', '+r'])
    dp.register_message_handler(derep_system, text=['rep', 'реп', '-r'])
    dp.register_message_handler(id_system, text='id')
    dp.register_message_handler(hug_system, text=["hug" 'обнять'])
    dp.register_message_handler(kiss_system, text=["kiss", 'поцеловать'])
    dp.register_message_handler(intim_system, text=["intim", 'интим'])
    dp.register_message_handler(kill_system, text=["kill", 'убить'])
    dp.register_message_handler(dashboard_system, text=["dashboard", 'топ'])
