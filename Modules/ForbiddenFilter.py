from vkbottle.bot import Bot, BotLabeler, Message
from Config import GROUP, TOKEN
from DataBase import DataBaseTools as DBtools
from Rules.CustomRules import PermissionSelfIgnore, HandleLogConversation

bot = Bot(token=TOKEN)
bl = BotLabeler()

# TODO: I must try to modify TTF. Right now it's working well, but have small power
forbidden = ['смалкейс', 'смаллкейс', 'смалл кейс' 'смолкейс', 'смоллкейс', 'смолл кейс', 'сталкейс', 'смал кейс',
             'стал кейс', 'черный рынок', 'валюта', ' чр ', 'смоллкеис',
             'смаллкеис', 'еадг', 'фгм', 'клизма', 'катаклизм', 'прожект катаклуcм', 'катаклузм', 'сталкуб', 'сталкубе',
             'смол кеис', 'стол кеис', 'смолкеис']


@bl.chat_message(
    HandleLogConversation(False),
    PermissionSelfIgnore(1),
    blocking=False
)
async def check_forbidden(message: Message):
    print(message)

    spotted = False

    if not spotted:
        for word in forbidden:
            if word in message.text.lower():
                spotted = True
                break

    if not spotted and not DBtools.get_setting(message, 'Allow_Picture'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.photo is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Video'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.video is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Music'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.audio is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Voice'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.audio_message is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Post'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.wall_reply is not None or attachment.wall is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Votes'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.poll is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Files'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.doc is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Miniapp'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.mini_app is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Graffiti'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.graffiti is not None:
                    spotted = True
                    break

    if not spotted and not DBtools.get_setting(message, 'Allow_Sticker'):
        if message.attachments:
            for attachment in message.attachments:
                if attachment.sticker is not None:
                    spotted = True
                    break

    if spotted:
        warn_count = DBtools.get_warn_count(message, message.from_id)

        title = f'Этот контент запрещен в данной беседе.\n' \
                f'@id{message.from_id} (Пользователь) получил предупреждение [{warn_count + 1}/3].'
        await message.answer(title)
        await msg_delete(message)

        # DBtools.add_warn(message, message.from_id, warn_count + 1)

        if warn_count + 1 == 3:
            await call_ban_proc(message)


'''
-----------------------------------------------------------------------------------------------------------------------
'''


async def call_ban_proc(message: Message):
    ban_users_info = await bot.api.users.get(message.from_id)

    time = '3'
    time_type = 'day(s)'

    title = f'@id{ban_users_info[0].id} (Пользователь) ' \
            f'был заблокирован на {time} {time_type}.'
    await message.answer(title)

    DBtools.add_temp_ban(message, message.from_id, time, time_type)

    '''await bot.api.messages.remove_chat_user(message.reply_message.from_id)'''


async def msg_delete(message: Message):
    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)
