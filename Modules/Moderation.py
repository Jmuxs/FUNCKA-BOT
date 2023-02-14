from vkbottle.bot import Bot, BotLabeler, Message
from typing import Tuple

from Config import TOKEN, GROUP, BAN_TYPE, ALIASES
from CustomRules import CommandRuleCustom
from urlextract import URLExtract

bot = Bot(token=TOKEN)
bl = BotLabeler()


@bl.chat_message(CommandRuleCustom(ALIASES['ban'], ['!', '/'], 2))
async def ban(message: Message, args: Tuple[str]):
    if args:
        # if you want to ban something user
        if (message.reply_message is not None) and (message.reply_message.from_id != message.from_id):
            await call_ban_proc(message, args)

        # if you want to ban yourself
        elif (message.reply_message is not None) and (message.reply_message.from_id == message.from_id):
            await alert_forbidden_to_self(message)

        # if you called command with more than one replied message
        elif message.fwd_messages and message.reply_message is None:
            await alert_forbidden_to_group(message)

        # if you called command w\o replied message
        elif message.reply_message is None:
            await self_msg_delete(message)

    else:
        await self_msg_delete(message)


@bl.chat_message(CommandRuleCustom(ALIASES['warn'], ['!', '/'], 0))
async def warn(message: Message):
    # if you want to warn something user
    if (message.reply_message is not None) and (message.reply_message.from_id != message.from_id):
        await call_warn_proc(message)

    # if you want to warn yourself
    elif (message.reply_message is not None) and (message.reply_message.from_id == message.from_id):
        await alert_forbidden_to_self(message)

    # if you called command with more than one replied message
    elif message.fwd_messages and message.reply_message is None:
        await alert_forbidden_to_group(message)

    # if you called command w\o replied message
    elif message.reply_message is None:
        await self_msg_delete(message)


@bl.chat_message(CommandRuleCustom(ALIASES['delete'], ['!', '/'], 0))
async def delete(message: Message):
    # if you called command with one replied messages
    if message.reply_message is not None:
        await rpl_msg_delete(message)

        await self_msg_delete(message)

    # if you called command with more than one replied messages
    elif message.reply_message is None and message.fwd_messages is not None:
        await fwd_msgs_delete(message)

        await self_msg_delete(message)

    # if you called command w\o replied message
    elif message.reply_message is None:
        await self_msg_delete(message)


@bl.chat_message(CommandRuleCustom(ALIASES['unban'], ['!', '/'], 1))
async def unban(message: Message, args: Tuple[str]):
    # if CmdRule returned args
    if args:
        # if you want to unban something user by URL
        if message.reply_message is None and not message.fwd_messages:
            extractor = URLExtract()

            if extractor.has_urls(args[0]):
                if args[0].startswith('https://vk.com/id'):
                    shortname = int(args[0].replace('https://vk.com/id', ''))
                    unban_users_info = await bot.api.users.get([shortname])

                    await call_unban_proc(message, unban_users_info)

                elif args[0].startswith('https://vk.com/'):
                    shortname = args[0].replace('https://vk.com/', '')
                    unban_users_info = await bot.api.users.get([shortname])

                    await call_unban_proc(message, unban_users_info)

                else:
                    await alert_not_pointing_url(message)

            else:
                await alert_arg_missing_url(message)

        # if you want to unban something user by arg and replying
        else:
            await alert_using_both_methods(message)

    # if CmdRule not returned args and func have forwarded messages
    elif not args and message.reply_message is None and message.fwd_messages:
        await alert_forbidden_to_self(message)

    # if CmdRule not returned args and func have replied message
    elif not args and message.reply_message is not None:
        if message.reply_message.from_id != message.from_id:
            unban_users_info = await bot.api.users.get(message.reply_message.from_id)

            await call_unban_proc(message, unban_users_info)

        else:
            await alert_forbidden_to_self(message)

    # if CmdRule not returned args and func have nothing (fwd\reply)
    else:
        await self_msg_delete(message)


