label start:
    $ persistent.zastavka_skip = True
    play sound maloletka
    scene menushitfade:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    stop music fadeout 2
    scene black with dissolve2
    pause 0.5
    jump scenariogovna

label scenariogovna:
    show screen change_say_box_blya
    scene nmallblur with ed_night_dis
    play ambience rain_out fadein 5
    scene nmall
    show doshd
    with dissolve2
    "Куда наваливаем?"
    menu:
        "The Carter Zero: Мы ещё полетаем":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump atkzero
        "The Carter One: Постигая основы безумия":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktone
        "The Carter Two: Планапокалипсис":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump akttwo
        "The Carter Three: iNeoony's Revenge":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktthree
        "The Carter Four: Rotten Diary":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktfour
        "The Carter Five: Doppelganger":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktfive
        "The Carter Six: Взломать Скитецкого":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktsix
        "The Carter Seven: Frozen Zone":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktseven
        "The Carter Eight: Eclipse":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktseven
        "The Carter Nine: After Midnight":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump akteight
        "The Carter Ten: Exodus":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktnine
        "The Carter DLC: After 4DPA":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump dlc

label atkzero:
    scene black with ed_night_dis
    play music rad
    scene corridor
    $ Aw_Alko("corridor")
    with ed_night_dis
    nvlbazar "Мягкие,{w=0.2} белые стены{w=0.2}.{w=0.2}.{w=0.2}."
    nvlbazar "Они создают непередоваемое ощущение тяжести."
    nvlbazar "Вся эта параша буквально давит на мозги."
    nvlbazar "И лишь одна фраза мелькает в мыслях..."
    nvl clear
    nvlbazar "Мы ещё полетаем."
    nvl clear
    nvlbazar "А я ведь оказался тут не просто так{w=0.2}.{w=0.2}.{w=0.2}."
    nvlbazar "Стоило лишь один раз отказаться{w=0.2}.{w=0.2}.{w=0.2}."
    nvlbazar "И всё было бы по-другому{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlbazar "Однако белый корридор не может быть бесконечным.{w} Теоритически."
    nvl clear
    play sound door_break
    scene zihao at aw_master_tryas
    nvlbazar "И меня выпиздили в кабнет {b}терапевта?{/b}{w} Вполне возможно,{w=0.2} что это действительно {b}психотерпаевт{/b}."
    nvl clear
    zih1 "Здравствуй." with vpunch
    lis "Ага,{w=0.2} шалом."
    zih1 "Дагадываешься,{w=0.2} за что ты здесь?"
    lis "Меня терзают смутные сомнения."
    lis "Однако не без причины меня тут держат, {w=0.2}раз уж вы так {b}толсто{/b} на это намекаете."
    zih1 "Ты не стой." with vpunch
    zih1 "Присаживайся."
    "Он сел на кресло напротив Доктора."
    "В то же время Докотор достал два гранёных стакана и начал заливать туда коньяк {b}<<Александр>>{/b}."
    zih1 "Как тебя звать?"
    lis "Как меня зовут{w=0.2}.{w=0.2}.{w=0.2}.{w} Ха."
    lis "У меня много имён." with vpunch
    zih1 "Раз уж так,{w=0.2} то какое имя тебе нравится больше всего?"
    vchn "Зовите Вечный." with vpunch
    zih1 "Так пафосно."
    zih1 "В честь чего такое имечко?"
    vchn "Моя история -{w} это история о Вечном."
    vchn "Вот и весь секрет.{w} Которого нет."
    zih1 "Вечный,{w=0.2} так Вечный."
    zih "Меня можешь звать Зихао."
    vchn "Ага,{w=0.2} то есть ты гонишь на моё эпическое прозвище,{w=0.2} а сам имеешь не лучше?{w} Ха.{w} Удивил,{w=0.2} базару зиро."
    zih "Тебе лучше не знать где,{w=0.2} да за что я его получил."
    vchn "Мне это не интересно." with vpunch
    "Зихао наполнил гранёные стаканы на половину."
    zih "За знакомство?"
    vchn "Отказываться не буду."
    "Вечный опрокинул стакан аки {b}шот{/b} в баре -{w} буквально залпом,{w=0.2} в то время как Зихао неспеша потягивал коньяк и смаковал каждую каплю."
    vchn "Ядрёна вошь{w=0.2}.{w=0.2}.{w=0.2}."
    vchn "Нормально так пошёл{w=0.2}.{w=0.2}.{w=0.2}."
    "Вечный понурил ебалом."
    "Коньяк заставил его слегка ахуеть от градуса."
    "Сам по себе Вечный -{w} не пьёт."
    "Почти совсем."
    "Хотя скорее пьёт,{w=0.2} но редко.{w} Главное -{w} как."
    "Упарываться до потери памяти -{w} в его стиле."
    "Хоть он и пытается совладать с собой{w=0.2}.{w=0.2}.{w=0.2}."
    "У него это плохо получается."
    "Зихао решил прервать нарастающую тишину."
    zih "Ты можешь рассказать,{w=0.2} с чего всё начиналось?"
    vchn "Что именно?"
    zih "Не строй из себя идиота." with vpunch
    zih "Все мы прекрасно понимаем,{w=0.2} что ты основоположник {b}заварушки в Новошахтинске{/b}."
    vchn "А,{w=0.2} ты про это."
    vchn "Я в натуре сначала не понял,{w=0.2} хы."
    vchn "Так уж и быть."
    vchn "Коньячок у тебя чёткий."
    stop music fadeout 4
    vchn "При такой обстановке грех не попиздеть,{w=0.2} мазафака."
    "Спародировав пару раз {b}обзорщика намба ван на руси{/b},{w=0.2} Вечный начал свой рассказ опиздохуительных историй."
    show zatemnenie with dissolve2
    $ MND_Chapter("The Carter Zero:")
    $ MND_Chapter("Мы ещё полетаем")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music cw fadein 5
    scene nvnight
    show overlay aw_memory_back_1
    with Fade(1.5, 1, 2)
    nvl clear
    nvlbazar "Всё начиналось немного не здесь,{w} но мне поебать."
    nvlbazar "Буду рассказывать {b}full story{/b} про Скита от своего лица."
    nvl clear
    nvlbazar "Началось всё в августе 2017 года,{w=0.2} когда Скит написал в теме {b}Lenovo Vibe B{/b} на {b}4PDA{/b}."
    nvlbazar "Он хуесосил модеров с {b}Lenovo-Forums{/b} за их {b}слабоумие{/b} {w=0.2}(хотя сам интеллектом не блистал)."
    nvlbazar "И у нас с ним в личке начался базар за {b}boot image{/b}."
    nvlbazar "Скиту он нужен был для запуска,{w=0.2} когда у меня вызывал бутлуп."
    nvl clear
    nvlbazar "В итоге после создания {b}VRT{/b} {w=0.2}(сокращённо -{w=0.2} {b}Vibe Rom Team{/b}),{w=0.2} где уже были все типы с темы,{w=0.2} туда был добавлен и Скит."
    nvlbazar "Он показал себя как хороший и душевный парниша."
    nvlbazar "Это сейчас никакая не ирония блять,{w=0.2} не мегапостпизда,{w=0.2} это,{w=0.2} сука,{w=0.2} факт."
    nvlbazar "Скит до 2020 был типом неплохим."
    nvl clear
    nvlbazar "Он тестировал прошивки,{w=0.2} выдавал базу о багах."
    nvlbazar "Никогда меня лично говном не поливал."
    nvlbazar "Так продолжалось года до 18."
    nvl clear
    nvlbazar "Тогда начался наш конфликт с {b}Тунечиком{/b} {w=0.2}(второй сооснователь VRT,{w=0.2} пиздатый паря.{w=0.2} Сейчас носит имя {b}sourcandy{/b}.)."
    nvlbazar "Скит стоял за меня горой во всех вопросах."
    nvlbazar "Скринов не будет т.к. мне лень их вставлять.{w=0.2} На счёт них спрашивать {b}dedlylxrdа{/b} (Вадимка) или меня ({b}BERGEN{/b}) в тг ({b}Telegram Messenger{/b})."
    nvl clear
    nvlbazar "После перемирия {b}VRT{/b} пересоздалась в {b}project.listick{/b} {w=0.2}(По сути то же самое)."
    nvlbazar "Где до сентября 2019 мы нормально общались со Скитом и обсуждали {b}GSI{/b} кастомы."
    nvlbazar "Но в сентябре настал решающий момент."
    nvl clear
    nvlbazar "Начался срач по поводу мобильных операторов."
    nvlbazar "Скит защищал {b}билайн{/b},{w=0.2} Тунечик защищал {b}мегафон{/b},{w=0.2} пока я защищал {b}теле2{/b}."
    nvlbazar "В итоге Скит распсиховался и {b}слился{/b},{w=0.2} со словами:"
    nvl clear
    play sound shkolnikivernulis
    nvlskt "О блять,{w=0.2} школьники со школы вернулись!"
    nvl clear
    nvlbazar "И ливнул с беседы."
    nvlbazar "Больше я о нём до 2022 года ничё не слышал."
    nvl clear
    nvlbazar "Потом в 2022 мне кто-то скинул канал {b}iNeoony{/b} {w=0.2}(Дамирка,{w=0.2} главный хейтер Скита,{w=0.2} после меня конечно же{w=0.2}.{w=0.2}.{w=0.2}.)."
    nvlbazar "Я начал делать свой первый шедевр - {w=0.2}{b}Skitetsky Story{/b}."
    nvl clear
    nvlbazar "Там было всего 3 концовки и 1 решающий выбор в сюжете."
    nvlbazar "В первой Скит чистил говно,{w=0.2} во второй вскрывался,{w=0.2} в третьей собирал {b}VRT{/b}."
    nvlbazar "Я залетел в чат Неони с этим творением и его оценили по достоинтсву."
    nvl clear
    nvlbazar "Там же я познакомился с парнишкой с ником {b}Deadlylxrd{/b} {w=0.2}(Вадимка) и его кентом {b}Lizzur{/b} {w=0.2}(Диман)."
    nvlbazar "Диман просто был со своими именными рофлами,{w=0.2} чем и поднимал моё настроение."
    nvlbazar "А {b}deadlylxrd{/b} вместе с {b}Overlord{/b} {w=0.2}(Данила){w=0.2} роняли нахуй {b}Wapdomik{/b} {w=0.2}(сайт Скита)."
    nvlbazar "Также он дал код для меню модов,{w=0.2} ну и просто был ахуенным типом."
    nvlbazar "После чего я сразу же начал делать вторую часть своего говна."
    nvl clear
    nvlbazar "Вышла она в марте 2022 и называлась -{w=0.2} {b}Dmitry Diary{/b} {w=0.2}(самое смешное говно про скита по версии {b}deadlylxrds chat{/b}.)."
    nvlbazar "Там так же было три концовки -{w=0.2} в первой Скита взрывали в параше, {w=0.2}во второй он помирился с тяночкой, {w=0.2}в третьей он эту тяночку загубил {w=0.2}(вот гандон)."
    nvlbazar "Это та самая новелла,{w=0.2} где роняли забор Скиту,{w=0.2} взрывали его туалет, {w=0.2}снимали его срущим на кране,{w=0.2} устраивали пилу и чёта ещё,{w=0.2} что я не помню,{w=0.2} блять{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlbazar "По итогу этот шедевр залетел."
    nvlbazar "Мы общались в чате {b}iGandone LLC{/b} {w=0.2}(рофл Неони,{w=0.2} типа компания по доёбу Скита.),{w=0.2} где Неоня доксил всяких типов."
    nvlbazar "Туда пришёл тип с ником {b}SS{/b} {w=0.2}(По версии {b}deadlylxrd{/b} - {w=0.2}Серёга Коран,{w=0.2} по моей версии -{w=0.2} Артур.)."
    nvl clear
    nvlbazar "Я с ним пообщался -{w=0.2} {b}вроде{/b} нормальный тип."
    nvlbazar "Однако он занимался {b}лжеминированием{/b} {w=0.2}(позволяло местоположение в {b}Болгарии{/b},{w=0.2} сам с Одесской области,{w=0.2} фото он так же кидал.)."
    nvlbazar "Именно он сподвиг Неоню на {b}докс{/b} {w=0.2}(слив личных данных) {w=0.2}типа с ником {b}тоска{/b}."
    nvl clear
    nvlbazar "После этого инцедента слили самого Неоню и он {b}самоликвидировался{/b} {w=0.2}(удалил тг акк и канал)."
    nvlbazar "Видос вставлять мне влом,{w=0.2} просто спросите меня или {b}deadlylxrd{/b}."
    nvl clear
    nvlbazar "После этого были и мои чаты,{w=0.2} и чаты {b}deadlylxrd{/b}а,{w=0.2} и так до сегодняшнего времени."
    nvlbazar "А ремастер этот - {w=0.2}одна большая солянка из лучших рофлов про Скита и мой сенсационный проект."
    nvl clear
    nvlbazar "Вроде всё рассказал."
    nvlbazar "Ах,{w=0.2} да."
    nvl clear
    scene black
    window hide
    stop music
    play sound bergdiskprolog
    pause 7
    scene zihao
    with ed_night_dis
    zih "Интересно{w=0.2}.{w=0.2}.{w=0.2}."
    zih "Неужели всё началось из-за чата в вк?" with vpunch
    vchn "Именно так."
    zih "Ладно."
    zih "У нас с тобой заканчивается время."
    zih "Я подумаю над этим позже."
    zih "А ты пока посидишь в камере." with vpunch
    vchn "Чё?"
    vchn "Я не хочу обратно!"
    vchn "Только если в одиночную."
    zih "Как вам будет угодно."
    zih "Юра,{w=0.2} Джозеф -{w} сопроводите этого господина."
    "И два амбала по два метра каждый вытолкали Вечного в коррридор."
    window hide
    pause 1
    play music lovewooman1 fadein 2
    "В перерывах между приёмами всяких дегенератов Зихао подрубал ностальгические для себя треки и думал о том,{w=0.2} что ему рассказывают пациенты."
    "Не по-{w=0.2}серьёзке,{w=0.2} конечно же."
    "Кто в здравом уме будет задумываться о том,{w=0.2} что говорят психи?"
    "Этим и оправдывал себя Зихао."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Химори:")
    hide zatemnenie with dissolve2
    play sound door_open
    "Химори зашла в кабинет Зихао."
    him "Свободен сейчас?"
    zih "Конечно."
    zih "Только недавно выпроводили {b}Новошахтинского суетолога{/b}."
    zih "Не,{w=0.2} ну ты только представь:{w} он себя Вечным именует!"
    zih "Ха.{w} Маразм крепчает с каждым днём."
    him "Это всё,{w=0.2} конечно весело{w=0.2}.{w=0.2}.{w=0.2}."
    "Химори никак не могла собраться с мыслями."
    "В её голове царил полный кавардак."
    "Её самый опасный пациент сбежал."
    "Она не знала,{w=0.2} как рассказать всё Зихао."
    "Он,{w=0.2} как коллега,{w=0.2} должен её понять."
    "Но поймёт ли он её правильно?"
    "Этот вопрос не даёт её покоя."
    "Ай,{w=0.2} к чёрту!"
    him "У меня сбежала {b}Ростовская Шахматистка{/b}." with vpunch
    window hide
    play sound reaction_joke_4
    pause 4
    him "А я и не {b}<<хохмлю>>{/b}."
    him "Она действительно сбежала." with vpunch
    him "Причём ещё мой личный {b}Glock 17{/b} прихватила."
    zih "И как давно?"
    him "Месяц назад." with vpunch
    window hide
    play sound laughter_3
    pause 3
    zih "И чё же ты раньше не сказала?"
    him "Боялась."
    window hide
    play sound reaction_joke_1
    pause 3
    zih "Ладно."
    zih "Пока ничего не случилось."
    zih "Не паникуй раньше времени."
    zih "Она сама себя выдаст."
    zih "Там и порешаем все проблемы."
    zih "Сделаем красиво."
    him "Спасибо,{w=0.2} Зихао."
    zih "Пока не за что."
    zih "Ладно,{w=0.2} давай,{w=0.2} у меня перерыв заканчивается."
    zih "Встретимся позже."
    him "Бывай."
    play sound door_open
    "И Химори,{w=0.2} окрылённая надеждой,{w=0.2} упархнула в свой кабинет."
    zih "Шахматитстка сбежала{w=0.2}.{w=0.2}.{w=0.2}."
    zih "Ебануться можно{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    "Но Зихао пришлось натянуть своё фирменное похуистическое лицо,{w=0.2} ведь его ждал очередной пациент."
    zih "Погнали,{w=0.2} хули{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 5
    show zatemnenie with dissolve2
    $ MND_Chapter("Конец первого картера...")
    hide zatemnenie with dissolve2
    return

