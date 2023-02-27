# ☢️ FUNCKA-BOT (RU only) #
![lIp6qFj_oSw](https://user-images.githubusercontent.com/76991612/221510792-38d1cfea-d5a9-4971-bc61-3022da20555e.jpg)

---
### Оглавление
  - [Введение](#-введение)
  - [Установка](#-установка)
  - [Команды](#-команды)
  - [Forbidden Filter](#%EF%B8%8F-система-forbidden-filter)
  - [URL Filter](#%EF%B8%8F-система-url-filter)

## 📄 Введение ##
  Данный бот был создан и заточен исключительно для работы с модерационными ресурсами неформального фан-сообщества [FUNCKA](https://vk.com/funcka) по игре [STALCRAFT](https://vk.com/stalcraft_official).<br/>
  Проект не несет в себе цели быть универсальным или массовым продуктом, он отвечает за чётко поставленные задачи, которые были выделены узким кругом лиц.
  Снизу представленна краткая инструкция по настройке бота и мануал по его использованию. Приятного прочтения!

## 🧰 Установка ##
  ___Для начала обозначу: Залив на хост - сугубо ваша забота. Здесь описаны основные процедуры приведения бота в работоспособность.___ <br/>
  Прежде всего необходимо получить токен сообщества для проботы с LongPoll API, сделать это можно тут: <br/>
  
  >Сообщество\Управление\Работа с API\СОЗДАТЬ КЛЮЧ <br/>
  
  Боту, желательно, выдать все права. Если вы выдали не все права и что-то не работает - это ваша забота. <br/>
  Созданый токен копируем и вставляем в __Config.py__, в переменную TOKEN. <br/>
  
    TOKEN = '******'
  
  Еще нам понадобится целочисленное значение ID паблика, на котром будет стоять бот. Копируем и вставляем в переменную GROUP в файле __Config.py__. <br/>
    
    GROUP = ***
    
  После чего необходимо обозначить доступ и версию для Long Poll API, для этого переходим сюда: <br/>
  
  >Сообщество\Управление\Работа с API\Long Poll API <br/>
  
  Включаем Long Poll API, выставляем версию __5.131__. Далее переходим во вкладку типов событий и выставляем все права для сообщений. <br/>
  
  ---
  
  А так же: Если вы используете бота в беседах, созданных ВНЕ сообщества, т.е. бот приглашен из вне, то боту нужно выдать сначала доступ ко всей переписке, а потом и админку в беседе 
  Бот готов к запуску!
  
  ---
  
## ⚙ Команды ##
    Общие правила работы команд:
      - Комадна удаляется в случае выполнение\невыполнения
      - В случае выполнения команда отправляет лог в назначенный лог-чат
      - Команда невыполняется в случае невыполнения условий работы или неверного аргумента
      - Для корректной работы команды должны быть вызваны в том же чате, в котором находится таргет
      - Команда сама подчищает за собой следы
      - VK Админ может применить любую команду вне зависимости оо группы прав
      - Команда не подчищает следы за VK Админом
      
  ---
  
 - set_permission <permission_lvl>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'set_permission', 'Set_permission', 'дать_права', 'Дать_права' <br/>

    > Обработка только совместно с пересланым сообщением <br/>

    > Доступ для группы прав 2 уровня или выше <br/>

    > Может быть вызвана в лог-чате


    Описание: <br/>
      Команда устанавливает для пользоватяле группу прав, равную по уровню введенному аргументу. <br/>
      Доступные группы прав: User(0), Moderator(1), Administrator(2). <br/>
  
  
  - set_permission_url <permission_lvl> <user_url>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: set_permission_url', 'Set_permission_url', 'дать_права_ссылкой', 'Дать_права_ссылкой' <br/>

    > Доступ для группы прав 2 уровня или выше <br/>

    > Может быть вызвана в лог-чате


    Описание: <br/>
      Команда устанавливает для пользоватяле группу прав, равную по уровню введенному аргументу. <br/>
      Доступные группы прав: User(0), Moderator(1), Administrator(2). <br/>
      
      
  - set_log_conversation 
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'set_log_conversation', 'Set_log_conversation', 'установить_лог_беседу', 'Установить_лог_беседу' <br/>

    > Доступ для группы прав 2 уровня или выше <br/>

    > Может быть вызвана в лог-чате


    Описание: <br/>
      Команда устанавливает __общий__ логчат для всех бесед. В этот логчат будут отсылаться логи выполненых команд.
 
 
  - reference
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'reference', 'Reference', 'справка', 'Справка' <br/>

    > Доступ для группы прав 1 уровня или выше <br/>

    > Может быть вызвана в лог-чате


    Описание: <br/>
      Выводит в чат ссылку на этот README, если кто вдруг забыл какую-то команду.
  
  
  - delete
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'delete', 'Delete', 'Удалить', 'удалить' <br/>

    > Обработка только совместно с пересланым сообщением <br/>

    > Доступ для группы прав 1 уровня или выше <br/>

    > Может быть вызвана в лог-чате


    Описание: <br/>
      Удаляет пересланое или группу пересланых сообщений.
  
  
  - ban <time_value> <time_type>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'ban', 'Ban', 'бан', 'Бан', 'блок', 'Блок' <br/>

    > Обработка только совместно с пересланым сообщением <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Банит пользователя на некоторый промежуток времени и удаляет из чата. После окончания блокировки поступает сигнал в логчат. <br/>
      Доступные аргументы time_type: h (hour), d (day), m (month), p (permanent) <br/>
  
  
  - ban_url <time_value> <time_type> <user_url>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'ban_url', 'Ban_url', 'бан_ссылкой', 'Бан_cсылкой', 'блок_ссылкой', 'Блок_ссылкой' <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Банит пользователя на некоторый промежуток времени и удаляет из чата. После окончания блокировки поступает сигнал в логчат. <br/>
      Доступные аргументы time_type: h (hour), d (day), m (month), p (permanent) <br/>
  
  
  - mute <time_value> <time_type>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'mute', 'Mute', 'мут', 'Мут', 'заглушить', 'Заглушить' <br/>

    > Обработка только совместно с пересланым сообщением <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      заглушает пользователя на некоторый промежуток времени. При нарушении заглушения пользователь блокируется на 3 дня. После окончания заглушения поступает сигнал в логчат. <br/>
      Доступные аргументы time_type: h (hour), d (day), m (month) <br/>
  
  
  - mute_url <time_value> <time_type> <user_url>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'mute_url', 'Mute_url', 'мут_ссылкой', 'Мут_ссылкой', 'заглушить_ссылкой', 'Заглушить_ссылкой' <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Банит пользователя на некоторый промежуток времени и удаляет из чата. При нарушении заглушения пользователь блокируется на 3 дня. После окончания заглушения поступает сигнал в логчат. <br/>
      Доступные аргументы time_type: h (hour), d (day), m (month) <br/>
   
   
  - warn 
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'warn', 'Warn', 'варн', 'Варн', 'пред', 'Пред' <br/>

    > Обработка только совместно с пересланым сообщением <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Выдает пользователю 1 предупреждение. Все предупреждения снимаются через сутки после получения последнего. При получении пользователем 3х предупреждений он будет заглушен на 1 день.
  
  
  - warn_url <user_url>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'warn_url', 'Warn_url', 'варн_ссылкой', 'Варн_ссылкой', 'пред_ссылкой', 'Пред_ссылкой' <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Выдает пользователю 1 предупреждение. Все предупреждения снимаются через сутки после получения последнего. При получении пользователем 3х предупреждений он будет заглушен на 1 день.
     
     
  - unban
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'Unban', 'unban', 'Разбан', 'Разбан', 'Разблок', 'разблок' <br/>

    > Обработка только совместно с пересланым сообщением <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Снимает блокировку с пользователя. <br/>
  
  
  - unban_url <user_url>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'Unban_url', 'unban_url', 'Разбан_ссылкой', 'Разбан_ссылкой', 'Разблок_ссылкой', 'разблок_ссылкой' <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Снимает блокировку с пользователя. <br/>
  
  
  - unmute 
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'unmute', 'Unmute', 'размут', 'Размут', 'разглушить', 'Разглушить' <br/>

    > Обработка только совместно с пересланым сообщением <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Снимает заглушение с пользователя. <br/>
  
  
  - unmute_url <user_url>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'unmute_url', 'Unmute_url', 'размут_ссылкой', 'Размут_ссылкой', 'разглушить_ссылкой', 'Разглушить_ссылкой' <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Снимает заглушение с пользователя. <br/>
   
   
  - unwarn 
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'unwarn', 'Unwarn', 'Разварн', 'разварн', 'Распред', 'распред' <br/>

    > Обработка только совместно с пересланым сообщением <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Снимает с пользователя 1 предупреждение. <br/>
  
  
  - unwarn_url <user_url>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'unwarn_url', 'Unwarn_url', 'Разварн_ссылкой', 'разварн_ссылкой', 'Распред_ссылкой', 'распред_ссылкой' <br/>

    > Доступ для группы прав 1 уровня или выше <br/>


    Описание: <br/>
      Снимает с пользователя 1 предупреждение. <br/>
  
  
  - set_cooldown <seconds>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'set_cooldown', 'Set_cooldown', 'установить_задержку', 'установить_задержку' <br/>

    > Доступ для группы прав 2 уровня или выше <br/>


    Описание: <br/>
      Устанавливает задержку в чате на сообщения. При нарушении задержки пользователь получает 1 предупреждение. <br/>
      Отключить задержку можно, выставив задержку на 0 секунд.
  
  
  - change_setting <setting> <true\false>
  
    > Доступные префиксы: ! или / <br/>

    > Псевдонимы команды: 'change_setting', 'Change_setting', 'изменить_настройку', 'Изменить_настройку' <br/>

    > Доступ для группы прав 2 уровня или выше <br/>


    Описание: <br/>
      Преключает настройку беседы. Каждая настройка разрешает\запрещает определенный контент в чате. В случае обнаружения запрещенного контента пользователю выдается 1 предупреждение. <br/>
      Доступные настройки: "Allow_Picture", "Allow_Video", "Allow_Music", "Allow_Voice", "Allow_Post", "Allow_Votes", "Allow_Files", "Allow_Miniapp", "Allow_Graffiti", "Allow_Sticker"
  
## ⚠️ Система Forbidden Filter ##
  
      Стандартные настройки для беседы:
                "Allow_Picture": true,
                "Allow_Video": true,
                "Allow_Music": true,
                "Allow_Voice": true,
                "Allow_Post": true,
                "Allow_Votes": true,
                "Allow_Files": true,
                "Allow_Miniapp": true,
                "Allow_Graffiti": true,
                "Allow_Sticker": true
  ---
    
      Слова, упоминающие Чёрный Рынок или как-либо затрагивающие\рекламирующие сторонние проекты входят в список запрещенных слов

  ---
  Описание: <br/>
    Система, распознающая запрещенный контент в сообщениях. В случае обнаружения системой выдается 1 предупреждение пользователю.
  
## ⚠️ Система URL Filter ##
      
      Ссылки, разрешенные для публикации:
                'https://forum.exbo.net',
                'https://vk.com/funcka',
                'https://vk.cc/ca5l9d',
                'https://stalcalc.ru',
                'https://vk.cc/c9RYhW',
                'https://vk.com/write-2677092',
                'https://stalcraft.net',
                'https://exbo.net',
                'https://support.exbo.net',
                'https://t.me/stalcraft',
                'https://discord.com/invite/stalcraft',
                'https://store.steampowered.com/app/1818450/STALCRAFT',
                'https://www.twitch.tv/exbo_official',
                'https://www.youtube.com/c/EXBO_official',
                'https://www.tiktok.com/@stalcraft_official',
                'https://www.facebook.com/stalcraft.official',
                'https://twitter.com/STALCRAFT_ENG',  # URL not working (?)
                'https://www.instagram.com/stalcraft_official',
                'https://www.instagram.com/exbo_studio'
  ---
  Описание: <br/>
    Система, распознающая ссылки в сообщениях. В случае обнаружения системой неразрешенной ссылки пользователю выдается заглушение на 1 день.