@bl.chat_message(CommandRuleCustom(ALIASES['unwarn'], ['!', '/'], 1))
async def unwarn(message: Message, args: Tuple[str]):
    # if CmdRule returned args
    if args:
        # if you want to unwarn something user by URL
        if message.reply_message is None and not message.fwd_messages:
            extractor = URLExtract()

            if extractor.has_urls(args[0]):
                if args[0].startswith('https://vk.com/id'):
                    shortname = int(args[0].replace('https://vk.com/id', ''))
                    unwarn_users_info = await bot.api.users.get([shortname])

                    await call_unwarn_proc(message, unwarn_users_info)

                elif args[0].startswith('https://vk.com/'):
                    shortname = args[0].replace('https://vk.com/', '')
                    unwarn_users_info = await bot.api.users.get([shortname])

                    await call_unwarn_proc(message, unwarn_users_info)

                else:
                    await alert_not_pointing_url(message)

            else:
                await alert_arg_missing_url(message)

        # if you want to  unwarn something user by arg and replying
        else:
            await alert_using_both_methods(message)

    # if CmdRule not returned args and func have forwarded messages
    elif not args and message.reply_message is None and message.fwd_messages:
        await alert_forbidden_to_group(message)

    # if CmdRule not returned args and func have replied message
    elif not args and message.reply_message is not None:
        if message.reply_message.from_id != message.from_id:
            unwarn_users_info = await bot.api.users.get(message.reply_message.from_id)

            await call_unwarn_proc(message, unwarn_users_info)

        else:
            await alert_forbidden_to_self(message)

    # if CmdRule not returned args and func have nothing (fwd\reply)
    else:
        await self_msg_delete(message)


@bl.chat_message(CommandRuleCustom(ALIASES['help'], ['!', '/'], 0))
async def help(message: Message):
    users_info = await bot.api.users.get(message.from_id)

    title = f'@id{users_info[0].id} ({users_info[0].first_name}), вот реализованый список команд: \n' \
            f'· warn - Выдать предупреждение пользователю (in work)\n' \
            f'· unwarn - Снять предупреждение с пользователя (in work)\n' \
            f'· ban \'time\' \'time_type\' - Заблокировать пользователя (in work)\n' \
            f'· unban - Разблокировать пользователя (in work)\n' \
            f'· delete - Удалить сообщение (done)\n' \
            f'· upperm \'n\' - Повысить уровень прав на \'n\' пунктов (in work)\n' \
            f'· downperm \'n\' - Понизить уровень прав на \'n\' пунктов (in work)\n'
    await message.answer(title)

    title = f'Список реализованых систем:\n' \
            f'· URL Filter (in work)\n' \
            f'· Forbidden Filter (in work)\n' \
            f'· Group Answerer (done)'
    await message.answer(title)

    await self_msg_delete(message)


@bl.chat_message(CommandRuleCustom(ALIASES['upperm'], ['!', '/'], 1))
async def upperm(message: Message, args: Tuple[str]):
    pass


@bl.chat_message(CommandRuleCustom(ALIASES['downperm'], ['!', '/'], 1))
async def downperm(message: Message, args: Tuple[str]):
    pass


async def call_ban_proc(message: Message, args: Tuple[str]):
    ban_users_info = await bot.api.users.get(message.reply_message.from_id)

    if not ban_users_info:
        title = f'Пользователь ' \
                f'не может быть заблокирован или не существует.'
        await message.answer(title)

    else:
        time = args[0]
        time_type = BAN_TYPE[args[1]]

        if args[1] == 'p':
            time = ''
        elif args[1] == 'm':
            if int(time) < 0:
                time = '1'
            if int(time) > 12:
                time = '12'
        elif args[1] == 'd':
            if int(time) < 0:
                time = '1'
            if int(time) > 31:
                time = '31'
        elif args[1] == 'h':
            if int(time) < 0:
                time = '1'
            if int(time) > 24:
                time = '24'
        else:
            time = '1'
            time_type = BAN_TYPE['d']

        title = f'@id{ban_users_info[0].id} (Пользователь) ' \
                f'был заблокирован на {time} {time_type}.'
        await message.answer(title)

        # TODO: Ban procedure somewhere

    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id,
                                  delete_for_all=True)

    message_id = message.reply_message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id,
                                  delete_for_all=True)

    '''await bot.api.messages.remove_chat_user(message.reply_message.from_id)'''


async def call_warn_proc(message: Message):
    warn_users_info = await bot.api.users.get(message.reply_message.from_id)

    # TODO: Make DB request to get current user's warn count

    warn_count = 0
    if not warn_users_info:
        title = f'Пользователь ' \
                f'не может быть предупреждён или не существует.'
        await message.answer(title)

    else:
        title = f'@id{warn_users_info[0].id} (Пользователь) ' \
                f'получил предупреждение [{warn_count + 1}/3].'
        await message.answer(title)

        # TODO: Warn procedure somewhere

    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)

    message_id = message.reply_message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)