label aktone:
    scene black with ed_night_dis
    play music sail
    scene corridor
    $ Aw_Alko("corridor")
    with ed_night_dis
    nvlbazar "Снова ведут по знакомому корридору{w=0.2}.{w=0.2}.{w=0.2}."
    nvlbazar "Я знаю,{w=0.2} что будет дальше."
    nvlbazar "Всё просто.{w} И всё очень сложно."
    nvl clear
    play sound door_break
    scene zihao at aw_master_tryas
    vchn "И снова здравствуйте."
    zih "Здарова бандит."
    zih "Как твоё ничего?" with vpunch
    "Толсто потраливая подметил Доктор."
    vchn "Да как обычно."
    vchn "В одиночке хоть человеком себя почувствовал."
    stop music fadeout 3
    zih "Ты говорил,{w=0.2} что продолжишь свой рассказ опиздохуительных историй."
    zih "Ну так?" with vpunch
    vchn "Было б ещё что рассказывать."
    "С девятой попытки рассказ таки пошёл."
    play music revenge fadein 5
    show zatemnenie with dissolve2
    $ MND_Chapter("The Carter One:")
    $ MND_Chapter("Постигая основы безумия")
    hide zatemnenie with dissolve2
    scene novoshahtinsk
    show overlay aw_memory_back_1
    with Fade(1.5, 1, 2)
    nvl clear
    nvlbazar "Был один интересный пацанчик..."
    nvlbazar "Он состоял в партии {b}ОУН{/b}."
    nvlbazar "Его действия были крайне радикальными..."
    nvlbazar "Он был сопротивлением советскому режиму."
    nvl clear
    nvlbazar "Нет,{w=0.2} я не буду его оправдывать.{w} Скорее - {u}хуесосить{/u}."
    nvlbazar "{u}Почему?{/u}"
    nvl clear
    nvlbazar "Он воевал на стороне доб{nw}"
    nvl clear
    nvlbazar "Он воевал на стороне {fast} {b}зла{/b}."
    nvlbazar "Но фишка-то не в этом."
    nvlbazar "Во время очередного партийного собрания..."
    nvlbazar "К нему подкатывала одна очень интересная мадам..."
    nvl clear
    nvlbazar "Хули ходить вокруг да около?"
    nvlbazar "Выебал он её и дело с концом...{w} Но нет."
    nvlbazar "Она залетела от него."
    nvl clear
    nvlbazar "Так как в {b}ОУН{/b} к этому относились крайне хуёво,{w=0.2} он был вынужден отказаться от своего сына."
    nvlbazar "По итогу {u}сын получил фамилию матери{/u}."
    nvlbazar "Так появился на свет {b}Андрей Степанович Скитецкий{/b}."
    nvl clear
    nvlbazar "После разгрома {b}ОУН{/b} и {b}НСДАП{/b},{w=0.2} с последующим ваншотом {b}Степана Бандеры{/b} (Ебучего нацика хохлёнка{w}(автор осуждает))...."
    nvlbazar "Семья Скитецких была вынуждена принять сторону коммунистов и остаться в СССР."
    nvlbazar "В городе Новошахтинске в Ростовской области."
    nvl clear
    nvlbazar "Андрюшка не был настолько радикальным ебанатом,{w=0.2} как его отец."
    nvlbazar "Он был вполне себе законопослушным гражданином."
    nvlbazar "Но в партию его всё равно не взяли."
    nvl clear
    nvlbazar "Ему было грустно,{w=0.2} конечно... {w}(кто ж спорит-то блять?)"
    nvlbazar "Но он продолжал жить."
    nvlbazar "в 1975 году у него родился сын."
    nvlbazar "Назвали ео в честь отца -{w} {b}Андрей Андреевич Скитецкий{/b}."
    nvlbazar "Ему тоже не везло с положением в виду своей родословной линии...{w} Но..."
    nvl clear
    nvlbazar "В 1991 году {b}СССР{/b} распался."
    nvlbazar "Канул в лету социалистический режим."
    nvlbazar "И Андрюшка смог зажить полноценной жизнью в стране под названием -{w} {b}Российская Федерация{/b}."
    nvlbazar "И в 1995 году,{w=0.2} в свои 20 лет он стал семьянином."
    nvlbazar "Жинился на не самой плохой тяночке."
    nvl clear
    nvlbazar "И в 1996 году у него родился сын."
    nvlbazar "Вы уже догадались,{w=0.2} про кого пойдёт рассказ."
    nvlbazar "Назвал он сына не Андреем..."
    nvl clear
    nvlbazar "Так появился на свет {b}Дмитрий Андреевич Скитецкий{/b}."
    nvlbazar "Вот на нём уже и отыгралось прошлое его прадеда."
    nvl clear
    nvlbazar "Димасик был редкосным ебанько и многолеткой конченной."
    nvlbazar "Он своим уебанским поведением вымораживал всех и каждого."
    nvlbazar "Что в интернете,{w=0.2} что в реальной жинзни."
    nvl clear
    nvlbazar "Но это будет потом."
    nvlbazar "Я начну своё повествование с 2017 года."
    nvl clear
    nvlbazar "В то время Димасик общался с двумя школьниками..."
    nvlbazar "Их ники были {b}thestrelok228{/b} и {b}tunechi_news{/b}."
    nvl clear
    nvlstr "Ну шо,{w=0.2} Димас...{w} Будешь новый порт рр тестировать?"
    nvlskt "Ну ясен хуй,{w=0.2} дружище!"
    nvlskt "Для чего я тогда тут по твоему?"
    nvl clear
    nvlbazar "А началось их знакомство с форума 4петуха{nw}"
    nvl clear
    nvlbazar "А началось их знакомство с форума {fast} {b}4PDA{/b}."
    nvlbazar "Дима,{w=0.2} после бомбежа на леново-форуме,{w=0.2} пришедший на 4pda реально кайфовал."
    nvlskt "Школьники знают больше,{w=0.2} чем модераторы,{w=0.2} ахуеть..."
    nvl clear
    nvlbazar "И так Димас с ними общался..."
    nvlbazar "Делился своими секретами..."
    nvlbazar "Они чё только не обсуждали."
    nvl clear
    nvlbazar "Дима ведал им тайны своей нелёгкой жизни в Новошахтинске."
    nvlbazar "Про работу на складе..."
    nvlbazar "Про то,{w=0.2} как он к дедушке через весь город топал..."
    nvl clear
    nvlbazar "В общем,{w=0.2} комьюнити у них было сплочённое."
    nvlbazar "Они вместе переживали все невзгоды форума."
    nvlbazar "Печатались в вк."
    nvlbazar "Потом один из членов команды VRT {w=0.2}(сокращённо - Vibe Rom Team) {w=0.2}предложил перекатиться в телеграмм."
    nvl clear
    nvlbazar "В тг началась новая эра срачей."
    nvlbazar "Ильнур и Медвед были на стороне Тунечика,{w=0.2} а Скит с Саньком и Сайленсом -{w=0.2} на стороне Стрелка."
    nvlbazar "Стрелок неистово психовал из-за неординарных рофлов Тунечика."
    nvlbazar "В то время Скит поддерживал Стрелка."
    nvl clear
    nvlbazar "Дима хоть и мудаком стал -{w=0.2} тем не менее..."
    nvlbazar "Раньше он был кульным мужичком."
    nvl clear
    nvlbazar "Но в один момент всё пошло по пизде."
    nvlbazar "Он перешёл дорогу одним нехорошим {b}школьникам из телеграмма{/b}."
    nvlbazar "А школьники-то злопяматные попались."
    nvl clear
    stop music fadeout 5
    scene zihao with ed_night_dis
    play music sail
    zih "Интересно{w=0.2}.{w=0.2}.{w=0.2}."
    zih "Но это же лишь твоя выдумка,{w=0.2} получается?"
    vchn "Именно так." with vpunch
    vchn "Просто если бы я,{w=0.2} как тебе изначально, {w=0.2}рассказывал всем,{w=0.2} что это {b}обычный додик из Новошахтинска{/b},{w=0.2} это звучало бы достаточно неказисто."
    vchn "А так -{w} ебать,{w=0.2} тут целая эпопея с происками {b}таинственного бандеровца из Новошахтинска{/b}."
    zih "Тяжко с тобой." with vpunch
    zih "Ну да ладно."
    zih "Как ты-то туда попал?"
    vchn "Всё просто." with vpunch
    vchn "Я в тот момент отдыхал с кентами в своём прекрасном городе Курске."
    vchn "В тг написал Дима и предложил наказать малолеток конченных."
    vchn "Так как весь рейв уже закончился,{w=0.2} я решил согласится на эту авантюру."
    vchn "Димка потом долго психовал из-за того,{w=0.2} что я не действую в открытую."
    vchn "Я и не собирался." with vpunch
    vchn "Просто потраливал этого лысика аккуратно."
    vchn "Всего-то."
    vchn "Да и весело было наблюдать за этими патау."
    zih "Интересно{w=0.2}.{w=0.2}.{w=0.2}."
    zih "Ты изначально не собирался его{nw}"
    vchn "Нет." with vpunch
    vchn "Это исключительно его вина."
    stop music fadeout 4
    zih "Так что дальше то было?"
    vchn "А дальше стоит прибегнуть к рассказу от лица тех,{w=0.2} с кем я там был."
    vchn "Там дальше вообще криндж пиздец." with vpunch
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    play music spineless fadein 5
    scene kohnyashvilli
    with ed_night_dis
    window hide
    show hataneonydisk at ed_get_achievement
    with dspr
    pause 7
    hide hataneonydisk with dspr
    nvlbazar "Неоня чиллил на кухне."
    nvlbazar "Делать было нечего."
    nvlbazar "Но на этой кухне он был не один."
    nvl clear
    play sound naebnylsya
    window hide
    pause 0.9
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
            'deadlylxrd'
        parallel:
            ypos 0.0 
            linear 0.01 ypos 0.0 
            linear 0.30 ypos 2.0 
        parallel:
            rotate 0.0 
            linear 0.01 rotate 90.0 
    with Pause(0.61)
    show deadlylxrd:
        ypos 2.0 rotate 90.0 
    pause 1.5
    hide deadlylxrd
    play sound uebalsya
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
            'deadlylxrd'
        parallel:
            ypos 2.0 
            linear 0.68 ypos 1.5 
            linear 0.20 ypos 1.2 
        parallel:
            rotate 90.0 
            linear 0.88 rotate 0.0 
    with Pause(0.98)
    show deadlylxrd:
        ypos 1.2 rotate 0.0 
    pause 1.6
    nn "Я,{w=0.2} конечно,{w=0.2} всё понимаю..."
    nn "Но этого я{nw}"
    nn "Но этого я{fast} не понимаю." with vpunch
    nn "Ты нахуя на стену полез?"
    lxrd "Да скучно,{w=0.2} пиздец..."
    nn "Именно поэтому ты решил пострадать хуйнёй?"
    lxrd "Именно."
    stop music fadeout 5
    play sound fb
    show overlay aw_memory_back_1
    hide deadlylxrd
    show deadlylxrd
    with flash
    "Неоня плюхнулся на диван и начал фантазировать."
    th "Как же меня иногда бесят его выходки..."
    th "Иногда настолько,{nw}"
    th "Иногда настолько,{fast} что я готов порешить этого гада." with vpunch
    th "Прям сплю и вижу:{w} достаю эмочку и начинаю шмалять по нему..."
    play music bif
    window hide
    play sound dostalstvol
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 2.0 
            linear 0.30 ypos 1.0 
    with Pause(0.60)
    show m1:
        ypos 1.0 
    play sound osechka
    hide m1
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            pos (0.5, 1.0) 
            linear 0.08 pos (0.53, 1.05) 
            linear 0.08 pos (0.5, 1.0) 
    with Pause(0.60)
    show m1:
        pos (0.5, 1.0) 
    play sound blyat
    pause 0.5
    hide m1
    play sound mone
    show m2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm2'
        parallel:
            ypos 1.0 
            linear 0.20 ypos 1.07 
    with Pause(0.60)
    show m2:
        ypos 1.07 
    hide m2
    play sound mtwo
    show m3:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm3'
        parallel:
            pos (0.5, 1.07) 
            linear 0.16 pos (0.6, 1.0) 
    with Pause(0.60)
    show m3:
        pos (0.6, 1.0) 
    hide m3
    play sound mthree
    show m4:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm4'
        parallel:
            pos (0.5, 1.15) 
            linear 0.16 pos (0.5, 1.0) 
    with Pause(0.60)
    show m4:
        pos (0.5, 1.0) 
    hide m4
    play sound mfour
    show m5:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm5'
        parallel:
            xpos 0.5 
            linear 0.16 xpos 0.75 
            linear 0.16 xpos 0.5 
        parallel:
            ypos 1.0 
            linear 0.40 ypos 1.06 
    with Pause(0.60)
    show m5:
        pos (0.5, 1.04) 
    hide m5
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 1.06 
            linear 0.16 ypos 1.0 
    with Pause(0.60)
    show m1:
        ypos 1.0 
    hide m1
    play sound strelnul
    hide deadlylxrd
    show lordspr1
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            pos (0.5, 1.0) 
            linear 0.08 pos (0.6, 1.15) 
            linear 0.08 pos (0.5, 1.0) 
    with Pause(0.60)
    show m1:
        pos (0.5, 1.0)   
    hide m1
    play sound strelnul
    hide lordspr1
    show lordspr2
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            pos (0.5, 1.0) 
            linear 0.08 pos (0.6, 1.15) 
            linear 0.08 pos (0.5, 1.0) 
    with Pause(0.60)
    show m1:
        pos (0.5, 1.0)  
    hide m1
    play sound strelnul
    hide lordspr2
    show lordspr3
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            pos (0.5, 1.0) 
            linear 0.08 pos (0.6, 1.15) 
            linear 0.08 pos (0.5, 1.0) 
    with Pause(0.60)
    show m1:
        pos (0.5, 1.0) 
    hide lordspr3
    hide m1
    show lordspr3:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    show m1
    play sound padenie
    stop music fadeout 5
    pause 1
    hide m1
    play sound ubralstvol
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 1.0 
            linear 0.21 ypos 2.0 
    with Pause(0.60)
    show m1:
        ypos 2.0 
    hide m1
    hide lordspr3
    pause 0.5
    play sound fb
    hide overlay aw_memory_back_1
    show deadlylxrd
    with flash
    play music totden fadein 2
    lxrd "О чём задумался?" with vpunch
    "Вывел Неоню из раздумий голос Вадимки."
    nn "Да так..."
    nn "Ничего интересного..."
    window hide
    pause 1
    lxrd "Ты понимаешь,{w=0.2} что нам нужно действовать?" with vpunch
    nn "Да ты ебать только об этом и говоришь."
    nn "Но вот дельного плана у тебя нет."
    lxrd "Всмысле нет,{w=0.2} блять?" with vpunch
    lxrd "Чем тебе не нравится идея протаранить скитовые ворота на лиазике?"
    nn "Начнём с того,{w=0.2} что у тебя{nw}"
    nn "Во первых блять..." with vpunch
    nn "Нет прав категории C."
    nn "Во вторых блять..." with vpunch
    nn "Где ты возьмёшь лиазик?"
    lxrd "Свои прихваты."
    lxrd "Да и зачем мне права,{w=0.2} ёпта?"
    lxrd "Ради одного раза?"
    nn "Ты не понял."
    nn "Если у тебя есть права категории C,{w=0.2} то,{w=0.2} как минимум, {w=0.2}ты знаешь,{w=0.2} как рулить этим самым лиазиком,{w=0.2} чтоб сделать всё красиво."
    lxrd "Тут не поспоришь."
    nn "У меня идея лучше есть."
    nn "Ебанём забор с помощью тротилла." with vpunch
    play sound smeh
    window hide
    pause 2
    lxrd "Орнул сука."
    lxrd "Где ты тротил высрешь?"
    nn "Как говорил один дцп патау додик..."
    nn "Имею свои прихваты." with vpunch
    lxrd "Ах ты ска..."
    lxrd "Ладно."
    lxrd "Но в Новошахтинск мы с тобой как попадём?" with vpunch
    nn "Об этом позже подумаем."
    stop music fadeout 5
    nn "Сейчас есть вещи более насущные."
    lxrd "Например?"
    nn "В одном из походов я умыкнул из под носа лысой кое что..."
    lxrd "Не тяни."
    window hide
    play music totden1
    pause 3.2
    nn "Это сейф Скитецкого." with vpunch
    window hide
    play sound chivo_blyat
    pause 1
    nn "Да-{w=0.2}да,{w=0.2} ты не ослышался."
    nn "И его желательно бы открыть."
    lxrd "Погоди." with vpunch
    lxrd "Не торопи события."
    lxrd "Может быть,{w=0.2} там находится {b}ТО{/b},{w=0.2} что нам видеть нежелательно вот от слова {b}СОВСЕМ{/b}?"
    nn "Может ты и прав."
    nn "Но я не хочу сидеть и ждать у моря погоды."
    nn "Там что-то точно есть." with vpunch
    nn "И это что-то может пролить свет на тайны лысой нимфоманки."
    nn "Улавливаешь суть?"
    lxrd "Ебать ты конченный псих." with vpunch
    lxrd "Тебе не приходило в голову элементарное,{w=0.2} очевидное,{w=0.2} да даже блять максимально простое и понятное..."
    lxrd "Что этот сейф{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "Может быть заминирован?" with vpunch
    window hide
    pause 1
    nn "И чем же?"
    nn "Первым корсаром блять?" with vpunch
    lxrd "Не обязательно им."
    lxrd "Там может быть что угодно."
    lxrd "Может,{w=0.2} там лежит страпон для анальных утех Димы?"
    lxrd "Нахуй оно тебе такое надо?" with vpunch
    lxrd "Сам себе ответь на вопрос."
    nn "Может,{w=0.2} ты и прав..."
    nn "Пока тогда оставим этот сейф до лучших времён."
    lxrd "Вот и хорошо."
    lxrd "Единственная дельная мысль от тебя."
    stop music fadeout 5
    lxrd "Ну а насчёт Новошахтинска{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "Какие у тебя есть варианты?"
    nn "Есть одна идея{w=0.2}.{w=0.2}.{w=0.2}."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Бергенчика:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music chrnthme fadein 2
    play sound fb
    play ambience rain_in fadein 2
    scene nmall
    show doshd
    with flash
    brg "Ты говорил,{w=0.2} что всё пройдёт гладко{w=0.2}.{w=0.2}.{w=0.2}."
    brg "Они скрепя зубами приняли меня в своё кредо."
    brg "Один из них даже выделился в хейте меня."
    brg "Own,{w=0.2} или как там его звать..."
    brg "И что в итоге?"
    brg "Ты напиздел." with vpunch
    brg "Для чего?"
    lis "Ты забываешь про поставленную задачу."
    brg "Ты мне тут не тыкай!" with vpunch
    brg "Я знаю,{w=0.2} что делаю."
    lis "Если бы я выдал тебе всю базу,{w=0.2} ты бы никогда не согласился."
    lis "Даже за ящик твоей любимой лимонной аскании." with vpunch
    lis "Хотя я прекрасно знаю,{w=0.2} насколько ты падок на такие вещи."
    lis "Да и потом -{w=0.2} неужели ты кинешь своего старого друга из-за какой-то хуйни?"
    lis "Ах,{w=0.2} да{w=0.2}.{w=0.2}.{w=0.2}.{w} Ахаха{w=0.2}.{w=0.2}.{w=0.2}."
    lis "{b}Номер Третий{/b} тоже не хотел верить в это{w=0.2}.{w=0.2}.{w=0.2}."
    lis "И где он теперь?" with vpunch
    lis "А ведь ты дал негласную клятву{w=0.2}.{w=0.2}.{w=0.2}."
    lis "И самым ублюдским способом её нарушил."
    lis "Кто ты после этого?"
    lis "А,{w=0.2} блядь?!" with vpunch
    brg "Ха{w=0.2}.{w=0.2}.{w=0.2}."
    brg "Ну ты и чертила,{w=0.2} конечно{w=0.2}.{w=0.2}.{w=0.2}."
    brg "Не зная цимуса всей ситуации мне тут нотации читаешь{w=0.2}.{w=0.2}.{w=0.2}."
    brg "А сам то?"
    brg "Сам себе ответь на вопрос -{w} мне нужно отомстить,{w=0.2} или тебе?" with vpunch
    lis "А тут уж с какой стороны посмотреть."
    lis "Говорят,{w=0.2} они и тебе говна много сделали{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    brg "Давай не будем,{w=0.2} а?"
    brg "Я тебе ни о чём не напоминаю зазря."
    lis "Ха.{w} Ладно."
    lis "Но придётся кое-что сделать."
    brg "Что же?"
    lis "Я немного подотру твою память."
    lis "Закодирую некоторые моменты."
    lis "Анлокнуть смогу их тоже только я."
    lis "Поверь,{w=0.2} это для твоей же безопасности."
    brg "Типа,{w=0.2} чтоб не раскусили?"
    lis "Именно."
    lis "Сейчас я закодирую несколько этапов твоей памяти,{w=0.2} после чего отправлю прямиком к ним."
    lis "Возьмёшь СВД из моих личных запасов."
    lis "Только не наделай глупостей,{w=0.2} ладно?" with vpunch
    brg "Будет сделано."
    stop music fadeout 5
    stop ambience fadeout 5
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Пацанвы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music deviltown fadein 2
    play sound fb
    scene domext
    show deadlylxrd
    with flash
    window hide
    pause 1
    lxrd "Это,{w=0.2} блять,{w=0.2} как?!" with vpunch
    nn "Да я сам хуй знает."
    nn "Магия." with vpunch
    nn "Просто я умею пользоваться телепортом."
    lxrd "Ладно,{w=0.2} хуй с ним."
    lxrd "Ты тротил взял?"
    play sound dostal
    show bomba:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'bomba'
        parallel:
            ypos 2.0 
            linear 0.35 ypos 1.0 
    with Pause(0.60)
    show bomba:
        ypos 1.0 
    nn "Обижаешь."
    hide bomba
    play sound ubral
    show bomba:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'bomba'
        parallel:
            ypos 1.0 
            linear 0.35 ypos 2.0 
    with Pause(0.60)
    show bomba:
        ypos 2.0 
    lxrd "Мы прямо к дому Скитови переместились."
    lxrd "Чилль пока тут,{w=0.2} я сгоняю на разведку."
    nn "Базару зиро."
    hide deadlylxrd
    play sound nitroblya
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 0.5 
            linear 0.90 xpos 2.0 
    with Pause(1.00)
    show deadlylxrd:
        xpos 2.0 
    stop sound fadeout 1
    "И Вадимка погнал на разведку."
    window hide
    pause 1.5
    "Не прошло и пяти секунд,{w=0.2} как Вадимка вернулся."
    hide deadlylxrd
    play sound nitroblya
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos -1.0 
            linear 0.80 xpos 0.5 
    with Pause(0.90)
    show deadlylxrd:
        xpos 0.5 
    stop sound fadeout 1
    lxrd "Всё чисто,{w=0.2} пошли."
    nn "Держи камеру на готове,{w=0.2} ща будет разъёб лысой чучундры."
    stop music fadeout 5
    scene zaborskit with ed_lap
    window hide
    show zvukdisk at ed_get_achievement
    pause 7
    hide zvukdisk with dspr
    lxrd "Я снимаю,{w=0.2} стартуй!" with vpunch
    window hide
    play sound zabor1
    pause 21
    play sound dostal
    show bomba:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'bomba'
        parallel:
            ypos 2.0 
            linear 0.35 ypos 1.0 
    with Pause(0.60)
    show bomba:
        ypos 1.0 
    window hide
    play sound csgo1
    window hide
    pause 1.2
    scene zaborskit2
    pause 0.8
    play sound csgo
    pause 2
    scene zaborskit
    show normalno_ebanulo with dspr:
        ypos 0.15
        xpos 0.25
        zoom 1.6
    with vpunch
    pause 0.4
    scene zaborskit3
    play sound zabor
    with vpunch
    window hide
    pause 5
    scene zaborskit3:
        zoom 1.05 anchor (48, 27)
        ease 0.20 pos (0, 0) 
        ease 0.20 pos (25, 25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25, 25)
        repeat
    window hide
    pause 5
    scene domext:
        zoom 1.05 anchor (48, 27)
        ease 0.20 pos (0, 0) 
        ease 0.20 pos (25, 25)
        ease 0.20 pos (0, 0)
        ease 0.20 pos (-25, 25)
        repeat
    window hide
    pause 4
    scene domext
    window hide
    pause 3
    play sound nitroblya
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos -1.0 
            linear 0.80 xpos 0.5 
    with Pause(0.90)
    show deadlylxrd:
        xpos 0.5 
    stop sound fadeout 1
    lxrd "Не хочу тебя расстраивать, но..."
    hide deadlylxrd
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 0.5 
            linear 0.80 xpos 0.85 
    with Pause(0.90)
    show deadlylxrd:
        xpos 0.85 
    play sound bdog_groan_1
    show dobermann:
        default subpixel True 
        parallel:
            Null(900.0, 720.0)
            'dobermann'
        parallel:
            xpos -1.0 
            linear 0.80 xpos 0.5 
    with Pause(0.90)
    show dobermann:
        xpos 0.5 
    lxrd "Походу у нас проблемы!" with vpunch
    play sound flashbacksound
    scene black with flash
    $ MND_Chapter("От лица Димы:")
    scene zaborskit3 with ed_lap
    skt "Бля как прижало то,{w=0.2} потом забор починю!" with vpunch
    "И Дима полетел дристать."
    "В свой ненаглядный толчок."
    play sound flashbacksound
    scene black with flash
    $ MND_Chapter("От лица Пацанвы:")
    play music cop fadein 5
    scene domext
    show dobermann
    show deadlylxrd at right 
    with ed_lap
    play sound bdog_groan_1
    window hide
    pause 5
    lxrd "Нам пиздец..."
    th "Чё делать,{w=0.2} чё делать,{nw}"
    th "Чё делать, чё делать,{fast} ЧЁ ДЕЛАТЬ,{w=0.2} БЛЯТЬ?!" with vpunch
    play sound bdog_attack_2
    window hide
    pause 2
    "Доберман психует."
    th "Есть одна идея..."
    th "Надеюсь прокатит..."
    nn "Гули,{w=0.2} гули,{w=0.2} гули!"
    play sound ti_che_dyrak_blya
    with vpunch
    window hide
    pause 2
    nn "Ну я хотя бы попробовал!" with vpunch
    "И тут случилось то,{w=0.2} чего никто никак не мог ожидать."
    window hide
    play sound svdshot
    hide dobermann
    show dobermann1
    with vpunch
    pause 0.5
    play sound bdog_hurt_3
    pause 2
    play sound svdshot
    hide dobermann1
    show dobermann2
    with vpunch
    pause 0.5
    play sound bdog_hurt_2
    pause 2
    play sound svdshot
    hide dobermann2
    stop music fadeout 5
    show dobermann3
    with vpunch
    pause 0.5
    play sound bdog_die_0
    hide dobermann3
    show dobermann3:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    pause 2
    play sound zdarovaagali
    hide dobermann3
    show bergensvd:
        default subpixel True 
        parallel:
            Null(726.0, 754.0)
            'bergensvd'
        parallel:
            xpos -0.3 
            linear 0.50 xpos 0.25 
    with Pause(0.60)
    show bergensvd:
        xpos 0.25 
    play music nemec fadein 5
    pause 0.7
    lxrd "Здарова,{w=0.2} заебал."
    nn "Нихуяо."
    brg "Вы по душу Дмитрески притопали шоль?"
    brg "И без снаряги?" with vpunch
    lxrd "Онли тротил."
    brg "Это,{w=0.2} конечно,{w=0.2} ахуительно,{w=0.2} но стволы вам бы не помешали."
    nn "И где нам их взять?"
    brg "Пока с этим помочь не могу."
    brg "Но как на кармане лишние заваляются -{w} дам знать."
    lxrd "Хорошо, хорошо."
    window hide
    pause 1
    brg "Хули стоять?" with vpunch
    brg "Погнали Скитецкого натянём,{w=0.2} ёбаный в рот блять."
    brg "Я буду всаживать пулю за пулей в эту мразь."
    lxrd "Он остался без своего ручного добби..."
    lxrd "Я думаю,{w=0.2} этого достаточно."
    play sound da_ti_zaebal
    window hide
    pause 1.3
    nn "Погнали хоть уроним скитовый туалет."
    nn "У меня ещё остался кило C-4." with vpunch
    scene skittolkan with ed_lap
    stop music fadeout 5
    brg "Ты готов?"
    nn "Вроде да."
    brg "Дедлилхрд стартуй запись."
    lxrd "Запись пошла."
    window hide
    play sound tualetskit
    pause 22
    $ renpy.movie_cutscene('source/skitsret1.ogv')
    play sound tolkan4
    window hide
    pause 3
    play sound dostal
    show bomba:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'bomba'
        parallel:
            ypos 2.0 
            linear 0.35 ypos 1.0 
    with Pause(0.60)
    show bomba:
        ypos 1.0 
    window hide
    play sound csgo1
    window hide
    pause 1.2
    scene skittolkan2
    pause 0.8
    $ renpy.movie_cutscene('source/skitsret2.ogv')
    scene skitupalvtolkan
    play sound tolkan6
    window hide
    pause 12
    "Бергенчик не стал медлить."
    "Каждый свой панч он сопровождал не кислым подсрачником."
    window hide
    show bergensvd:
        default subpixel True 
        parallel:
            Null(726.0, 754.0)
            'bergensvd'
        parallel:
            xpos -0.3 
            linear 0.50 xpos 0.25 
    with Pause(0.60)
    show bergensvd:
        xpos 0.25 
    play music nemec fadein 5
    play sound cheskazathotelablyat
    with vpunch
    pause 3
    play sound maloletka
    pause 2
    play sound pomoika
    with vpunch
    pause 4
    play sound sobalatvoyaloh
    pause 7
    play sound viebueshsya
    with vpunch
    pause 3
    play sound ahuel
    pause 1
    play sound baklan
    with vpunch
    pause 2
    play sound ebanko
    pause 1
    play sound zaebali
    hide bergensvd
    show bergensvd:
        default subpixel True 
        parallel:
            Null(726.0, 754.0)
            'bergensvd'
        parallel:
            xpos 0.25 
            linear 1.31 xpos -0.3 
    with Pause(1.41)
    show bergensvd:
        xpos -0.3 
    stop music fadeout 5
    nn "Ты куда,{w=0.2} заебал?" with vpunch
    brg "Подальше отсюда." with vpunch
    lxrd "Я тоже ливаю."
    nn "Омг,{w=0.2} блять..."
    nn "Ладно."
    "И они втроём отправились в ближайшее кафе в Новошахтинске."
    play music wood fadein 5
    scene bar
    show deadlylxrd at right
    show bergennorm at left
    with ed_night_dis
    brg "Присаживайтесь,{w=0.2} пообщаемся."
    nn "Может по коктейльчику?" with vpunch
    brg "Дружище,{w=0.2} на 18 ты не тянешь."
    nn "Омг,{w=0.2} тут Скиту продают алко."
    nn "А он явно не похож на 26 летнего."
    lxrd "На все 40 тянет." with vpunch
    brg "Хах..."
    nn "Да у меня фотка паспорта подфотошопленная есть."
    brg "Ну дерзай."
    brg "Мне тогда бери грейпфрутовую хугу."
    lxrd "Мне возьми вишнёвый эссе."
    brg "Ёбу дал?" with vpunch
    lxrd "Да захотелось чёт..."
    hide deadlylxrd
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 0.75 
            linear 0.80 xpos 2.0 
    with Pause(0.90)
    show deadlylxrd:
        xpos 2.0 
    hide deadlylxrd
    hide bergennorm
    show bergennorm:
        default subpixel True 
        parallel:
            Null(508.0, 733.0)
            'bergennorm'
        parallel:
            xpos 0.25 
            linear 0.80 xpos -3.0 
    with Pause(0.90)
    show bergennorm:
        xpos -3.0 
    "Неоня пошёл к барной стойке."
    "Из под неё вынырнул Бармен."
    hide bergennorm
    show barman:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'barman'
        parallel:
            ypos 2.0 
            linear 0.80 ypos 1.0 
    with Pause(0.90)
    show barman:
        ypos 1.0 
    barmn "Чего изволите?"
    barmn "У меня как в греции -{w} всё есть!"
    "Неоня,{w=0.2} стараясь не выглядеть как инфантильный омежка,{w=0.2} выдал такую хуйню:"
    nn "Дружище,{w=0.2} плесни грейпфрутовой хуги,{w=0.2} вишнёвый эссе,{w=0.2} ну и..."
    th "Бля,{w=0.2} а мне чё взять?"
    barmn "Могу предложить вам свой лучший коктейль..."
    barmn "Называется он..."
    barmn "Лысая Малышка!" with vpunch
    th "Усилием воли и сжатием стаи анальных колец я смог удержать смешок."
    th "Коктейль Скита..."
    nn "А вы случаем не знаете Дмитрия Скитецкого?"
    th "Как бы ни к чему спросил я."
    barmn "Ёпт,{w=0.2} конечно знаем!"
    barmn "Этот патау был моим одноклассником."
    barmn "Его все хуесосили по-жести."
    barmn "Лично я ссал в то ведро,{w=0.2} которое он выносил,{w=0.2} когда дежурил."
    nn "У меня начал назревать вопрос..."
    barmn "Да-{w=0.2}да,{w=0.2} ручку я тоже обссыкал."
    barmn "Потом он с 9 ушёл в какую-то путягу."
    barmn "И больше я его не видел."
    nn "Оно и хорошо."
    nn "Он сейчас и не такой хуйнёй промышляет."
    nn "Создал сайт для своих ботов."
    nn "Вапдомик что-ли."
    nn "Там вроде даже есть раздел с интимками админок."
    nn "Но я чёт не догоняю..."
    nn "Если админки -{w} это боты..."
    nn "То в интимках у них..."
    nn "Код?"
    barmn "Дружище,{w=0.2} я в этом не разбираюсь."
    barmn "Ты вообще с чего этого ОКРщика вспомнил?"
    nn "Да просто он недавно на рутрекере детское порно спрашивал."
    nn "Насчёт раздачи."
    nn "Я ебать ахуел."
    nn "Первая мысль об этом в голову пришла,{w=0.2} ну и...{w} Да."
    lxrd "Ты скоро там?" with vpunch
    nn "Ща."
    barmn "Так ты коктейль будешь?"
    nn "Ох...{w} Давай свою лысую мартышку,{w=0.2} или как её там..."
    barmn "Ты не пожалеешь о сделанном выборе."
    nn "Посмотрим."
    "Неоня взял коктейли,{w=0.2} расплатился дебетовой картой {b}TINKOFF BLACK{/b} и пошёл к братве."
    hide barman
    show barman:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'barman'
        parallel:
            yanchor 1.0 
            linear 0.80 yanchor -2.0 
    with Pause(0.90)
    show barman:
        yanchor -2.0 
    hide barman
    hide deadlylxrd
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 3.0 
            linear 0.80 xpos 0.75 
    with Pause(0.90)
    show deadlylxrd:
        xpos 0.75 
    hide bergennorm
    show bergennorm:
        default subpixel True 
        parallel:
            Null(508.0, 733.0)
            'bergennorm'
        parallel:
            xpos -3.0 
            linear 0.80 xpos 0.25 
    with Pause(0.90)
    show bergennorm:
        xpos 0.25 
    brg "Ну,{w=0.2} чё там?"
    nn "Держите товар."
    window hide
    pause 1
    lxrd "А ты себе чё взял?"
    nn "Да вот..."
    nn "Местное фирменное."
    nn "Коктейль -{nw}"
    nn "Коктейль -{fast} Лысая Малышка." with vpunch
    window hide
    play sound smeh
    pause 2.5
    lxrd "Кто блять?"
    lxrd "Лысая Кочерыжка?"
    window hide
    play sound ksm7
    pause 4.8
    lxrd "Ну ты вжарил..."
    lxrd "Ух..."
    brg "Бля,{w=0.2} чуваки." with vpunch
    brg "Я на днях эту малышку впервые замешал с кентом!" with vpunch
    lxrd "С двухкнопочным,{w=0.2} надеюсь?"
    "Не удержался от подъёба Вадимка."
    brg "С двухметровым,{w=0.2} ёпта."
    brg "Да у меня даже видос на телефоне есть!" with vpunch
    "Все уставились на экран redmi 9t."
    $ renpy.movie_cutscene('source/buhlo.webm')
    nn "И когда это было?"
    brg "29 числа."
    nn "Это же вчера..."
    brg "Ага."
    lxrd "Чё у тебя видос весь рябит?"
    brg "Камеру поцарапал,{w=0.2} братиш."
    lxrd "Понял тебя."
    stop music fadeout 5
    window hide
    pause 2
    "После пары глотков этого чудесного этила, {w=0.2}Неоня перестал понимаять, {w=0.2}чё там вообще происходит бля."
    show blink
    "И вот, {w=0.2}он только прикрыл глаза, {w=0.2}как..."
    play music del3
    play ambience ogon fadein 5
    scene black
    scene avtobusgorit
    show unblink
    window hide
    pause 2
    hide unblink
    play sound chezah
    show bergennorm:
        default subpixel True 
        parallel:
            Null(508.0, 733.0)
            'bergennorm'
        parallel:
            xpos -3.0 
            linear 0.80 xpos 0.25 
    with Pause(0.90)
    show bergennorm:
        xpos 0.25 
    brg "Живой?" with dissolve
    brg "Заебись."
    nn "Я вообще ничего не помню!" with vpunch
    brg "Хорошо хоть не обрыганный."
    brg "А то после малышки и не такое бывает."
    nn "Откуда тут..."
    nn "Автобус?" with vpunch
    brg "Ну сейчас я тебе вкратце напомню."
    stop music
    stop ambience
    play sound fb
    scene black with flash
    window hide
    pause 1
    play sound flashbacksound
    play music wood fadein 5
    scene bar
    show bergennorm at left
    show deadlylxrd at right
    with ed_night_dis
    show blink
    "Неоня прикрыл глаза."
    lxrd "Всё таки я хочу эти ворота протаранить..."
    brg "На чём блять?" with vpunch
    lxrd "Не видел возле ментовки уазик припаркованный?"
    brg "Дядь,{w=0.2} ты ебу дал?" with vpunch
    lxrd "А что нас остановит?"
    lxrd "Кароче..."
    lxrd "Вы отвлекаете,{w=0.2} пока я его пизжу."
    brg "Ногами?"
    lxrd "Хуем по лбу!" with vpunch
    lxrd "Так ты в деле или как?"
    brg "Хуй с тобой."
    brg "Ты только моего сообщника разбуди."
    lxrd "Кхм."
    window hide
    play sound shashlik
    with vpunch
    pause 4
    hide blink
    show unblink
    pause 0.5
    lxrd "Наконец-то!"
    lxrd "Выдвигаемся."
    scene basketbol
    show bergennorm at left
    with ed_lap
    stop music fadeout 5
    nn "И..."
    nn "Чё нам с этим делать?"
    nn "Ещё подташнивает,{w=0.2} сука..."
    brg "У меня есть идея."
    brg "Включай свой ифон 6 и подрубай камеру."
    brg "Только пропущенных от мамы не пугайся,{w=0.2} гыгыгы..." with vpunch
    "Неоня включил камеру."
    "И начался пиздец."
    scene black
    $ renpy.movie_cutscene('source/basketbolnogoy.webm')
    play sound fb
    play music otec
    scene bg ext_path_day
    show bergennorm
    with flash
    "Им пришлось улепётывать по дворам и лесам."
    nn "Вроде оторвались..."
    brg "Ага."
    brg "Только вот одно мы не учли."
    brg "Как блять выбраться отсюда?" with vpunch
    window hide
    pause 1
    nn "Извиняюсь конечно за мат..."
    nn "Пизда." with vpunch
    brg "Ладно,{w=0.2} будем идти вперёд."
    brg "Куда-нибудь да точно выйдем."
    nn "Ну пошли."
    "И они двинули прямиком в ад нахуй{nw}"
    "И они двинули{fast} куда глаза глядят."
    window hide
    pause 1
    "Молчание заебало обоих."
    "Неоня первым решил прервать молчание."
    nn "Как ты со Скитом познакомился?" with vpunch
    "Бергенчик подумал над ответом."
    brg "Да на 4петуха."
    brg "В теме леновы этот полоумный писал,{w=0.2} что не может поставить рут из-за бутлупа."
    brg "И что на леново форуме одни дцп сидят,{w=0.2} из-за чего не могут внятно объяснить,{w=0.2} как рут ставить."
    nn "Ха."
    nn "Я тоже со скитом на пда познакомился."
    nn "Ток в теме редми 8."
    nn "По началу казалось,{w=0.2} что он норм тип."
    nn "А потом он башкой наебнулся."
    nn "Конкретно так."
    nn "И начал оскать без причины нашу троицу."
    nn "Вот так вот."
    brg "Понятно."
    window hide
    pause 1
    brg "Смотри,{w=0.2} там вроде автобус какой-то едет." with vpunch
    window hide
    pause 1
    stop music fadeout 4
    "Ладно."
    "Чем занимались наши два дцпешника уже понятно."
    "А чем же в это время занимался Вадимка?"
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Вадимки:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play sound fb
    scene int_bus with flash
    lxrd "Я смог..."
    lxrd "Я ахуенен." with vpunch
    play sound sfx_ed_gas
    window hide
    pause 4
    scene int_bus at ed_bus_move
    lxrd "Проще простого."
    window hide
    pause 1
    "Вадимка ехал к Львовскому переулку на скорости 228 километров в час."
    "Он кайфовал от сидения за баранкой."
    "Скорость возбуждала его."
    "Его {b}finger{/b} был близок к полюции."
    "Но он сдерживал запал страсти."
    "Ему ещё надо пацанов забрать."
    "Негоже ведь кентов кидать через писюн,{w=0.2} когда успех так близок."
    "Правда?" with vpunch
    window hide
    pause 1
    "Вадимка продолжал ехать нарушая все правила пдд."
    "И тут ему вспомнилась его бурная молодость."
    "Те времена,{w=0.2} когда он уже давно сдал на права,{w=0.2} да учил базе новисов."
    "Ментовских новисов." with vpunch
    "Даже на Курганское ТВ попал."
    stop sound
    $ renpy.movie_cutscene('source/lxrddrift.webm')
    play ambience gasmashina fadein 3
    play music pigges fadein 3
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Бергенчика:")
    hide zatemnenie with dissolve2
    "Дальше я смутно помню,{w=0.2} чё там вообще было."
    "Лысая Малышка даёт о себе знать."
    "Я мальца у тебя отпил."
    "Так же я не запомнил истинной цели нашей поездки."
    "Но самый яркий момент я помню точно."
    "После того, {w=0.2}как Вадимка угнал ментовскую тачку, {w=0.2}он поехал нас забирать."
    "Он забрал нас на выходе из лесополосы."
    "Ну а потом..."
    "Начался пиздец." with vpunch
    brg "ДАВИ ГАЗОК, {w=0.2}БРАТИШ!" with vpunch
    brg "МЫ ДОЛЖНЫ ПРОТАРАНИТЬ СКИТОВЫЕ ВОРОТА!" with vpunch
    "Вадимка выжал максимум из этого тазика."
    window hide
    play sound adrazgon
    pause 2
    scene vorotampizda
    play sound vorotampizdec
    with vpunch
    pause 1
    lxrd "ПИЗДА РУЛЮ!" with vpunch
    stop music fadeout 3
    stop ambience fadeout 2
    "И мы тогда полетели в кювет."
    play sound sfx_ed_crash
    scene black with dspr
    window hide
    pause 5
    play sound fb
    scene avtobusgorit
    show bergennorm at left
    with flash
    brg "Вот такая хуйня,{w=0.2} в общем."
    nn "Пиздец..."
    "К ним подошёл Вадимка."
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 3.0 
            linear 0.80 xpos 0.75 
    with Pause(0.90)
    show deadlylxrd:
        xpos 0.75 
    lxrd "Чуваки, {w=0.2}это пиздец..."
    brg "Да кто ж спорит-{w=0.2}то блять?"
    nn "Куда теперь двигаем?"
    play sound ssikanul
    play music orchid fadein 5
    skt "Никуда." with vpunch
    nn "Мне лучше не оборачиваться?"
    brg "Не стоит."
    brg "Бля,{w=0.2} я же ведь свд забыл..." with vpunch
    lxrd "Пиздец..."
    "Неоня очень не хотел оборачиваться."
    "Пиздец как."
    "Но это было необходимо."
    play sound ssikanul
    scene skitscary with vpunch
    skt "Ну что?"
    skt "Малолетки конченные?!" with vpunch
    skt "Сейчас вы за всё ответите!" with vpunch
    skt "ТЫ!" with vpunch
    "Он показал на Вадима Морозова."
    skt "ЗАЕБЁШЬСЯ СТРАДАТЬ!" with vpunch
    skt "ТЫ!" with vpunch
    "Он показал на Дамирку Неоню."
    skt "ЗАЕБЁШЬСЯ ЖАЛЕТЬ!" with vpunch
    skt "А ТЫ!" with vpunch
    "Он показал на Бергенчика."
    skt "ТЫ... {w}Бля..." with vpunch
    skt "Кароче, ты заебёшься выкарабкиваться."
    skt "Но если сможешь..."
    stop music fadeout 5
    brg "Ты про что вообще блять?"
    window hide
    play sound zaebali
    pause 3
    scene black with flash
    play sound shelchok
    "Щелчок пальцами."
    "Мир перед глазами погас."
    $ MND_Chapter("Повествование от лица Неони:")
    th "И где я,{w=0.2} блять?"
    "Перед его глазами была самая настоящая пустота."
    "Со временем картина начала проясняться."
    play music raw fadein 5
    scene int_bus_night with ed_night_dis
    nn "Какого..."
    nn "Где я?" with vpunch
    "Дамирка очнулся в пустом автобусе,{w=0.2} что стоял посреди дороги и не двигался."
    play sound teleport
    scene int_bus_black
    show skitpio
    with flash
    skt "Добро пожаловать." with vpunch
    nn "ДА КУДА,{w=0.2} СУКА?!" with vpunch
    skt "Это твой персональный ад." with vpunch
    skt "А нет,{w=0.2} вру."
    skt "Не только твой." with vpunch
    nn "ЧТО?!" with vpunch
    skt "Счастливо оставаться." with vpunch
    play sound teleport
    hide skitpio with flash
    nn "Заебись..."
    golosone "Дамирка{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    "Хуй пойми откуда взявшиеся голоса начали пугать Неоню."
    golostwo "{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}ты пожалеешь{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    golosthree "{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}о сделанном выборе{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    nn "СУКИ,{w=0.2} ЧТО ВАМ ОТ МЕНЯ НАДО!?" with vpunch
    "Дамирка уже конкретно психовал."
    golosone "МЫ не дадим тебе{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    golostwo "{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}нормально существовать{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    golosthree "{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}как раньше." with vpunch
    nn "ЧТО ВЫ ИМЕЕТЕ В ВИДУ?" with vpunch
    golosone "Ты должен{w=0.2}.{w=0.2}.{w=0.2}."
    golostwo "{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}пройти{w=0.2}.{w=0.2}.{w=0.2}."
    golosthree "{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}наше испытание."
    nn "Куда я попал..."
    nn "Пиздец..."
    stop music fadeout 5
    scene black with ed_night_dis
    play music sail
    scene zihao with ed_night_dis
    zih "Истории у тебя{w=0.2}.{w=0.2}.{w=0.2}."
    zih "Конечно{w=0.2}.{w=0.2}.{w=0.2}."
    zih "Огонь.{w} Ничего не сказать тут больше." with vpunch
    vchn "Тебе не понравился момент,{w=0.2} где мы ему забор уронили?"
    zih "Это цветочки."
    zih "Как он вас с бесконечное лето отправил,{w=0.2} блять?" with vpunch
    vchn "У него спр{nw}"
    vchn "А,{w=0.2} ну да." with vpunch
    vchn "Уже не получится."
    vchn "Не знаю я,{w=0.2} кароче."
    zih "Ладно."
    zih "На сегодня с меня хватит твоих бредней."
    zih "Выводите его нахуй отсюда." with vpunch
    "Два амбала поднялись и взяли Вечного."
    "Тот лишь горько усмехнулся."
    vchn "Всё ещё не веришь мне?"
    "Зихао ничего на это не ответил."
    "Он лишь пожал плечами,{w=0.2} когда амбалы выводили Вечного из кабинета Зихао."
    "Зихао лишь налил коньячку и расслабился в кресле под треки {b}AWOLNATION{/b}."
    "Ему было уже всё равно."
    "Он ценил каждую секунду своего одиночества."
    "Именно в этом они были очень похожи друг на друга."
    "Вечный тоже своё время очень ценит."
    "В отличие от нервов."
    "Но это уже совсем другая история{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 5
    show zatemnenie with dissolve2
    $ MND_Chapter("Конец первого картера")
    return

label akttwo:
    scene black with ed_night_dis
    play music sail fadein 2
    scene zihao with ed_night_dis
    zih "Продолжим наш разговор?"
    vchn "Ты уже во второй раз мне это говоришь."
    zih "На вопрос ответь." with vpunch
    vchn "Мне некуда бежать больше."
    vchn "Так вот..."
    vchn "Скит подтёр мне маленько память."
    vchn "Я вообще не помню,{w=0.2} как оказался в Курске."
    vchn "Причём не помнит и Саня."
    vchn "Либо я у него просто не спрашивал."
    zih "Интересно..."
    vchn "Ну и в итоге дальше всё снова закрутилось необъяснимыми методами..."
    zih "Тебе не приходило в голову,{w=0.2} что это всё психоделический трип?" with vpunch
    vchn "Приходило."
    vchn "Но я за свои 20 лет так и не попробовал наркотики."
    vchn "Не моё это."
    zih "Просто мне иногда кажется..."
    zih "Чуть-{w=0.2}чуть совсем..."
    zih "Что ты этот бред на ходу сочиняешь." with vpunch
    vchn "Я тоже хочу в это верить."
    vchn "Но,{w=0.2} братиш..."
    stop music fadeout 5
    vchn "Я всё это видел своими глазами."
    vchn "На трезвую голову."
    vchn "Так что..."
    zih "Ладно,{w=0.2} что там дальше было-{w=0.2}то?"
    play music frosty
    scene sovenok with ed_night_dis
    scene sovenokblur with dissolve2
    $ MND_Chapter("The Carter Two:")
    $ MND_Chapter("Планапокалипсис")
    scene sovenok with dissolve2
    nvl clear
    nvlbazar "Ты говорил -{w=0.2} я слушал."
    nvlbazar "Так было всегда."
    nvlbazar "До одного момента."
    nvl clear
    nvlbazar "Какова цена ошибки?"
    nvlbazar "Каждый эту фразу понимает по-разному."
    nvlbazar "Как по мне -{w=0.2} если ты долбоёб,{w=0.2} то и ответишь соответствующе."
    nvlbazar "И наши святая троица пошла против дяди Димы совершенно не представляя,{w=0.2} что он может высрать в ответ."
    nvl clear
    nvlbazar "Не буду сразу выкидавать все козыри на стол."
    nvlbazar "Начнём с Дамирки Неони."
    nvl clear
    nvlbazar "Скит закинул его в бесконечное лето."
    nvlbazar "Каким образом?"
    nvlbazar "Блять ты заебал нахуй сказку интересную портить блядь ебанько{nw}"
    nvl clear
    nvlbazar "А попал он именно в подобие рута Мику."
    nvlbazar "Интригует,{w=0.2} правда?{w} Ахаха."
    nvl clear
    nvlbazar "Так вот наш Kossack очнулся в автобусе после драммы с тремя голосами."
    nvlbazar "А что было дальше мы с вами сейчас и узнаем."
    nvl clear
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene int_bus_night
    show unblink
    pause 1
    nn "Хорошо вчера побухал..."
    nn "Ща в школу пойду..."
    window hide
    pause 2
    nn "Не понял." with vpunch
    nn "Какого хуя?" with vpunch
    "Дамирка огляделся и понял,{w=0.2} что попал в бесконечное лето."
    "Он знал об этой игре по рассказам Бергенчика."
    "Так что шансов у него было мало."
    $ say_poplil = True
    scene anim pizda_ot_skita with dissolve2:
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
    "Весь мир перед глазами Дамирки начал плыть."
    nn "Что{w=0.2}.{w=0.2}.{w=0.2}."
    "Он просто не знал,{w=0.2} что в такой ситуации делать."
    "Он стоял и ахуевал."
    "Ну,{w=0.2} как стоял..."
    "Лежал и корчился." with vpunch
    nn "Пи{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2}здец{w=0.2}.{w=0.2}.{w=0.2}."
    "Это всё что он смог выдавить из себя."
    "Помимо лужи блевотины."
    "Лысая малышка не щадит никого." with vpunch
    window hide
    pause 1
    $ say_poplil = False
    scene int_bus_night with flash
    "Однако,{w=0.2} его быстро отпустило."
    nn "Ебануться..."
    window hide
    pause 1
    "Окончательно придя в себя,{w=0.2} Дамирка возле сидения обнаружил ствол."
    nn "АХУЕТЬ!" with vpunch
    "Это была автоматическая винтовка M4A1 с расцветкой Сайрекс."
    window hide
    play sound dostalstvol
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 2.0 
            linear 0.30 ypos 1.0 
    with Pause(0.60)
    show m1:
        ypos 1.0 
    window show
    nn "Да тут по-богатому..."
    nn "Кем бы ты ни был,{w=0.2} от души,{w=0.2} братишка!" with vpunch
    window hide
    play sound ubralstvol
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 1.0 
            linear 0.21 ypos 2.0 
    with Pause(0.60)
    show m1:
        ypos 2.0 
    hide m1
    window show
    "Дамирка повесил ствол на плечо."
    "После чего поспешно ретировался на улицу."
    stop music fadeout 5
    window hide
    scene int_bus_night:
        align (0.5, 0.5) zoom 1
        ease 1.2 align (0.7, 0.4) zoom 1.5
    pause 1
    scene sovenok with vpunch
    nn "Ну типа."
    "Дамирка разглядывал эти ебучие ворота."
    nn "Похожи на те самые скитовые ворота."
    nn "Которые Вадимка вынес вперёд{w=0.2}.{w=0.2}.{w=0.2}.{w} Дверями?"
    nn "гы" with vpunch
    window hide
    play music sexmetal
    pause 1
    "Около ворот лежало три магазина для винтовки."
    "Дамирка поднял их."
    window hide
    pause 1
    "Он стоял и глазел как баран на новые ворота."
    "Впрочем,{w=0.2} так и было."
    "До одного момента."
    window hide
    pause 1
    "Дамирка услышал сзади какое-то копошение."
    "Он обернулся."
    scene ext_bus_night
    show slzombar
    with pushright
    window hide
    play sound da_ti_zaebal
    pause 1
    play sound dostalstvol
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 2.0 
            linear 0.30 ypos 1.0 
    with Pause(0.60)
    show m1:
        ypos 1.0 
    play sound osechka
    hide m1
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            pos (0.5, 1.0) 
            linear 0.08 pos (0.53, 1.05) 
            linear 0.08 pos (0.5, 1.0) 
    with Pause(0.60)
    show m1:
        pos (0.5, 1.0) 
    play sound blyat
    pause 0.5
    hide m1
    play sound mone
    show m2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm2'
        parallel:
            ypos 1.0 
            linear 0.20 ypos 1.07 
    with Pause(0.60)
    show m2:
        ypos 1.07 
    hide m2
    play sound mtwo
    show m3:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm3'
        parallel:
            pos (0.5, 1.07) 
            linear 0.16 pos (0.6, 1.0) 
    with Pause(0.60)
    show m3:
        pos (0.6, 1.0) 
    hide m3
    play sound mthree
    show m4:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm4'
        parallel:
            pos (0.5, 1.15) 
            linear 0.16 pos (0.5, 1.0) 
    with Pause(0.60)
    show m4:
        pos (0.5, 1.0) 
    hide m4
    play sound mfour
    show m5:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm5'
        parallel:
            xpos 0.5 
            linear 0.16 xpos 0.75 
            linear 0.16 xpos 0.5 
        parallel:
            ypos 1.0 
            linear 0.40 ypos 1.06 
    with Pause(0.60)
    show m5:
        pos (0.5, 1.04) 
    hide m5
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            ypos 1.06 
            linear 0.16 ypos 1.0 
    with Pause(0.60)
    show m1:
        ypos 1.0 
    hide m1
    play sound strelnul
    hide slzombar
    show slzombar1
    show m1:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'm1'
        parallel:
            pos (0.5, 1.0) 
            linear 0.08 pos (0.6, 1.15) 
            linear 0.08 pos (0.5, 1.0) 
    with Pause(0.60)
    show m1:
        pos (0.5, 1.0)   
    hide slzombar1
    hide m1
    show slzombar1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    show m1
    play sound padenie
    pause 1
    hide slzombar1
    nn "Фух мля..."
    "Дамирка одним хедшотом вынес эту мразь."
    "Потом он опомнился,{w=0.2} ведь могут и со стороны ворот полезть хуебесы."
    "Дамирка развернулся,{w=0.2} и{w=0.2}.{w=0.2}.{w=0.2}."
    scene sovenok
    with pushleft
    nn "Вроде никого."
    play sound fnaf 
    show us_dead:
        xalign 0.5 yalign 0.5 
        linear 0.3 zoom 5.5
    with vpunch
    $ renpy.pause(0.3)
    hide us_dead with dspr
    play sound2 padenie
    scene nebo1 with vpunch
    window hide
    pause 0.4
    play sound neeet
    with vpunch
    pause 0.4
    with vpunch
    pause 0.4
    with vpunch
    pause 0.4
    with vpunch
    pause 0.4
    play sound bm16_shoot
    scene nebo2 with vpunch
    window hide
    pause 0.8
    play sound padenie
    stop music fadeout 3
    scene nebo with vpunch
    cld "ВСТАВАЙ!" with vpunch
    scene sovenok
    show coldspr1
    with pushup
    play music flowers
    cld "Ебать ты лох,{w=0.2} брателло."
    nn "Колд, {w=0.2}ты?" with vpunch
    cld "Именно."
    cld "Пришёл спасти твою сраку."
    nn "Вовремя однако."
    cld "Мог и раньше." with vpunch
    cld "Просто хотел посмотреть на ебло твоё ахуевающее." with vpunch
    nn "Ну ты и мудила."
    nn "Я там чуть не усрался."
    cld "Ахаха." with vpunch
    cld "Ладно,{w=0.2} нам пора валить отсюда нахуй."
    cld "Это,{w=0.2} конечно, {w=0.2}остатки зомбарей."
    cld "Бергенчик и Вадимка тут уже постарались."
    cld "Тут вообще такая заваруха была, {w=0.2}пока тебя не было." with vpunch
    scene ext_road_night
    show coldspr1
    with pushright
    nn "Почему нам не съебаться на автобусе?"
    cld "Диман пробовал."
    cld "Как итог -{w=0.2} не заводится."
    nn "И он тут был?"
    cld "Да."
    cld "Там история просто под чай с пельменями."
    cld "Бергенчику воспоминание подменили."
    cld "Он думал,{w=0.2} что выехал со своим братом в другой конец города до девушки брата,{w=0.2} после чего уснул в 99 лиазике."
    cld "Но на деле всё оказалось куда серъёзнее."
    cld "Ебучий Скит..." with vpunch
    cld "И откуда у него такие силы только,{w=0.2} а?"
    stop music fadeout 5
    cld "Ну так вот{w=0.2}.{w=0.2}.{w=0.2}."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Бергенчика:")
    hide zatemnenie with dissolve2
    window hide
    pause 1
    play music sirius fadein 2
    pause 2
    scene act1komnata with ed_earth_draw
    "Наше унылое чудо сидело за компом." with dissolve2
    "Лениво потягиваюсь оно сделало последний глоток лимонной аскании."
    play sound drink
    window hide
    pause 0.6
    stop sound
    "Оно оглядело комнату."
    brg "Снова я втыкаю в никуда."
    "Да ну нахуй? {w=0.2}Неужели доходить начинает?"
    brg "Ща ещё малень поебланю и сяду за написание сюжета."
    "А,{w=0.2} нет."
    window hide
    pause 1
    brg "Сколько там сигарет осталось?"
    brg "Надеюсь,{w=0.2} что Саня не все спыхал."
    "Оно лениво посмотрело в пачку."
    "Там оставалась -{w=0.2} аж целая одна сигарета."
    brg "Надо пойти покурить."
    "И оно двинуло на балкон."
    play sound ssanayadver
    window hide
    pause 3
    scene act1ciga1 with ed_alpha_diss_fast
    window hide
    pause 3
    brg "Последняя..."
    "Оно...{w} Ладно,{w=0.2} знаю,{w=0.2} заебал с этим Оно..."
    "Кароче:{w=0.2} Берген подкурил ластовую сигу."
    play sound ciga0
    scene akt1ciga2 with ed_earth_draw
    play sound ciga1
    window hide
    pause 2
    "Он делает глубокую тягу."
    play sound kashel
    window hide
    pause 1.4
    brg "Крепкие,{w=0.2} сука..."
    scene akt1ciga4 with ed_night_dis
    brg "Пепельница уже почти вся полная..."
    scene akt1ciga3 with ed_night_dis
    "Пока Берген курил, {w=0.2}он думал о сюжете финальной обновы."
    brg "Если бы это не было бы слишком локльно,{w=0.2} можно было бы и в воркшоп..."
    brg "Но..."
    brg "Похуй.{w=0.2} Всё равно я это доделаю."
    brg "Уже скольким обещал."
    window hide
    play sound ciga1
    pause 2
    scene akt1ciga5 with ed_night_dis
    play sound ciga2
    window hide
    pause 2
    stop sound
    scene act1ciga6 with ed_earth_draw
    "Берген пошел садиться обратно за комп."
    play sound ssanayadver
    window hide
    pause 3
    scene act1ciga7 with ed_alpha_diss_fast
    window hide
    pause 3
    "На ноуте был открыт Notepad с первыми набросками текста."
    "Руки уже потянулись к клавиатуре,{w=0.2} как..."
    play sound pda1
    scene act1ciga7 with vpunch
    window hide
    pause 1.5
    brg "Блять,{w=0.2} я очконул..."
    "Он проверил уведомления на телефоне."
    "Ему написал старый добрый..."
    vsn "Здарова."
    play sound pda1
    vsn "Свободен сегодня?"
    "Ответ не заставил себя долго ждать."
    brg "Ясен хуй."
    brg "Предлагаешь пойти куда,{w=0.2} чтоль?"
    play sound pda1
    vsn "Именно."
    th1 "Бля,{w=0.2} надо звук выключить,{w=0.2} громко сука."
    vsn "Прикатывай до меня."
    vsn "Тебя будет ждать не кислый такой сюрприз."
    brg "Выдвигаюсь."
    scene act1komnata with ed_earth_draw
    brg "Не судьба мне сегодня сесть за написание."
    scene act1komnata with vpunch
    shv "Забеись поспал."
    brg "Да ёбана."
    play sound smehshvilli
    "Швилли начал заливаться."
    stop music fadeout 5
    brg "Это ещё что за нахуй?"
    shv "Тебе мой смех не нравится?"
    window hide
    pause 0.5
    brg "Ладно,{w} похуй."
    window hide
    pause 0.7
    brg "Че снилось-{w=0.2}то хоть?"
    shv "Хм..."
    "Швилли погрузился в воспоминания."
    play sound fb
    play music crysis3epilogue fadein 2
    scene roofburn
    with flash
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    shv "Идите к папочке!" with dissolve2
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    brg "Саня,{w=0.2} стреляй блеать!"
    $ _window_hide(dissolve)

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607

    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    $ renpy.pause (1)

    $ _window_show(dissolve)
    shv "Заряжаюсь!"
    window hide
    pause 0.5
    play sound gamaz
    pause 1
    stop sound
    "Берген с криком влетел внутрь здания, {w=0.2}в то время когда Саня не мог сосредодочиться и попасть в голову зомбарю."
    shv "Еблан,{w=0.2} ты что делаешь?!"
    "Швилли полетел за ним."
    $ _window_hide(dissolve)

    scene burnint
    with ed_alpha_diss_fast
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    $ renpy.pause (2, hard=True)

    show avtoreblansuka with dissolve:
        xpos 0.1
        zoom 1.5
        ypos -0.25

    $ _window_show(dissolve)
    brg "Прощай...{w=0.2} Швилли...{w=0.2} нет, Саня...{w=0.2} увидимся там,{w=0.2} где окажемся."
    $ _window_hide(dissolve)
    hide avtoreblansuka
    play sound gamaz
    show avtoreblansuka:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    pause 1
    stop sound
    $ _window_show(dissolve)
    "Гниль вцепилась в шею BERGENу."
    play sound suka1
    shv "СУКА!" with vpunch
    play sound suka2
    shv "СУКААААА!" with vpunch
    play sound suka3
    shv "СУКА{w=0.1}А{w=0.1}А{w=0.1}А{w=0.1}А{w=0.1}А!" with vpunch
    window hide
    hide SVD_wovystr_LW0607
    play sound clipin
    show SVD_wovystr_LW0607:
        ypos 0.0
        ease 0.5 ypos 0.5

    pause 1
    hide SVD_svystrel_LW0607
    play sound clipout
    show SVD_wovystr_LW0607:
        ypos 0.5
        ease 0.5 ypos 0.05

    pause 1
    "Швилли перезарядил СВД."
    scene burnint
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1

    $ _window_hide(dissolve)

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607

    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center


    $ _window_show(dissolve)
    shv "сдохните...{w} Сдохните...{w} СДОХНИТЕ!"
    $ _window_hide(dissolve)

    stop music fadeout 3
    pause (0.4)

    show slzombar:
        xpos 0.1
        ease 0.4 zoom 1.7 xpos 0.5

    play sound noj1
    show sl_blkg_LW0607 with hpunch
    show dark_LW0607
    show blood_LW0607
    hide sl_blkg_LW0607
    with ed_flash_red
    $ say_pizdec = False
    play sound smehshvilli2
    pause 0.32
    play sound smehshvilli3
    pause 0.32
    play sound smehshvilli2
    pause 0.75
    stop sound
    play sound fb
    scene act1ciga7 with flash
    pause 1
    "Вернувшись в реальность,{w=0.2} он ответил." with dissolve2
    shv "Да не, {w}нихуя интересного..."
    play music fools fadein 2
    window hide
    pause 1
    shv "Ты идёшь щас куда?"
    brg "Только собирался выдвигаться."
    brg "А что?"
    shv "Я тоже выдвигаюсь."
    shv "На 99 поедем?"
    brg "Он туда недоижжяит."
    shv "Ну похуй,{w} прогуляешься."
    brg "Да ты ахуел."
    brg "Да и с каких пор ты решил оставить такси и погонять на лиазике?"
    window hide
    pause 1
    shv "Ну, блять{w=0.2}.{w=0.2}.{w=0.2}.{w} Сложная экономическая ситуация."
    brg "Хах."
    brg "Я тебя понял."
    window hide
    pause 2
    scene vishel1 with ed_night_dis
    "Вот они уже стоят в лифте."
    window hide
    pause 1
    "Теперь они на первом этаже."
    play sound liftsuka
    window hide
    pause 2
    scene vishel2 with ed_night_dis
    brg "Какой прекрасный день!"
    brg "Запахи говна из под свежескошенной обосраной собаками травы неприятно щекочут ноздри."
    brg "Хочеться блевануть."
    shv "Ну а хули ты хотел?"
    brg "Вот то-то ж и оно."
    scene vishel2:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    "Они двинули к остановке."
    scene vishel3 with ed_night_dis:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    shv "Мне надо сегодня будет кое-что проверить."
    window hide
    pause 1
    brg "Что именно?"
    window hide
    pause 1
    shv "Да есть тут одна диллема..."
    shv "Мне будет грустно,{w} если она подтвердится."
    window hide
    pause 1
    scene vishel4 with ed_night_dis:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    brg "Будешь ловить рофлан грустинки?"
    shv "Конечно."
    window hide
    pause 1
    scene vishel5 with ed_night_dis:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    brg "А меня Вишневский вызывает."
    brg "Нахуя?{w} Я так и не понял."
    window hide
    pause 1
    brg "Надеюсь,{w} на что-то стоящее."
    window hide
    pause 1
    scene vishel6 with ed_night_dis:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat
    "Они почти пришли."
    window hide
    pause 1
    "Вдалеке показался подъезжающий лиазик."
    brg "Бля..."
    shv "Успеем."
    "Они они рванули,{w} буд-то убегали от злого доберманчика."
    scene vishel6 at ed_running_fast
    window hide
    pause 2
    scene vishel7 at ed_running_fast
    window hide
    pause 2
    scene vishel8 at ed_running_fast
    window hide
    pause 2
    scene vishel9 at ed_running_fast
    window hide
    pause 2
    scene liazik99 with vpunch
    play sound ustal
    window hide
    pause 2
    shv "Успели..."
    stop music fadeout 5
    window hide
    pause 1
    brg "Да..."
    show blink
    stop sound
    "Он закрыл глаза,{w} чтоб лучше перевести дыхание."
    play sound avtobus11
    window hide
    pause 9
    "Ииии..."
    window hide
    pause 1
    play sound avtobus12
    scene int_bus
    show unblink
    window hide
    pause 13
    play sound baran
    scene int_bus with vpunch
    window hide
    pause 1
    th1 "Чё бля происходит?" with dissolve2
    hide unblink
    window hide
    pause 1
    play sound manda
    scene int_bus with vpunch
    "Берген решил подойти ближе."
    scene int_bus:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat

    window hide
    pause 2
    scene int_bus
    show dimanspr at right
    play sound bochka
    dmn "Да ехай блять ебучая бочка!"
    play sound supersmeh
    window hide
    pause 1
    window hide
    pause 0.5
    play sound dimann
    brg "Диман!"
    window hide
    play music rastncbp
    pause 1
    dmn "А ты ещё откуда взялся?"
    brg "Честно?"
    brg "А ну хер его знает."
    window hide
    pause 1
    brg "Я со Швильком ехал..."
    window hide
    pause 1
    brg "Бля..."
    brg "А где Швилли?"
    dmn "Я тут только тебя вижу."
    th2 "Пиздец, без Сани тут будет грустно."
    window hide
    pause 1
    brg "Я тут спросить хотел."
    brg "Ты чё орёшь сука?!"
    window hide
    pause 1
    dmn "Да эта ебучая бочка не заводится нихера!"
    dmn "А меня за этим и послали."
    brg "Кто?"
    dmn "Мёртвый Лорд."
    window hide
    pause 1
    brg "Колокольчик нигде не отозвался."
    dmn "Ну блять,{w=0.3} Вадимка,{w=0.2} во!"
    brg "Понятно."
    window hide
    pause 1
    dmn "Зайди к нему тогда,{w} мне ещё возиться и возиться с этой хуйнёй!"
    brg "Где его найти хоть?"
    dmn "В здании клубов должен быть."
    window hide
    pause 1
    th1 "Я чё блять..."
    th1 "В бесконечное лето попал?"
    "Берген посмотрел в окно."
    brg "Ахуеть..."
    dmn "Что?"
    brg "Да я в окно наконец додумался посмотреть..."
    window hide
    pause 1
    dmn "Тебя только это удивляет?"
    brg "Да нет."
    brg "В ориге же как было..."
    brg "Semen попадал в лагерь из будущего и из зимы."
    brg "А я,{w=0.2} сука,{w=0.2} с лета приехал."
    brg "Да и ты явно не похож на Славю."
    window hide
    pause 1
    "Диман о чём-то задумался."
    dmn "Всё,{w=0.2} иди до Вадимки,{w=0.2} мне ещё работать надо."
    brg "Увидимся."
    "Берген двинул наружу."
    scene int_bus:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat

    show dimanspr at right:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat

    window hide
    pause 1.5
    scene ext_bus with ed_earth_draw:
        xalign 0.5
        yalign 0.5
        zoom 1.0
        parallel:
            linear 1.0 zoom 1.05
        parallel:
            ease 1.0 xalign 0.45
            ease 1.0 xalign 0.54
            repeat
        parallel:
            ease 1.5 rotate 1.2 zoom 1.07
            ease 1.5 rotate -1.4 zoom 1.045
            repeat

    window hide
    pause 1
    scene ext_bus
    window hide
    pause 0.5
    brg "И когда я успел только..." with dissolve2
    scene bg ext_camp_entrance_day with pushleft
    brg "Оказаться в игре,{w=0.2} сука!?"
    window hide
    pause 1
    stop music fadeout 4
    th1 "Это же один большой сюжет..."
    th1 "Который написал один больной на голову человек..."
    th1 "Смешно..."
    play music ctamus fadein 2
    window hide
    pause 2
    scene bg ext_bus with pushright
    show dimanspr at right
    dmn "У нас ебейшие проблемы!"
    "Берген обернулся на крики этого полоумного."
    dmn "Хватай винтовку и смотри в оба!"
    dmn "Сейчас сюда целая орава приползёт нахуй!"
    window hide
    pause 0.5
    play sound dostal
    show shstvol1:
        ypos 0.25
        ease 0.5 ypos 0.05

    "Берген взял в руки G36."
    brg "Повеселимся?"
    dmn "Нас сожрут нахуй!"
    dmn "Какое веселье?!"
    th1 "Диман чёта паникует попусту."
    th1 "Всё равно пока никого нет."
    scene bg ext_road_day with pushright
    play ambience zattack
    dmn "Смотри!"
    window hide
    show slzombar:
        default subpixel True 
        parallel:
            Null(233.0, 720.0)
            'slzombar'
        parallel:
            xpos -1.0 
            linear 0.35 xpos 0.2 
    with Pause(0.60)
    show slzombar:
        xpos 0.2 
    window show
    "Первый зомбарь был уже очень близко."
    "Но,{w=0.2} как вы понимаете,{w=0.2} Берген так просто не помрёт."
    play sound dostal
    show shstvol1:
        ypos 0.25
        ease 0.5 ypos 0.05

    $ _window_hide(dissolve)

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1
    hide slzombar
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide shstvol1
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show shstvol1
    play sound padenie
    pause 1
    scene bg ext_road_day
    show shstvol1
    brg "Первый зомбарь готов."
    play sound gotovgad
    dmn "Хорошо приложил гада!"
    "В магазине осталось 26 патронов."
    dmn "Но это ещё не все!"
    window hide
    pause 1
    dmn "Смотри!"
    window hide
    show slzombar:
        default subpixel True 
        parallel:
            Null(233.0, 720.0)
            'slzombar'
        parallel:
            xpos -1.0 
            linear 0.35 xpos 0.2 
    with Pause(0.60)
    show slzombar:
        xpos 0.2 
    window show

    brg "Вижу!"

    $ _window_hide(dissolve)

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1
    hide slzombar
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide shstvol1
    stop ambience
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show shstvol1
    stop music fadeout 3
    play sound padenie
    pause 1
    brg "Второй зомбарь готов."
    play music surface fadein 2
    scene bg ext_bus with pushleft
    show dimanspr at right
    dmn "Давай ствол и беги в лагерь,{w=0.2} я задержу остальных!"
    dmn "Ты там гораздо нужнее!"
    brg "Хорошо."
    brg "А почему второго ствола нет?"
    dmn "Да потому что блеать никто не ожидал тебя тут увидеть."
    brg "Ладно,{w=0.2} я побежал!"
    scene bg ext_bus at ed_running_fast
    show dimanspr at ed_running_fast
    window hide
    pause 2
    scene bg ext_camp_entrance_day at ed_running_fast with pushleft
    window hide
    pause 1
    scene bg ext_clubs_day at ed_running_fast
    window hide
    pause 1
    play sound sukispasite
    scene bg ext_clubs_day with vpunch
    th2 "Это из клубов."
    th1 "У меня ствола нет,{w=0.2} хули мне туда лезть?"
    th2 "Да может кого шкафом придавило."
    th "Ладно,{w=0.2} была не была!"
    play sound door_break
    scene bg int_clubs_male_day_baza
    show sheped_grust at right
    show slzombar:
        xpos 0.1
    with vpunch
    play ambience zattack
    "В клубах сидел наш старый знакомый."
    shg "Помоги брат!"
    shg "Зомбарь отжал у меня ПМ!"
    "Берген заметил ПМ возле своих ног."
    play sound dostal
    show pistolpm1:
        ypos 0.25
        ease 0.5 ypos 0.05

    "Берген взял пистолет."
    play sound pomogite
    window hide
    pause 2
    play sound idu1
    pause 2.5

    play sound pmshot111
    show pistolpm11
    hide pistolpm1
    $ renpy.pause (0.05)
    show pistolpm1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide pistolpm11

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound pmshot111
    show pistolpm11
    hide pistolpm1
    $ renpy.pause (0.05)
    show pistolpm1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide pistolpm11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound pmshot111
    show pistolpm11
    hide pistolpm1
    $ renpy.pause (0.05)
    show pistolpm1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide pistolpm11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound pmshot111
    show pistolpm11
    hide pistolpm1
    $ renpy.pause (0.05)
    show pistolpm1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide pistolpm11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide pistolpm1
    stop ambience
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show pistolpm1
    play sound padenie
    pause 1
    stop music fadeout 3
    brg "Вот и всё."
    window hide
    hide pistolpm1
    play sound ubralstvol
    show pistolpm1:
        ypos 0.05
        ease 0.5 ypos 1.0
    hide sheped_grust
    show sheped at right
    window show
    "Берген убрал ствол и отдал его Депешу."
    shg "По гроб жизни должен буду!"
    hide pistolpm1
    play music cctvcut
    brg "В лагере есть есть зомби?"
    shg "Да хз."
    shg "Я по датчикам смотрел когда,{w=0.2} то видел какие-то три приближающиеся объекта."
    brg "То есть,{w=0.2} зомбарей было всего трое?"
    shg "Получается."
    brg "И всех троих грохнул я."
    brg "Совпадение?"
    shg "А остальные два где были?"
    brg "Со стороны дороги пёрли."
    brg "Благо Диман помог."
    shg "Как,{w=0.2} если он даже стрелять не умеет?"
    brg "Ну так ствол-то у него был."
    shg "Ну,{w=0.2} тоже верно."
    window hide
    pause 1
    "Берген вспомнил,{w=0.2} зачем он пришел к клубам."
    brg "Не знаешь,{w=0.2} где найти Мёртвого Лорда?"
    shg "Зачем он тебе?"
    brg "Диман посоветовал его найти."
    window hide
    pause 1
    shg "Вообще,{w=0.2} он может быть где угодно."
    shg "Но для начала я бы советовал тебе проверить музклуб."
    shg "Если ещё помнишь, {w=0.2}где это."
    stop music fadeout 3
    brg "Я тебя понял."
    window hide
    pause 1
    "И Берген двинул искать Мертвого Лорда в музклуб."
    "Ну а сейчас..."
    play music highschool fadein 3
    scene bg int_catacombs_living1 with ed_earth_draw
    strlk "Заколебало уже тут париться..." with dissolve2
    strlk "Только телеэфиры меня и спасают."
    "Стрелок включил телевизор."
    window hide
    pause 1
    stop music fadeout 2
    "Включив единственный ловящий тут канал,{w=0.2} началась реклама."
    play sound reklama1
    window hide
    pause 18
    stop sound
    play music highschool fadein 3
    strlk "Обожаю эту хуйню!"
    "Такая реклама всегда поднимала настроение."
    "Наверное потому,{w=0.2} что он ещё не думал о том..."
    "Что все эти смехуёчки превратились в реальную деградацию."
    window hide
    pause 1
    "А может и думал."
    "Но ему было похуй."
    "Это же Стрелок."
    window hide
    pause 1
    "После рекламы началась его любимая передача..."
    "Comedy Sheped."
    "Там ведущий рассказывает свои ахуительные истории."
    "Сопровождая их нереальным ором."
    razrab "Где-то это уже было, {w}не?"
    th1 "Иди нахуй отсюда."
    razrab "У{w=0.2}-у{w=0.2}-у{w=0.2},{w=0.2} сука{w=0.2}({w=0.2}9"
    window hide
    pause 1
    strlk "Началось!"
    stop music fadeout 2
    scene comedysheped with flash
    play sound tv1
    window hide
    pause 86
    stop sound
    play sound supersmeh
    scene bg int_catacombs_living1 with vpunch
    window hide
    pause 2
    strlk "До слёз,{w} сука!" with dissolve2
    window hide
    pause 2
    "Но тут стрелку пришло голосовое сообщение."
    window hide
    play sound pda3
    pause 0.5
    play sound bergensmsstrelok
    pause 8
    "Незамедлительно последовал ответ,{w=0.2} тоже гска."
    play sound pda3
    pause 0.5
    play sound streloksmsbergen
    pause 9
    stop sound
    strlk "Сука,{w=0.2} тащиться к этому дцпешнику..." with dissolve2
    lis "Ради чего?"
    strlk "Вопрос остаётся открытым."
    "У него был целый гарем в этом мега подвале."
    th1 "Да и почему был?"
    "Стрелок создал себе всё для хорошей жизни."
    "И в этой хорошей жизни нет места всяким Семпаям."
    "Ну а сейчас..."
    scene black with ed_night_dis
    play sound fb
    scene squareanim with flash
    play music goloederevo fadein 3
    "Берген сидел на лавочке и наслаждался видами." with dissolve2
    th "Эхх..."
    window hide
    pause 1
    th "Сколько модов было мной пройдено..."
    window hide
    pause 1
    th "БвС, Пацанское лето, 7ДЛ, Саманта, прочий треш..."
    th "Но это не главное..."
    window hide
    pause 1
    th "А как я впервые лето проходил?"
    th "Ебааа..."
    window hide
    pause 1
    th "И ведь все правильно сделал!" with vpunch
    th "Ну,"
    play sound podik
    extend " почти..."
    "Берген затянулся ахуенной морозной жижей из миникана."
    "И кайфанул."
    th "А ведь когда лето впервые проходил,"
    play sound podik
    th " я ж ещё даже курить не начал..."
    window hide
    pause 1
    th "Насколько ж давно это было..."
    window hide
    pause 1
    th "Всё таки самый любимый момент -{w=0.2} с шахтами."
    th "И я хер его знает,{w=0.2} почему."
    window hide
    pause 1
    "Можно бесконечно гоняться хер пойми за кем."
    "С неизвестными целями."
    "Но одно Берген знал точно -"
    play sound podik
    brg "Надо насладиться моментом."
    brg "Такая возможность выпадает {w=0.2}(если и выпадает){w=0.2} очень редко."
    window hide
    pause 1
    "Берген ещё бы долго так просидел..."
    "Прокручивая очень старые,{w=0.2} очень добрые,{w=0.2} ностальгичные моменты."
    stop music fadeout 3
    "Как вдруг..."
    huiznaet "Берген!"
    scene black with ed_night_dis
    play sound fb
    scene bg int_old_building_night with flash
    play music pridengahpidor2 fadein 2
    strlk "Так,{w=0.2} а сейчас нужно сюрприз обойти..." with dissolve2
    window hide
    pause 2
    strlk "Ну вот и всё,{w=0.2} ебать."
    strlk "Где там это чучело?"
    "Стрелок вышел из здания."
    scene bg ext_old_building_night_moonlight
    show strelok
    with pushright
    window hide
    pause 1
    play sound chenado
    pause 1
    bergen1 "Да ниче особенного."
    bergen1 "Ты же понимаешь,{w=0.2} что это место под защитой?"
    strlk "Нет, {w=0.2}нихуя.{w=0.2} Я забыл о том,{w=0.2} что сам же её поставил."
    strlk "Дружище."
    play sound doebaliuzhe
    window hide
    pause 13
    bergen1 "Хм."
    bergen1 "Я сделаю вид,{w=0.2} что этого не было."
    bergen1 "Если ты ебальник завалишь и перестанешь возмущаться."
    bergen1 "И тогда может быть твоя жопка не будет изнасилована моим песюном."
    "Жопка Стрелка начала плавиться."
    strlk "Да ты ахуел!" with vpunch
    play sound dostal
    "Но когда Семпай достал ствол,{w=0.2} весь батхёрд сошёл на нет."
    window hide
    pause 1
    bergen1 "Ладно."
    bergen1 "Завтра сюда прибудет очень интересный персонаж."
    bergen1 "Если не забыл,{w=0.2} что на меня твоя защита не дейтсвует,{w=0.2} а ещё должен понимать,{w=0.2} что для завтрашнего гостя её нужно будет отключить."
    strlk "Сегодня чтоль?"
    bergen1 "Нет."
    bergen1 "Завтра и отключим."
    strlk "Ну, {w=0.2}хули{w=0.2}, пошли тогда в бункер."
    bergen1 "У меня как раз медовуха есть пол литра."
    strlk "Да ну нахуй?"
    bergen1 "Да-да,{w=0.2} пошли уже."
    stop music
    scene int_catacombs
    $ renpy.movie_cutscene("source/afewmomentslater.ogv")
    play music pridengahpidor1
    scene bg int_catacombs with flash
    show strelok
    bergen1 "Ну что ж..."
    bergen1 "Неплохо ты тут устроился..."
    lis "Это ещё что за хрен?"
    strlk "Давай потом,{w=0.2} а?"
    strlk "От желания глотнуть медовухи аж челюсти сводит."
    bergen1 "Хм."
    bergen1 "Хорошо."
    "Семпай заметил,{w=0.2} что Стрелок имел в виду кого-то другого."
    "Но сделал вид что не заметил."
    window hide
    pause 1
    bergen1 "Лови медовуху!"
    show blazer at spizdil
    pause 2
    hide blazer with dissolve
    play sound otkrilblazer
    pause 1
    play sound na_popei
    pause 1.5
    "Стрелок сделал глоток."
    window hide
    pause 1
    strlk "Есть курить..."
    strlk "Я как снова в 2019..."
    bergen1 "Курить нету,{w=0.2} есть только подик."
    strlk "Да это образно говоря."
    strlk "Так-то я в завязке уже третий месяц."
    bergen1 "Понял тебя."
    bergen1 "А я попарю этот tance черного цвета 2020 века."
    play sound podik
    strlk "Ха-ах..."
    play sound na_popei
    extend " Вовремя ты ж появился,{w=0.2} однако..."
    "Стрелок сделал большой глоток."
    bergen1 "Да."
    play sound na_popei
    extend " Сука,{w=0.2} мне оставь, {w=0.2}а!"
    "Стрелок протягивает священную бутыль Семпаю."
    window hide
    pause 1
    bergen1 "Я хотел снова Врата Штейна пересмотреть..."
    play sound na_popei
    extend " Второй сезон, {w=0.2}как в старые добрые..."
    "Семпай делает большой глоток, {w=0.2}затем делает тягу на поде."
    play sound podik
    extend " Ту самую жижку бруско гранат."
    bergen1 "Добивай."
    "Семпай протягивает бутыль священого нектара."
    strlk "А чё так?"
    bergen1 "Да не лезет уже."
    "И стрелок добивает бутыль."
    play sound na_popei
    extend " Одним большим глотком."
    window hide
    pause 1
    strlk "Ох,{w=0.2} лягу,{w=0.2} пожалуй."
    strlk "Заебался за день."
    bergen1 "Давай."
    bergen1 "Ты только не засни!"
    strlk "А, {w=0.2}ок."
    window hide
    show blink
    stop music fadeout 3
    pause 3
    play music menu11
    hide blink
    scene black
    play sound slonik
    window hide
    pause 1.5
    scene bunkerson
    show pahom:
        xpos 0.1
        ypos 0.0
    show unblink
    window hide
    pause 44.5
    hide pahom
    show pahom1:
        xpos 0.1
        ypos 0.0
    pause 23
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    pause 1
    play sound vystrel_LW06071
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607
    hide pahom1
    show pahom2:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    show hitmarkermlg_LW0607:
        ypos 0.0 xpos 0.28

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    pause 0.90
    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.015 xpos 0.28

    pause 0.125
    hide hitmarkermlg_LW0607
    hide pahom2
    hide SVD_wovystr_LW0607
    show pahom3:
        anchor (0.5, 0.5)
        pos (0.3, 0.5)
        ease 1.0 rotate 150 xpos 0.3 ypos 2.0
    show SVD_wovystr_LW0607
    pause 0.125
    play sound padenie
    pause 1
    stop music fadeout 3
    scene black with ed_earth_draw
    window hide
    pause 1
    play sound vstavai
    play music pridengahpidor1
    scene bg int_catacombs
    show strelok
    show unblink
    window hide
    pause 2
    bergen1 "Чё приснилось хоть?"
    "Стрелок вспомнил свой сон."
    window hide
    pause 1
    strlk "Там такая хуета,{w=0.2} тебе лучше не знать."
    window hide
    pause 1
    razrab "А сейчас мы вернемся к BERGENу."
    stop music fadeout 3
    scene black with ed_night_dis
    window hide
    pause 1
    play sound fb
    scene squareanim with flash
    play music goloederevo fadein 3
    huiznaet "Берген!" with dissolve
    th1 "Кто там такой настрный только..."
    "Берген обернулся."
    window hide
    show avelimespr:
        default subpixel True 
        parallel:
            Null(754.0, 724.0)
            'avelimespr'
        parallel:
            ypos 2.0 
            linear 1.00 ypos 1.0 
    with Pause(1.10)
    show avelimespr:
        ypos 1.0 
    window show
    avlm "Здарова,{w=0.2} заебал."
    brg "А,{w=0.2} ты."
    window hide
    pause 1
    avlm "А ты тут какими судьбами?"
    brg "Попал сюда я при невыясненных обстоятельствах."
    brg "Зачем?"
    play sound herznaet
    window hide
    pause 3
    brg "Как отсюда выбраться?"
    brg "Кхм." with vpunch
    brg "Аналогично."
    avlm "Да-а..."
    avlm "Не повезло тебе."
    brg "Мне никогда не везло."
    window hide
    pause 1
    "Повисло молчание."
    window hide
    pause 1
    avlm "Я че пришёл-то..."
    window hide
    pause 1
    avlm "Не поможешь пройти к одному очень интересному месту?"
    avlm "Старый лагерь зовётся оно."
    brg "А почему я?"
    brg "А как же Диман?"
    avlm "Нахуй его."
    avlm "Да и ты,{w=0.2} помнитcя,{w=0.2} говорил,{w=0.2} что лето проходил по 500 раз на дню."
    avlm "А я и решил, {w=0.2}что ты в этом ебучем лагере каждый уголок знаешь."
    brg "Сначала дойдём до музклуба."
    brg "Мертвий Лорд должен ждать меня там."
    brg "По крайнеё мере, мне так сказал Депеш."
    avlm "Ты уверен,{w=0.2} что он там?"
    brg "Нет." with vpunch
    brg "Но вариантов лучше у меня нет."
    avlm "Может,{w=0.2} он в старом{nw}"
    brg "Не может." with vpunch
    brg "Мы или идёт сначала в музклуб, {w=0.2}или ты просто пойдёшь нахуй." with vpunch
    "У Авелайма не оставалось выбора."
    avlm "Веди."
    play sound door_open
    scene bg int_musclub_day
    show avelimespr at right
    with ed_lap
    foma "Здарова бандиты." with vpunch
    brg "И тебе не хворать,{w=0.2} Фома."
    brg "Какими судьбами ты тут?"
    foma "Да вот школу,{w=0.2} в которой я работал,{w=0.2} закрыли."
    foma "А тут вакансия физрука была."
    foma "Вот я и решил податься в хлебные края."
    brg "Занимательно."
    brg "Слушай,{w=0.2} а ты не видел тут Мертвиго Лорду?"
    foma "Такой патлач и бородач одновременно?" with vpunch
    brg "Да."
    "Берген немного орнул с такого точного описания Вадима Морозова."
    foma "Был недавно."
    foma "Искал какого-{w=0.2}то типа в белой пятнистой куртке..."
    foma "Погоди." with vpunch
    foma "Так это ж получается,{w=0.2} что он тебя искал?"
    brg "Походу."
    foma "Он был тут полчаса назад."
    foma "Сказал,{w=0.2} что отправится к какому-{w=0.2}то старому лагерю."
    foma "Честно,{w=0.2} я в рот не ебу,{w=0.2} где это."
    foma "Но он должен быть там."
    avlm "А я тебе говорил..."
    brg "Ладно,{w=0.2} бывай,{w=0.2} Фома!" with vpunch
    foma "Ну как проветритесь,{w=0.2} заходите."
    "И они двинули по направлению к старому лагерю."
    "По пути рассматривая окресности."
    play sound door_open
    scene bg ext_playground_day
    show avelimespr
    with ed_night_dis
    avlm "Это местная спортплощадка?"
    brg "Да."
    brg "А ты обход территории не делал шоль,{w=0.2} как попал сюда?"
    avlm "Нет, {w=0.2}мне похуй было."
    brg "Я тебя понял."
    "И они двинули дальше."
    scene bg ext_path_sunset
    show avelimespr
    with ed_night_dis
    brg "Я думал,{w=0.2} что будет чуть ближе."
    avlm "Да я тоже так думал."
    brg "Ладно.{w=0.2} Похуй."
    "Они двинули дальше."
    scene bg ext_path2_day_posral with ed_night_dis
    play sound polzasral
    window hide
    pause 2
    avlm "Чё там?"
    brg "Там говно."
    brg "Куча говна."
    brg "Огроменная куча говна."
    show avelimespr with dissolve
    avlm "Да я уже учуял."
    brg "И кто мог столько насрать..."
    play sound fb
    scene bg int_clubs_male_day_baza
    show sheped_grust at right
    show slzombar:
        xpos 0.1
    with flash
    window hide
    pause 2
    play sound fb
    scene bg ext_path2_day_posral with flash
    brg "Хотя..."
    brg "Я,{w=0.2} походу понял,{w=0.2} кто столько насрал."
    avlm "И кто же?"
    brg "Да ты всё равно его не знаешь."
    window hide
    pause 1
    razrab "А я вам,{w=0.2} пожалуй,{w=0.2} покажу,{w=0.2} как всё было на самом деле."
    stop music fadeout 3
    scene black with ed_night_dis
    play sound fb
    play music bilbordi fadein 3
    scene bg ext_path_day at ed_running_fast with flash
    play sound begtrava
    melles "Прижало-то как,{w=0.2} блять!"
    "Бедная жопка буквально трещала по швам."
    "Димочке было очень больно."
    "Он не знал,{w=0.2} где можно сбилдить новый чидори кернел."
    "И поэтому пришлось выбирать рандомное место."
    scene bg ext_path2_day with ed_flash_red
    stop sound
    melles "Всё,{w=0.2} пиздец,{w=0.2} больше не могу..."
    "А что было дальше..."
    window hide
    play sound perdun
    pause 1
    play sound rid1
    pause 0.6
    play sound rid2
    pause 0.7
    play sound rid3
    pause 0.6
    play sound rid4
    pause 0.7
    play sound rid5
    pause 1
    play sound rid6
    pause 0.9
    play sound rid7
    pause 1
    play sound rid8
    pause 1
    scene bg ext_path2_day_posral with dissolve2
    window hide
    pause 1
    "...Вы только что сами узнали."
    melles "Хорошо-то как..."
    play sound shepedtrava
    window hide
    pause 1
    melles "Кто здесь?"
    "На поляну вышел наш старый знакомый."
    "Далее от его лица."
    scene bg ext_path2_day_posral
    show melles_spr
    with flash
    shg "Ты ахуел?" with vpunch
    shg "Не,{w=0.2} ну ты внатуре ахуел!!" with vpunch
    shg "Тут я посрать должен был!"
    "Шепед тоже пританцовывал."
    "Бедный."
    shg "Да за такое..."
    shg "Я всем расскажу,{w=0.2} что это ты насрал!" with vpunch
    shg "Вот!" with vpunch
    window hide
    pause 0.5
    "Но Димочка не растерялся и выдал свою коронную фразу."
    melles "Ты никому ничего не скажешь..."
    play sound mellesbazarit
    window hide
    pause 4
    shg "Я тебя услышал..."
    stop music fadeout 3
    scene black with ed_night_dis
    play sound fb
    scene bg ext_path2_day_posral with flash
    avlm "А,{w=0.2} может,{w=0.2} знаю?" with dissolve2
    brg "Хм."
    brg "Не исключено."
    stop music fadeout 5
    window hide
    pause 3
    brg "Почти пришли."
    "Обойдя огромную каху,{w=0.2} они двинули дальше."
    window hide
    pause 2
    play music pritheme fadein 2
    play sound shepedtrava
    scene bg ext_old_building_sunset with ed_earth_draw
    play sound nameste
    window hide
    pause 1.5
    "BERGENу на говнозвон приходит голосовое сообщение." with dissolve
    window hide
    pause 1
    show smska:
        default subpixel True xpos 0.5 
        parallel:
            Null(603.0, 724.0)
            'smska'
        parallel:
            ypos 2.0 
            linear 1.00 ypos 1.0 
    with Pause(1.10)
    show smska:
        pos (0.5, 1.0) 
    play sound zona_a
    pause 8
    hide smska
    show smska:
        default subpixel True 
        parallel:
            Null(603.0, 724.0)
            'smska'
        parallel:
            ypos 1.0 
            linear 1.00 ypos 2.0 
    with Pause(1.10)
    show smska:
        ypos 2.0 
    brg "Не понял..."
    hide smska
    "Берген отошел на безопасное расстояние."
    brg "Ты куда меня завёл?" with vpunch
    window hide
    pause 1
    "Берген огляделся."
    window hide
    pause 1
    "Но Авелайма нигде не было."
    window hide
    play sound hernyakakayato
    pause 1
    show smska:
        default subpixel True xpos 0.5 
        parallel:
            Null(603.0, 724.0)
            'smska'
        parallel:
            ypos 2.0 
            linear 1.00 ypos 1.0 
    with Pause(1.10)
    show smska:
        pos (0.5, 1.0) 
    play sound zona_a_off
    pause 3
    hide smska
    show smska:
        default subpixel True 
        parallel:
            Null(603.0, 724.0)
            'smska'
        parallel:
            ypos 1.0 
            linear 1.00 ypos 2.0 
    with Pause(1.10)
    show smska:
        ypos 2.0 
    brg "И?"
    hide smska
    "Тем временем в бункере..."
    stop music fadeout 5
    scene black with ed_earth_draw
    play sound fb
    play music chrnthme fadein 2
    scene bg int_catacombs
    show strelok
    with flash
    strlk "Защита отключена." with dissolve2
    strlk "Дальше что?"
    bergen1 "Ты не торопись."
    bergen1 "Лорд сделает всё красиво."
    bergen1 "Совсем скоро мы станем едины!"
    bergen1 "Как раньше..."
    strlk "Как до 2022 года?"
    bergen1 "Да!" with vpunch
    strlk "Скит,{w=0.2} конечно,{w=0.2} тоже молодец блять." with vpunch
    strlk "И нахуя он нас разделил?" with vpunch
    window hide
    pause 1
    bergen1 "Мы ему конкретно с забором подосрали." with vpunch
    window hide
    pause 1
    strlk "Поделом этой сучаре!" with dissolve
    window hide
    pause 1
    bergen1 "Вот и я про то же."
    window hide
    pause 1
    "Стрелку не нашлось, {w=0.2}что и сказать."
    bergen1 "Ну вот и всё."
    bergen1 "Решено!" with vpunch
    bergen1 "Ждём Лорда."
    stop music fadeout 6
    bergen1 "Он знает,{w=0.2} как эта херня работает."
    "Тем временем Диман и Депеш."
    scene black with ed_night_dis
    play sound fb
    play music lovewooman fadein 2
    scene bg int_clubs_male_day_baza
    show sheped
    with flash
    shg "Ты смотри!" with dissolve2
    "Шепед показал экран монитора Диману."
    shg "На лагерь прёт целая орава!"
    shg "Причём со стороны старого корпуса."
    play sound skolkoihzdes
    dmn "Как думаешь, {w=0.2}сколько их здесь?"
    play sound desyat
    shg "Десять?"
    play sound bolshe
    lxrd "Их тут гораздо больше." with vpunch
    play music mdknmus
    window hide
    pause 3
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos -1.0 
            linear 0.45 xpos 0.15 
    with Pause(0.60)
    show deadlylxrd:
        xpos 0.15 
    lxrd "Здарова,{w=0.2} дцпешники." with dissolve
    dmn "Здарова, {w=0.2}заебал."
    shg "Как жизнь пожилая?"
    lxrd "Неплохо."
    dmn "Чем вообще занимаешься?"
    lxrd "Да вот."
    window hide
    pause 0.7
    lxrd "Мне из трёх дцпешников нужно сделать одного."
    lxrd "Да направить его на путь истинный."
    shg "Он не в старом лагере, {w=0.2}случайно?"
    lxrd "Да."
    lxrd "А что?"
    window hide
    pause 1
    shg "Да туда ща орава зомбей прёт."
    dmn "Суда по датчикам,{w=0.2} скоро будет на месте."
    window hide
    pause 1
    lxrd "Хуёво."
    shg "И что делать будем?"
    lxrd "А сделаем так -"
    play sound fb
    scene bg ext_old_building_night_moonlight with flash
    extend " уже темно,{w=0.2} конечно,{w=0.2} но сражаться мы ещё сможем."
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    lxrd "Зомбарей будет тонна,{w=0.2} нам нужно крупнокалиберное оружие..." with dissolve2
    dmn "Есть СВД с экспансивными пулями."
    lxrd "Ну вот и отлично."
    lxrd "Возьмёшься отщёдкивать зомбей?"
    window hide
    pause 1
    dmn "Бля{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} Я стрелять не умею..."
    window hide
    pause 0.5
    lxrd "Мда...{w=0.2} А ты,{w=0.2} Депеш?"
    shg "Стрелять-то да.{w=0.2}.{w=0.2}.{w=0.2} Но вот попасть уже будет сложнее..."
    window hide
    pause 1
    lxrd "Ладно."
    extend " Хоть на что-то вы способны."
    dmn "Всегда рады!"
    lxrd "План такой:"
    show avtoreblansuka at right
    with dissolve
    extend " нам нужно,{w=0.2} чего бы это не стоило, {w=0.2}спасти BERGENа и его пиздабратию."
    hide avtoreblansuka with dissolve
    lxrd "А ещё,{w=0.2} мы скорее всего успеем туда до прибытия зомбей."
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    lxrd "А если нет -{w=0.2} Депеш,{w=0.2} пробуй стрелять!"
    $ _window_hide(dissolve)

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607

    show hitmarkermlg_LW0607:
        ypos 0.3 xpos 0.15

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    extend " Не убьёшь,{w=0.2} так заставишь ползти медленее."
    lxrd "А там посмортим,{w=0.2} может Берген стрелять умеет."
    shg "Я тебя услышал."
    window hide
    pause 0.5
    dmn "А мне что делать?"
    lxrd "Старайся глазами найти BERGENа."
    dmn "Хорошо."
    play sound fb
    scene bg int_clubs_male_day_baza
    show sheped
    show dlxrd at left
    with flash
    pause 0.5
    play sound pogudeli
    lxrd "Ну, чё тупим?{w=0.6} Всё, погудели." with vpunch
    "И они в темпе вальса начали собираться."
    scene bg int_clubs_male2_dildo with pushright
    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    "Депеш взял свд в подсобке."
    scene bg int_clubs_male_day_baza with pushleft
    play sound dostal
    show shstvol1:
        ypos 0.25
        ease 0.5 ypos 0.05

    "Диман крутил в руках свою старую добрую G36."
    window hide
    pause 1
    "А Лорд думал,{w=0.2} как по-быстрому добраться к старому корпусу."
    "В общем,{w=0.2} каждый был занят своим делом."
    stop music fadeout 5
    "Тем временем Берген..."
    scene black with ed_night_dis
    play sound fb
    play music leilamus fadein 4
    scene bg ext_old_building_sunset with flash
    window hide
    play sound torsmisnet
    pause 4
    play sound door_open
    scene bg int_old_building_night with pushleft
    brg "Темно здесь,{w=0.2} однако."
    window hide
    pause 0.5
    "Берген заметил люк."
    brg "Почему нет?"
    scene bg int_catacombs
    show strelok at right
    with pushleft
    "Далее от лица Стрелка."
    strlk "Слышишь?"
    bergen1 "Кто-то идёт..."
    play sound door_open
    window hide
    show avtoreblansuka:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'avtoreblansuka'
        parallel:
            xpos -1.0 
            linear 0.45 xpos 0.25 
    with Pause(0.60)
    show avtoreblansuka:
        xpos 0.25 
    window show
    "В конмату залетает Берген."
    brg "Эээ..."
    brg "Привет?"
    window hide
    pause 0.5
    strlk "Ну типа привет."
    brg "Я вас где-то уже видел..."
    bergen1 "Да мы тебя тоже."
    brg "И где же?"
    "Берген начал осмаривать комнату."
    "В его взор попала панель управления."
    "Берген осмотрел панель."
    "За его движениями внимательно следил Семпай."
    strlk "Ну как это откуда..."
    strlk "Нас Дима Скит разделил." with vpunch
    brg "Чего?" with vpunch
    strlk "Когда вы втроём протаранили забор,{w=0.2} Скит распсиховался и разделил тебя на нас троих."
    strlk "Ещё эта сучара подтёрла тебе память."
    strlk "Ты не ехал никуда с Саней."
    strlk "Хотя он тоже тут есть."
    strlk "Шоп он не подпортил тебе воспоминания,{w=0.2} Скит и ему память подтёр."
    strlk "Мы нашли его в атобусе до тебя."
    strlk "Он прихуел немного,{w=0.2} конечно..."
    strlk "Но мы дали ему чайку со снотворным и уложили спать."
    strlk "Шоп не мешался."
    brg "И где он?"
    bergen1 "Он в{w=0.2}.{w=0.2}.{w=0.2}.{nw}"
    strlk "Об этом позже." with vpunch
    strlk "Скит проебался."
    strlk "В этом бункере есть устройство,{w=0.2} что чисто теоретически должно собрать нас воедино."
    strlk "Но это чисто теоретически."
    strlk "Нас может и на атомы разнести."
    strlk "Улавливаешь суть?"
    brg "И вы двое зассали,{w=0.2} типа?" with vpunch
    brg "Ахаха..."
    strlk "Нет."
    strlk "Нам нужен был ты для объеденения."
    brg "И что мешает сделать это сейчас?"
    strlk "Нам нужен Лорд для более чёткой консультации."
    strlk "Проще говоря,{w=0.2} я в душе не ебу,{w=0.2} чё там нажимать блять."
    strlk "Вот так вот."
    window hide
    pause 0.5
    "В этот момент Берген заметил одну инетересную кнопку..."
    "Собрать Legion OS."
    "Семпай лишь успел крикнуть..."
    play sound stoimlya
    window hide
    pause 1
    "А Берген..."
    "Ему что-то подсказывало,{w=0.2} что эту кнопку нужно нажать."
    "Что-то вроде чуйки."
    extend " Называйте как хотите."
    "А в итоге..."
    extend " Берген не раздумывая нажал её."
    stop music
    play sound vibrosgvna
    scene bg int_catacombs:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat

    show tripsMVWWW777:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat
    with dissolve
    window hide
    pause 4
    strlk "Что случилось-то бляяяя...." with vpunch
    play sound vibrosgvna2
    window hide
    pause 4
    bergen1 "Почти..." with vpunch
    play sound vibrosgvna3
    pause 4
    play sound padenie
    scene bg int_catacombs
    show dark_LW0607
    show blood_LW0607
    with vpunch
    window hide
    pause 0.6
    play sound coldazvuk
    scene bg int_catacombs
    show dark_LW0607
    show blood_LW0607
    pause 3.75
    scene black
    window hide
    pause 2
    scene bg int_catacombs
    play music dumaet
    play sound lesnikstart
    show unblink
    window hide
    pause 9
    th "Бляяя..." with dissolve
    th "Кто здесь?"
    th1 "Молодец,{w=0.2} сука."
    th1 "Теперь мы одно целое."
    th2 "Я никогда не пойму,{w=0.2} чё ж тебе так не нравится?"
    th1 "Да всё пока заебись." with dissolve
    th "А чей это голос был?"
    th1 "Твой."
    stop music fadeout 5
    th2 "Ну,{w=0.2} или кого-то из нас."
    th "Ладно."
    th "Это уже не важно."
    scene black with ed_night_dis
    play sound fb
    scene bg ext_old_building_night_moonlight
    show dlxrd at right
    show sheped at left
    with flash
    play music crysis2 fadein 3
    "Далее от лица Димана." with dissolve
    lxrd "Зомбари близко..."
    lxrd "Мы должны вытащить BERGENа до их прибытия..."
    dmn "Времени у нас почти не осталось..."
    shg "Нам остаётся надеяться лишь на то,{w=0.2} что в бункере есть оружие..."
    lxrd "Что там есть хоть кто-то,{w=0.2} кто умеет нормально стрелять..."
    "Они зашли внутрь."
    play sound door_open
    scene bg int_old_building_night
    show dlxrd at right
    show sheped at left
    with pushleft
    dmn "Ты же помнишь,{w=0.2} где тут вход?"
    lxrd "Обижаешь."
    play sound door_open
    scene bg int_catacombs
    show bergennorm
    show dlxrd at right
    show sheped at left
    with pushleft
    "Они ахуели от того,{w=0.2} что увидели."
    "Посреди конматы сидел тип,{w=0.2} который был похож на всех троих."
    lis "Долго же вы."
    lxrd "Кто ты?"
    lis "Зови меня -"
    vchn "Зови меня -{fast} Вечный." with vpunch
    "Стрелок,{w=0.2} BERGEN и Семпай наконец собрались в одного единого дцпешника."
    "Он сразу решил проверить,{w=0.2} на месте ли его старые кенты?"
    th "Чмошники, {w=0.2}отзовитесь!"
    th1 "Чё надо?"
    th2 "Я тут."
    "Теперь они уж точно одно целое."
    window hide
    pause 0.5
    shg "Интересное имечко ты себе придумал..."
    vchn "Заткнись,{w=0.2} Шепед." with vpunch
    "И Шепед язык в жопе потерял."
    stop music fadeout 5
    window hide
    pause 1
    vchn "А теперь у меня к вам вопрос -"
    extend " где Швилли?" with vpunch
    window hide
    pause 0.5
    play music otec fadein 4
    lxrd "Это мы у тебя должны спросить."
    lxrd "Может,{w=0.2} он в конце шахты?"
    extend " В той части,{w=0.2} что под лагерем?" with vpunch
    shg "Под лагерем?"
    extend " Они там разве есть?"
    lxrd "Конечно."
    extend " Ты лето вообще давно проходил?"
    shg "Никогда."
    lxrd "Понятно."
    vchn "Пошли." with vpunch
    "И они двинули в конец шахты."
    play sound door_break
    scene bg int_catacombs_hole
    show bergennorm
    show dlxrd at right
    show sheped at left
    with pushleft
    shg "Не зря фонарик взял..."
    "Депеш предусмотрительно в подсобке взял фонарь,{w=0.2} который ручной тягой заряжается."
    dmn "Далеко там идти?"
    vchn "Если в оригинале долго ходил,{w=0.2} то и воспоминание будет соответствующее."
    vchn "А я даже в первый раз наугад верно прошел и быстро."
    lxrd "Везёт же некоторым."
    "Они двинули дальше."
    scene bg int_mine
    show bergennorm
    show dlxrd at right
    show sheped at left
    with pushleft
    vchn "Ностальгировать и по баянистым местам ходить будем,{w=0.2} или вам больно время дорого?"
    menu:
        "Некогда нам" if True:
            stop music fadeout 5
            vchn "Коли так,{w=0.2} идём короткой тропой."
            vchn "Выйдем быстро и вовремя."
            jump akt1shahtaending
        "Почему нет?" if True:
            vchn "Двинули."
            jump akt1shahtadop

label akt1shahtadop:
    scene bg int_mine_halt
    show bergennorm
    show dlxrd at right
    show sheped at left
    with pushleft
    vchn "Это святые места."
    vchn "Я даже хз,{w=0.2} что тут и рассказывать..."
    lxrd "Пацанское лето помнишь?"
    scene bg int_mine_coalface
    show bergennorm
    show dlxrd at right
    show sheped at left
    with pushleft
    vchn "А,{w=0.2} ты про то,{w=0.2} как в одном из рутов тут прятали пионерок?"
    lxrd "А ты всё ещё помнишь сюжет..."
    dmn "Ахуеть,{w=0.2} даже я забыл!"
    scene bg int_mine_crossroad
    show bergennorm
    show dlxrd at right
    show sheped at left
    with pushleft
    vchn "Вот она -{w=0.2} та легендарная развилка."
    lxrd "Именно тут начинающие летофаги харкаются и матерятся."
    stop music fadeout 5
    vchn "Да."
    vchn "Но мы пойдём дальше."
    window hide
    pause 0.5
    vchn "Почти пришли."
    jump akt1shahtaending

label akt1shahtaending:
    play music jamaikamus fadein 2
    scene bg int_mine_door
    show bergennorm
    show dlxrd at right
    show sheped at left
    with pushleft
    vchn "Ну что ж..."
    vchn "За этой дверью, {w=0.2}вероятно,{w=0.2} находится Швилли."
    vchn "А вот живой или мертвый,{w=0.2} уже вопрос интересный."
    lxrd "Заходим?"
    vchn "А ты прямо хочешь?"
    lxrd "Не для того мы сюда пёрлись,{w=0.2} что бы просто тут стоять и втыкать в дверь."
    lxrd "Открывай!" with vpunch
    "И вечный открыл дверь."
    play sound door_break
    scene bg int_mine_room
    show bergennorm
    show dlxrd at right
    show porrigeshv
    show sheped at left
    with pushleft
    pause 1
    vchn "Ты хив!" with vpunch
    extend " Ахуеть..."
    shv "Дэбил,{w=0.2} ты ж меня тут и закрыл."
    th "Кто из вас гандонов это сделал?" with vpunch
    th1 "Ну йобана..."
    th1 "Иначе бы он просто где-то проебался."
    th1 "Нам пришлось..."
    th2 "Тебе." with vpunch
    extend " Не нам."
    th "Ладно.{w=0.2} Забыли."
    lxrd "Там зомбари пойдут на старый лагерь."
    lxrd "Мож тут вылезем?"
    shv "Закрыто, {w=0.2}я пытался."
    dmn "Вечный,{w=0.2} попробуй!" with vpunch
    vchn "Да ебать,{w=0.2} ща пойду и ебалом проломлю эту ссаную решетку,{w=0.2} да?"
    dmn "А мож получится!"
    vchn "Ну ты загадочный..."
    scene bg int_mine_exit_night_light with pushleft
    "Далее от лица Вечного."
    th "Не, {w=0.2}хуй я тут чё сделаю..."
    "Послышалось копошение сверху."
    vchn "Э БЛЯ!" with vpunch
    extend " Есть кто?"
    "Спустя пару секунд за решеткой нарисовалось знакомое еблище."
    scene bg int_mine_exit_night_light_ramazan with dissolve
    play sound hellomotherfucker
    window hide
    pause 1
    vchn "Дружище,{w=0.2} откроешь решёточку?"
    rmzn "Я попробую."
    window hide
    pause 0.5
    rmzn "Кстати,{w=0.2} а ты знаешь,{w=0.2} что самсунг уделывает ксяоми?"
    play sound nezn1
    window hide
    pause 2
    rmzn "Знаешь, {w=0.2}какие телефоны круче чем ванплас?"
    play sound nezn2
    window hide
    pause 1
    rmzn "Знаешь, {w=0.2}какие телефоны долго держат батарею?"
    play sound nezn3
    window hide
    pause 1
    rmzn "Знаешь, {w=0.2}какие телефоны самые лучшие?"
    play sound nezn4
    window hide
    pause 4
    play sound ramazanperdun
    pause 11
    play sound padenie
    scene bg int_mine_room
    show dlxrd at right
    show porrigeshv
    show sheped at left
    show dimanspr
    show dark_LW0607
    show blood_LW0607
    with vpunch
    pause 0.6
    play sound ramazansmeh
    pause 4
    lxrd "Беги,{w=0.2} малолетка конченная,{w=0.2} пока он не встал!"
    hide dark_LW0607
    hide blood_LW0607
    with dissolve
    vchn "Сука мразь мелкая..."
    vchn "Найду,{w=0.2} в очко лампочку вкручу..."
    window hide
    pause 1
    lxrd "Ладно,{w=0.2} двинули?"
    vchn "Малолетка не даст открыть решетку,{w=0.2} даже если Шепед натянет свой противогаз."
    vchn "Так что нам идти обратно только если."
    dmn "Мляяя...."
    dmn "Там зомбари как раз уже должны были подоспеть..."
    vchn "Ну, {w=0.2}пиздец."
    vchn "А что делать?"
    window hide
    pause 1
    "И они двинули назад."
    "Далее от лица Димана."
    stop music
    $ renpy.movie_cutscene("source/afewmomentslater.ogv")
    play music mdknmus fadein 3.5
    scene bg int_catacombs
    show bergennorm
    show dlxrd at right
    show sheped at left
    show porrigeshv
    with dissolve
    lxrd "Вы слышали?"
    hide bergennorm
    hide dlxrd at right
    hide sheped at left
    hide porrigeshv
    with dissolve
    play ambience zattack
    dmn "Смотри!"
    window hide
    show slzombar:
        default subpixel True 
        parallel:
            Null(233.0, 720.0)
            'slzombar'
        parallel:
            xpos -1.0 
            linear 0.35 xpos 0.2 
    with Pause(0.60)
    show slzombar:
        xpos 0.2 
    window show

    "Первый зомбарь был уже очень близко."
    "Но,{w=0.2} Диман не растерялся и начал шмалять."
    play sound dostal
    show shstvol1:
        ypos 0.25
        ease 0.5 ypos 0.05

    $ _window_hide(dissolve)

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1
    hide slzombar
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound shmalnulvpidora
    show shstvol11
    hide shstvol1
    $ renpy.pause (0.05)
    show shstvol1:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide shstvol11


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.1

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide shstvol1
    stop ambience
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show shstvol1
    play sound padenie
    pause 1
    lxrd "Красава,{w=0.2} Димас."
    extend " А говорил, {w=0.2}что стрелять не умеешь."
    dmn "Теперь умею."
    hide shstvol1
    play sound ubralstvol
    show shstvol1:
        ypos 0.0
        ease 0.5 ypos 0.5

    pause 0.6
    hide shstvol1
    "Димас опустил ствол."
    play sound volinichehlit
    lxrd "Рано волыны чехлить,{w=0.2} пацаны!"
    show bergennorm with dissolve
    vchn "Выходим?"
    dmn "Пошли."
    window hide
    pause 0.5
    vchn "Хотя подожди."
    vchn "Депеш,{w=0.2} ты,{w=0.2} наверное,{w=0.2} дай Саньку СВД."
    shv "Всё лучше -{w=0.2} чем ничего."
    stop music fadeout 5
    "Шепед отдал СВД Швилли."
    window hide
    pause 0.5
    "Далее от лица Вечного."
    hide bergennorm with dissolve
    play music nerocrackmus fadein 5
    play sound razebal
    window hide
    pause 1.5
    show rmznspr1 with vpunch
    pause 1
    play sound obana
    pause 0.7
    play sound xanatebe
    vchn "Хана тебе,{w=0.2} дядя!"
    lxrd "Ща у малелотки ебало битое будет,{w=0.2} чекайте инфо!"
    hide rmznspr1
    hide blink
    show hernya_kakaya_toMVWWW777 with flash
    play music nerocrackmus1
    show rmznspr:
        zoom 2.0
        ypos 0.0
        pause (0.38)
        linear 0.09 ypos -0.07
        linear 0.09 ypos 0.0
        pause (0.19)
        repeat

    show dlya_ebalaMVWWW777:
        xpos 1.0
        ypos 1.0
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.40)
        linear 0.15 xpos 1.0 ypos 1.0
        pause (1.0)
        repeat





    show dlya_ebalaleftMVWWW777:
        xpos -1.0
        ypos 0.5
        pause (1.0)
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.40)
        linear 0.15 xpos -1.0 ypos 0.5

        repeat



    $ renpy.pause (0.39)


    window show
    vchn "Смешно тебе, сука!?" with vpunch
    vchn "Пердун сука!" with vpunch
    rmzn "Ай прастите больше не буду!!!" with vpunch
    vchn "Сначала я тебе ебало начищу!!" with vpunch

    window hide
    pause 1
    hide hernya_kakaya_toMVWWW777 with dissolve
    hide dlya_ebalaMVWWW777
    hide dlya_ebalaleftMVWWW777
    hide rmznspr
    with dissolve
    stop sound
    "Вечный делает финальный хук в ебло толстой малолетней гниды."
    window hide
    show rmznspr with dissolve:
        xpos -0.05 ypos -0.37 zoom 3.0
        pause (0.38)
        linear 0.19 ypos -0.42
        linear 0.19 ypos -0.33
        linear 0.19 ypos -0.30
        linear 0.19 ypos -0.37
        pause (0.19)

    show dlya_ebalaMVWWW777:
        xpos 1.0
        ypos 1.0
        linear 0.20 xpos -0.0 ypos -0.0
        pause (0.50)
        linear 0.15 xpos 1.0 ypos 1.0

    play sound udarMVWWW777
    $ renpy.pause (0.5)
    hide hernya_kakaya_toMVWWW777 with dissolve
    show rmznspr with dissolve:
        xpos -0.05 ypos -0.37 zoom 3.0
        pause (0.2)
        linear 1.0 ypos 1.5
    play sound padenie
    pause 1
    play sound fatalitysound
    pause 2
    window show
    stop music fadeout 5
    vchn "И так будет с каждой конченной малолеткой блеать!" with vpunch
    window hide
    pause 1
    vchn "Кароче блеать."
    vchn "Предлагаю такой расклад:"
    play music theorem fadein 2
    extend " наверх идём мы с Швилли и Рамазанчиком." with vpunch
    rmzn "Нииеееттт!!!" with vpunch
    rmzn "Позязя нинада!!!" with vpunch
    vchn "Ты у меня сука первым на корм зомбарям пойдешь..." with vpunch
    "Вечный пнул Рамазанчика."
    rmzn "Ай,{w=0.2} бля!!!" with vpunch
    window hide
    pause 0.5
    play sound voprosiizzala
    pause 2
    stop music fadeout 4
    rmzn "Я протестую,{w=0.2} сукаааа{w=0.2}а{w=0.2}а{nw}"
    vchn "Раз ни у кого вопросов нет,{w=0.2} мы выдвигаемся!"
    "И они втроем вылезли наверх."
    play sound door_open
    $ say_pizdec = True
    play music redcatgandon fadein 3
    scene burnint
    with pushleft
    vchn "Какого хера тут всё горит?"
    rmzn "Я бежал сюда...{w=0.3} Плакал,{w=0.2} просто рыдал как сучка..."
    rmzn "И поджог за собой дверь." with vpunch
    vchn "Ты ебанутый?"
    rmzn "Ну,{w=0.2} они же в огонь не полезут,{w=0.2} да?"
    "Далее от лица Швилли."
    play ambience zattack
    shv "Смотри!"
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    vchn "Саня, {w=0.2}у тебя же есть СВД!" with vpunch
    window hide
    play sound valiskatinu
    pause 2
    shv "Приступаю!" with vpunch


    $ _window_hide(dissolve)


    play sound dostal
    show SVD_wovystr_LW0607:
        ypos 0.25
        ease 0.5 ypos 0.05

    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    with dissolve

    $ renpy.pause (2, hard=True)

    $ _window_show(dissolve)
    rmzn "О нет,{w=0.2} меня тут сожрут ща!" with vpunch
    "Саня не спешил стрелять."
    window hide
    pause 0.5
    "И в итоге гниль сожрала Рамазанчика уебанчика."
    $ _window_hide(dissolve)
    hide rmznspr1
    play sound gamaz
    show rmznspr1:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.7 ypos 2.0
    pause 1
    stop sound
    $ _window_show(dissolve)
    "Вот так и погибают чмошники."
    window hide
    pause 0.5
    "О чём это я?"
    "Ах,{w=0.2} да..."
    scene burnint
    show SVD_wovystr_LW0607
    play sound zattack
    show sl_zombie_sprite4_LW0607:
        xpos 0.085
    show sl_zombie_sprite3_LW0607:
        xpos 0.115
    show slzombar:
        xpos 0.1
    vchn "Гаси их,{w=0.2} ну!"
    "И Швилли открыл огонь."
    $ _window_hide(dissolve)

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607

    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide SVD_wovystr_LW0607
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show SVD_wovystr_LW0607
    play sound padenie
    pause 1
    hide slzombar
    shv "Один готов!"
    vchn "Продолжай!"
    "У Вечного не было ствола,{w=0.2} шоп пострелять."
    "Вот так вот."

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45
    hide sl_zombie_sprite3_LW0607
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center
    hide slzombar
    hide SVD_wovystr_LW0607
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show SVD_wovystr_LW0607
    play sound padenie
    pause 1
    hide slzombar
    shv "Второй готов!"
    vchn "Продолжай!"

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45
    hide sl_zombie_sprite4_LW0607
    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center

    play sound vystrel_LW0607
    show SVD_svystrel_LW0607
    hide SVD_wovystr_LW0607
    $ renpy.pause (0.05)
    show SVD_wovystr_LW0607:
        ypos 0.05
        xpos 0.0
        ease 0.1 ypos 0.0
        ease 0.1 ypos 0.05
    hide SVD_svystrel_LW0607


    show hitmarkermlg_LW0607:
        ypos 0.05 xpos 0.13

    pause 0.45

    show slzombar:
        xpos 0.1
        ypos 0.0
        ease 0.1 xpos 0.093
        ease 0.1 xpos 0.107
        ease 0.1 xpos 0.1

    $ renpy.pause (0.1)
    hide hitmarkermlg_LW0607 at center


    hide slzombar
    hide SVD_wovystr_LW0607
    stop ambience
    show slzombar:
        anchor (0.5, 0.5)
        pos (0.2, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    show SVD_wovystr_LW0607
    play sound padenie
    pause 1
    hide slzombar
    $ renpy.pause (1)

    $ _window_show(dissolve)
    shv "Поcледний готов!"
    vchn "Красава!"
    window hide
    pause 0.4
    vchn "Валим отсюда!" with vpunch
    "Они вышли наружу,{w=0.2} удачно миновав огонь."
    scene roofburn
    show SVD_wovystr_LW0607
    with pushleft
    "Швилли решил перезарядить СВД."
    hide SVD_wovystr_LW0607
    play sound clipin
    show SVD_wovystr_LW0607:
        ypos 0.0
        ease 0.5 ypos 0.5

    pause 1
    hide SVD_svystrel_LW0607
    play sound clipout
    show SVD_wovystr_LW0607:
        ypos 0.5
        ease 0.5 ypos 0.05

    pause 1
    "Швилли перезарядил СВД."
    window hide
    pause 0.5
    "Вечный решил прервать молчание после того,{w=0.2} как кому-то отписался в телефоне."
    window hide
    show bergennorm:
        default subpixel True xpos 0.25 
        parallel:
            Null(508.0, 733.0)
            'bergennorm'
        parallel:
            xpos 0.25 ypos 2.0 
            linear 0.40 xpos 0.25 ypos 1.0 
    with Pause(0.60)
    show bergennorm:
        pos (0.25, 1.0) 
    window show
    vchn "Я написал,{w=0.2} чтоб они выходили."
    vchn "Лорд сказал,{w=0.2} что выведет группу другим путём."
    shv "Как?{w=0.2} Шахта закрыта же."
    vchn "Он сказал,{w=0.2} что когда я Рамазанчика хуярил,{w=0.2} с него ключ от решетки выпал."
    vchn "С пидорка этого."
    shv "Хех."
    stop music fadeout 4
    vchn "У тебя есть варианты,{w=0.2} как свалить?"
    vchn "Просто они уже ушли своей тайной тропой с этого богом забытого места."
    window hide
    pause 0.5
    play music soldatmusssic fadein 2
    hide SVD_wovystr_LW0607
    play sound ubralstvol
    show SVD_wovystr_LW0607:
        ypos 0.0
        ease 0.5 ypos 0.5

    pause 0.6
    hide SVD_wovystr_LW0607
    shv "Пока ты хуярил этого додика,{w=0.2} я кое-кому написал..."
    shv "И этот человек сейчас на машине ждёт нас у ворот лагеря."
    window hide
    pause 0.5
    vchn "Я походу понял,{w=0.2} про кого ты говоришь."
    shv "Так вот нам бы ускориться..."
    window hide
    pause 0.5
    shv "Ибо на территории лагеря сейчас небось полно зомбарей..."
    window hide
    pause 0.5
    shv "Да и заждался он."
    window hide
    pause 0.5
    vchn "Ну,{w=0.2} как в старые добрые,{w=0.2} на перегонки?"
    hide bergennorm with flash
    "Не дав ответить Швилли,{w=0.2} Вечный рванул вперёд."
    shv "Всё равно догоню,{w=0.2} ска!" with vpunch
    "И швилли тоже рванул."
    play sound begtrava
    $ say_pizdec = False
    scene roofburn at ed_running_fast
    scene bg ext_path_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    scene bg ext_playground_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    scene bg ext_square_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    scene bg ext_clubs_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    scene bg ext_bus_night at ed_running_fast
    with pushleft
    window hide
    pause 2
    stop sound fadeout 2
    scene bg goscar
    show dark_LW0607
    with pushleft
    play sound ustal
    "Швилли задыхался, {w=0.2}но был первым."
    shv "Привет...{w=0.2} Илюш..."
    galenin "Здарова,{w=0.2} заебал."
    "Швилли пытался отдышаться."
    window hide
    stop sound fadeout 3
    pause 0.5
    "Вскоре прибежал и Вечный."
    window hide
    show bergennorm:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'bergennorm'
        parallel:
            xpos -1.0 
            linear 0.45 xpos 0.15 
    with Pause(0.60)
    show bergennorm:
        xpos 0.15 
    window show
    play sound ustal
    vchn "И куда ж ты...{w=0.3} Такой быстрый...{w=0.3} А?"
    vchn "Привет,{w=0.2} Илюш..."
    galenin "Тебе тоже привет."
    window hide
    stop sound fadeout 3
    pause 0.5
    shv "Да я просто всё это время не парил."
    shv "Зарядку экономил для этого случая."
    window hide
    pause 0.5
    "Швилли уже отдышался и поэтому мог позволить себе тягу на поде."
    window hide
    play sound podik
    pause 2
    shv "Заебись."
    "Вечный парить не захотел."
    window hide
    pause 0.5
    galenin "Поехали?"
    vchn "Точно что..."
    window hide
    pause 0.5
    shv "Я тебе ща такую историю расскажу,{w=0.2} ты не поверишь..."
    window hide
    pause 0.5
    galenin "Смотря что за история."
    window hide
    stop music fadeout 5
    pause 1
    "И они прыгнули в тачку Ильяса и укатили в надвигающийся рассвет."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene ext_road_night
    show coldspr1
    with ed_night_dis
    play music grock
    cld "Вот такая вот история."
    nn "Нихуёво."
    "Неоня заметил,{w=0.2} что они идут уж слишком долго."
    "Он оглянулся и увидел в 5 метрах от себя лагерь."
    cld "Да ёбаный насос!"
    cld "Надо было взять координаты у Ильяса."
    cld "Без них мы отсюда не уйдём."
    nn "Чё делать-то блять?"
    cld "Не паникуй."
    "И они начали звать на помощь через рацию,{w=0.2} найденную в пупке у Колда."
    show zatemnenie with dissolve2
    $ MND_Chapter("Тем временем пацаны:")
    hide zatemnenie with dissolve2
    play sound fb
    scene black with flash
    scene ext_road_night at ed_bus_move
    show volga at ed_bus_move
    with ed_night_dis
    galenin "Бля чуваки."
    galenin "Чёта рация шипит."
    "Из рации наконец начала доноситься нормальная речь блять."
    play sound cold_help
    window hide
    pause 24
    galenin "А я ведь предупреждал..."
    shv "Кто там?"
    galenin "Колд."
    window hide
    play sound neony_help
    pause 5
    galenin "Ловите схему, заебали."
    window hide
    play sound cold_vibralis
    pause 19
    galenin "Вас забирать?"
    galenin "Я ща недалеко."
    cld "Было б неплохо."
    galenin "Ща заедем."
    cld "Конец связи."
    stop music fadeout 5
    galenin "Мостись,{w=0.2} Вечный!" with vpunch
    galenin "Там твои братки скоро сядут."
    scene black with ed_night_dis
    play music hott fadein 3
    scene buhaem
    show overlay aw_memory_back_1
    with ed_night_dis
    nvl clear
    nvlbazar "Вот так они всей бригадой выбрались из ловушки Скита."
    nvlbazar "И поехали на тачке Ильяса бухать в Курск."
    nvl clear
    nvlbazar "Диман и Депеш ушли в скайнет."
    nvlbazar "Диман обещал научить его играть в CS GO."
    nvl clear
    nvlbazar "Ильяс и Саня Швилли поехали развлекаться к тёлкам в Искру."
    nvlbazar "Надо же как-то снять напряжение после такого-то дерьма."
    nvl clear
    nvlbazar "Ну а Вадимка,{w=0.2} Колд, {w=0.2}Неоня и Вечный поехали на хату Вечного,{w=0.2} дабы испить священный нектар..."
    nvlbazar "Под названием лысая головка."
    nvlbazar "Это нечто вроде самопального Revo."
    nvlbazar "Алкогольный энергетик."
    nvl clear
    nvlbazar "Мешаем пиво и ягуар желтый или любой другой."
    nvlbazar "Самый чёткий на моей памяти был белый медведь и красный драйв."
    nvlbazar "Меня тогда развезло и я полетел исполнять солнышко на качели."
    nvl clear
    nvlbazar "Не о том разговор."
    nvl clear
    nvlbazar "Неоня нахуярился и уснул."
    nvlbazar "Вечный и Колд начали исполнять караоке,{w=0.2} Вадимка куда-то ушёл."
    nvl clear
    stop music fadeout 3
    play sound fb
    scene coldbuhaet with flash
    cld "Ну,{w=0.2} давай ГрОб споём шоль?"
    vchn "А хуле нет!" with vpunch
    show zatemnenie with dissolve2
    $ MND_Chapter("Тем временем Вадимка:")
    hide zatemnenie with dissolve2
    play sound fb
    scene vannaya with flash
    lxrd "Не срёться нихуя{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "Ну и ладно."
    lxrd "Пора бы и тоже в караоке спеть."
    "Вадимка начал слезать с параши."
    show zatemnenie with dissolve2
    $ MND_Chapter("Тем временем Пацаны:")
    hide zatemnenie with dissolve2
    play sound fb
    scene coldbuhaet with flash
    window hide
    play sound grobtopcover
    pause 31
    stop sound
    scene morozovcover with vpunch
    lxrd "Сорян,{w=0.2} посоны."
    lxrd "Это я выключил гроб{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    lxrd "Пришло моё время исполнять."
    lxrd "Этот кавер посвещаятся моей бывшей."
    lxrd "Кхм." with vpunch
    window hide
    play sound otrignul
    pause 3
    "Вадимка пару раз рыгнул в микрофон,{w=0.2} тем самым его проверив."
    lxrd "Погнали,{w=0.2} хули." with vpunch
    window hide
    play sound face
    pause 30
    stop sound fadeout 5
    "Вадимка закончил свой кавер."
    vchn "Это было великолепно."
    cld "Ты не мог раньше заткнуться?" with vpunch
    cld "У меня из ушей малафья полилася."
    cld "Пиздец." with vpunch
    play sound zarevu
    window hide
    pause 3
    show overlay aw_memory_back_1 with dissolve2
    nvl clear
    nvlbazar "Вот так они и отдыхали."
    nvlbazar "Разрисовали ебало неони зубной пастой."
    nvlbazar "Или это был cum?{nw}"
    nvl clear
    nvlbazar "Впрочем,{w=0.2} не важно."
    nvlbazar "Вот так и заканчивается этот эпизод этой одной большой и длинной истории."
    nvlbazar "Вот так вот."
    nvl clear
    nvlbazar "Будьте хорошими малолетками и не срите на парты в школе."
    nvl clear
    play music zp2_main_l
    scene zihao with ed_night_dis
    zih "Занимательно..."
    zih "Это ж надо такое придумать..."
    vchn "Я тебя понял." with vpunch
    vchn "Ты мне всё ещё не веришь."
    vchn "Дай угадаю..."
    vchn "Ты тут не для помощи?" with vpunch
    vchn "А вытащить из меня инфу,{w=0.2} да?" with vpunch
    vchn "Ахаха..."
    vchn "И чё я сразу об этом не подумал..."
    vchn "Хуй короче ты теперь получишь." with vpunch
    vchn "А не реальную сводку событий."
    vchn "Пидор." with vpunch
    zih "В карцер его."
    "И амбалы снова увели Вечного."
    play sound door_open
    "После чего в кабинет к Зихао залетет Химори."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Химори:")
    hide zatemnenie with dissolve2
    him "Её нашли." with vpunch
    zih "Да ну нахуй?"
    zih "Неужели?"
    him "Именно."
    him "Сейчас в общей камере сидит."
    him "Дали успокоительного."
    him "Буйная ещё больно." with vpunch
    zih "У меня тут тоже не без проишествий..."
    zih "Суетолог решил не продолжать свою историю."
    him "Ты забыл про наши тайные методы?" with vpunch
    zih "Да ну,{w=0.2} ты гонишь."
    zih "Он окончательно поплывёт." with vpunch
    zih "Пока повременим с этим."
    zih "Может,{w=0.2} сидя в карцере,{w=0.2} он одумается."
    him "Дело твоё."
    him "Будут ещё новости -{w} сразу к тебе."
    zih "Добро." with vpunch
    play sound door_open
    "И Зихао, проводив Химори,{w=0.2} начал готовится к очередному приёму..."
    zih "Как же меня всё заебало..."
    show zatemnenie with dissolve2
    $ MND_Chapter("Конец второго картера...")
    hide zatemnenie with dissolve2
    return

label aktthree:
    scene black with ed_night_dis
    play music myheroine fadein 2
    scene komnata_seksa with ed_night_dis
    nvlbazar "Сидя в тёмной комнате,{w=0.2} Вечный думал о вечном."
    nvlbazar "Амбалы всё хотели вытрясти из него продолжение истории,{w=0.2} но он был непоколебим."
    nvlbazar "Делать было нечего,{w=0.2} поэтому Вечный решил окунуться в ностальгию."
    nvl clear
    nvlbazar "Ему вспомнился 2019 год.{w} Лето."
    nvlbazar "Тот самый переломный момент в его жизни."
    nvlbazar "Когда он из затворника стал превращаться в человека."
    nvl clear
    nvlvhcn "Жаль никаких наушников тут нет."
    nvlvhcn "Да и мобилу отжали."
    nvlvhcn "Так бы послушал сейчас Silverstein..."
    nvl clear
    nvlbazar "То самое лето,{w=0.2} в котором было много распитой водяры и выпарено несколько флаконов щелочной жижи 6 мг."
    nvlbazar "То самое лето,{w=0.2} в котором он познал много нового."
    nvlbazar "То самое лето,{w=0.2} в начале и середине которого он делал свой прекрасный шедевр про Депеша..."
    nvl clear
    nvlbazar "Это всё утрачено."
    nvlbazar "Однако,{w=0.2} ничего не мешает воспроизвезти в памяти этот фрагмент гораздо детальнее."
    nvlbazar "Кроме одного."
    nvl clear
    aw_mj1 "Мы нашли её." with vpunch
    him "Отлично."
    him "В одиночной закрыли?"
    aw_mj1 "Да."
    aw_mj1 "Или надо было к суетологу её?"
    him "Нет,{w=0.2} всё правильно сделали."
    him "Пока пусть отсидится."
    him "Потом будем трясти инфу с неё." with vpunch
    aw_mj1 "Принято."
    nvlbazar "Голоса за дверью стали отдаляться."
    nvlbazar "И Вечный вспомнил кое-{w=0.2}что важное."
    nvlbazar "То, {w=0.2}что поменяло его взгляд на всю операцию в целом."
    stop music fadeout 3
    nvl clear
    "Он снова ударился в рефликсию и продолжил прокручивать в голове прошедшие моменты."
    play music lasttrack fadein 5
    scene ineony
    show overlay aw_memory_back_1
    with Fade(1.5, 1, 2)
    show zatemnenie with dissolve2
    $ MND_Chapter("The Carter Three:")
    $ MND_Chapter("iNeoony's Revenge")
    hide zatemnenie with dissolve2
    nvlbazar "Неоня сидел за своим столом."
    nvlbazar "С той самой пьянки в Курске прошёл год."
    nvlbazar "Все начали заниматься своими делами."
    nvl clear
    nvlbazar "Вадимка начал хакерить и законтачился с одним интересным типом."
    nvlbazar "Колд занимался поиском подсосов Скитецкого и последующей карой."
    nvlbazar "Неоня открыл свою личную лабораторию {b}iGandone Labs{/b}."
    nvlbazar "А Вечный пропал с радаров."
    nvl clear
    nvlbazar "Да,{w=0.2} он просто исчез."
    nvlbazar "Либо же не выходил на связь."
    nvlbazar "Пускай об этом и очень быстро забыли."
    nvlbazar "Слишком быстро.{w} Буд то и не было его вовсе."
    nvl clear
    nvlbazar "Тем не менее -{w} Неоня вызвал всех лучших сотрудников на совещание."
    nvlbazar "Всё это по поводу презентации своего нового,{w=0.2} совершенного,{w=0.2} да и просто пиздатого вида вооружения."
    nvlbazar "А что же за оружие?{w} А это мы сейчас и узнаем."
    nvl clear
    scene laba with ed_night_dis
    "Неоня стоял в подземке с колбами."
    "Там и храниться всё,{w=0.2} что {b}запрещено Женевской конвенцией{/b}."
    window hide
    pause 1
    "В помещение зашёл Вадимка."
    play sound door_open
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 3.0 
            linear 0.80 xpos 0.75 
    with Pause(0.90)
    show deadlylxrd:
        xpos 0.75 
    lxrd "Здарова.{w} Чё там у тебя?"
    nn "Где Колд?" with vpunch
    lxrd "Скоро будет."
    nn "Ну,{w=0.2} как будет -{w} так и посмотрим.{w} Чё там у меня."
    nn "Добро?"
    lxrd "Темнишь ты что-то{w=0.2}.{w=0.2}.{w=0.2}."
    nn "Да неужели?" with vpunch
    nn "Я просто хочу увидеть вашу реакцию."
    nn "Сразу обоих."
    nn "И всё." with vpunch
    lxrd "Ну и что?"
    lxrd "Неужели там настолько экстраординарное что-то?" with vpunch
    nn "Скоро увидишь."
    "В помещение зашёл колд."
    play sound door_open
    show coldspr:
        default subpixel True 
        parallel:
            Null(508.0, 733.0)
            'coldspr'
        parallel:
            xpos -3.0 
            linear 0.80 xpos 0.25 
    with Pause(0.90)
    show coldspr:
        xpos 0.25 
    cld "Всем шалом.{w} Так чё там у тебя?"
    "Неоня колебался."
    "Он не хотел до последнего раскрывать все карты."
    "Но ему рано или поздно пришлось бы это сделать."
    nn "Новое оружие против Скитецкого."
    nn "Клоны." with vpunch
    "Стенка колбы начала съезжать."
    "Там лежало тело{w=0.2}.{w=0.2}.{w=0.2}.{w} Вадима Морозова?"
    lxrd "Это{w=0.2}.{w=0.2}.{w=0.2}.{w} Блять{w=0.2}.{w=0.2}.{w=0.2}.{w} Как?!" with vpunch
    "Тело начало приходить в себя,{w=0.2} выпадая из стадии анабиоза."
    window hide
    show lordsprclon1 at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    window show
    "Из колбы вышел... {w}Прошу прощения.{w} В лабу,{w=0.2} ебанув тройное сальто,{w=0.2} завалился клон Вадима Морозова."
    window hide
    hide lordsprclon1
    hide coldspr
    show coldspr:
        subpixel True 
        xpos 0.25 
        linear 0.56 xpos 0.3 
    show lordsprclon1:
        default subpixel True 
        parallel:
            Null(499.0, 842.0)
            'lordsprclon1'
        parallel:
            xpos 0.5 
            linear 0.56 xpos 0.25 
    with Pause(0.66)
    show coldspr:
        xpos 0.3 
    show lordsprclon1:
        xpos 0.25 
    window show
    lxrd1 "Я курю,{w=0.2} буд то нечего терять мне!" with vpunch
    window hide
    play sound ssmeh2
    hide coldspr
    show coldherovo 
    pause 4
    window show
    hide coldherovo
    show coldspr
    "Колд с этой лысой двухметровой хиппарской хуеты поймал некислую смешинку."
    "А вот Вадимка негодовал."
    lxrd "Слышь{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "Казах,{w=0.2} сука." with vpunch
    lxrd "Это чё такое,{w=0.2} придурок?" with vpunch
    stop music fadeout 5
    "Неоня усмехнулся."
    "Неоднозначная реакция его сотрудников была ему очевидна с самого начала."
    "Он упивался моментом,{w=0.2} ведь удивить Вадима Морозова нельзя уже давно."
    "А у Неони получилось."
    "Пусть он и потратил на это целый год."
    play music dumaet
    window hide
    scene black with ed_night_dis
    window show
    "Дамирка снова ушёл в свои воспоминания."
    window hide
    scene skitserun with ed_night_dis
    window show
    "В свои золотые мгновения жизни он сидел на крыше одного из домов."
    "Приглядевшись,{w=0.2} он увидел нечто странное."
    window hide
    play sound dostal
    show skitserun1:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'skitserun1' with dissolve
        parallel:
            ypos 2.0 
            linear 0.80 ypos 1.0 
    with Pause(0.90)
    show skitserun1:
        ypos 1.0 
    window show
    "Взяв свой {b}Nikon{/b},{w=0.2} он начал приближать изображение на экране камеры."
    "Немного сильно так ахуев от увиденного,{w=0.2} Неоня моргнул шоколадным глазом."
    window hide
    show blink
    pause 1
    hide blink
    scene vladik-serun2
    show unblink
    pause 1
    window show
    stop music fadeout 5
    "Там,{w=0.2} на конце крана,{w=0.2} всего лишь срал какой-то рандомный чел."
    "С кем не бывает,{w=0.2} казалось бы."
    play sound fb
    scene laba
    show lordsprclon1 at left
    show coldspr
    show deadlylxrd at right
    with flash
    play music goloederevo fadein 2
    "Но щелбан Вадима Морозова вернул его в реальность."
    lxrd "Уснул что ли?" with vpunch
    nn "Нет."
    nn "Просто вспомнил былое."
    nn "Старых друзей,{w=0.2} так сказать{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd1 "Предай нахуй всех друзей,{w=0.2} ведь уже всё равно{w=0.2}.{w=0.2}.{w=0.2}."
    play sound zubek
    hide lordsprclon1
    show lordsprclon3 at left
    with flash
    "Клон Вадимки одарил всех своей ослепительной улыбкой."
    "Его ремень за 25к то и дело злорадно поблёскивал,{w=0.2} наровясь зажать яйца клона."
    "А Неоня снова усмехнулся."
    "Клону передались повадки Вадимки."
    "Та же способность подпёздывать цитатками Уаджета и покупать мегадорогие шмотки."
    "В этот момент Колд выходит из куража своих мыслей."
    "Он замечает лучезарную улыбку клона."
    "А Клон в этот момент решил подыграть."
    window hide
    play sound lacalut
    pause 3
    play sound ssmeh1
    hide coldspr
    show coldspr:
        default subpixel True xpos 0.25 
        parallel:
            Null(600.0, 720.0)
            'coldspr'
        parallel:
            xzoom 1 
            linear 0.20 xzoom 2 
            linear 0.20 xzoom 1 
            linear 0.60 xzoom 2 
            linear 0.20 xzoom 1 
        parallel:
            yzoom 1 
            linear 0.20 yzoom 1 
            linear 0.40 yzoom 2 
            linear 0.20 yzoom 1 
            linear 0.20 yzoom 2 
            linear 0.20 yzoom 1 
    with Pause(1.30)
    show coldspr:
        xzoom 1 yzoom 1 
    hide coldspr
    show coldspr:
        default subpixel True xpos 0.25 
        parallel:
            Null(600.0, 720.0)
            'coldspr'
        parallel:
            xzoom 1 
            linear 0.20 xzoom 2 
            linear 0.20 xzoom 1 
            linear 0.60 xzoom 2 
            linear 0.20 xzoom 1 
        parallel:
            yzoom 1 
            linear 0.20 yzoom 1 
            linear 0.40 yzoom 2 
            linear 0.20 yzoom 1 
            linear 0.20 yzoom 2 
            linear 0.20 yzoom 1 
    with Pause(1.30)
    show coldspr:
        xzoom 1 yzoom 1 
    pause 1.1
    hide coldspr
    show coldspr:
        default subpixel True xpos 0.25 
        parallel:
            Null(600.0, 720.0)
            'coldspr'
            0.01
            'coldspr'
        parallel:
            ypos 1.0 rotate 0.0 
            linear 0.07 ypos 0.8 rotate 60.0 
            linear 0.07 ypos 0.7 rotate 120.0 
            linear 0.07 ypos 0.6 rotate 180.0 
            linear 0.07 ypos 0.5 rotate 240.0 
            linear 0.07 ypos 0.4 rotate 320.0 
            linear 0.07 ypos 0.3 rotate 380.0 
            linear 0.07 ypos 0.2 rotate 440.0 
    with Pause(1.11)
    show coldspr:
        pos (0.25, 0.2) rotate 440.0 
    pause 1.65
    hide coldspr
    "После чего Колд,{w=0.2} ебанув несколько сальтух разом,{w=0.2} улетает нахуй на луну."
    "Настолько сильным был его ор."
    lxrd "Он так долго ещё улетать с этого дела будет?"
    nn "Ты погоди."
    nn "Это ещё Вечный не видел."
    lxrd "А ты уверен,{w=0.2} что он увидит?"
    "Неоня задумался."
    "Если Вечный раскусил его схему по добыче ДНК для создания его клона..."
    "То хуй он больше сюда вернётся."
    "А что за схема?{w} Это мы сейчас и узнаем."
    stop music fadeout 5
    scene black with ed_night_dis
    scene ineony
    show vasilisa at right
    show overlay aw_memory_back_1
    with ed_night_dis
    play music lovewooman fadein 2
    nn "Ты мой первый удачный клон."
    nn "Я скрупулёзно подбирал внешность."
    nn "Даже черты характера."
    nn "Ты должна{w=0.2}.{w=0.2}.{w=0.2}.{w} Нет,{w=0.2} блядь,{w=0.2} просто {b}ОБЯЗАНА{/b} ему понравится!"
    lis "И для чего же?"
    nn "Мне нужен его ДНК." with vpunch
    nn "Зная Вечного -{w} я уверен на все двести процентов,{w=0.2} что он не даст мне свой биоматериал."
    nn "Поэтому ты должна втереться в доверие и гопнуть это самое ДНК." with vpunch
    nn "Каким образом ты будешь это делать -{w} меня мало интересует."
    nn "Я дам тебе катетер с тоненькой иголкой."
    nn "Этого хватит более чем."
    nn "Остаётся надеяться,{w=0.2} что ты унаследовала от оригинала когнетивные способности и чуткость."
    nn "Иначе плакала моя затея."
    nn "Намёк понят?"
    lis "Понят."
    lis "Только один вопрос остался."
    lis "Какое имя мне взять?" with vpunch
    nn "Хм{w=0.2}.{w=0.2}.{w=0.2}."
    "Недолго думая,{w=0.2} Неоня выдал жидкий пёрл."
    nn "Будешь Василисой." with vpunch
    vas "Василиса так Василиса.{w} Чё бухтеть-то."
    nn "С твоим вопросом разобрались."
    nn "Есть ещё?"
    vas "Нет."
    vas "Приступаю к выполнению поставленной задачи."
    window hide
    play sound door_open
    hide vasilisa
    show vasilisa:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'vasilisa'
        parallel:
            xpos 0.75 
            linear 0.80 xpos 2.0 
    with Pause(0.90)
    show vasilisa:
        xpos 2.0 
    window show
    hide vasilisa
    "Клон покинул кабинет Неони."
    nn "Остаётся надеяться{w=0.2}.{w=0.2}.{w=0.2}.{w} Да."
    stop music fadeout 5
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Вечного:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music wmm fadein 2
    scene bergdomint1
    show vlados2
    with ed_night_dis
    nvl clear
    nvlbazar "Это должен был быть один самый обычный день.{w} Да как бы не так."
    nvlbazar "Всё началось дня за 2 до этого."
    nvlbazar "Именно тогда Вишневский предложил Вечному отправиться в нереальный рейв."
    nvl clear
    vsn "Почему бы тебе не прийти?"
    vsn "Тем более,{w=0.2} на моё др должен заскочить Максончик и компания."
    vchn "Тот самый негритос?"
    vsn "Да." with vpunch
    vsn "Он ахуенен."
    vchn "Да кто ж спорит."
    vchn "Просто желания куда-то идти нет абсолютно."
    vsn "Да неужели?" with vpunch
    vsn "Может быть такого шанса у тебя больше не будет."
    vsn "Сам подумай:{w} там будем не мы вдвоём."
    vsn "Будут тёлки!"
    vsn "Так из своей депрессии выйдешь когда-нибудь."
    vchn "Смешно{w=0.2}.{w=0.2}.{w=0.2}."
    vchn "Тут наоборот скорее."
    vchn "Хотя ёпта,{w=0.2} когда меня тёлки волновали?" with vpunch
    vchn "Сам вспомни пятый класс тот же,{w=0.2} когда меня прилюдно отшили!" with vpunch
    vchn "Да похуй мне было совершенно." with vpunch
    vsn "Мне нравится твой настрой."
    vsn "Тем более -{w=0.2} чем тебе не нравится идея отправиться на др кента?"
    vchn "Ну,{w=0.2} тоже верно."
    vsn "Кароче,{w=0.2} я буду ждать тебе через два дня в 4 вечера в клубаке на запольной."
    vsn "Не опаздывай."
    vsn "Будет расставлять алко и прибамбасы."
    vsn "Познакомлю тебя с Кирюхой."
    window hide
    hide vlados2
    play sound door_open
    show vlados2:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'vlados2'
        parallel:
            yanchor 1.0 
            linear 0.80 yanchor -2.0 
    with Pause(0.90)
    show vlados2:
        yanchor -2.0 
    hide vlados2
    stop music fadeout 5
    nvlbazar "На этой не особо весёлой ноте они распрощались."
    nvl clear
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("День X")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene tusa with ed_night_dis
    play music korabl fadein 2
    nvlbazar "Ради чего всё это? {w}- Думал Вечный, сидя недалеко от диджейского пульта."
    nvlbazar "Не сказать,{w=0.2} что его опасения подтвердились."
    nvlbazar "Просто пока что он не знает об этом."
    nvlbazar "Для него сейчас всё под контролем и всё ахуенно."
    nvlbazar "Ничего не предвещает беды,{w=0.2} так сказать."
    nvl clear
    nvlbazar "До одного момента."
    nvl clear
    nvlbazar "К нему на тусе подсаживается одна рыжеволосая тян{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    window hide
    show vasilisa:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'vasilisa'
        parallel:
            xpos 3.0 
            linear 0.80 xpos 0.75 
    with Pause(0.90)
    show vasilisa:
        xpos 0.75 
    window show
    vas "Привет."
    vas "Ты тот самый Миша?" with vpunch
    vchn "Допустим."
    "Вечный был не в самом хорошем настроении."
    vchn "Тебе надо что-то?"
    vas "Да." with vpunch
    vchn "И что же?"
    vas "Ты сидишь и унываешь."
    vas "Я собираюсь это исправить." with vpunch
    vas "Рассказывай."
    vas "Чё случилось?"
    vchn "Да ничего особенного." with vpunch
    vchn "Просто неприятно находиться в месте,{w=0.2} где я никого не знаю."
    vchn "Давит на мозги конкретно." with vpunch
    vchn "И чё с этим делать -{w} я не знаю."
    vchn "Вот так вот."
    vas "Понятно."
    vas "Ты просто мало приголубил." with vpunch
    vas "Пойдём,{w=0.2} там где-то был Джеймесон."
    window hide
    scene bar1
    show vasilisa at right
    with ed_lap
    nvlbazar "И они отправились к барной стойке."
    nvlbazar "Василиса в пьяном угаре пыталась открыть сок ножом."
    nvlbazar "По итогу она отхуячила пол пакета и сок начал разливаться на пол."
    nvlbazar "Вечный,{w=0.2} прям как истинный джентельмен,{w=0.2} кропотливо начал пытаться выхватить у неё сок,{w=0.2} пока она его не доразлила."
    nvl clear
    nvlbazar "По итогу она сделала ему свой фирменный коктейль -{w} казах в астане."
    nvlbazar "Что это?"
    nvl clear
    nvlbazar "Много Джеймесона и немного яблочного сока {b}<<Добрый>>{/b}."
    nvlbazar "Уносит с него не так сильно,{w=0.2} как с лысой малышки."
    nvlbazar "Иначе Вечный бы просто всё забыл."
    nvl clear
    nvlbazar "Тем не менее,{w=0.2} бахнув этого чудесного {b}<<морса>>{/b},{w=0.2} он осмелел."
    nvlbazar "Нихуёво так."
    nvlbazar "После чего они вернулись ближе к танцполу."
    nvl clear
    window hide
    scene tusa
    with ed_lap
    nvlbazar "Один из темнокожих кентов {b}Maxxyma{/b} заметил угашенного Вечного и затащил его на танцпол."
    nvlbazar "И когда врубили на диджейском пульте {b}народные песни республики Конго{/b},{w=0.2} Вечный ушёл в отрыв."
    nvl clear
    nvlbazar "Все проблемы и загоны отошли на второй план."
    nvlbazar "Он просто чувствовал себя прекрасно."
    nvlbazar "Позабыв о потере {b}Номера Третьего{/b},{w=0.2} о зачётах в шараге,{w=0.2} о уборке хаты и прочем говне,{w=0.2} Вечный узнал,{w=0.2} что есть настоящее счастье."
    nvl clear
    nvlbazar "Счастье для него -{w} не париться ни о чём."
    nvlbazar "Иметь людей вокруг себя."
    nvlbazar "Не чувствовать туманности завтрашнего дня."
    nvl clear
    nvlvhcn "Вот так надо отдыхать."
    nvlbazar "Думал про себя Вечный."
    nvl clear
    show vasilisa:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'vasilisa'
        parallel:
            xpos 3.0 
            linear 0.80 xpos 0.75 
    with Pause(0.90)
    show vasilisa:
        xpos 0.75 
    nvlbazar "Присев на пуфики перевести дыхание,{w=0.2} Вечный заметил Василису,{w=0.2} которая летела на всех парах к нему с бухлом."
    nvlbazar "Продолжая его спаивать,{w=0.2} она спрашивала наводящие вопросы."
    nvl clear
    vas "А у тебя девушка есть?" with vpunch
    "Вечный прихуел от своей удачи."
    vchn "Теперь нет." with vpunch
    "Немного резво ответил наш паря."
    "Всё таки градус не самый низкий залит внутри у него."
    vas "Не верится мне что-то." with vpunch
    vas "Ты ж не урод."
    vas "Не конченный."
    vas "Да даже не отбитый."
    vas "Брешешь небось?" with vpunch
    vchn "Нет."
    vchn "Просто я вечно кого-то чем-то не устраиваю."
    "Не соврал он."
    vas "Не заметила в тебе ничего такого."
    vchn "Значит,{w=0.2} все мои бывшие -{w} шмаромойки?"
    vas "Вот ты и ответил на вопрос,{w=0.2} который,{w=0.2} я уверена,{w=0.2} не давал тебе покоя."
    vchn "Хм."
    vchn "А ведь действительно." with vpunch
    stop music fadeout 4
    nvlbazar "За их разговором последовало включение трека {b}Enjoykinа <<Ламповая Няша>>{/b}."
    nvlbazar "Они просто наслаждались моментом и парили одноразку."
    nvl clear
    play music thatlife fadein 2
    nvlbazar "Не сказать,{w=0.2} что Василиса не начала что-то чувствовать."
    nvlbazar "Было что-то отдалённое,{w=0.2} из далёкого прошлого."
    nvlbazar "Ощущение давно забытое."
    nvlbazar "Как из прошлой жизни.{w} Которой не было."
    nvl clear
    nvlbazar "Пока Вечный завтыкал на исполняющего танец {b}Рикардо{/b} Максимку,{w=0.2} Василиса поняла,{w=0.2} что другого шанса не будет."
    nvlbazar "Она аккуратно извлекла катетер из подсумка,{w=0.2} прикреплённого к бедру и спрятанного под юбкой."
    nvlbazar "Почти добравшись до поясницы Вечного,{w=0.2} тот решил обернуться,{w=0.2} дабы поделиться впечатлениями от увиденного."
    nvlbazar "Василиса еле успела убрать катетер обратно."
    vchn "Чёта ты загрустила."
    vas "А?{w} Да не,{w=0.2} тебе показалось."
    "Она неумело натянула улыбку."
    vchn "Я же вижу,{w=0.2} что что-то не так."
    vas "Просто ты мне нравишься." with vpunch
    "Сумела выкрутиться,{w=0.2} ничего не сказать."
    "Только вот методы такие на Вечном просто не сработают."
    vchn "Да неужели?"
    "Он решил играть в дурака."
    vchn "Ты мне тоже." with vpunch
    vas "Правда?"
    vchn "Конечно."
    nvl clear
    nvlbazar "Парализованный разговор спас кент Максимки,{w=0.2} который вытянул обоих на танцпол."
    nvl clear
    nvlbazar "На медляке каждый из них думал о своём."
    nvl clear
    nvlvhcn "Кому она пиздит?"
    nvlvhcn "Не верю я в подобное."
    nvlvhcn "Она вообще меня впервые видит."
    nvl clear
    nvlvas "Надеюсь,{w=0.2} он не засёк ничего."
    nvlvas "Не успела подсумок застегнуть."
    nvlvas "Хоть бы не выпал{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Хоть бы{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlvas "Точно!"
    nvlvas "Есть вариант,{w=0.2} как гопнуть ДНК."
    nvlvas "Он мне его сам и отдаст."
    nvlvas "Буквально."
    vas "Слушай{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Пойдём отсюда,{w=0.2} а?" with vpunch
    vchn "А чё так?"
    "Хотя Вечный тоже был не против ливнуть."
    "Ему был интересен её мотив."
    vas "Мне тоже{w=0.2}.{w=0.2}.{w=0.2}.{w} Тяжко находится в подобных местах{w=0.2}.{w=0.2}.{w=0.2}."
    "Вечный из-за затуманенного разума не смог определить элементарное противоречие."
    "Её сюда никто не тащил.{w} В отличие от него."
    "Вечному просто было похуй.{w} И это стало его большо{w=0.2}о{w=0.2}ой ошибкой."
    vchn "Ну,{w=0.2} пошли."
    "Они отправились ко входу в помещение для уеденения."
    play sound door_break
    scene komnata_seksa with vpunch
    "Василиса проталкивает его в двери,{w=0.2} после чего,{w=0.2} имитируя порыв страсти,{w=0.2} ловко достаёт катетер и гопает ДНК Вечного из поясницы."
    vchn "Ай,{w=0.2} сука!" with vpunch
    "Вечный почувствовал лёгкий укол в поясницу."
    vchn "Неудачно приземлился,{w=0.2} однако."
    nvl clear
    nvlbazar "Он всё ещё туго соображал."
    nvlbazar "План Василисы был выполнен."
    nvlbazar "Почти.{w} Осталось отделаться от него и ливнуть."
    nvl clear
    nvlbazar "И шанс подвернулся."
    nvlbazar "Вечный пошёл в толкан."
    nvl clear
    scene vannaya with ed_lap
    nvlvhcn "Сука,{w=0.2} не идёт совершенно..."
    nvl clear
    nvlbazar "Из-за дымящего шишака напор вообще отсутствовал."
    nvlbazar "Он стоял там минут десять с {b}fat cockом{/b} в руке."
    nvlbazar "К нему даже пару раз типа залетали."
    nvlbazar "И сразу же улетали обратно."
    nvl clear
    nvlbazar "Вечный стоял с лицом,{w=0.2} полным недоумения.{w} В толчке.{w} С хуем в руке."
    nvlbazar "Со стороны странное зрелище."
    nvlbazar "Но ему было похуй."
    nvlbazar "Были проблемы и понасущнее."
    nvl clear
    scene tusa with ed_lap
    nvlbazar "С горем пополам поссав,{w=0.2} он возвращается обратно."
    nvl clear
    nvlbazar "В зале нигде не было Василисы."
    nvlbazar "Вечный взглядом замечает Вишневского."
    window hide
    show vlados2:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'vlados2'
        parallel:
            ypos 2.0 
            linear 0.80 ypos 1.0 
    with Pause(0.90)
    show vlados2:
        ypos 1.0 
    window show
    vchn "Юра!" with vpunch
    vsn "О,{w=0.2} Михон!"
    vchn "Слушай,{w=0.2} ты не видел тут одну тяночку..."
    vsn "ООО!" with vpunch
    vsn "Поздравляю,{w=0.2} братиш!"
    stop music fadeout 5
    vchn "Да погоди ты."
    vchn "Рыжеволосую такую не видел?"
    "Вечный осознал,{w=0.2} что он даже её имени не спросил."
    th "Пиздец.{w} Полный."
    vsn "Была какая-то."
    vsn "Она спешно покинула это заведение." with vpunch
    window hide
    show rageone with ed_alpha_diss_fast
    play music redhead
    pause 1
    nvl clear
    nvlvhcn "Ебать я лошара."
    nvlvhcn "Это просто пиздец."
    nvlvhcn "Меня кинули?{w} Ха."
    nvlvhcn "Как буд-то ты ожидал чего-то другого?"
    nvlvhcn "Всё было очевидно с самого начала."
    nvl clear
    nvlvhcn "Не зря я не верил во все эти сказки."
    nvlvhcn "Не верил{w=0.2}.{w=0.2}.{w=0.2}.{w} Ха!"
    nvlvhcn "Оно и видно блять."
    nvlvhcn "Пиздец."
    vsn "Что с тобой?" with vpunch
    vsn "На тебе лица нет."
    vsn "Ты буд то призрака увидел."
    stop music fadeout 5
    vchn "Ничего особенного,{w=0.2} не бери в голову."
    hide rageone with ed_alpha_diss_fast
    nvl clear
    window hide
    hide vlados2
    show vlados2:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'vlados2'
        parallel:
            yanchor 1.0 
            linear 0.80 yanchor -2.0 
    with Pause(0.90)
    show vlados2:
        yanchor -2.0 
    hide vlados2
    pause 3
    play music idiot fadein 2
    nvlvhcn "Какой же я идиот{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvhcn "Мне тут делать больше нечего."
    nvl clear
    nvlbazar "Думал про себя Вечный,{w=0.2} попутно проверяя баланс."
    nvlbazar "Там были лишь полторы сотки."
    nvlbazar "Потом он чекнул яндекс такси,{w=0.2} где цена была 250."
    nvl clear
    nvlvhcn "Заебись."
    nvl clear
    nvlbazar "Но у него появилась идея."
    nvl clear
    nvlvhcn "Надеюсь,{w=0.2} ещё не забыли меня{w=0.2}.{w=0.2}.{w=0.2}."
    nvl clear
    nvlbazar "Он начал писать в свой заброшенный чат в телеграмме,{w=0.2} пингуя всех."
    nvl clear
    nvlvhcn "Бля посоны.{w} Киньте сотку,{w=0.2} по-братски.{w} На такси не хватает."
    nvl clear
    nvlbazar "Первым откликнулся Вадим Морозов."
    nvl clear
    nvllxrd "Здарова.{w} Где ты пропадаешь?{w} Сотку ща кину.{w} Номер карты дай."
    nvl clear
    nvlbazar "После того,{w=0.2} как Вадимка скинул Вечному сотку на сбербанк,{w=0.2} Вечный записал видеосос,{w=0.2} где танцевали негритосы."
    nvl clear
    nvllxrd "АХАХА!{w} Ебать ты там отжигаешь."
    nvl clear
    nvlvhcn "Я ливаю отсюда.{w} Заебало всё нахуй."
    nvl clear
    nvlbazar "И Вечный закрыл тг,{w=0.2} после чего заказал эконом."
    nvlbazar "Юра и негритосы проводили его в долгий путь домой."
    nvlbazar "Вечный прыгнул в Kia Rio и поехал домой."
    window hide
    scene black with ed_night_dis
    $ MND_Chapter("От лица Василисы:")
    scene tusaposle
    show doshd
    with ed_night_dis
    nvl clear
    nvlbazar "Василиса двигалась к автовокзалу,{w=0.2} который был недалеко от изначального места дислокации."
    nvlbazar "Попутно она размышляла о правильности совершенного поступка."
    nvl clear
    nvlvas "И зачем всё это?"
    nvlvas "Он явно не тот,{w=0.2} кого стоит так жестко наёбывать."
    nvlvas "Ебучий казах,{w=0.2} сука!"
    nvl clear
    nvlbazar "На её глазах начали появляться слёзы."
    nvl clear
    nvlvas "Оригинал бы точно не хотела себе такого клона{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Жаль только,{w=0.2}  что её больше нет в живых."
    nvlvas "И за что она полегла только?"
    nvlvas "Казах и за это ответит{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "А ты -{w}  дура."
    nvlvas "Согласилась работать на идиота."
    nvlvas "Зачем только{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Можно же было просто съебаться!"
    nvl clear
    nvlvas "Ладно."
    nvlvas "Всё равно собралась возвращаться."
    nvlvas "Надо потребовать у него свободу."
    nvlvas "Ему ничего не останется мне предоставить."
    nvl clear
    nvlvas "Так и сделаю."
    nvlvas "А сейчас{w=0.2}.{w=0.2}.{w=0.2}."
    nvlvas "Меня ждёт рейс в Курган."
    stop music fadeout 5
    nvl clear
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("Через пару дней")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music raw
    scene ineony
    with ed_night_dis
    vas "Ты моральный урод." with vpunch
    vas "Для чего тебе это ебаное ДНК?" with vpunch
    nn "Ха."
    nn "Кто из нас урод ещё{w=0.2}.{w=0.2}.{w=0.2}.{w} Тем более моральный{w=0.2}.{w=0.2}.{w=0.2}."
    nn "Я-то в отличие от тебя никого не наёбывал." with vpunch
    vas "Всё из-за тебя{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Я отказываюсь работать на тебя." with vpunch
    vas "Всё кончено."
    vas "Можешь идти нахуй." with vpunch
    nn "Так уверена в себе?{w} Ахаха{w=0.2}.{w=0.2}.{w=0.2}."
    nn "Не забывай,{w=0.2} кто твой создатель."
    nn "Я заложил в тебя механизм отката."
    nn "Стоит мне сказать секретную комбинацию,{w=0.2} как ты полностью потеряешь самоконтроль." with vpunch
    vas "Ах ты{w=0.2}.{w=0.2}.{w=0.2}."
    nn "А теперь утирай сопли и пиздуй блять на новое задание."
    nn "Выбора у тебя всё равно нет."
    vas "И что на этот раз?"
    vas "Грабёж,{w=0.2} убийство,{w=0.2} изнасилование?" with vpunch
    nn "Каво?"
    vas "Никаво.{w} Чё тебе в этот раз надо?{w} Ускоглазая ты морда." with vpunch
    nn "Попроще будь.{w} Иначе пойдёшь по пути утилизации,{w=0.2} прям как отбраковка."
    nn "Чувства у неё появились,{w=0.2} видите ли.{w} Ха."
    nn "В общем.{w} Тебе нужно убрать одну нехорошую фигуру из нашей партии."
    nn "Его имя -"
    nn "Его имя -{fast} Дмитрий Скитецкий." with vpunch
    nn "Лысый такой."
    nn "В капюшоне постоянно ходит."
    nn "Как ты его нейтрализуешь -{w} уже твои проблемы."
    nn "Задача ясна?"
    "В ответ молчание."
    nn "ЯСНА,{w=0.2} БЛЯТЬ?!" with vpunch
    vas "да{w=0.2}.{w=0.2}.{w=0.2}."
    "Тихо проронила Василиса и покинула комплекс."
    scene labaext with ed_lap
    th3 "И чё мне с этим делать?"
    th3 "Ладно."
    th3 "Подумаю об этом позже."
    stop music fadeout 5
    th3 "А сейчас меня ждёт рейс в Новошахтинск."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Димы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music nightmare fadein 5
    scene nmall
    show doshd
    play ambience dviglo
    with ed_night_dis
    "Дмитрий ехал по Новошохтинску на своём некро-ведре."
    "Из хрипящих динамиков доносился до ушей старый добрый русский транс."
    "Движок десятки пердел,{w=0.2} хрипел,{w=0.2} умирал,{w=0.2} но,{w=0.2} сука,{w=0.2} работал."
    "Самое главное -{w=0.2} что ехал."
    "Иначе Димка бы ехал на маршрутке."
    "С бабками.{w} Которые не моются."
    "И тогда бы ему было пиздец как грустно."
    window hide
    pause 1
    "Куда он едет?"
    play sound herznaet
    window hide
    pause 1.6
    "Димка повернул в сторону своей trap хаты."
    "Как говориться -{w=0.2} навалил боком под плёнку на Лвовский переулок, 4."
    scene traphata
    show doshd
    with dissolve2
    window hide
    pause 1
    "Выглядит как бомжатник?" with vpunch
    "У{w=0.2}у{w=0.2}у{w=0.2},{w=0.2} это вы ещё внутри не были!"
    "Там вообще пиздец свалка нахуй."
    "Как говорит Димасек:"
    skt "Главное -{w=0.2} кто пахан.{w=0.2} Остальное не ебёт.{w=0.2} Если,{w=0.2} конечно,{w=0.2} ты не под шконкой))){w=0.2} гы"
    window hide
    pause 1
    scene domext
    play sound tazik1
    show doshd
    stop ambience fadeout 2
    "Дима припарковал свой тазик,{w=0.2} обклеенный аниме наклейками с зеро ту."
    play sound tazik2
    "Оставив тазик гнить под открытым небом,{w=0.2} Скит отправился домой."
    scene domint with dissolve2
    window hide
    pause 1
    "Зайдя, как полагается,{w=0.2} на хату,{w=0.2} Дерьмон начал думать{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Чем бы заняться сука?" with vpunch
    window hide
    pause 1
    "Димка решил поклацать свой пк."
    scene pc with ed_lap
    "Его комп на AMD Athlon 64 4000+ с 256 мб ддр1 еле тянул браузер."
    "А IDE хард на 40 гигов был забит файлами для прошивки на LegionOS."
    skt "ДА ЗАГРУЖАЙСЯ БЫСТРЕЕ,{w=0.2} СУКА!" with vpunch
    play sound udarklava
    "Скитолс распсиховался и въебал двоечку по клавиатуре ps/2."
    window hide
    pause 2
    skt "Может ссд исправит ситуацию?"
    window hide
    pause 1
    "Не долго думая,{w=0.2} Димка решил отправится в DNS в своём любимом тц Новошахтинск MALL."
    scene traphata
    show doshd
    with dissolve2
    window hide
    pause 1
    skt "Ща по фасту все сделаем."
    skt "Хули время терять."
    "И Димка поехал в тц."
    scene nmall
    show doshd
    with dissolve2
    "Димас припарковал свой тазик и вышел на улицу."
    scene novomall
    show doshd
    window hide
    pause 1
    skt "Бля там охранник сука." with vpunch
    scene propusk with dissolve2
    "Предъявив охране свой паспорт,{w=0.2} Дима отправился гулять по тц."
    scene nmallint with dissolve2
    window hide
    pause 3
    stop music fadeout 6
    "Походив по павильонам,{w=0.2} Димка таки купил ссд."
    "Это был Goldenfir на 120 гб."
    "Доместос отдал за него three hundred bucks."
    "Зато теперь его windows 98 будет загружаться очень быстро."
    window hide
    pause 1
    "У Димона проскочила шальная мысль пойти обоссать золотой ободок параши{w=0.2}.{w=0.2}.{w=0.2}."
    "И он решил совершить сие действие."
    "Золотые толчки {b}Новошахтинск MALL{/b}а начали трепетать."
    "Ведь туда идёт Дима."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Василисы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music wmm1 fadein 2
    scene train with ed_night_dis
    nvl clear
    nvlbazar "Поезд проехал Ростов и двигается прямо к Новошахтинску."
    nvlbazar "Василиса задумчиво смотрела в окно."
    nvl clear
    nvlvas "Пойти парашу обоссать?"
    nvl clear
    nvlbazar "После этой мысли у неё пошли странные ассоциации.{w} Как из прошлой жизни.{w} Которой не было."
    nvlbazar "Как к ней приходит какой-то старпёр с пельменем на голове и представляется сантехником {b}<<Личинус Турбо>>{/b}."
    nvlbazar "Он обирается почистить толчок вилкой,{w=0.2} но всё же у него этого не вышло,{w=0.2} после чего ему пришлось харкнуть и блять ебануть ногой."
    nvlbazar "После чего развалился толчок и он сбежал с криком {b}<<ИДИ НАХУЙ>>{/b}."
    nvl clear
    nvlvas "С чего такие мысли пошли,{w=0.2} интересно?"
    nvl clear
    nvlbazar "Впрочем,{w=0.2} это её мало заботило."
    nvl clear
    play sound door_open
    scene train2 with ed_lap
    "Василиса вышла в корридор."
    "Её не покидало плохое предчувствие."
    th3 "Может не стоит туда заходить?"
    th3 "Не так уж и сильно охота{w=0.2}.{w=0.2}.{w=0.2}."
    th3 "Хотя,{w=0.2} делать всё равно нехрен{w=0.2}.{w=0.2}.{w=0.2}."
    th3 "С Богом."
    "И она зашла в толкан поезда РЖД."
    window hide
    play sound door_break
    scene train3 with vpunch
    pause 0.5
    play sound chenado
    window hide
    pause 1.5
    "Открыв дверь ногой,{w=0.2} она,{w=0.2} мягко говоря,{w=0.2} ахуела."
    vas "Блять." with vpunch
    "В параше царил полный хаос."
    "По стенкам стекала малафья."
    "Запах стоял соответствующий."
    "А на параше,{w=0.2} как на троне,{w=0.2} сидел какой-то обезумевший дед."
    "Зрелище не из приятных."
    play sound door_break
    scene train2 with vpunch
    "Василиса поспешно ретировалась оттуда,{w=0.2} не проронив ни слова."
    "Ссать перехотелось капитально."
    scene train with ed_lap
    "Остаток поездки она провела в подвешанном состоянии."
    "Сдерживаться под конец было тяжко."
    "Но,{w=0.2} слава мэру Новошахтинска,{w=0.2} вокзал находился не за пределами города."
    scene novomallblya with ed_lap
    "В итоге Василиса вышла к тц {b}Новошахтинск MALL{/b}."
    "Выбора не было,{w=0.2} пришлось искать толкан там."
    play sound door_break
    scene nmallint with vpunch
    "Сбив с ног охранника,{w=0.2} она помчалась в рандомном направлении."
    "Не прогадала."
    "Толкан как раз находился в той стороне."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Димы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene tolkanmall with ed_night_dis
    window show
    "Димас стоял и играл своими {b}<<мускулами>>{/b} перед зеркалом."
    "Его ничто не могло отвлечь."
    window hide
    play sound nitroblya
    show vasilisa:
        default subpixel True 
        parallel:
            Null(640.0, 640.0)
            'vasilisa'
        parallel:
            xpos -0.3 
            linear 0.80 xpos 1.3 
    with Pause(0.90)
    show vasilisa:
        xpos 1.3 
    play sound2 door_break
    window show
    "Даже рыжая тян,{w=0.2} которая с разбегу выносит дверь и залетает в толкан."
    play sound possala
    "Скит всё так же любовался своими руками."
    "А ведь если просто начать заниматься спортом{w=0.2}.{w=0.2}.{w=0.2}."
    "То и Димас может стать кочкой."
    "Масса -{w} есть."
    "Небольшая,{w=0.2} но есть."
    "Остались тренировки и спортивное питание."
    "Но с этим всё посложнее."
    "Дима,{w=0.2} конечно,{w=0.2} никогда не славился пробитием очка с любой хавки."
    "Но крафтовый спортпит с ходу пить он очкует."
    "Хотя,{w=0.2} когда работаешь сантехником{w=0.2}.{w=0.2}.{w=0.2}."
    "Не похуй ли?"
    "Толчок всегда под рукой."
    window hide
    pause 1
    "Димас прислушался{w=0.2}.{w=0.2}.{w=0.2}."
    "И помимо стандартных звуков мочеиспускания он услышал приглушённые маты{w=0.2}.{w=0.2}.{w=0.2}."
    "Единственная мысль,{w=0.2} которая его посетила{w=0.2}.{w=0.2}.{w=0.2}."
    stop sound fadeout 3
    th4 "Бля{w=0.2}.{w=0.2}.{w=0.2}.{w} А какой из толчков я обоссал?" with vpunch
    play sound smiltolkan
    th4 "Будет нехорошо если она на обоссаный мною полетела."
    "Рыжая тян выходит с параши."
    window hide
    play sound door_open
    pause 1
    show vasilisa:
        default subpixel True 
        parallel:
            Null(640.0, 640.0)
            'vasilisa'
        parallel:
            xpos -0.3 
            linear 0.56 xpos 0.25 
    with Pause(0.66)
    show vasilisa:
        xpos 0.25 
    window show
    stop music fadeout 7
    vas "Дружище,{w=0.2} не знаешь,{w=0.2} кто весь ободок обоссал?" with vpunch
    "Скит начал паниковать."
    play sound nezn2
    window hide
    pause 1.7
    vas "Уверен?" with vpunch
    play sound nezn3
    window hide
    pause 1.9
    vas "Ну ладно."
    "И тут Василиса заметила подозрительное сходство этого типа с описанием Неони."
    play music theorem
    vas "Как тебя звать?" with vpunch
    skt "К чему такие вопросы?"
    vas "Это важно."
    "Димка почуял неладное."
    "Рука машинально потянулась к старенькому макарычу,{w=0.2} что Скит всегда с собой таскал за пазухой."
    play sound dostal
    "Однако,{w=0.2} было уже поздно."
    "Прямо в лоб Диме был направлен {b}семнадцатый Glock{/b}."
    skt "Что тебе нужно?"
    vas "Узнать,{w=0.2} кто обоссал стульчак." with vpunch
    "Скит понял,{w=0.2} что с этой девочкой шутить не стоит."
    skt "Это был я." with vpunch
    skt "Прости пожалуйста."
    skt "Я не хотел."
    skt "Честно."
    "Соврал он."
    skt "Просто голова закружилась,{w=0.2} и я наклонился,{w=0.2} пока ссал{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Голова закружилась?!" with vpunch
    vas "Да там твоя ссанина с потолка аж капает!" with vpunch
    vas "Это ж какой напор должен был быть?!" with vpunch
    skt "Да у тебя тоже неслабый был{w=0.2}.{w=0.2}.{w=0.2}."
    play sound pistolkurok
    "Она взвела курок пистолета."
    vas "Ты мне тут не тыкай!" with vpunch
    vas "Вытерпи с моё."
    vas "И не такой напор будет."
    skt "Давай забудем то,{w=0.2} что тут было,{w=0.2} а?"
    vas "Ты погоди."
    vas "Так как тебя звать-то?"
    skt "Меня зовут Дмитрий."
    skt "Дмитрий Скитецкий."
    "Василиса ахуела."
    "Это тот самый Скит."
    th3 "И что мне теперь с ним делать?"
    skt "Малолетка конченная тебя послала ко мне,{w=0.2} да?"
    "Скит горько усмехнулся."
    skt "Убьёшь меня?" with vpunch
    "У неё начали дрожать руки."
    "Начался самый настоящий мандраж."
    play sound ubralstvol
    "Василиса опустила пистолет."
    vas "Не собираюсь я тебя убивать."
    "Димасик выдохнул."
    stop music fadeout 5
    vas "У меня есть информация для тебя."
    vas "А за стульчак ты ответишь."
    vas "Извращенец." with vpunch
    skt "А почему извращенец?"
    vas "А зачем тогда подслушивал?"
    "Скиту не нашлось,{w=0.2} что ответить."
    play music hgod fadein 3
    "И следом назрел вопрос."
    skt "А ты где ствол ныкаешь-то?" with vpunch
    skt "На юбках карманов вроде нету,{w=0.2} насколько я знаю."
    vas "Ты уверен,{w=0.2} что хочешь это знать?"
    "Скит задумался."
    skt "Конечно."
    vas "На трусах карманчик есть." with vpunch
    skt "Да ну."
    skt "Он слишком маленький для глока."
    vas "Ладно,{w=0.2} развести тебя не получилось."
    vas "Я храню ствол между трусами и пиздой." with vpunch
    vas "Я возбуждаюсь,{w=0.2} когда мой клитер касается холодного металла."
    vas "И начинаю течь."
    vas "Весь ствол пахнет смазкой."
    vas "Не хочешь занюхнуть?" with vpunch
    "Все эти фразы она выпалила с явной долей язвы в голосе,{w=0.2} но скит этого не заметил."
    "Мб тупой слишком."
    skt "Давай." with vpunch
    "Василиса достала ствол из под юбки."
    "Сделала всё так,{w=0.2} чтобы Скит не заметил подсумок,{w=0.2} который прикреплён к бедру."
    play sound vdohnul
    "Скит понюхал ствол."
    skt "Но он же ничем не пахнет!"
    vas "Потому что ты идиот." with vpunch
    "Резко констатировала факт Василиса."
    "Скит лишь пожал плечами."
    skt "Ты говорила,{w=0.2} что у тебя есть информация для меня?"
    vas "Да."
    vas "Но не здесь."
    vas "Много лишних ушей."
    vas "Тип с дверного проёма уже минут 15 на нас глазеет." with vpunch
    play sound door_break
    "После этих слов дверь в толкан захлопнулась."
    skt "Тогда поехали ко мне."
    vas "Не хотелось бы,{w=0.2} конечно{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 4
    vas "Но вариантов лучше у меня нет."
    skt "Тогда прыгаем в мою ладу 2110 и стартуем."
    skt "Ехать недалеко там."
    scene nmall
    show doshd
    play music rassvet fadein 2
    play ambience dviglo fadein 4
    with dissolve2
    "Они прыгнули в тачку Скита."
    "Он изначально хотел подрубить треков {b}EMINEM{/b}а, но передумал."
    "Они ему уже просто надоели."
    "А {b}plenka{/b} она бы не оценила."
    "По крайней мере,{w=0.2} так думал Дима."
    "Поэтому он подрубил молодёжного исполнителя."
    "Василиса это никак не прокоментировала."
    "И они продолжали двигаться к Львовскому переулку 4."
    scene traphata
    show doshd
    with dissolve2
    stop ambience fadeout 3
    stop music fadeout 3
    skt "Приехали."
    window hide
    scene domext
    show doshd
    play ambience rain_out
    play sound tazik1
    with vpunch
    show vasilisa:
        default subpixel True 
        parallel:
            Null(640.0, 640.0)
            'vasilisa'
        parallel:
            xpos -0.3 
            linear 0.56 xpos 0.25 
    with Pause(0.66)
    show vasilisa:
        xpos 0.25 
    window show
    vas "Веди,{w=0.2} сорвиголова."
    window hide
    stop ambience fadeout 3
    play music morandi fadein 3
    scene domint
    show vasilisa at left
    with ed_lap
    skt "Вот они,{w=0.2} мои хоромы."
    vas "Бомжатник." with vpunch
    skt "Да почему?"
    vas "Воняет носками."
    vas "Ремонт не делался лет двадцать."
    vas "Ну и твои трусы с черкашами под тумбочкой лежат."
    show krisa at right
    dobby "Привет." with vpunch
    window hide
    pause 1
    vas "ЕБАТЬ!" with vpunch
    "Василиса аж подпрыгнула от неожиданности."
    vas "Ты что ещё за хуйня?!"
    dobby "Я не хуйня,{w=0.2} я -{w} {b}доберман{/b}."
    vas "С хуя ли у тебя тут такой зоопарк?" with vpunch
    skt "Ответь мне на один вопрос."
    "Обратился он к доберману."
    skt "Кто такой Ракун?"
    dobby "Да я ебу?" with vpunch
    skt "Понятно."
    "Скит достал из под заваленного шкафа ргдшку."
    dobby "Что тебе понятно?"
    show grena at right
    play sound prosto
    skt "Всё просто!"
    dobby "Что ты делаешь?!" with vpunch
    hide grena
    play sound grena0
    dobby "БЛЯ!" with vpunch
    play sound grena1
    show normalno_ebanulo with dspr:
        ypos 0.15
        xpos 0.50
        zoom 1.6
    
    with vpunch
    window hide
    hide krisa
    hide normalno_ebanulo
    play sound2 perdun
    show krisa:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 2 rotate 1080 zoom 0.0 xpos 0.45 ypos 0.1
    window hide
    pause 2
    "После того,{w=0.2} как доберманчик улетел всратосферу,{w=0.2} Димка решил объяснить своё поведение Василисе."
    skt "Это не мой доберман."
    skt "Как оказалось,{w=0.2} подставным был и тот,{w=0.2} который пытался отогнать школьников."
    skt "В итоге они его застралели с СВД."
    th4 "Вечный,{w=0.2} сука,{w=0.2} ты за это ответишь."
    vas "Дурдом." with vpunch
    vas "Сплошной." with vpunch
    "Дима хотел что-то возразить,{w=0.2} как вдруг{w=0.2}.{w=0.2}.{w=0.2}."
    play sound mobila_zvonok
    skt "Да сука!" with vpunch
    "Димочке позвонили на {b}POCO M3 PRO 5G{/b}."
    "Пиздатый рингтон,{w=0.2} да?"
    play sound mobila_dostal
    skt "Оло."
    "На проводе был его брат -{w=0.2} Даня Скитецкий."
    "Он как раз сдавал егэ."
    play sound ege1
    with vpunch
    window hide
    pause 6
    skt "И?"
    play sound ege2
    with vpunch
    window hide
    pause 17
    skt "Какой Сталин-Гулаг?"
    play sound ege3
    with vpunch
    window hide
    pause 20
    skt "Успокойся."
    play sound ege4
    with vpunch
    window hide
    pause 19
    skt "Они всем так говорят."
    play sound ege5
    with vpunch
    window hide
    pause 7
    skt "Ну а как ты хотел?{w} Всё по чесноку."
    play sound ege6
    with vpunch
    window hide
    pause 19
    play sound mobila_polojil
    skt "Заебал своим нытьём сука."
    "Скит сбросил звонок."
    vas "Типа на линии явно таращит."
    skt "Ой,{w=0.2} блять." with vpunch
    skt "Как буд то сама ЕГЭ не сдавала{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 4
    "Василиса впала в ступор."
    "Однако быстро оклемалась."
    skt "Так что за информация?"
    play music crysis21
    vas "Тебя заказал Казах." with vpunch
    window hide
    pause 1
    play sound chivo_blyat
    pause 1
    vas "Не удивляйся."
    vas "Это действительно так."
    skt "Значит,{w=0.2} всё суперхуёво{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Я тебе больше скажу."
    vas "Он разработал методику теневого клонирования людей." with vpunch
    vas "Он смог клонировать меня и Вадима Морозова."
    vas "Мой оригинал он убил." with vpunch
    vas "Сучара{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Небось долго над ней издевался{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    vas "А клоны Вадимки просто уродливые получаюся."
    vas "Один лысый,{w=0.2} другой сизый{w=0.2}.{w=0.2}.{w=0.2}."
    vas "В общем,{w=0.2} он настоящий садист." with vpunch
    skt "Пиздец{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Он приказал мне убить тебя." with vpunch
    skt "Ты же не собираешься{nw}"
    vas "Нет."
    vas "Расслабься."
    skt "И что предлагаешь делать?"
    vas "Пока что нас двое."
    vas "И я не самый надежный вариант для тебя."
    skt "Почему?"
    vas "Казах говорил,{w=0.2} что у него есть секретная комбинация отката клона."
    vas "Стоит ему сказать эту фразу как меня переклинит." with vpunch
    vas "Всё это с его слов."
    vas "Может быть,{w=0.2} он блефовал."
    vas "Но я проверять не особо хочу."
    stop music fadeout 4
    skt "Армии клонов и этой технологии впринципе у меня нет."
    skt "Но у меня есть один туз в рукаве." with vpunch
    skt "Причем козырный."
    skt "Позывной Вечный тебе о чём нибудь говорит?" with vpunch
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Василисы:")
    hide zatemnenie with dissolve2
    play music crysis3pausetheme
    hide vasilisa
    show skitpio
    with flash
    window show
    show rageone with ed_alpha_diss_fast
    th3 "Ещё как говорит{w=0.2}.{w=0.2}.{w=0.2}."
    vas "Так я же{w=0.2}.{w=0.2}.{w=0.2}."
    "У неё началось головокружение и адская пульсация в висках."
    hide rageone
    show ragetwo with ed_alpha_diss_fast
    vas "Что-то мне нехорошо{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Ты только не помирай мне тут!"
    hide ragetwo
    show ragethree with ed_alpha_diss_fast
    "Боль стала невыносимой."
    "Кричать не было сил."
    show blink
    "Василиса просто закрыла глаза."
    window hide
    scene black
    pause 1
    scene tusa
    show bergennorm
    show overlay aw_memory_back_1
    show unblink
    vchn "И для чего тебе всё это надо было?" with vpunch
    "Василиса потеряла дар речи."
    "Увиденное шокировало похлеще вкладки {b}trans на сайте x-videos{/b}."
    vchn "Ты так и будешь молчать?" with vpunch
    "Похуистическим тоном спросил Вечный."
    vas "прости{w=0.2}.{w=0.2}.{w=0.2}."
    "Тихо вымолвила Василиса."
    vchn "Что мне твоё прости?" with vpunch
    vchn "Ты уже показала себя в деле."
    "У Василисы машинально потекли слёзы."
    vchn "Слезами горю не поможешь."
    vchn "Успокойся для начала."
    vchn "Потом помоги Димону наказать школьников."
    vchn "Этим ты и заработаешь себе искупление." with vpunch
    "Василиса лишь угрюмо кивнула."
    stop music fadeout 3
    vchn "А теперь очнись." with vpunch
    vas "Что?"
    lis "ОЧНИСЬ!" with vpunch
    "Картина перед глазами начала рушиться."
    window hide
    scene black with ed_night_dis
    play sound fb
    scene domint
    show skitpio
    with flash
    play music crysis3 fadein 2
    skt "ОЧНИСЬ!" with vpunch
    "Василиса начала жадно хватать ртом воздух."
    skt "Оклемалась?"
    "Василиса отдышалась."
    vas "Вроде да."
    skt "Всё забываю спросить{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Как тебя звать-то хоть?"
    vas "Ва{w=0.2}.{w=0.2}.{w=0.2}."
    "Её терзали мысли о том сне."
    vas "ва{w=0.2}.{w=0.2}.{w=0.2}."
    "Она же сейчас разревётся!"
    vas "ВАСИЛИСА!" with vpunch
    "Она обняла Скита и начала реветь навзрыд."
    "Но Скит не такой чёрствый,{w=0.2} как вы думаете."
    skt "Ну тише,{w=0.2} тише{w=0.2}.{w=0.2}.{w=0.2}."
    "Скиту стало грустно."
    skt "Перестань,{w=0.2} а не то я тоже заплачу{w=0.2}.{w=0.2}.{w=0.2}."
    "Дима пытался держаться изо всех сил{w=0.2}.{w=0.2}.{w=0.2}."
    "Но по итогу тоже пустил скупую мужскую."
    window hide
    pause 1
    "Они сидели на полу обняв друг друга."
    "Каждый думал о своём."
    "Скит продумывал план с кодовым названием {b}<<CRASH MALOLETOK>>{/b}."
    "Василиса пыталась успокоится."
    "Как бы она себя не пыталась переубедить{w=0.2}.{w=0.2}.{w=0.2}."
    "Она окончательно поняла,{w=0.2} что любит Вечного."
    "И по итогу поступила с ним так{w=0.2}.{w=0.2}.{w=0.2}."
    "Но положение спас Скит."
    skt "Я отправлю ему гс."
    skt "Он нам нужен как воздух."
    skt "Без него мы не справимся."
    "Василиса понимала это."
    "Но она не могла представить себе{w=0.2}.{w=0.2}.{w=0.2}."
    ".{w=0.2}.{w=0.2}.{w=0.2}как теперь смотреть ему в глаза{w=0.2}.{w=0.2}.{w=0.2}."
    "Тем временем скит уже достал свой {b}POCO M3 PRO 5G{/b} и открыл телеграм."
    "Потом начал записывать гс,{w=0.2} убрав дрожь в голосе."
    skt "Здарово,{w=0.2} агалый."
    skt "Мне сейчас как никогда нужна твоя помощь."
    skt "Если ты приедешь сюда быстро,{w=0.2} так уж и быть,{w=0.2} прощу тебе те подсрачники и подстреленного добермана."
    skt "Буду ждать ответа."
    "Скит убрал телефон."
    vas "волнуюсь{w=0.2}.{w=0.2}.{w=0.2}.{w} очень{w=0.2}.{w=0.2}.{w=0.2}."
    stop music fadeout 7
    "Из-за эмоционального перенапряжения Василиса начала говорить очень тихо."
    "Видно, эта фича досталась ей от покойного оригинала."
    play sound zubek
    with vpunch
    "Пиликнул поко Димы,{w=0.2} где был установлен звук айфона на уведомлениях."
    "Дима увидел гску и сразу же её включил."
    window hide
    play sound gskabergena
    pause 19
    window show
    skt "Будем ждать."
    play music theorem
    play ambience domofon
    with vpunch
    window hide
    pause 1
    skt "Какого{w=0.2}.{w=0.2}.{w=0.2}."
    vas "кто там?"
    skt "Я никого сегодня не жду{w=0.2}.{w=0.2}.{w=0.2}."
    stop ambience fadeout 3
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Колда:")
    hide zatemnenie with dissolve2
    scene domext with ed_lap
    cld "Опачки..."
    rcn "мфмфмфм!1!" with vpunch
    cld "Потерпи сладкий."
    cld "Оказывается,{w=0.2} у нас завелась крыса{w=0.2}.{w=0.2}.{w=0.2}."
    cld "Никогда бы не подумал{w=0.2}.{w=0.2}.{w=0.2}."
    play ambience domofon1
    "Колд начал звонить в домофон."
    window hide
    pause 2
    stop ambience
    play sound mobila_dostal
    skt "Ало."
    cld "Привет,{w=0.2} Лысая." with vpunch
    cld "Узнаешь меня?"
    window hide
    pause 1
    skt "Это ты,{w=0.2} малолетка конченная?"
    cld "И я тут не один."
    "Колд сдавил правое яичко Ракуна,{w=0.2} что оно чуть не лопнуло."
    rcn "МФМФМФМ!" with vpunch
    cld "Узнаешь голосок?"
    skt "За Ракуна ты ответишь,{w=0.2} школьница."
    cld "Если не хочешь,{w=0.2} чтобы я отстрелил ему башку,{w=0.2} то выходи."
    cld "А не то{nw}"
    rcn "МФМФМФМФМ!!!!" with vpunch
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Скита:")
    hide zatemnenie with dissolve2
    scene domint
    show vasilisa
    with ed_lap
    skt "Нужно идти."
    vas "не оставляй меня{w=0.2}.{w=0.2}.{w=0.2}."
    "Тихо вымолвила окончательно поникшая Василиса."
    skt "Иначе ему крышка."
    skt "Скоро вернусь."
    cld "Ты там скоро?" with vpunch
    skt "Заебал,{w=0.2} дай носки найти!"
    cld "Реще,{w=0.2} заебал." with vpunch
    cld "Если жизнь твоего подсоса для тебя хоть сколько-нибудь важна{w=0.2}.{w=0.2}.{w=0.2}."
    skt "Да подожди ты,{w=0.2} заебал!" with vpunch
    stop music fadeout 4
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Колда:")
    hide zatemnenie with dissolve2
    play music zp22 fadein 3
    scene domext with ed_lap
    pause 2
    play sound door_open
    show skitpio:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'skitpio'
        parallel:
            ypos 2.0 
            linear 0.80 ypos 1.0 
    with Pause(0.90)
    show skitpio:
        ypos 1.0
    pause 1 
    window show
    play sound bm16_shoot
    "В момент выхода Димы из падика Колд отстреливает башку Ракуну со своей трофейной {b}ТОЗ-34{/b}."
    skt "Пидрила,{w=0.2} ты ответишь за это!" with vpunch
    "И начался нереальный махач в стиле {b}JoJo Blizzare Adventure{/b}."
    hide skitpio
    show skitpio1 at center:
        ypos 1.1
        xpos 0.5
        zoom 1.2
        ease 0.1 xpos 0.51 ypos 1.09
        ease 0.1 xpos 0.5 ypos 1.1
        ease 0.1 xpos 0.49 ypos 1.11
        ease 0.1 xpos 0.5 ypos 1.1
        repeat
        
    with dspr
    play sound_loop Ora_ora_ora_LW0607
    
    show kulak_LW0607:
        zoom 0.1
        xpos 0.3
        ypos 0.45
        ease 0.15 zoom 0.8 xpos 0.1 ypos 0.45
        pause (0.05)
        repeat
        
    show kulak2_LW0607:
        zoom 0.1
        xpos 0.6
        ypos 0.45
        pause (0.05)
        ease 0.15 zoom 0.8 xpos 0.5 ypos 0.45
        repeat
    
    play sound_loop2 sfx_punch_washstand
    pause (0.2)
    play sound_loop3 sfx_punch_washstand
    
    $ renpy.pause (0.3)
    
    $ _window_show(dissolve)
    skt "ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA, ORA!"
    
    show Fight_Ddv_Dun_png with dspr
    play sound_loop Ora_Muda_LW0607
    
    show skitpio1 at center:
        ypos 1.1
        xpos 0.5
        zoom 1.2
        ease 0.2 zoom 1.5 xpos 0.5 ypos 1.0
        
    show skitpio1 at center:
        ypos 1.1
        xpos 0.5
        zoom 1.5
        ease 0.1 xpos 0.53 ypos 1.13
        ease 0.1 xpos 0.5 ypos 1.1
        ease 0.1 xpos 0.47 ypos 1.07
        ease 0.1 xpos 0.5 ypos 1.1
        repeat
        
    show dlya_ebala_LW0607 behind Fight_Ddv_Dun_png:
        xpos 2.0
        ypos 2.0
        ease 0.1 xpos 0.1 ypos -0.0
        pause (0.10)
        ease 0.1 xpos 2.0 ypos 2.0
        pause (0.1)
        repeat
        
    show dlya_ebalaleft_LW0607 behind Fight_Ddv_Dun_png:
        xpos -2.0
        ypos 1.5
        pause (0.1)
        ease 0.1 xpos -0.1 ypos -0.0
        pause (0.10)
        ease 0.1 xpos -2.0 ypos 1.5
        repeat
        
    show kulak_LW0607:
        zoom 0.1
        xpos 0.3
        ypos 0.65
        ease 0.15 zoom 0.8 xpos 0.1 ypos 0.65
        pause (0.05)
        repeat
        
    show kulak2_LW0607:
        zoom 0.1
        xpos 0.6
        ypos 0.65
        pause (0.05)
        ease 0.15 zoom 0.8 xpos 0.5 ypos 0.65
        repeat
    
    $ renpy.pause (0.3)
    
    skt "MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA, MUDA!"

    $ _window_hide(dissolve)
    
    stop sound_loop fadeout 2
    stop sound_loop2 fadeout 2
    stop sound_loop3 fadeout 2
    hide Fight_Ddv_Dun_png
    hide kulak_LW0607
    hide kulak2_LW0607
    hide dlya_ebala_LW0607
    hide dlya_ebalaleft_LW0607
    with dissolve
    
    show skitpio1 at center:
        ypos 1.1
        xpos 0.5
        zoom 1.5
        ease 0.8 zoom 0.6 xpos 0.5 ypos 1.0
    
    $ _window_show(dissolve)
    skt "Получай, Колд-Дио!"
    $ _window_hide(dissolve)
    
    play sound JoJo_vsk_LW0607
    
    show skitpio1 at center:
        ypos 1.5
        xpos 0.5
        zoom 0.6
        ease 0.4 zoom 1.6 xpos 0.5 ypos 1.1
        
    show kulak_LW0607:
        zoom 0.2
        xpos 0.4
        ypos 0.5
        ease 0.4 zoom 1.5 xpos 0.15 ypos 0.0
    play sound3 sfx_punch_washstand
    
    $ renpy.pause (0.3)
    hide kulak_LW0607 with dspr
    
    play sound2 sfx_body_bump
    with vpunch
    with ed_flash_red
    show blink
    
    $ _window_show(dissolve)
    "Скит разъебал малолетку просто в щепки!" with vpunch
    $ _window_hide(dissolve)
    scene black
    cld "Лысый{w=0.2}.{w=0.2}.{w=0.2}."
    "Колд помирал от причинённого урона."
    cld "Скажи мне одно{w=0.2}.{w=0.2}.{w=0.2}."
    cld "Почему ты нас начал оскать с казахом?" with vpunch
    scene domext
    show skitpio
    show unblink
    "Колд кинул последний взгляд на Диму."
    skt "Всё просто."
    skt "Вы конченные малолетки." with vpunch
    cld "Да пошёл ты{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    cld "Многолетка{w=0.2}.{w=0.2}.{w=0.2}."
    window hide
    stop music
    play sound sfx_punch_washstand
    show dark_LW0607
    show blood_LW0607
    with vpunch
    pause 1
    play sound coldazvuk
    pause 4.3
    scene black
    pause 2
    $ MND_Chapter("От лица Скита:")
    play music Death_Note_theme_LW0607 fadein 2
    scene domext with ed_night_dis
    skt "Минус одна малолетка."
    vchn "Жесткий ты тип,{w=0.2} однако." with vpunch
    "Скит обернулся."
    window hide
    show bergennorm:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'bergennorm'
        parallel:
            ypos 2.0 
            linear 0.80 ypos 1.0 
    with Pause(0.90)
    show bergennorm:
        ypos 1.0
    window show
    skt "Какой есть." with vpunch
    skt "Вовремя ты."
    vchn "Как успел." with vpunch
    "Передразнил Скита Вечный."
    skt "У меня для тебя подарок."
    vchn "Я в предвкушении."
    skt "Пошли на хату."
    skt "Она ждёт тебя там."
    vchn "Я походу понял,{w=0.2} про кого ты говоришь."
    skt "Ну тогда не будем медлить!"
    skt "Ток ты по моей команде заходи."
    skt "Я хочу её удивить."
    vchn "А она нас с окон не увидела ещё?"
    skt "У меня они на другую сторону выходят."
    vchn "Ну,{w=0.2} тогда погнали,{w=0.2} хуле."
    play sound door_open
    scene domint
    show vasilisa at right
    with ed_lap
    vas "И как всё прошло?" with vpunch
    "С ходу начала газовать Василиса."
    "Видно,{w=0.2} уже пришла в себя."
    skt "С переменным успехом."
    skt "Спасти Ракуна не удалось."
    skt "Однако малолетку я эту забил."
    skt "До смерти."
    vas "Ебать." with vpunch
    skt "А ещё у меня для тебя сюрприз."
    vas "Какой?"
    skt "Заходи давай,{w=0.2} ало."
    "И после этих слов в хату залетает Вечный."
    window hide
    play sound door_open
    show bergennorm:
        default subpixel True 
        parallel:
            Null(473.0, 712.0)
            'bergennorm'
        parallel:
            ypos 2.0 
            linear 0.80 ypos 1.0 
    with Pause(0.90)
    show bergennorm:
        ypos 1.0
    window show
    vas "МИША!" with vpunch
    vchn "ХЗ КАК ТЕБЯ ЗВАТЬ!" with vpunch
    "Василиса крепко сжала Вечного в обьятиях."
    "Тот,{w=0.2} отойдя от шока,{w=0.2} сделал то же самое."
    "А Димас смотрел на это как смотрит отец на своего сына."
    "С пониманием."
    vas "Мне столько всего тебе рассказать надо!" with vpunch
    vchn "Успеешь ещё."
    vchn "Димас,{w=0.2} есть чё пожрать?"
    skt "Есть бигмак."
    skt "Он,{w=0.2} правда,{w=0.2} с полудня лежит в холодосе."
    vchn "Сойдёт."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene ineony
    show deadlylxrd at right
    with ed_night_dis
    lxrd "Мы потеряли Колда." with vpunch
    lxrd "Я посмотрел по ip камерам с Новошахтинска."
    lxrd "Говорилось ему блять,{w=0.2} что не стоит в соло на такого бегемота лезть!" with vpunch
    nn "Это прискорбно."
    nn "У меня нет его образца ДНК,{w=0.2} дабы сделать клон."
    nn "ДНК Вечного тоже голимый оказался."
    lxrd "Может,{w=0.2} у образцов срок действия заканчивается?"
    nn "Может быть."
    nn "А из него клоны-то пиздатые бы вышли!" with vpunch
    lxrd "Но это не самое главное сейчас."
    lxrd "Посмотри на экран."
    "Вадимка отмотал на нужный таймкод."
    "Рядом со Скитом чиллил Вечный."
    nn "Ты тоже это видишь?"
    lxrd "Ага."
    lxrd "Кароче говоря,{w=0.2} у нас завёлся {b}IMPOSTER{/b}." with vpunch
    nn "Это суперприскорбно{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "Но у меня есть идея как их обоих нейтрализовать."
    nn "И как же?"
    lxrd "Нужно связаться с одним человеком."
    lxrd "Он ща в подполье."
    lxrd "Я пойду один." with vpunch
    nn "Я походу понял,{w=0.2} про кого ты."
    lxrd "Думаешь о том же,{w=0.2} о чём и я?"
    nn "Именно."
    nn "Пизда им." with vpunch
    nn "Но ты не торопись." with vpunch
    nn "Ещё нужно кое-что доделать,{w=0.2} дабы быть уверенным в его соглашении."
    nn "Только впечатлив его,{w=0.2} мы сможем добиться его согласия."
    nn "Просто так -{w} он не влезет в это дело."
    nn "Никак." with vpunch
    lxrd "Я понимаю."
    lxrd "И что ты предлагаешь?"
    nn "Я досовершенствую систему клонирования."
    nn "Результат увидишь сам."
    lxrd "Всё таки стоит ломануть сейф."
    lxrd "Похуй уже,{w=0.2} что там может быть заминировано." with vpunch
    nn "С этим позже."
    lxrd "Этот человек умеет ломать такие замки."
    lxrd "Так что..."
    nn "Да." with vpunch
    nn "Сначала клоны."
    lxrd "Я тебя услышал."
    stop music fadeout 5
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Колда:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music oni fadein 2
    scene domext with ed_night_dis
    "Колд встал и отряхнулся."
    cld "Сука..." with vpunch
    "Боль пронзила всё тело в попытке встать."
    cld "Многолетка..." with vpunch
    "Скит ебашил по болевым точкам."
    "На районе его научили драться."
    "Пускай,{w=0.2} он и не дрался за район..."
    "Но неумехой он не был."
    "В итоге он нанёс чисто болевой дамаг Колду."
    cld "Что б я ещё хоть раз..."
    cld "Учавствовал в подобном..."
    "Очко малолетки подпекало."
    "Но ничего не оставалось,{w=0.2} кроме как..."
    cld "Осталось дождаться ночи." with vpunch
    cld "А там и спросим с Вечного."
    cld "Его план,{w=0.2} конечно,{w=0.2} ахуенный..."
    cld "Но мне такое не по душе."
    play sound fb
    scene coldbuhaet
    show overlay aw_memory_back_1
    with flash
    vchn "Пока Вадимка в толчке -{w} нам нужно разработать план."
    cld "Что ты предлагаешь?"
    vchn "Я на хорошем счету у Скита."
    vchn "Нужно его немного расшатать,{w=0.2} дабы я смог поднять уровень доверия выше,{w=0.2} помогая ему."
    cld "И как?"
    vchn "Легко." with vpunch
    vchn "У Неони в планах создать лабараторию по клонированию типов."
    vchn "Днк Ракуна у тебя где-{w=0.2}то был."
    vchn "Вот и сделаешь его клон,{w=0.2} дабы шантажить Скита."
    vchn "Он про клона знать не будет."
    vchn "Будет думать,{w=0.2} что это ориг."
    vchn "И всё!" with vpunch
    vchn "Дело в шляпе."
    vchn "Патрон один возьми на всякий."
    vchn "Не то вторым Скита ваншотнешь."
    vchn "Убить он тебя не сможет в любом случае."
    vchn "Подберёшься близко -{w} начинай давить на него."
    vchn "Дальше будешь импровизировать."
    cld "Почему я?" with vpunch
    "Единственный вопрос,{w=0.2} который не давал Колду покоя."
    vchn "Больше некому." with vpunch
    "Лишь кратко бросил Вечный,{w=0.2} после чего пафосно ушёл в другую комнату за подиком или чем-{w=0.2}то ещё."
    cld "Легко сказать..."
    "Колду ничего не оставалось,{w=0.2} кроме как попробовать провернуть эту афёру."
    play sound fb
    scene domext with flash
    cld "Такая судьба у нас..."
    cld "Нелёгкая..."
    cld "Ха." with vpunch
    "После этих слов,{w=0.2} Колд принялся ждать ночи."
    "Больше ничего не оставалось делать."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Василисы:")
    hide zatemnenie with dissolve2
    play sound fb
    scene himori with flash
    him "И зачем убегала?" with vpunch
    th2 "Очевидно,{w=0.2} зачем."
    ivt1 "Подальше от тебя,{w=0.2} тварь." with vpunch
    him "Ты не принимаешь препараты."
    vas "Они делают хуже." with vpunch
    vas "Я уже говорила."
    him "Да ну?" with vpunch
    him "Как по мне,{w=0.2} ты начала идти на поправку."
    ivt1 "АХАХА..." with vpunch
    him "Но ты снова бросила их пить."
    vas "Я так не могу уже." with vpunch
    vas "Мне просто тяжело."
    vas "Сделай одолжение."
    ivt1 "Сделай автоназию." with vpunch
    vas "Благодарны будем обе."
    him "Законодательство не позволяет."
    him "Но есть один способ..." with vpunch
    "В глазах Василисы появилась надежда."
    him "Но сперва ты мне всё расскажешь." with vpunch
    window hide
    play sound2 aw_psy_eff_1
    stop music 
    play sound aw_psy_eff_6
    scene bg aw_f_cor_1
    show aw_afd_dth1
    show aw_afd_ky1
    with flash_fast_red2
    $ renpy.pause(5, hard=True)
    stop sound fadeout 20
    him "Не слушай их."
    him "Они сделают хуже." with vpunch
    "Голова Василисы была готова взорваться."
    "Голоса выметали все мысли."
    "Пульсация в висках буквально капала на мозги."
    show blink
    "Не в силах сопротивляться голосам,{w=0.2} Василиса провалилась во тьму."
    "И когда всё это закончится?"
    show zatemnenie with dissolve2
    $ MND_Chapter("Конец третьего картера...")
    hide zatemnenie with dissolve2
    return

label aktfour:
    scene black with ed_night_dis
    play music living
    scene domintnight
    with ed_night_dis
    show zatemnenie with dissolve2
    $ MND_Chapter("The Carter Four:")
    $ MND_Chapter("Rotten Diary")
    hide zatemnenie with dissolve2
    nvlbazar "Я сидел и просто харкал в потолок, ожидая, что харча начнёт падать вниз - мне в кармашек."
    nvlbazar "Просто делать было больше нечего."
    nvlbazar "И тут мне на мобилу приходит сообщение в тг."
    nvl clear
    nvlcld "Жду тебя снаружи. Надо встретиться."
    nvl clear
    nvlbazar "На дворе была уже ночь."
    nvlbazar "Скит и Василиса уже легли спать."
    nvlbazar "Один я, долбоёб, хуйнёй маялся."
    nvlbazar "Делать было нечего."
    nvlbazar "Пришлось выходить."
    nvl clear
    play sound door_open
    scene nightdvor
    show coldsprnight
    with ed_lap
    vchn "Здарова. Ну так чё там у тебя?"
    cld "Как продвигается наша миссия?"
    vchn "Пока всё идёт по плану."
    vchn "Скит ещё не подозревает, в какой он заднице."
    cld "Это хорошо, бро."
    cld "Но меня терзают смутные сомнения насчёт этой Василисы."
    vchn "Она же вроде клон, что сделал казах, не?"
    cld "Это понятно."
    cld "Я про её истинно-арийское происхождение."
    cld "Никто не знает, кто она и откуда."
    vchn "Да я всё понимаю, братиш."
    vchn "Просто загвоздка вот в чём - она ничего не помнит об оригинале."
    cld "Это она тебе так сказала?"
    "И тут Вечный понял, что он редкосный идиот."
    cld "И у тебя не закралось сомнений по поводу ровности её базара?"
    vchn "Теперь закрались."
    vchn "Но в лоб спрашивать бесполезно, братиш, сам же знаешь."
    cld "Тут ты прав."
    cld "Но у меня и на этот счёт есть идея."
    cld "Она может и не рассказывала, но могла записать."
    vchn "Мобилы у неё нет."
    vchn "Это я бы точно заметил."
    cld "Необязательно на мобиле."
    cld "Мб нашла дома у скита ежедневник и начала выплёскивать туда все свои переживания."
    cld "Пока меня ебашил Скит, сука."
    vchn "А ведь ты прав."
    vchn "И чё я раньше об этом не подумал?"
    cld "Меня тот же вопрос мучает."
    vchn "Как тело твоё кста?"
    cld "Этот сосунок не смог дамага нанести толком."
    cld "Петушара в тягу ебашил и по нервам."
    cld "Боль была жесткая."
    cld "Я притворился мёртвым, лишь бы лысая успокоилась."
    cld "И нахуя ты мне сказал один патрон взять?"
    vchn "Ты бы ему просто башку отстрелил."
    vchn "Ограничимся одним клоном Ракуна пока."
    cld "Сука, ты ответишь за эту потасовку."
    cld "Мог бы и помочь."
    vchn "Я бы точно спалился перед Димочкой."
    vchn "Очевидно же."
    vchn "Я, конечно, догадывался, что Скитовского научили драться на районе, но чтоб так..."
    vchn "Он же лохом ебаным кажется со стороны."
    vchn "Это ослажняет нашу задачу, братиш."
    cld "Да кто ж спорит."
    cld "Осталось надеяться, что Казах и Вадимка придут и отомстят за меня."
    cld "Они по-любому по камерам мою <<смерть>> видели."
    cld "Тебе пока не стоит попадаться им на глаза."
    cld "Как только нароешь инфы про эту <<Василису>>, делай ноги оттуда."
    cld "Как можно быстрее."
    cld "Почуят неладное - нам обоим пизда."
    cld "С обоих фронтов, бро."
    cld "Шутки закончились."
    cld "Пора делать реальные дела."
    vchn "Я тебя услышал."
    vchn "Ещё раз сорян за Лысую."
    vchn "Я рили такого говна не ждал."
    cld "Удачи."
    play sound door_open
    scene domintnight with ed_lap
    "И они разошлись."
    "Вечный пошёл домой к Скиту - рыть инфу о Василисе."
    "Пошарив по столу, за газетами он нашёл нечто одалённо напиманающее дневник."
    window hide
    play sound dostal
    show diary:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'diary'
        parallel:
            ypos 2.0 
            linear 0.50 ypos 1.0 
    with Pause(0.60)
    show diary:
        ypos 1.0 
    vchn "Походу, это он и есть."
    vchn "Тот самый дневник Василисы."
    hide diary
    play sound ubralstvol
    show diary:
        ypos 0.0
        ease 0.5 ypos 1.5

    pause 0.6
    hide diary
    "Открыв его, он увидел на первой странице единственную надпись большим шрифтом."
    show zatemnenie with dissolve2
    $ MND_Chapter("Слушай сюда, дорогой мой.")
    $ MND_Chapter("Пока не поздно, положи его на место.")
    $ MND_Chapter("Иначе сделаю с тобой то,")
    $ MND_Chapter("Что не успела тогда в туалете.")
    hide zatemnenie with dissolve2
    stop music fadeout 5
    vchn "Это Скиту адресовано чтоль?"
    vchn "Лично я провалами в памяти не страдаю."
    vchn "Такое бы точно не забыл."
    vchn "Ха. Надо будет у Скита спросить потом, хы."
    play music saveme
    nvl clear
    nvlvas "Дорогой дневник и бла-бла-бла."
    nvl clear
    nvlvas "Я не могу больше молчать."
    nvlvas "Рассказат Скитецкому всю правду = убить себя."
    nvlvas "Закопать глубже некуда."
    nvlvas "Вечному тоже не стоит."
    nvlvas "Он меня возненавидит."
    nvl clear
    nvlvhcn "Какое интригующее начало..."
    nvl clear
    nvlvas "Я всё прекрасно помню."
    nvlvas "Это буквально мешает мне жить."
    nvlvas "Я сделана из натуральной психопатки."
    nvlvas "Не зря Неоня её прикопал на пустыре."
    nvl clear
    nvlvas "С самого детства были проблемы с социализацией."
    nvlvas "Меня не просто считали странной..."
    nvlvas "Буквально издевались."
    nvl clear
    nvlvas "Ещё в школе... Всегда была изгоем..."
    nvlvas "Однако апогеем всей этой истории стал переломный момент в детском лагере <<Совёнок>>."
    nvl clear
    nvlvhcn "Бля а не тот ли это лагерь, в который нас отправил Дима Скит с пацанвой?"
    nvlvhcn "История приобретает новые обороты..."
    nvlvhcn "Если всё действительно так связано..."
    nvl clear
    stop music fadeout 3
    vchn "В пизду."
    vchn "Не хочу об этом думать."
    play music prxjek
    "Вечный захлопнул дневник и убрал на место."
    vchn "Я силишком трезвый для этого дерьма."
    vchn "Надо пойти проветриться."
    vchn "Не могу я эту чушь на горячую голову читать."
    "Вечный проверил счёт в <<сбербанк онлайн>> и увидел там пару соток."
    vchn "На малыша не хватит... Придётся брать коктейльчики..."
    play sound door_open
    scene nightdvor with ed_lap
    "Он накинул свою любимую чёрную рубашку и, взяв <<Brusko Minican Plus>>, отправился на улицу."
    "Ночной Новошахтинск опьяняюще действовал на разум Вечного."
    "Он сделал глубокую тягу на <<миникане>> с жижкой <<Brusko Таёжный Морс 50мг>> и начал релаксировать."
    "Прохладный весенний ветер снимал нарастающее напряжение."
    scene nvnight with ed_lap
    vchn "Подумать только... Если всё реально НАСТОЛЬКО связано..."
    vchn "Это же пиздос..."
    vchn "Скит не так прост, каким кажется."
    vchn "И это очень парашно по отношению к нашему плану."
    vchn "Если всё пойдёт по пизде..."
    "Вечный решил не думать о всём этом говне, после чего зашел в шарашку и, взяв там три шота <<аналога лысого малыша>>, отправился обратно."
    scene nightdvor with ed_lap
    "По пути он опрокинул в себя один из лимонных шотов."
    "Вернулся обратно он достаточно быстро, ведь ночь-то не резиновая."
    play sound door_open
    scene domintnight
    show vasilisanight
    with ed_lap
    "Когда он зашёл в хату, его встретила Василиса."
    vas "Ну и куда это мы уходим в два часа ночи?"
    vas "А?"
    vas "К тёлкам своим небось бегаешь?"
    "Вечный немного сильно так прихуел с резкого приступа <<женской логики>>."
    vchn "Я ходил..."
    vchn "За бухлом."
    vas "Тебе настолько херово, что ты начал пить?"
    "Василиса прониклась жалостью к нему."
    "В то же время Вечный тихо угорал внутри своего разума с этого <<тувинского цирка>>."
    "Василиса нежно обняла Вечного."
    vas "Бедный мой..."
    vas "Погоди."
    vas "У тебя ещё осталось бухло?"
    "Вечный сразу всё понял."
    "Не стал отнекиваться. В соло бухать ему никогда не нравилось."
    "В такие моменты начинает <<свистеть фляга>>."
    "Поэтому он отдал третий шот Василисе."
    "У него остался второй шот."
    hide vasilisanight
    window hide
    show vasilisanight:
        default subpixel True 
        parallel:
            Null(640.0, 640.0)
            'vasilisanight'
        parallel:
            xpos 0.5 
            linear 1.00 xpos -0.3 
            linear 1.00 xpos 1.3 
            linear 1.00 xpos 0.5 
            repeat
    window show
    vas "Ур-а-а-а!"
    vas "Пойдём буха-а-а-ать!"
    "Кружилась вокруг него Василиса."
    "Вечный почти словил вертолёты."
    hide vasilisanight
    window hide
    show vasilisanight:
        default subpixel True 
        parallel:
            Null(640.0, 640.0)
            'vasilisanight'
        parallel:
            xpos -0.3 
            linear 0.39 xpos 0.5 
    with Pause(0.60)
    show vasilisanight:
        xpos 0.5 
    window show
    vchn "УСПОКОЙСЯ, БЛЯДЬ!"
    "Почти криком осадил её Вечный."
    vas "Ну ладно. Чё бухтеть-то..."
    play sound door_open
    scene kuhnyanight
    show vasilisanight
    with ed_lap
    "После пары секунд затупа они пошли на кухню."
    "Думать об этом было поздно, но всё же..."
    "Не разбудили ли они Скитецкого?"
    "Вечному уже влом было бы идти в шарашку за четвёртым шотом."
    "Да и бабки кончились. Капитально."
    vchn "Ну и мусорка сука."
    "И тут Василиса мастерски пародирует один малоизвестный пёрл."
    window hide
    play sound ozon
    pause 5
    vchn "Хы."
    stop music fadeout 5
    "Эта фраза отдалась эхом в голове Вечного."
    "Причем именно оригинал."
    "Голосом Озона."
    "Ну а потом они начали опрокидывать оставшиеся шоты."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Димы:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    scene domint with ed_night_dis
    play music mnd_gluhar_utro
    "Дело было 18 июня."
    "За окном шёл дождь."
    "Дима лежал и пердел у себя на диване дома в Новошахтинске."
    "Ковяряясь в носу, он думал о вечном."
    "Как он в детстве металолом пиздил со склада..."
    "Как он в первый раз засадил свой dick одной прекрасной девочке..."
    "Он уже и не помнит, насколько давно это было."
    "Ведь после того раза ему больше не перепадало."
    "По-началу он держался молодцом и тестировал прошивки, работал на складе..."
    "Потом его это заебало и он ушел со склада работать на фабрику и начал оскать школьников в телеграме."
    "Он извергал столько желчи, сколько нельзя увидеть в реальности."
    "Это всё вам для понимания того, насколько Скит едкая сука."
    "А ведь по-началу всё было хорошо..."
    "Но он сам выбрал свой путь."
    "Многолетка ебучая."
    stop music fadeout 3
    "Скит думал, что ничего не могло испортить этот день."
    "И он ошибался."
    play sound door_zvonok
    play music madelina fadein 2
    skt "Да сука..."
    skt "Я же никого сегодня не жду..."
    skt "Странно всё это..."
    "И Скит поплёлся открывать дверь."
    "Он только подошёл к двери, как вдруг..."
    play music madelina1
    play sound door_break
    scene padik
    show morozko
    mrz "С НОВЫМ ГОДОМ, СУКА!" with vpunch
    window hide
    show dlya_ebalaMVWWW777:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'dlya_ebalaMVWWW777'
        parallel:
            pos (1.0, 1.5) 
            linear 0.20 pos (0.5, 1.0) 
    with Pause(0.30)
    show dlya_ebalaMVWWW777:
        pos (0.5, 1.0) 
    play sound sfx_punch_washstand
    hide dlya_ebalaMVWWW777
    show dlya_ebalaMVWWW777:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'dlya_ebalaMVWWW777'
        parallel:
            pos (0.5, 1.0) 
            linear 0.20 pos (1.0, 1.6) 
    with Pause(0.30)
    show dlya_ebalaMVWWW777:
        pos (1.0, 1.6) 
    hide morozko
    show morozko:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    play sound sfx_body_bump
    "Скит ударом уложил нахуй это <<чудо>> и пытался побежать вниз."
    window hide
    hide morozko
    show lordsprclon4 at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    window show
    hide lordsprclon4
    show lordsprclon4
    "Но с лестницы сверху вышел... {w}Прошу прощения.{w} На лестничную клетку,{w=0.2} ебанув тройное сальто,{w=0.2} завалился новый клон Вадима Морозова."
    lxrd1 "ТЕБЕ ПИЗДЕЦ!"
    "Скит не растерялся и въебал в дыхло новому клону."
    window hide
    show dlya_ebalaMVWWW777:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'dlya_ebalaMVWWW777'
        parallel:
            pos (1.0, 1.5) 
            linear 0.20 pos (0.5, 1.0) 
    with Pause(0.30)
    show dlya_ebalaMVWWW777:
        pos (0.5, 1.0) 
    play sound sfx_punch_washstand
    hide dlya_ebalaMVWWW777
    show dlya_ebalaMVWWW777:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'dlya_ebalaMVWWW777'
        parallel:
            pos (0.5, 1.0) 
            linear 0.20 pos (1.0, 1.6) 
    with Pause(0.30)
    show dlya_ebalaMVWWW777:
        pos (1.0, 1.6) 
    hide lordsprclon4
    show lordsprclon4:
        anchor (0.5, 0.5)
        pos (0.5, 0.5)
        ease 1.0 rotate 150 xpos 0.2 ypos 2.0
    play sound sfx_body_bump
    play sound2 vozduh
    "Выдался отличный момент съебаться, чем Дима и воспользовался."
    "Он с разбегу рванул по лестнице вниз."
    play sound door_break
    play ambience rain_out fadein 2
    scene domext at ed_running_fast
    show doshd
    with vpunch
    skt "Где там моя родная десяточка..."
    play sound tazik1
    play ambience rain_in
    scene traphata
    show doshd
    with vpunch
    skt "Осталось завести."
    window hide
    stop ambience fadeout 3
    play sound vaz
    pause 5
    play sound bochka
    with vpunch
    pause 4
    window hide
    play sound vaz
    pause 3
    stop sound
    play ambience dviglo
    window hide
    scene traphata at ed_bus_move
    show doshd
    with vpunch
    play sound attack_1
    pause 2
    "И Скит поехал подальше от этого места."
    scene nmall at ed_bus_move
    show doshd
    with ed_lap
    "Дмитрий гнал под 120 по Новошохтинску на своём некро-ведре."
    "Из хрипящих динамиков доносился до ушей старый добрый русский транс."
    "Движок десятки пердел,{w=0.2} хрипел,{w=0.2} умирал,{w=0.2} но,{w=0.2} сука,{w=0.2} работал."
    "Самое главное -{w=0.2} что ехал."
    "Иначе Димка бы познал кару Морозки."
    "И тогда бы ему было пиздец как грустно."
    window hide
    pause 1
    "Куда он едет?"
    play sound herznaet
    window hide
    pause 1.6
    "Димка повернул в сторону хаты своей бывшей."
    "Как говориться -{w=0.2} навалил боком под плёнку на Львовский переулок, 9."
    "Вот только не смог он до неё доехать{w=0.2}.{w=0.2}.{w=0.2}."
    pause 2
    "В конце переулка Димка увидел что-то странное,{w=0.2} но не разглядел,{w=0.2} что это."
    "А это было{w=0.2}.{w=0.2}.{w=0.2}."
    play sound fb
    stop ambience
    scene tank
    show deadlylxrd at left
    show doshd
    with flash
    lxrd "Опа{w=0.2}.{w=0.2}.{w=0.2}."
    lxrd "А вот и наш клиент."
    "Вадимка зарядил крупнокалиберный снаряд в дуло."
    lxrd "Жаль конечно этого добряка."
    lxrd "Но ничего не поделаешь."
    window hide
    pause 2
    stop music fadeout 3
    lxrd "Прощай, лысая{w=0.2}.{w=0.2}.{w=0.2}."
    "И Вадимка нажал на кнопку выстрела."
    play sound fb
    scene nmall at ed_bus_move
    show doshd
    with flash
    play ambience dviglo fadein 2
    skt "Что там такое бля?"
    skt "Не вижу нихуя..."
    with flash
    stop music
    stop sound
    stop ambience fadeout 6
    scene black
    $ renpy.movie_cutscene('source/pizdamashine.webm')
    window hide
    play sound probitie1
    pause 2
    scene domintnight
    play sound vozduh
    show unblink
    pause 1.5
    skt "ЕБАТЬ!"
    "Скит немного сильно так ахуел от своего сна."
    skt "Присниться же такое..."
    skt "Надо на кухню сходить - водички глотнуть."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Неони:")
    hide zatemnenie with dissolve2
    scene black with ed_night_dis
    play music outofit0 fadein 2
    scene laba with ed_night_dis
    nvl clear
    nvlbazar "Он стоял напротив колбы в своей лаборатории."
    nvlbazar "Делать было нехуй."
    nvlbazar "Только ждать Вадимку."
    nvlbazar "Он должен ЭТО видеть."
    nvl clear
    "В лабу заскакивает Вадос."
    window hide
    play sound door_open
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            xpos 3.0 
            linear 0.80 xpos 0.75 
    with Pause(0.90)
    show deadlylxrd:
        xpos 0.75
    window show 
    lxrd "Что на этот раз?"
    lxrd "Снова свои детские секс-игрушки будешь демонстрироват в деле?"
    lxrd "Типа ОЙ СМАРИ ВАДЯ, КАКОЙ МАЛЕНЬКИЙ СТРАПОН, АХАХА?"
    window hide
    play sound smehb1
    pause 3
    "Вадимка сам проорал со своего пёрла."
    lxrd "Меня это уже заебало, веришь?"
    "Говорил он сквозь смех."
    nn "На этот раз - кое-что грандиознее."
    nn "Смари."
    window hide
    show lordsprclon4 at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    window show
    "Стенка колбы отодвинулась, после чего оттуда в знакомой манере вылетело чудо, отдалённо напоминающее Канеки."
    play sound gul
    lxrd2 "Ащихитео..."
    window hide
    scene laba
    show deadlylxrd
    show lordsprclon4 at right
    with flash_fast2
    play sound smehb2
    hide deadlylxrd
    show deadlylxrd:
        default subpixel True xpos 0.25 
        parallel:
            Null(600.0, 720.0)
            'deadlylxrd'
        parallel:
            xzoom 1 
            linear 0.20 xzoom 2 
            linear 0.20 xzoom 1 
            linear 0.60 xzoom 2 
            linear 0.20 xzoom 1 
        parallel:
            yzoom 1 
            linear 0.20 yzoom 1 
            linear 0.40 yzoom 2 
            linear 0.20 yzoom 1 
            linear 0.20 yzoom 2 
            linear 0.20 yzoom 1 
    with Pause(1.30)
    show deadlylxrd:
        xzoom 1 yzoom 1 
    hide deadlylxrd
    show deadlylxrd:
        default subpixel True xpos 0.25 
        parallel:
            Null(600.0, 720.0)
            'deadlylxrd'
        parallel:
            xzoom 1 
            linear 0.20 xzoom 2 
            linear 0.20 xzoom 1 
            linear 0.60 xzoom 2 
            linear 0.20 xzoom 1 
        parallel:
            yzoom 1 
            linear 0.20 yzoom 1 
            linear 0.40 yzoom 2 
            linear 0.20 yzoom 1 
            linear 0.20 yzoom 2 
            linear 0.20 yzoom 1 
    with Pause(1.30)
    show deadlylxrd:
        xzoom 1 yzoom 1 
    window show
    "Вадимка проорал с этого чуда."
    lxrd "Курганский Гуль - это, конечно, ахуительно..."
    "Говорил он сквозь смех."
    lxrd "Но я видал и круче."
    nn "На этот случай у меня припасено особое оружие."
    "Стенка уже другой колбы отодвинулась в сторону, дабы не мешать эффектному появлению... Этого <<чуда>>."
    hide lordsprclon4
    hide deadlylxrd
    $ renpy.movie_cutscene('source/topgamer.webm')
    window hide
    show deadlylxrd at right
    show ddoser at center:
        xcenter -0.4 ycenter 0.5 rotate 0
        easein 0.4 xcenter 0.5 rotate 360
        ease 0.05 zoom 1.3
        ease 0.05 zoom 1.0
        ease 0.1 rotate -360
    $ renpy.pause (0.5)
    window show
    "В лабу, порвав футболку за 25к, влетело создание, отдалённо напоминающее Вадима Морозова."
    window hide
    play sound ddos
    pause 21
    play sound stul
    show kreslo:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'kreslo'
        parallel:
            matrixtransform ScaleMatrix(0.3, 0.3, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
            linear 0.59 matrixtransform ScaleMatrix(2.0, 2.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
    with Pause(0.39)
    show kreslo:
        matrixtransform ScaleMatrix(2.0, 2.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0) 
    play sound2 sfx_punch_washstand
    scene laba
    show deadlylxrd at right
    show ddoser
    show dark_LW0607
    show blood_LW0607
    with flash_fast_red2
    play ambience huevo
    nn "Ай, сука..."
    "Топгеймер кинул стулом в Казаха."
    "Тот аж ахуел."
    window hide
    play sound ddos1
    stop ambience fadeout 2
    hide dark_LW0607
    hide blood_LW0607
    with dissolve2
    pause 11
    play sound ddos2
    pause 16
    hide ddoser
    hide deadlylxrd
    play sound nitroblya
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            pos (0.75, 1.0) rotate 0.0 
            linear 0.16 pos (0.75, 1.0) rotate 0.0 
            linear 0.90 pos (0.5, 3.0) rotate -180.0 
    show ddoser:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'ddoser'
        parallel:
            xpos 0.5 
            linear 0.16 xpos 0.75 
            linear 0.60 xpos 2.0 
    with Pause(0.90)
    show deadlylxrd:
        pos (0.5, 3.0) rotate 180.0 
    show ddoser:
        xpos 2.0 
    play sound2 sfx_body_bump
    pause 1
    hide deadlylxrd
    play sound2 uebalsya
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
            'deadlylxrd'
        parallel:
            ypos 2.0 
            linear 0.68 ypos 1.5 
            linear 0.20 ypos 1.2 
        parallel:
            rotate 90.0 
            linear 0.88 rotate 0.0 
    with Pause(0.98)
    show deadlylxrd:
        ypos 1.2 rotate 0.0 
    pause 1.6
    window show
    "Топгеймер со свистом шин улетел из лабы, попутно сбив Вадима Морозова."
    lxrd "Это чё такое, придурок?"
    lxrd "С хера ли клоны такие буйные пошли?"
    lxrd "Он ещё и съебался..."
    stop music fadeout 5
    nn "Похуй."
    nn "У всех бывают неудачные дни."
    nn "Но у меня остался ещё один сюрприз."
    window hide
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Иветты:")
    hide zatemnenie with dissolve2
    play music vampire
    scene black with ed_night_dis
    scene kk with ed_night_dis
    nvl clear
    nvlbazar "Она сидела в абсолютных потёмках."
    nvlbazar "Видны были лишь очертания бункера."
    nvlbazar "Того самого бункера, что стал её тюрьмой."
    nvl clear
    nvlbazar "А всё обострилось после разлуки с самым близким для неё человеком."
    nvlbazar "Иветта не могла легко этого вынести."
    nvlbazar "В начале своего заточения она пыталась разъебшить стены и сбежать, но..."
    nvlbazar "Это же не гипсокартон."
    nvl clear
    nvlbazar "Плотные бетонные стены, что поперёк натырканы арматурой, ослабляющей любые радиочастоты."
    nvlbazar "В общем, даже GSM тут не ловил."
    nvlbazar "Да и сам бункер находился достаточно глубоко под землёй."
    nvlbazar "Глубже лабы Казаха."
    nvl clear
    nvlbazar "Но - режущая уши тишина не могла длиться вечно."
    nvlbazar "И следом за открывшейся дверью, в бункер залетает Казах."
    nvl clear
    play sound door_open
    show kazahspr:
        default subpixel True 
        parallel:
            Null(726.0, 754.0)
            'kazahspr'
        parallel:
            xpos -0.3 
            linear 0.50 xpos 0.25 
    with Pause(0.60)
    show kazahspr:
        xpos 0.25 
    nn "Успокоилась?"
    ivt1 "Пошёл на хуй."
    nn "А ты не меняешься."
    ivt1 "Где Василиса?"
    ivt1 "Куда ты её дел?"
    nn "Спокойнее."
    nn "Я обещал вам отдельные тела - я своё обещание выполнил."
    nn "С вас спрос тоже был."
    nn "Василиса пока свою часть выполняет."
    nn "Хоть и со скрипом."
    nn "Ну а ты..."
    nn "Нет бы по-нормальному..."
    nn "Опять наши планы срываешь."
    ivt1 "Пошёл в жопу."
    ivt1 "Без Василисы я и палец-о-палец не ударю."
    nn "Ха."
    nn "Надолго ли тебя так хватит?"
    ivt1 "Посмотришь."
    window hide
    play sound door_open
    show deadlylxrd:
        default subpixel True 
        parallel:
            Null(726.0, 754.0)
            'deadlylxrd'
        parallel:
            xpos 1.3 
            linear 0.50 xpos 0.75 
    with Pause(0.60)
    show deadlylxrd:
        xpos 0.75 
    "В комнату залетает Вадим Морозов."
    lxrd "Это и есть твой сюрприз?"
    nn "Нет."
    nn "Но это очень важный винтик в этом большом механизме."
    nn "Тебе стоит увидить её в действии."
    lxrd "Я смотрел записи с камер в клубе."
    lxrd "Это, видимо, она..."
    lxrd "Хотя я изначально думал, что это Василиса."
    nn "Это и есть Василиса."
    nn "Точнее - её альтер-эго."
    lxrd "Понял."
    lxrd "И как ты их разъеденил?"
    nn "Василису в клона поместил и всё."
    nn "Наплёл ей про смерть оригинала."
    nn "Она даже ничего не вспомнила."
    ivt1 "МРАЗЬ!"
    window hide
    play sound hark
    show harchok:
        default subpixel True xpos 0.2 
        parallel:
            Null(368.0, 411.0)
            'harchok'
        parallel:
            ypos 1.7 
            linear 0.21 ypos 0.5 xpos 0.2
    with Pause(0.60)
    show harchok:
        pos (0.2, 0.5) 
    window show
    "Смачный харчок полетел в ебло Казаху."
    window hide
    play sound smehb1
    hide deadlylxrd
    show deadlylxrd:
        default subpixel True xpos 0.75 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            ypos 1.0 xpos 0.75
            linear 0.80 ypos 1.1 
        parallel:
            rotate 0.0 
            linear 0.13 rotate 180.0 
            linear 0.14 rotate 0.0 
            linear 0.18 rotate 90.0 
            linear 0.21 rotate 270.0 
            linear 0.14 rotate 0.0 
    with Pause(0.90)
    show deadlylxrd:
        pos (0.75, 1.1) rotate 0.0 
    hide deadlylxrd
    show deadlylxrd:
        default subpixel True xpos 0.75 
        parallel:
            Null(500.0, 842.0)
            'deadlylxrd'
        parallel:
            ypos 1.0 xpos 0.75
            linear 0.80 ypos 1.1
        parallel:
            rotate 0.0 
            linear 0.13 rotate 180.0 
            linear 0.14 rotate 0.0 
            linear 0.18 rotate 90.0 
            linear 0.21 rotate 270.0 
            linear 0.14 rotate 0.0 
    with Pause(0.90)
    show deadlylxrd:
        pos (0.75, 1.1) rotate 0.0 
    pause 1
    "Вадимка чётко гоготнул с этой всей хуеты."
    window hide
    show harchok:
        subpixel True 
        pos (0.2, 0.5) 
        linear 0.24 pos (-0.3, 1.0) 
    with Pause(0.34)
    show harchok:
        pos (-0.3, 1.0) 
    window show
    "Казах вытер харочк с ебла."
    nn "Слушай сюда, блядь."
    nn "У тебя нет выбора - послать нас или помочь."
    nn "Жизнь твоей <<подруги>> - в твоих руках."
    lxrd "Тут он прав."
    lxrd "Так что заканчивай харкаться и давай уже делом займись блеааать."
    "Натужно протянул Вадимка."
    ivt1 "Знаете, что?"
    ivt1 "Идите нахуй оба."
    ivt1 "Малолетки конченные."
    "Вадимка и Казах смирили её жгучими взглядами."
    nn "Ты ещё передумаешь."
    ivt1 "Идите нахуй. Оба."
    window hide
    play sound door_open
    show kazahspr:
        subpixel True 
        ypos 1.0 
        linear 0.50 ypos 2.0 
    show deadlylxrd:
        subpixel True 
        ypos 1.1 
        linear 0.50 ypos 2.2 
    with Pause(0.60)
    show kazahspr:
        ypos 2.0 
    show deadlylxrd:
        ypos 2.2 
    window show
    "И они ушли. Нахуй. Оба."
    nvl clear
    nvlivt "Я осталсь думать, чё же делать дальше?"
    nvlivt "Порыскав по комнате, нашла люк."
    nvl clear
    play sound stmetal
    scene vent with ed_lap
    nvlivt "Вентиляционная шахта, значит..."
    nvlivt "Придётся поползать..."
    nvlivt "Как в старые добрые..."
    nvl clear
    window hide
    pause 2
    play sound stmetal
    scene laba with ed_lap
    th2 "Вот я и на месте."
    th2 "Осталось только найти выход."
    window hide
    pause 2
    "Иветта заметила странную деревянную дверь."
    "С подписью ПОСТОРОННИМ ВХОД ВОПСРЕЩЁН БЛЯ."
    ivt1 "И чё это значит?"
    "Любопытство взяло верх."
    play sound door_open
    play ambience adp fadein 2
    scene portal with ed_lap
    "Иветта заглянула в какое-то странное помещение."
    "Возле странного сооружения была табличка с надписью: <<Портал в Новошахтинск>>."
    th2 "Попробовать войти?"
    th2 "И где этот Новошахтинск..."
    stop music fadeout 6
    "Но шестое чувство между ног давало понять Иветте, где искать Василису."
    "Нужно было войти в портал."
    "Работает ли он вообще?"
    th2 "Хуй с ним."
    th2 "Была не была."
    "После чего Иветта сиганула в портал вперёд ногами нахуй."
    stop ambience
    $ renpy.movie_cutscene('source/luntik.webm')
    window hide
    play sound trigger
    scene portal:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat

    show tripsMVWWW777:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat
    with dissolve
    pause 3
    scene zagruzka with ed_alpha_diss_fast
    pause 1
    play sound travel
    pause 1
    scene nport:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat

    show tripsMVWWW777:
        parallel:
            zoom 1.05 anchor (48,27)
            ease 0.10 pos (0, 0)
            parallel:
                ease 0.10 pos (30,30)
                ease 0.10 pos (0, 0)
                ease 0.10 pos (-25,25)
                repeat
    with dissolve
    pause 1.8
    scene nport with ed_alpha_diss_fast
    th2 "Фух мля..."
    "Иветта обернулась."
    scene domext with pushleft
    ivt1 "Я близко."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Димы:")
    hide zatemnenie with dissolve2
    play music zapad fadein 5
    scene black with ed_night_dis
    scene kuhnyanight with ed_night_dis
    "Зайдя на кухню, Дима узрел ахуенную картину."
    "Вечный спал за столом, обнимая пустые бутылки."
    "А в углу комнаты..."
    "Кхм..."
    "Вам лучше это увидеть самим."
    $ renpy.movie_cutscene('source/drochit.webm')
    "В углу комнаты сидела Василиса."
    "Голая."
    "Сидела и наяривала."
    "Смотря на спящего Вечного."
    "И лишь единственная мысль проскочила в голове у Скита:"
    th "Хорошая малолетка..."
    th "Она напоминает мне ту самую..."
    th "От которой у меня теперь есть дочь..."
    "Василиса заметила палящигося Скита."
    vas "ВЫЙДИ НАХУЙ ОТСЮДА, СУКА!"
    "От таких криков проснулся Вечный."
    show bergennorm:
        default subpixel True 
        parallel:
            Null(726.0, 754.0)
            'bergennorm'
        parallel:
            xpos -0.3 
            linear 0.50 xpos 0.25 
    with Pause(0.60)
    show bergennorm:
        xpos 0.25 
    vchn "Чё бля происходит?"
    play sound door_break
    "Скит плеснул с фильтра воды в чашку, и убежал, попутно попивая водичку свою ебейшую."
    show zatemnenie with dissolve2
    $ MND_Chapter("От лица Вечного:")
    hide zatemnenie with dissolve2
    scene kuhnyanight
    show vasilisanight
    with flash
    "Василиса уже успела одеться."
    vchn "Ну и чё это было?"
    "Она не знала, что и ответить."
    vas "Иногда мне бывает трудно себя сдерживать."
    vas "Ты заснул, и..."
    vchn "Понятно."
    "Вечный понурил ебалом."
    "Настроение было парашное."
    "Всё из-за прерванного сна, где он снова сидел и коддил какой-то SKITETSKY REMASTER."
    "Хер его знает, что это..."
    "Но во снах Вечного он сидел и делал это говно."
    "Игрушка какая-то вроде."
    stop music fadeout 5
    vas "Я иду спать."
    vchn "Иди."
    window hide
    play sound door_open
    show vasilisanight:
        subpixel True 
        ypos 1.0 
        linear 0.50 ypos 2.2 
    with Pause(0.60)
    show vasilisanight:
        ypos 2.2 
    window show
    "Вечный остался на кухне один."
    "Делать было нехуй."
    window hide
    play music mvdep fadein 2
    pause 2
    "Вечный вспомнил, что он так и не дочитал дневник."
    "На трезвую голову не пошло."
    "Но теперь-то он угашен в нулину блеать!"
    "И можно дочитать."
    play sound door_open
    scene domintnight with ed_lap
    window hide
    play sound dostal
    show diary:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'diary'
        parallel:
            ypos 2.0 
            linear 0.50 ypos 1.0 
    with Pause(0.60)
    show diary:
        ypos 1.0 
    nvl clear
    nvlbazar "Проверив, спят ли Василиса и Скит, вечный взял дневник."
    nvlbazar "Он лежал на том же месте."
    nvlvhcn "Она ничего не заметила, видимо."
    nvlvhcn "Оно и к лучшему."
    nvl clear
    hide diary
    play sound ubralstvol
    show diary:
        ypos 0.0
        ease 0.5 ypos 1.5

    pause 0.6
    hide diary
    nvlbazar "Вечный начал читать дальше."
    nvl clear
    nvlvas "В один момент я просто потеряла контроль над ситуацией."
    nvlvas "В том самом лагере были три идиота, которые канифолили мне мозги."
    nvlvas "Я для них была унтерменьшем."
    nvl clear
    nvlvas "Было достаточно грустно наблюдать их нападки."
    nvlvas "Однако, виду я не подавала."
    nvlvas "Но есть одно но."
    nvl clear
    nvlvas "Недавно я вспомнила, что нас было двое."
    nvlvas "Да-да, не удивляйтесь."
    nvl clear
    nvlvhcn "К кому она обращается блеать?"
    nvl clear
    nvlvas "Иветта."
    nvlvas "Та самая Иветта."
    nvlvas "Она же - моя тёмная сторона."
    nvlvas "Имея неподконтрольную ненависть в виде Иветты - можно вырезать целый батальйон."
    nvl clear
    nvlvas "Как бы это не звучало, но..."
    nvlvas "Нечто подобное и произошло после."
    nvlvas "После очередных подъёбок от этих патау Иветта начала меня буквально упрашивать отдать контроль над телом."
    nvlvas "Ей было просто больно на всё это смотреть."
    nvl clear
    nvlvas "На то, как они со мной обращаются."
    nvlvas "Вообще с нихуя."
    nvlvas "Они забили стрелку возле сцены вечером."
    nvlvas "Чем это закончится было очевидно."
    nvlvas "И я решилась."
    nvl clear
    stop music fadeout 5
    nvlvas "В самый важный момент я отдала ей контроль."
    nvlvas "После чего начался пиздец."
    nvl clear
    nvlbazar "Вечный буквально визуализировал это всё у себя в голове."
    nvl clear
    scene black with ed_night_dis
    play music mosh1 fadein 2
    scene scena_leto
    show sergo1 at right
    show marat1
    show sanya1 at left
    with ed_lap
    par1 "Мы пришли поговорить."
    par1 "Видишь ли,{w=0.2} нам надоела эта бессмысленная вражда."
    par1 "Предлагаем мирное соглашение на взаимовыгодных условиях."
    ivt "Да пошли вы." with vpunch
    par1 "Ну-{w=0.2}у,{w=0.2} раз ты сама против{w=0.2}.{w=0.2}.{w=0.2}.{w} То{w=0.2}.{w=0.2}.{w=0.2}."
    par2 "Решим всё менее гуманными методами." with vpunch
    par3 "Теперь ты никуда не денешься!" with vpunch
    par3 "Хоть в нашем гуманном обществе и не принято бить женщин,{w=0.2} сегодня я нарушу {b}закон гор{/b}."
    "Сказал правый парниша,{w=0.2} попутно надевая на пальцы кастет."
    "Василиса,{w=0.2} почуяв неладное,{w=0.2} дала команду своему {b}альтер-эго{/b}."
    th1 "Твой час настал."
    th1 "Покажи им свю нашу мощь,{w=0.2} {b}подруга{/b}."
    th2 "Я не подведу."
    $ Aw_HeartAttack("scena_leto")
    ivt1 "Вам пиздец." with vpunch
    window hide
    stop music
    play music mosh2
    scene scena_leto
    show sergo1
    $ Aw_HeartAttack("scena_leto")
    with flash_fast2
    play sound dostalstvol
    show pizdavsem:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem'
        parallel:
            ypos 2.0 
            linear 0.50 ypos 1.0 
    with Pause(0.60)
    show pizdavsem:
        ypos 1.0 
    hide pizdavsem
    play sound aw_knife_slash_3
    show pizdavsem:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem'
        parallel:
            xpos 0.5 
            linear 0.40 xpos -0.6 
    with Pause(0.60)
    show pizdavsem:
        xpos -0.6 
    hide pizdavsem
    play sound aw_knife_slash_3
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6 
            linear 0.50 xpos -0.6 
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6 
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6 
            linear 0.50 xpos -0.6 
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6 
    hide pizdavsem2
    hide sergo1
    play sound sfx_body_bump
    show sergo11:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'sergo11'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.8, 2.0) rotate 120.0 
    show sergo12:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'sergo12'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.35, 2.2) rotate -120.0 
    show sergo13:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'sergo13'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.2, 2.0) rotate -120.0 
    with Pause(0.60)
    show sergo11:
        pos (0.8, 2.0) rotate 120.0 
    show sergo12:
        pos (0.35, 2.2) rotate -120.0 
    show sergo13:
        pos (0.2, 2.0) rotate -120.0 
    window show
    "Она нашинковала первого парнушку аки {b}буряки на винегрет{/b}."
    "Ярость полностью овладела ею."
    "Исчезли абсолютно все чувства."
    "Кроме неконтролируемой ненависти."
    "А в это время со спины готовилось нападение."
    "Иветта ловко извернулась и начала кромсать второго обидчика."
    window hide
    scene scena_leto1
    show sanya1
    $ Aw_HeartAttack("scena_leto1")
    with pushleft
    play sound dostalstvol
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            ypos 2.0 
            linear 0.50 ypos 1.0 
    with Pause(0.60)
    show pizdavsem2:
        ypos 1.0 
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 0.5 
            linear 0.40 xpos -0.6 
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6 
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6 
            linear 0.50 xpos -0.6 
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6 
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6 
            linear 0.50 xpos -0.6 
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6 
    hide pizdavsem2
    hide sanya1
    play sound sfx_body_bump
    show sanya11:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'sanya11'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.8, 2.0) rotate 120.0 
    show sanya12:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'sanya12'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.35, 2.2) rotate -120.0 
    show sanya13:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'sanya13'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.2, 2.0) rotate -120.0 
    with Pause(0.60)
    show sanya11:
        pos (0.8, 2.0) rotate 120.0 
    show sanya12:
        pos (0.35, 2.2) rotate -120.0 
    show sanya13:
        pos (0.2, 2.0) rotate -120.0 
    window show
    "Иветта покрошила и вторую редиску."
    "Она,{w=0.2} аки {b}Шеф-повар{/b},{w=0.2} кромсающий свежую щуку,{w=0.2} которая отправится в уху."
    ivt1 "ДЕРЖИ{w=0.2}-И{w=0.2}-И{w=0.2}-ИСЬ,{w=0.2} ОГУЗОК!" with vpunch
    "Иветта повернула свой взор на последнего обидчика."
    window hide
    scene scena_leto
    show marat1
    $ Aw_HeartAttack("scena_leto")
    with pushright
    oguzok "Прошу,{w=0.2} остановись!" with vpunch
    ivt1 "А ГДЕ БЫЛ ТЫ,{w=0.2} КОГДА Я ПРОСИЛА ОСТАНОВИТЬСЯ?" with vpunch
    ivt1 "А,{w=0.2} БЛЯТЬ?" with vpunch
    "Буквально проорала ему в ебало эти слова Иветта."
    ivt1 "ГДЕ,{w=0.2} НАХУЙ?" with vpunch
    oguzok "{w=0.5}не{w=0.2}.{w=0.2}.{w=0.2}.{w=0.2} надо{w=0.2}.{w=0.2}.{w=0.2}."
    "Огузок совсем обмяк."
    "Иветте надоело с ним нянчится."
    "И она,{w=0.2} орудуя топором аки {b}Кратос{/b},{w=0.2} начала шинковать Огузка в свой {b}кровавый салат{/b}."
    window hide
    play sound dostalstvol
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            ypos 2.0 
            linear 0.50 ypos 1.0 
    with Pause(0.60)
    show pizdavsem2:
        ypos 1.0 
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 0.5 
            linear 0.40 xpos -0.6 
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6 
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6 
            linear 0.50 xpos -0.6 
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6 
    hide pizdavsem2
    play sound aw_knife_slash_3
    show pizdavsem2:
        default subpixel True 
        parallel:
            Null(1280.0, 720.0)
            'pizdavsem2'
        parallel:
            xpos 1.6 
            linear 0.50 xpos -0.6 
    with Pause(0.60)
    show pizdavsem2:
        xpos -0.6 
    hide pizdavsem2
    hide marat1
    play sound sfx_body_bump
    show sanya11:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'marat11'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.8, 2.0) rotate 120.0 
    show marat12:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'marat12'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.35, 2.2) rotate -120.0 
    show marat13:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'marat13'
        parallel:
            pos (0.5, 1.0) rotate 0.0 
            linear 0.50 pos (0.2, 2.0) rotate -120.0 
    with Pause(0.60)
    show marat11:
        pos (0.8, 2.0) rotate 120.0 
    show marat12:
        pos (0.35, 2.2) rotate -120.0 
    show marat13:
        pos (0.2, 2.0) rotate -120.0 
    window show
    show blink
    stop music fadeout 4
    "Иветта присела на ближайшую лавочку и прикрыла глаза,{w=0.2} дабы перевести дыхание."
    th2 "Вот и всё."
    th2 "Дышим глубже." with vpunch
    th1 "Я хотела их припугнуть{w=0.2}.{w=0.2}.{w=0.2}."
    play music outofit1
    scene scena_leto
    show unblink
    th1 "А ты их нашинковала{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    hide unblink
    th2 "Омг,{w=0.2} блять,{w=0.2} вечно тебе всё не нравится{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    th1 "Ты в курсе,{w=0.2} что нам с тобой напару пиздец?" with vpunch
    th2 "Не дрейфь,{w=0.2} прорвёмся."
    th2 "Не зря же я тут вон сколько небо копчу."
    th2 "И я,{w=0.2} и ты{w=0.2}.{w=0.2}.{w=0.2}."
    th2 "Проврёмся."
    "Белоснежные трусики уже насквозь промокли."
    "Иветта запустила туда свои шаловливые пальчики,{w=0.2} после чего начала делать прерывистые движения взад-{w=0.2}вперёд."
    th2 "Обожаю насилие." with vpunch
    th2 "И ничего не могу с собой поделать."
    th2 "Слишком сильно возбуждает."
    th1 "Не,{w=0.2} подруга.{w} Сильнее насилия возбуждают другие девочки."
    th2 "Знаешь такое выражение:{w=0.2} {b}<<Каждый дрочит как он хочет>>{/b}?"
    th1 "Не понаслышке знаю,{w=0.2} подруга."
    "Движения всё ускорились."
    th1 "Ак{w=0.2}-к{w=0.2}-уратне{w=0.2}-е{w=0.2}.{w=0.2}.{w=0.2}."
    th1 "Не марк{w=0.2}-о{w=0.2}-вку чист{w=0.2}-ишь{w=0.2}.{w=0.2}.{w=0.2}."
    "Пытаясь совладать с языком думала Василиса."
    th2 "Сделаем красиво?"
    "Они обе чувствовали кайф от дрочки."
    "Пусть со стороны и выглядит,{w=0.2} что он терпят друг друга из-за невозможности разделиться{w=0.2}.{w=0.2}.{w=0.2}."
    "Пусть со стороны это выглядит о{w=0.2}-{w=0.2}о-{w=0.2}очень странно{w=0.2}.{w=0.2}.{w=0.2}."
    "Они обажают друг друга."
    "Была бы возможность получить отдельные тела{w=0.2}.{w=0.2}.{w=0.2}."
    "Они бы стали лучшей лесби-{w=0.2}парой."
    "Как никто другие знают все нужные точки входа друг друга."
    "Как бы это не звучало." with vpunch
    "Тем не менее,{w=0.2} блаженство не может длиться вечно."
    "Кончив и словив экстаз,{w=0.2} Иветта,{w=0.2} рубашка и юбка которой были все в крови,{w=0.2} начала доставать сигарету из секретного кармана."
    "Она знала,{w=0.2} что случится что-то подобное."
    "Вот и положила последнюю сигу {b}Kent Quant{/b} и желтый {b}Cricket{/b} за лямку бюсгалтера."
    "На стороне спины,{w=0.2} разумеется."
    stop music fadeout 5
    "Пока она тянулась за сигой,{w=0.2} локтём уронила окровавленный топор с лавочки."
    th2 "Ну да и хуй с ним." with vpunch
    "И аки {b}Виктор Баринов{/b},{w=0.2} {b}Шеф-повар{/b} ресторана {b}Clod Monet{/b}, прикурив цыбару,{w=0.2} сделала глубокую тягу и лишь тихо выдохнула{w=0.2}.{w=0.2}.{w=0.2}."
    $ renpy.movie_cutscene('source/pobeda.webm')
    window hide
    scene black with ed_night_dis
    scene domintnight with ed_lap
    "Вечный немного прихуел от этой истории."
    "Но ведь это не конец всей истории, верно?"
    "Что же там дальше..."
    nvl clear
    nvlvas "После случившегося пришлось скрываться."
    nvlvas "В один из не самых примечательных дней была намечана стрелка с двумя ментами."
    nvlvas "Владик говорил, только они смогут помочь."
    nvlvas "Встреча была намечена в баре."
    nvl clear
    "Вечный снова представил себе всё это воочию."
    window hide
    scene black with ed_night_dis
    play music bambino fadein 2
    scene bar100 with ed_lap
    nvlvas "Встречу положено было провести Иветте."
    nvlvas "Всё потому, что она в нужном моменте сможет надавить."
    nvl clear
    nvlvas "Не тот случай? Ха."
    nvlvas "Не для неё."
    nvlvas "Она не знает такого понятия в принципе."
    nvlvas "Вот и всё."
    nvl clear
    nvlbazar "Наигрывала какая-то олдовая музычка..."
    nvlbazar "Вокруг Иветты, что потягивала свежий мохито кружились какие-то пьяные додики."
    nvlbazar "Самый рофлан в том, что они оба решили подкатить к ней."
    nvlbazar "И оба были бы посланы нахуй, если бы не начали рамсить прямо в баре."
    nvlbazar "После чего их спешно выдворила охрана."
    nvl clear
    nvlbazar "Напиток почти кончался, а мусаров всё нет и нет."
    nvlbazar "Иветта начинала нервничать."
    nvlbazar "Отвлечься было просто не на что."
    nvlbazar "Только если на громких деградантов в противоположной стороне бара."
    nvl clear
    nvlbazar "Они обсуждали навар от проделанной ходки."
    nvlbazar "Скрутить 20 кило медных проводов с заброшенной ковровой фабрики - это, конечно, ахуительно."
    nvlbazar "Но явно не то, чем можно гордится."
    nvlbazar "Нет бы на работку пойти..."
    nvl clear
    nvlbazar "Да ну, зачем?"
    nvlbazar "Можно же напиздить с государственной территории немного металла..."
    nvlbazar "Обжарить, да сдать."
    nvlbazar "И пробухать всё лаве в ближайшем баре."
    nvlbazar "Реально дегроды."
    nvl clear
    nvlbazar "За размышлениями о пьяных додиках Иветта не заметила, как к ней подсели те самые два мента."
    nvl clear
    window hide
    show ment:
        default subpixel True 
        parallel:
            Null(750.0, 720.0)
            'ment'
        parallel:
            xpos 2.0 
            linear 0.60 xpos 0.75 
    show ment1:
        default subpixel True 
        parallel:
            Null(600.0, 720.0)
            'ment1'
        parallel:
            xpos 2.0 
            linear 0.60 xpos 0.25 
    with Pause(0.70)
    show ment:
        xpos 0.75 
    show ment1:
        xpos 0.25 
    window show
    mt "Я вас категорически приветствую."
    "Отсалютовал левый Мент."
    ivt1 "Нихао."
    ivt1 "Вы можете помочь с нарастающей проблемой?"
    "Менты посмотрили друг на друга."
    "Потом на Иветту."
    "И сказали:"
    mt1 "Вполне."
    mt1 "Хотя это будет трудно."
    mt1 "Видел я фото того месива, что ты учудила."
    mt "Балерина прям."
    "Хохотнул левый Мент."
    mt "Есть вариант один..."
    mt "Косить под ненормальную."
    ivt1 "Чёт не особо вариант..."
    mt1 "На пожизненное хочешь загреметь?"
    "Сказал уже правый мент."
    "Причём одеты были не по форме."
    "Иветта не смогла разглядеть звание."
    "А то пришли небось два сержантика и пытаются глазёнками хлопать."
    "Приободрять."
    ivt1 "Не особо."
    "Тихо ответила Иветта."
    "Надо же драматизма нагнать."
    mt "Ну так вот."
    "Продолжил левый."
    mt "Мы дадим нужные показания."
    mt "Направим к нужному мозгоправу."
    mt "Он тебе всё чё хочешь подпишет и припишет."
    "У Иветты загорелись глаза."
    "Победа снова так близка."
    mt "Но у нас есть одно условие."
    "Глазёнки резко поменяли цвет своего огня."
    mt "Ты дашь нам в использование своё тело."
    th1 "Чего блять?"
    th1 "Это чё за шутки такие у них?"
    ivt1 "Прикол я оценила."
    ivt1 "Что делать-то нужно?"
    mt "А это и не прикол."
    mt "Вот ему..."
    "Показал левый на правого Мента."
    mt "...уже 27 скоро."
    mt "А он всё ещё бабу не приголубил."
    "Хохотнул левый Мент."
    mt1 "Серёг!"
    "Поспешно решил оправдать своё честное имя правый Мент."
    mt "Да ладно."
    mt "Я всё понимаю."
    mt "Поэтому и предоставлю тебе для этого всё необходимое."
    th1 "Не соглашайся, слышишь?"
    th1 "Это наёб!"
    "Лишь безумолку тараторила Василиса в мыслях Иветты."
    th2 "У нас с тобой нет выбора."
    th1 "Выбор есть всегда!"
    ivt1 "Я согласна."
    th1 "Ты чё, ебанулась?"
    th1 "Они же нас трахнут и кинут!"
    th1 "Бля, да это ребёнку понятно!"
    th2 "Я тебе ещё раз повторяю."
    th2 "У нас нет выбора."
    mt "Тогда пройдёмте."
    stop music fadeout 5
    show overlay aw_memory_back_1
    "И они прыгнули в ментовскую шкоду."
    "И укатили в надвигающийся рассвет."
    "На хату левого Мента."
    "Где и произошёл весь процесс."
    window hide
    scene black with ed_night_dis
    scene nebo with ed_lap
    play music kartinki
    nvl clear
    nvlbazar "<<Серёга>> был неопытен, но вот <<Николай>>..."
    nvlbazar "Был любителем БДСМ."
    nvlbazar "Кароче говоря, они конкретно так испытали на прочность ВСЕ отверстия Иветты."
    nvlbazar "Было больно. Ещё больше - неприятно."
    nvlbazar "Мерзко было за своё поведение перед Василисой."
    nvl clear
    nvlbazar "Которая, кстати, перестала разговаривать с Иветтой."
    nvlbazar "С концами нахуй."
    nvlbazar "Просто исчезла из сознания."
    nvlbazar "Но это на первый взгляд."
    nvlbazar "Она наблюдала за Иветтой."
    nvl clear
    nvlbazar "Последняя, в свою очередь, слилась с суда."
    nvlbazar "На котором должны были огласить приговор."
    nvlbazar "Она ушла в подполье с одной единственной целью."
    nvl clear
    nvlbazar "Нужно было совершить план мести."
    nvlbazar "Всё просто - пожарный топорик оружие небольшое, острое и надежное."
    nvlbazar "Осталось выцепить этих двоих."
    nvlbazar "И зачем соглашалась только?"
    nvl clear
    nvlbazar "Зря доверие Василисы проебала."
    nvlbazar "Ну ничего. Это ещё можно исправить."
    nvlbazar "Посмотрим, как вы у меня запляшете."
    nvl clear
    nvlbazar "Влад помог с поиском этих двух ментов."
    nvlbazar "Их ареал обитания - <<карамель>>."
    nvlbazar "Там, по выходным, они чаще всего и развлекаются."
    nvlbazar "Осталось только проскочить в випку."
    nvlbazar "Но у Иветты уже была нужная последовательность действий."
    nvlbazar "Осталось её воплотить. Да."
    nvl clear
    scene black with ed_night_dis
    window hide
    stop music fadeout 4
    $ renpy.pause(5, hard=True)
    play music aw_monsterbot fadein 4
    $ renpy.pause(1, hard=True)
    play sound na_popei
    scene black with flash_fast2
    $ renpy.pause(1, hard=True)
    scene bg aw_club_f at aw_dance_2 with dissolve2
    "Расшатанный и убитый в хлам мозг —{w} явно позитивно откликался на атакующую уши музыку." with dissolve
    "Убитые таблетками чувства —{w} невнятно выражались на лице посредством улыбки и,{w=0.2} то закатывающихся,{w=0.2} то закрывающихся,{w=0.2} глаз."
    play sound na_popei
    $ Aw_Alko("bg aw_club_f")
    "В весёлом хаосе,{w=0.2} я опрокинула в себя сразу четыре шота текилы,{w=0.2} разбавив их рюмкой джина,{w=0.2} отполировав всё это {b}«дорожкой»{/b} с груди какой-то проститутки в туалете." with flash_fast2
    "После непродолжительного,{w=0.2} всё с той же {b}«дамой по вызову»{/b},{w=0.2} занятия {b}«ласками»{/b} в туалетной кабинке,{w=0.2} я вернулась в зал." with dissolve
    "Тело,{w=0.2} неподвластно,{w=0.2} двигалось в такт музыке,{w=0.2} что разливалась по клубу,{w=0.2} медленно продвигаясь в сторону барной стойки."
    window hide
    $ renpy.pause(2, hard=True)
    lis "Нормально ебашит?!" with hpunch
    "Спросила меня одна из посетительниц,{w=0.2} когда я таки дошла до бара,{w=0.2} намекнув бармену на повторение употребленного ранее."
    ivt1 "Улёт!" with vpunch
    "Она довольно улыбнулась мне,{w=0.2} принявшись потягивать коктейль."
    "Я же —{w} взялась заливать в себя пойло,{w=0.2} что пила до этого."
    play sound na_popei
    lis "Эй,{w=0.2} подруга,{w=0.2} не хочешь немного{w=0.2}.{w=0.2}.{w=0.2}."  with flash_fast2
    "Шлепком по заду,{w=0.2} отвлекла меня всё та же девушка,{w=0.2} в конце своей реплики прикрыв одну своих ноздрей пальцем."
    ivt1 "После {b}«этого»{/b} меня распирает...{w} Если ты понимаешь." with dissolve
    lis "Меня тоже."
    "Прошептала она горячо мне на ухо."
    "Я обняла ее за плечи и,{w=0.2} поднявшись со стула —{w} пошла следом за ней в туалетную комнату."
    window hide
    scene black with fade3
    $ renpy.pause(3, hard=True)
    scene bg aw_club_f at aw_dance_2 with dissolve
    $ Aw_Alko("bg aw_club_f")
    lis "Нормас{w=0.2}.{w=0.2}.{w=0.2}." with dissolve
    "Только и проговорила {b}«она»{/b},{w=0.2} когда мы вышли вновь в зал."
    ivt1 "Повторим?"
    lis "Позже,{w=0.2} дорогуша."
    "Она принялась пританцовывать."
    lis "Как тебе музло?!" with hpunch
    "Ее стеклянные глаза уже не могли фокусироваться на мне,{w=0.2} из-за чего хаотично бегали вокруг,{w=0.2} пытаясь зацепиться за моё лицо,{w=0.2} которое,{w=0.2} по всей видимости,{w=0.2} у нее расшатывалось в такт музыке."
    ivt1 "Улёт!" with vpunch
    "Ответила я и она,{w=0.2} с глупой улыбкой и смехом —{w} удалилась вглубь зала,{w=0.2} а я,{w=0.2} в свою очередь, {w=0.2}вернулась к барной стойке."
    window hide
    stop music fadeout 6
    $ renpy.pause(2, hard=True)
    scene black with fade3
    $ renpy.pause(3, hard=True)
    play music aw_ost_blade
    scene bg aw_club_f at aw_dance_2 with dissolve2
    $ Aw_Alko("bg aw_club_f")
    $ renpy.pause(3, hard=True)
    "Спустя время —{w} я оторвалась от выпивки,{w=0.2} напоследок закинув в себя горсть обезболивающего и заливая его тумблером виски,{w=0.2} выбрасывая остаток денег на барную стойку и уходя от нее в приватный коридор,{w=0.2} в который,{w=0.2} пару минут назад,{w=0.2} прошли {b}«знакомые лица»{/b}." with dissolve
    aw_mj3 "Вы к кому?" with fade2
    "Спросил меня крупный парень,{w=0.2} стоящий на входе в «приватку»."
    ivt1 "Двое мужчин,{w=0.2} что пару минут назад зашли{w=0.2}.{w=0.2}.{w=0.2}."
    aw_mj3 "Комната?"
    ivt1 "Не знаю.{w} Но они тут частые гости.{w} Если не трудно —{w} можете сами у них спросить."
    ivt1 "Скажите,{w=0.2} что к ним пришла {b}«балерина»{/b}."
    aw_mj3 "Колян,{w=0.2} подойди." with vpunch
    "Второй,{w=0.2} не менее крупный парень,{w=0.2} отошел от лесенки,{w=0.2} что вела в служебные помещения."
    aw_mj3 "Погляди пока за этой."
    "{b}«Колян»{/b} -{w} лишь кивнул,{w=0.2} после чего первый отошел вглубь {b}«приватки»{/b},{w=0.2} скрываясь за занавесками."
    window hide
    $ renpy.pause(3, hard=True)
    "Спустя время —{w} {b}«не Колян»{/b} вернулся,{w=0.2} приподнимая передо мной занавеску."
    aw_mj3 "Шестая."
    "Я лишь кивнула ему,{w=0.2} проходя внутрь коридора."
    window hide
    scene black with fade3
    play sound door_open
    scene bg aw_private_r_1
    show ment at right
    show ment1 at left
    with ed_lap
    aw_mj1 "Какие лица,{w=0.2} ха-ха!{w} Серёг,{w=0.2} узнаешь?" with vpunch
    aw_mj2 "Узнаю.{w} Трудно забыть такой{w=0.2}.{w=0.2}.{w=0.2}.{w} Такие красивые губы."
    aw_mj2 "И с чем на этот раз,{w=0.2} {b}«балерина»{/b}?"
    ivt1 "Нужна помощь." with vpunch
    aw_mj1 "А чё за помощь то,{w=0.2} девонька?"
    aw_mj1 "Ты,{w=0.2} вроде как,{w=0.2} в прошлый раз кинула наше {b}«предприятие»{/b}."
    aw_mj2 "За пригласительным не явилась.{w} А людей мы уже оповестили.{w} Где надо —{w} словечко замолвили.{w} Всё для вас устроили,{w=0.2} дамочка,{w=0.2} людей подняли нужных,{w=0.2} а вы же что?{w} Так дела не делаются."
    ivt1 "Возникла пара проблем.{w} Не до этого было."
    aw_mj2 "Не красиво.{w} Очень не красиво{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    ivt1 "Мы можем обсудить и это тоже.{w} Думаю —{w} я придумаю,{w=0.2} как загладить {b}«свою вину»{/b}."
    aw_mj1 "Прикрой дверь,{w=0.2} девонька.{w} Да на замочек.{w} Там и {b}«подумаем»{/b}."
    "Я лишь улыбнулась,{w=0.2} не отворачиваясь нащупав дверной замок и защелкнув его."
    aw_mj2 "Проходи.{w} Водочки выпьем."
    "Жестом один из мужчин указал на диван,{w=0.2} вместе с этим опрокидывая в себя стопку водки."
    ivt1 "Зачем эти излишества." with vpunch
    "Скинув кроссовки,{w=0.2} я стянула с себя штаны,{w=0.2} откидывая их ногой в сторону,{w=0.2} после чего —{w} избавилась и от толстовки."
    aw_mj1 "Еп...{w} Эффективно и быстро,{w=0.2} согласись,{w=0.2} Серёг?" with vpunch
    aw_mj2 "Точно что." with vpunch
    aw_mj1 "А чего эт за обвязки?{w} Новые {b}«штуки»{/b} хочешь попробовать?"
    ivt1 "Это?"
    "Я указала на бинт,{w=0.2} которым была обмотана с торса до груди,{w=0.2} прикрывая шрам на животе и грудь."
    "А за спиной —{w} плотно держал топор,{w=0.2} спрятанный от любопытных глаз."
    ivt "Да.{w} Новые штуки." with vpunch
    "Потянув левой рукой за узел,{w=0.2} а правой придерживая топор за рукоять —{w} я распутала обмотки,{w=0.2} позволяя им упасть на пол."
    aw_mj1 "Как сейчас помню эти классные сиськи."
    stop music fadeout 4
    "Облизнувшись начал один,{w=0.2} вытирая руки и рот шелковым полотенцем,{w=0.2} после подымаясь с места."
    play sound aw_shut_up_and_bleed_snd
    ivt1 "Я тоже всё помню." with vpunch
    "Процедила я,{w=0.2} глядя исподлобья на достаточно приблизившегося ублюдка,{w=0.2} выводя правую руку с топором из-за спины."
    window hide
    stop sound fadeout 1
    play music aw_shut_up_and_bleed
    play sound2 aw_axe_hit_2
    scene bg aw_private_ms_1 at aw_master_tryas with flash_fast_red2
    $ Aw_Alko("bg aw_private_ms_1")
    $ renpy.pause(0.8, hard=True)
    play sound2 aw_axe_hit_2
    scene bg aw_private_ms_1 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene bg aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ Aw_Alko("bg aw_private_ms_2")
    play sound3 aw_wom_hight_scr
    scene black
    $ Aw_HeartAttack("black")
    $ renpy.pause(0.6, hard=True)
    play sound2 aw_axe_hit_2
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene aw_axe_zam at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_2
    scene bg aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_2
    scene bg aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene bg aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_2
    scene bg aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene bg aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_axe_hit_1
    scene bg aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound aw_axe_hit_1
    scene bg aw_private_ms_2 at aw_master_tryas with flash_fast_red2
    $ renpy.pause(0.2, hard=True)
    play sound2 aw_kill_snd
    scene bg aw_private_ms_4 at aw_master_tryas with flash_fast_red
    $ Aw_HeartAttack("bg aw_private_ms_4")
    $ renpy.pause(1.5, hard=True)
    aw_mj2 "С-{w=0.2}с-{w=0.2}стой{w=0.2}.{w=0.2}.{w=0.2}." with dissolve2
    "Лежа на полу,{w=0.2} выставив перед собой раздробленную руку,{w=0.2} процедил едва-{w=0.2}едва «Серёга»."
    aw_mj2 "П-{w=0.2}п-{w=0.2}просто{w=0.2}.{w=0.2}.{w=0.2}.{w} П-{w=0.2}п-{w=0.2}поговорим{w=0.2}.{w=0.2}.{w=0.2}."
    aw_mj2 "В-{w=0.2}в-{w=0.2}вы{w=0.2}ы{w=0.2}.{w=0.2}.{w=0.2}."
    "Давясь кровавым кашлем,{w=0.2} попытался сказать он."
    aw_mj2 "В-{w=0.2}в-{w=0.2}все{w=0.2}.{w=0.2}.{w=0.2}.{w} Обо вс{w=0.2}-ё{w=0.2}-ём{w=0.2}.{w=0.2}.{w=0.2}.{w} Можно дог{w=0.2}.{w=0.2}. {w}Договорится{w=0.2}.{w=0.2}.{w=0.2}."
    ivt1 "Ложись." with vpunch
    "Я кивнула на диван у стены."
    aw_mj2 "Ч-{w=0.2}что?" with vpunch
    ivt1 "Ложись." with vpunch
    "Тот,{w=0.2} судорожно кивая,{w=0.2} перевернулся и,{w=0.2} неуклюже и со стонами,{w=0.2} принялся заползать на диванчик."
    play sound aw_knife_slash_3
    "Одев на руку пакет,{w=0.2} что лежал в кофе,{w=0.2} я подошла к нему и,{w=0.2} взяв за {b}«хер»{/b} -{w} натянула его вверх,{w=0.2} свободной рукой взмахивая топором." with flash_fast_red2
    ivt1 "Как по маслу.{w} Даже смачивать не пришлось."
    "Процедила я,{w=0.2} склонившись над ним и запихав его достоинство ему же в глотку."
    ivt1 "Глубже.{w} Глотай,{w=0.2} сучка." with vpunch
    "Перехватив топор,{w=0.2} я просунула его рукоять в рот насильника,{w=0.2} тем самым {b}«проталкивая»{/b} отрубленный орган глубже в его глотку."
    "Его глаза — {w}выдавали в нём страх."
    "Они горели мольбой и криком о помощи."
    "И дичайшим ужасом."
    "Настолько ярко и явно это всё читалось,{w=0.2} что я не могла на это смотреть."
    th "Уж чего-{w=0.2}чего —{w} а видеть их лица в кошмарах я уже конкретно заебалась,{w=0.2} а уж такое{w=0.2}.{w=0.2}.{w=0.2}." with vpunch
    th "Беззащитное?{w} Испуганное?{w} Отчаявшиеся?{w} Наполненное ужасом?"
    th "…{w=0.2} и подавно." with vpunch
    window hide
    scene black with fade2
    $ Aw_Alko("black")
    "Поэтому —{w} я лишь перевернула его на живот, {w=0.2}закрыв голову подушкой,{w=0.2} чтобы от от вида его разбитой черепушки не сблевать прямо на месте." with dissolve
    stop music fadeout 3
    ivt1 "А теперь —{w} я сладко кончу." with vpunch
    window hide
    play sound aw_kill_snd
    scene bg aw_private_ms_end
    show overlay aw_memory_back_1
    with flash_fast_red2
    $ Aw_HeartAttack("bg aw_private_ms_end")
    $ renpy.pause(2, hard=True)
    scene black with fade3
    $ renpy.pause(5, hard=True)
    $ renpy.music.set_volume(0.6)
    play music rmdoshd fadein 2
    play ambience rain_out fadein 2
    scene nebo
    show doshd
    with ed_night_dis
    nvl clear
    nvlbazar "Иветта смотрела на ночное небо."
    nvlbazar "Она была уже вся мокрая."
    nvlbazar "Ливень всё хуярил и хуярил."
    nvlbazar "А настроения по-прежнему не было."
    nvl clear
    nvlivt "Всё ещё обижаешься?"
    nvl clear
    nvlbazar "Вопрос, казалось бы, ушёл в пустоту."
    nvl clear
    nvlvas "Было б на что."
    nvlvas "Ты просто конченная."
    nvlvas "Тебе проблем мало было?"
    nvl clear
    nvlivt "Прости."
    nvl clear
    nvlvas "Не прощу."
    nvlvas "Ты мне такая нахуй не нужна."
    nvlvas "Бля, я бы полжизни отдала за своё, отдельное тело."
    nvlvas "И чтоб забыть тебя нахуй."
    nvl clear
    nvlivt "Перестань."
    nvl clear
    nvlvas "Не перестану."
    nvlvas "Я всё ещё тебя ненавижу."
    nvlvas "И когда ты только появилась?"
    nvl clear
    nvlivt "Я и есть твой защитный механизм."
    nvlivt "Без меня - ты сдохнешь."
    nvl clear
    nvlvas "Можем проверить."
    nvlivt "И как же?"
    nvl clear
    nvlvas "Херово ты Влада слушала."
    nvlvas "Он ещё советовал в iGandone LLC обратиться с этим вопросом."
    nvlvas "А ты пошла к мусорам."
    nvlvas "И что в итоге?"
    nvlvas "Никакого нам с тобой помилования..."
    nvl clear
    nvlivt "Не хотела я его слушать."
    nvlivt "Он безответно влюблён в тебя."
    nvlivt "Не в меня."
    nvlivt "Лично я ему ничем не обязана."
    nvl clear
    nvlvas "Ха."
    nvlvas "Твою жопу он тоже спасал."
    nvlvas "И не раз."
    nvl clear
    nvlivt "Вместе с твоей, не забывай."
    nvl clear
    nvlvas "Так вот мне бы отдельную от тебя жопу."
    nvlvas "Да чтоб туда всякие мерзопакосные менты свои огрызки не сували."
    nvlvas "Улавливаешь суть?"
    nvl clear
    nvlivt "Значит, идём к айгандону?"
    nvlvas "Да хоть сейчас."
    nvl clear
    nvlbazar "И они отправились в офис iGandone LLC, который находился неподалёку."
    nvl clear
    stop ambience fadeout 5
    scene black with ed_night_dis
    nvlbazar "Они шли пешком, дабы проветрить голову."
    nvlbazar "И заболеть нахуй."
    nvlbazar "Ведь на улице ливень."
    nvlbazar "Но они всегда любили гулять под дождём."
    nvl clear
    nvlivt "Ты действительно хочешь отделиться?"
    nvl clear
    nvlvas "Да."
    nvlvas "И это не обсуждается."
    nvlvas "Тебе понятно?"
    nvl clear
    nvlivt "Ты ща довыёбываешься."
    nvlivt "Да так довыёбываешься, что я с разбегу под колёса проезжающей машини сигану."
    nvlivt "И не будет ни меня, ни тебя."
    nvlivt "Вот и всё блять."
    nvlivt "Распизделась она тут, видите ли."
    nvl clear
    nvlvas "Успокойся."
    nvl clear
    nvlbazar "Василиса и Иветта поменялись ролями бля."
    nvl clear
    nvlivt "Успокоится?"
    nvlivt "А, может, ты просто на хуй пойдёшь?"
    nvlivt "Заебала, в натуре."
    nvl clear
    nvlivt "Всё ей не нравится."
    nvlivt "Пыталась решить вопрос с гопниками в лагере - опять не так."
    nvlivt "Пыталась решить вопрос с сизо - снова не так бля."
    nvlivt "Наебенила я этих мудаков - да всё не так блять!"
    nvl clear
    nvlivt "Чё?"
    nvlivt "Скажи, чё тебе не нравится на этот раз?"
    nvl clear
    nvlbazar "Василисе не нашлось, что и сказать."
    nvlbazar "Остаток пути они молча ненавидели друг друга."
    nvl clear
    scene labaext with ed_lap
    nvlbazar "Под утро они таки дошли до офиса."
    nvlbazar "Недолго поколебавшись, Иветта зашла внутрь."
    nvl clear
    play sound door_open
    scene ineony with ed_lap
    nn "Здравия."
    nn "Чем обязан?"
    ivt1 "Есть проблема."
    ivt1 "Вы единственный, кто может её решить."
    nn "И что за проблема такая?"
    "Неоня немного удивился."
    "Самую малость."
    "Но ему льстил подобный базар."
    ivt1 "Нам нужно разделиться."
    nn "Нам?"
    nn "Это кому конкретно?"
    ivt1 "Мне."
    ivt "И Мне."
    nn "Понятно."
    nn "Собираетесь лечить раздвоение личности нестандартными методами?"
    ivt1 "Именно."
    ivt1 "Нам бы тела отдельные."
    ivt "И Мне бы память подтереть."
    ivt "Знать её не хочу нахуй."

    return

label dlc:
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
    vsn "МИХОН!" with vpunch
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