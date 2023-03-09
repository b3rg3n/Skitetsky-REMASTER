
label dlc1:
    scene black with ed_night_dis
    play music flowers
    scene bergenbook
    show overlay aw_memory_back_1
    with Fade(1.5, 1, 2)
    show zatemnenie with dissolve2
    $ MND_Chapter("DLC:")
    $ MND_Chapter("История одного неудачника")
    hide zatemnenie with dissolve2
    nvl clear
    nvlbazar "Что есть самое настоящее разочарование?"
    nvl clear
    nvlbazar "Просто представь,{w=0.2} что вся твоя деятельность была пустой тратой времени."
    nvlbazar "Представь,{w=0.2} что все те,{w=0.2} кто тебя восхвалял -{w=0.2} просто угарали."
    nvlbazar "Представь,{w=0.2} что ты проебал весь стимул дальнеёшего существования."
    nvl clear
    nvlbazar "Представил?{w} Молодец."
    nvlbazar "А теперь просто,{w=0.2} сука,{w=0.2} подумай{w=0.2}.{w=0.2}.{w=0.2}."
    nvlbazar "Что это всё реальность."
    nvl clear
    nvlbazar "Паршиво стало?"
    nvlbazar "Так вот,{w=0.2} я,{w=0.2} блять,{w=0.2} так уже давно существую."
    nvlbazar "Ради чего это всё только,{w=0.2} а?"
    nvl clear
    nvlshv "Устал ничего не делая."
    nvlbazar "Так говорит мне Саня.{w} Причём постоянно."
    nvlshv "Личной жизни у тебя нет,{w=0.2} друзей,{w=0.2} как ты говоришь -{w=0.2} тоже нет."
    nvlshv "Нахуя это всё?{w} Ответь сам себе."
    nvl clear
    nvlbazar "Парашно признавать,{w=0.2} но он прав."
    nvlbazar "И я намерен всё обернуть вспять."
    nvl clear
    nvlbazar "Исходники все удалены,{w=0.2} удалён тг и всё остальное."
    nvlbazar "Под диваном лежит помповый ТОЗ-34 и Макаров с одной обоймой."
    nvlbazar "Есть верёвка и мыло."
    nvlbazar "Так же есть остатки какого-то неизвестного порошка {w=0.2}(хуй знает,{w=0.2} откуда он{w=0.2}.{w=0.2}.{w=0.2}.)..."
    nvl clear
    nvlbazar "(Если каво я ничем не балуюсь,{w=0.2} просто знаю.{w} А откуда -{w=0.2} вас ебать не должно.)"
    nvlbazar "(Прололжаем.)"
    nvl clear
    nvlbazar "Где-то ещё был литр красного драйва и недопитая хуга{w=0.2}.{w=0.2}.{w=0.2}.{w} Можно сделать лысую головку {w=0.2}(коктейль)."
    nvlbazar "Сани дома не будет,{w=0.2} он до 10 вечера работает{w=0.2}.{w=0.2}.{w=0.2}.{w} Пары я всё равно проебал{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    vchn "И чем бы заняться,{w=0.2} сука?!" with vpunch
    menu:
        "Заюзать порошок?":
            jump dlcone
        "Помацать стволы?" if persistent.poroshok_zauzal:
            jump dlctwo
        "Скрафтить лысую головку?" if persistent.pomacal_stvoli:
            jump dlcthree
        "Выпилиться?" if persistent.popil_malisha:
            jump dlcfour
        "{font=source/3.otf}{color=#ff0000}УБИТЬ ВСЕХ НАХУЙ{/color}{/font}" if persistent.vsem_pizda:
            jump dlcfive

label dlcone:
    "Я решил заюзать немного этого порошка."
    "После того,{w=0.2} как я открыл баночку -{w=0.2} в нос ударил резкий запах миндаля."
    "Метилметкатинон{w=0.2}.{w=0.2}.{w=0.2}."
    "Лишь эта мысль пронеслась в голове."
    vchn "И откуда у нас дома валяется Мефедрон?" with vpunch
    vchn "Я этой хуйнёй не промышляю.{w} Саня вообще резко негативно настроен."
    vchn "Странно это всё."
    "Да и похуй."
    "Терять больше нечего."
    "Пришло время упарываться."
    window hide
    play sound vdohnul
    pause 1
    play sound kashel
    with vpunch
    pause 1
    vchn "Извинияюсь,{w=0.2} конечно,{w=0.2} за мат{w=0.2}.{w=0.2}.{w=0.2}."
    vchn "Пизда."
    window hide
    pause 1
    stop music fadeout 3
    "Накатила ебейшая волна эйфории."
    "Мысли о камингауте просто исчезли."
    "Стало так хорошо{w=0.2}.{w=0.2}.{w=0.2}.{w} Если бы не одно но."
    $ say_poplil = True
    play music finalzvuk
    play sound kashel
    "Глотку разрывал сухой кашель."
    scene bergenbook:
        subpixel True
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        zoom 1
        parallel:
            ease 4.4 zoom 2.1
        parallel:
            ease 4.4 xpos 0.45
        block:
            linear 20 rotate 360
            rotate 0
            repeat
    "Картина перед глазами просто поплыла."
    "Стало невероятно хуёво."
    play sound kashel
    window hide
    pause 1
    vchn "Я{w=0.2}.{w=0.2}.{w=0.2}.{w} Вспомнил{w=0.2}.{w=0.2}.{w=0.2}."
    "Я всё вспомнил."
    "Острая форма аллергии на любое порошкообразное гавно."
    "Это была фатальная ошибка."
    show blink
    play sound kashel
    vchn "Кха{w=0.2}.{w=0.2}.{w=0.2}."
    "Глаза закрылись сами собой."
    "{w=0.3}.{w=0.3}.{w=0.3}."
    "Хочется спать. "
    shv "БОРИСЬ,{w=0.2} ТВОЮ МАТЬ!" with vpunch
    vsn "ВЕЧНЫЙ!" with vpunch
    "Что-то вижу перед глазами{w=0.3}.{w=0.3}.{w=0.3}."
    scene anim_transition_1 with Dissolve(4.0)
    scene anim_transition_2 with Dissolve(4.0)
    scene anim_transition_3 with Dissolve(4.0)
    "Будто красный огонек далеко впереди. "
    "Красный туман? "
    "Кровавая луна{w=0.3}.{w=0.3}.{w=0.3}. "
    scene black with ed_night_dis
    $ MND_Chapter("Ты проебал...")
    $ MND_Chapter("Попробуй ещё раз...")
    $ MND_Chapter("Может, хоть сейчас повезёт?")
    $ persistent.poroshok_zauzal = True
    stop music fadeout 3
    return