async def call_unban_proc(message: Message, uui):
    unban_users_info = uui
    if unban_users_info:
        user_id = unban_users_info[0].id
        print(user_id)

        # TODO: make DB request to check existing user in DB

        inbase = True
        if inbase:

            # TODO: make DB request to annihilate user's bans

            title = f'С @id{unban_users_info[0].id} (пользователя) снята блокировка.\n' \
                    f'Теперь он снова может зайти в беседу.'
            await message.answer(title)

            message_id = message.conversation_message_id
            await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id,
                                          delete_for_all=True)

        else:
            users_info = await bot.api.users.get(message.from_id)

            title = f'@id{users_info[0].id} ({users_info[0].first_name}), пользователь не найден в базе' \
                    f' данных .'
            await message.answer(title)

            message_id = message.conversation_message_id
            await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id,
                                          delete_for_all=True)

    else:
        users_info = await bot.api.users.get(message.from_id)

        title = f'@id{users_info[0].id} ({users_info[0].first_name}), пользователь не найден.'
        await message.answer(title)

        message_id = message.conversation_message_id
        await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id,
                                      delete_for_all=True)


async def call_unwarn_proc(message: Message, uui):
    unwarn_users_info = uui
    if unwarn_users_info:
        user_id = unwarn_users_info[0].id
        print(user_id)

        # TODO: make DB request to check existing user in DB

        inbase = True
        if inbase:

            # TODO: make DB request to get user's warns count

            warn_count = 2

            # TODO: Make DB request to make back-inc user's warns count

            title = f'С @id{unwarn_users_info[0].id} (пользователя) снято предупреждение.\n' \
                    f'Текущее кол-во предупреждений [{warn_count - 1}/3]'
            await message.answer(title)

            message_id = message.conversation_message_id
            await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id,
                                          delete_for_all=True)

        else:
            users_info = await bot.api.users.get(message.from_id)

            title = f'@id{users_info[0].id} ({users_info[0].first_name}), пользователь не найден в ' \
                    f'базе данных.'
            await message.answer(title)

            message_id = message.conversation_message_id
            await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id,
                                          delete_for_all=True)


async def alert_not_pointing_url(message: Message):
    users_info = await bot.api.users.get(message.from_id)

    title = f'@id{users_info[0].id} ({users_info[0].first_name}), ссылка не указывает на профиль ' \
            f'пользователя.'
    await message.answer(title)

    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)


async def alert_arg_missing_url(message: Message):
    users_info = await bot.api.users.get(message.from_id)

    title = f'@id{users_info[0].id} ({users_info[0].first_name}), в аргументе команды отсутствует сылка.'
    await message.answer(title)

    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)


async def alert_using_both_methods(message: Message):
    users_info = await bot.api.users.get(message.from_id)

    title = f'@id{users_info[0].id} ({users_info[0].first_name}), ' \
            f'нельзя использовать аргументный и пересыльный метод одновременно.\n' \
            f'Попробуйте использовать что-то одно.'
    await message.answer(title)

    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)


async def alert_forbidden_to_group(message: Message):
    users_info = await bot.api.users.get(message.from_id)

    title = f'@id{users_info[0].id} ({users_info[0].first_name}), ' \
            f'нельзя применить команду к группе сообщений.'
    await message.answer(title)

    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)


async def alert_forbidden_to_self(message: Message):
    users_info = await bot.api.users.get(message.from_id)

    title = f'@id{users_info[0].id} ({users_info[0].first_name}), ' \
            f'нельзя применить команду к своему сообщению.'
    await message.answer(title)

    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)


async def self_msg_delete(message: Message):
    message_id = message.conversation_message_id
    await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)


async def rpl_msg_delete(message: Message):
    if message.reply_message is not None:
        message_id = message.reply_message.conversation_message_id
        await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)


async def fwd_msgs_delete(message: Message):
    if message.fwd_messages:
        for msg in message.fwd_messages:
            message_id = msg.conversation_message_id
            await bot.api.messages.delete(group_id=GROUP, peer_id=message.peer_id, cmids=message_id, delete_for_all=True)