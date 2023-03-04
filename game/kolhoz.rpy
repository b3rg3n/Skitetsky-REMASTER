init:
    style gitbut is button:
        background "source/ebanoemenu/github.png"
        hover_background "source/ebanoemenu/github_hover.png"
        selected_background "source/ebanoemenu/github_hover.png"
        selected_hover_background "source/ebanoemenu/github_hover.png"
        selected_idle_background "source/ebanoemenu/github_hover.png"
    style tgbut is button:
        background "source/ebanoemenu/tg.png"
        hover_background "source/ebanoemenu/tg_hover.png"
        selected_background "source/ebanoemenu/tg_hover.png"
        selected_hover_background "source/ebanoemenu/tg_hover.png"
        selected_idle_background "source/ebanoemenu/tg_hover.png"

init -100 python:

    store.selected_slot = "_"
    persistent._file_page = 1

init 5 python:
    import renpy.store as store

    class FunctionCallback(Action):
        def __init__(self,function,*arguments):
            self.function=function
            self.arguments=arguments
        def __call__(self):
            return self.function(self.arguments)

    def on_load_callback(slot):
        try:
            if persistent.on_save_timeofday[slot]:
                persistent.timeofday = persistent.on_save_timeofday[slot][0]
                persistent.sprite_time = persistent.on_save_timeofday[slot][1]
                persistent.font_size = persistent.on_save_timeofday[slot][2]
                
                _preferences.volumes['music'] = persistent.on_save_timeofday[slot][3]
                _preferences.volumes['sfx'] = persistent.on_save_timeofday[slot][4]
                _preferences.volumes['voice'] = persistent.on_save_timeofday[slot][5]
        
        except:
            pass

    def on_save_callback(slot):
        if not persistent.on_save_timeofday:
            persistent.on_save_timeofday={}
        
        persistent.on_save_timeofday[slot] = (persistent.timeofday, persistent.sprite_time, persistent.font_size, _preferences.volumes['music'], _preferences.volumes['sfx'], _preferences.volumes['voice'])

    def do_rollback(cnt):
        if not d2_cardgame_block_rollback:
            k=cnt[0]
            renpy.rollback(True, k+1)



init python:
    _main_menu_screen = "main_menu"
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)
    renpy.music.register_channel("test_seven", "sfx", False)

    main_font = "source/3.otf"
    header_font = "source/3.otf"
    link_font = "source/3.otf"
    info_font = "source/2.ttf"

    config.thumbnail_width = 211
    config.thumbnail_height = 117







    style.file_picker_ss_window.xpos = 0
    style.file_picker_ss_window.ypos = 0



    style.file_picker_text = Style(style.default)
    style.file_picker_text.antialias = True
    style.file_picker_text.font  = main_font
    style.file_picker_text.color = "#bdbdbd"
    style.file_picker_text.selected_color = "#ffffff"
    style.file_picker_text.hover_color = "#ffffff"
    style.file_picker_text.size = 24
    style.file_picker_text.drop_shadow=(2, 2)
    style.file_picker_text.drop_shadow_color = "#000"





    style.save_load_button = Style(style.button)
    style.save_load_button.background = get_image("gui/save_load/thumbnail_idle.png")
    style.save_load_button.hover_background = get_image("gui/save_load/thumbnail_hover.png")
    style.save_load_button.selected_background = get_image("gui/save_load/thumbnail_selected.png")
    style.save_load_button.selected_hover_background = get_image("gui/save_load/thumbnail_selected.png")
    style.save_load_button.selected_idle_background = get_image("gui/save_load/thumbnail_selected.png")




    style.blank_button = Style(style.button)
    style.blank_button.background = "source/none.png"
    style.blank_button.hover_background = "source/none.png"
    style.blank_button.selected_background = "source/none.png"
    style.blank_button.selected_hover_background = "source/none.png"
    style.blank_button.selected_idle_background = "source/none.png"





    style.base_font = Style(style.default)
    style.base_font.font  = main_font
    style.base_font.size = 28
    style.base_font.line_spacing = 2

    style.settings_header = Style(style.base_font)
    style.settings_header.font  = header_font
    style.settings_header.size = 50
    style.settings_header.color = "#FFFFFF"
    style.settings_header.hover_color = "#FFFFFF"

    style.settings_text = Style(style.settings_header)
    style.settings_text.size = 36
    style.settings_text.selected_color = "#FF0000"
    style.settings_text.hover_color = "#FFFFFF"

    style.settings_link = Style(style.base_font)
    style.settings_link.font  = link_font
    style.settings_link.size = 60
    style.settings_link.kerning = 3
    style.settings_link.color = "#909ca3"
    style.settings_link.hover_color = "#ffffff"
    style.settings_link.selected_color = "#909ca3"
    style.settings_link.selected_idle_color = "#909ca3"
    style.settings_link.selected_hover_color = "#ffffff"
    style.settings_link.insensitive_color = "#909ca3"

    style.finger = Style(style.base_font)
    style.finger.font  = info_font
    style.finger.size = 30
    style.finger.kerning = 3
    style.finger.color = "#909ca3"
    style.finger.hover_color = "#ffffff"
    style.finger.selected_color = "#909ca3"
    style.finger.selected_idle_color = "#909ca3"
    style.finger.selected_hover_color = "#ffffff"
    style.finger.insensitive_color = "#909ca3"

    style.hyperlink_text = Style(style.settings_link)
    style.hyperlink_text.underline = True
    style.hyperlink_text.hover_color = "#0ff"
    style.hyperlink_text.idle_color = "#08f"

    style.music_link = Style(style.settings_link)
    style.music_link.insensitive_color = "#4f4f4f"
    style.music_link.selected_color = "#ffffff"

    style.sprite_menu = Style(style.settings_text)
    style.sprite_menu.size = 37
    style.sprite_menu.color = "#466123"
    style.sprite_menu.selected_color = "#466123"
    style.sprite_menu.hover_color = "#9dcd55"

    style.say_dialogue = Style(style.base_font)
    style.say_label = Style(style.base_font)
    style.say_label.size = 28
    style.say_label.drop_shadow=(2, 2)
    style.say_label.drop_shadow_color = "#000"

    style.chapter = Style(style.base_font)
    style.chapter.font  = header_font
    style.chapter.size = 120
    style.chapter.color = "#fff"

    style.chapter.outlines = [ (1, "#ffdd7d", 0, 0) ]

    style.daynum = Style(style.chapter)
    style.daynum.font  = header_font
    style.daynum.size = 45

    style.normal_day = Style(style.base_font)
    style.normal_day.color = "#ffdd7d"
    style.normal_day.drop_shadow=(2, 2)
    style.normal_day.drop_shadow_color = "#000"
    style.narrator_day = Style(style.normal_day)
    style.narrator_day.italic = False
    style.thoughts_day = Style(style.normal_day)
    style.thoughts_day.bold = False

    style.normal_sunset = Style(style.base_font)
    style.normal_sunset.color = "#ffdd7d"
    style.normal_sunset.drop_shadow=(2, 2)
    style.normal_sunset.drop_shadow_color = "#000"
    style.narrator_sunset = Style(style.normal_sunset)
    style.narrator_sunset.italic = False
    style.thoughts_sunset = Style(style.normal_sunset)
    style.thoughts_sunset.bold = False

    style.normal_night = Style(style.base_font)
    style.normal_night.color = "#ffdd7d"
    style.normal_night.drop_shadow=(2, 2)
    style.normal_night.drop_shadow_color = "#000"
    style.narrator_night = Style(style.normal_night)
    style.narrator_night.italic = False
    style.thoughts_night = Style(style.normal_night)
    style.thoughts_night.bold = False

    style.normal_prolog = Style(style.base_font)
    style.normal_prolog.color = "#ffdd7d"
    style.normal_prolog.drop_shadow=(2, 2)
    style.normal_prolog.drop_shadow_color = "#000"
    style.narrator_prolog = Style(style.normal_prolog)
    style.narrator_prolog.italic = False
    style.thoughts_prolog = Style(style.normal_prolog)
    style.thoughts_prolog.bold = False

    style.cards_button = Style(style.button)
    style.cards_button.font  = header_font
    style.cards_button.background = RoundRect("#000", False)
    style.cards_button.hover_background = RoundRect("#555", False)
    style.cards_button.insensitive_background = RoundRect("#404040", False)

    style.cards_button_text = Style(style.button_text)
    style.cards_button_text.color = "#FFF"
    style.cards_button_text.selected_color = "#777"
    style.cards_button_text.insensitive_color = "#c8c8c8"

    style.log_button = Style(style.button)
    style.log_button.child = None
    style.log_button.focus_mask = None
    style.log_button.background  = None

    style.log_button_text = Style(style.normal_day)
    style.log_button_text.font  = main_font
    style.log_button_text.selected_color = "#115bc0"
    style.log_button_text.hover_color = "#115bc0"
    style.log_button_text.selected_color = "#b6ff00"
    style.log_button_text.hover_color = "#b6ff00"

screen main_menu:



    modal True tag menu


    imagemap:
        auto "source/ebanoemenu/menushka_%s.png"
        hotspot (40,212,227,51) clicked Start() hovered Play("test_one", "source/ebanko.ogg")
        hotspot (50,280,206,46) clicked ShowMenu('load') hovered Play("test_two", "source/prosnulsa2.ogg")
        hotspot (63,342,183,44) clicked ShowMenu('preferences') hovered Play("test_three", "source/ahuel.ogg")
        hotspot (99,404,105,42) clicked ShowMenu('infa') hovered Play("test_five", "source/deti.ogg")
        hotspot (69,462,169,46) clicked ShowMenu('quit') hovered Play("test_four", "source/gb.ogg")

    button style "gitbut" pos (0.93,0.01) action OpenURL("http://github.com/b3rg3n") hovered Play("test_six", "source/wapdomik.ogg")
    button style "tgbut" pos (0.93,0.15) action OpenURL("http://t.me/b3rg3n") hovered Play("test_seven", "source/tgskt.ogg")

init -1001 python:
    translation=translation_ru
    translation_new=translation

    def merge_two_dicts(x, y):
        z = x.copy()
        z.update(y)
        return z
    translation_temp={}
    for i,k in translation.iteritems():
        translation_temp[i]={}
        translation_temp[i][_preferences.language]=k
    translation=merge_two_dicts(translation,translation_temp)

    def get_translation(string):
        renpy.log("%s" % string )
        return translation[string][_preferences.language]

init -1002 python:
    translation_ru = {
        "Quit_confirm" : "Уверен? Обратного пути не будет.",
        "Yes" : "Конечно",
        "No" : "Не особо",
        "settings" : "КРУТИЛКИ",
        "LOAD" : "ВСПОМНИТЬ",
        "SAVE" : "ЗАПОМНИТЬ",
        "BACK" : "ВЕРНУТЬСЯ",
        "Back" : "Вернуться?",
        "Save_game" : "Запомнить?",
        "Delete" : "Забыть?",
        "Auto" : "Авто",
        "Empty_slot" : "Тут нихуя нет",
        "Load_game" : "Вспомнить?",
        "INFO" : "Инфо",
        "info_text" : "Игра была сделана одним человеком на чистом энтузиазме.\nРазработчик этого куска говна - {a=https://t.me/b3rg3n}BERGEN{/a}.",
        "android_text" : "Это один огромный сборник приколов про Дмитрия Скитецкого. Игра не имеет цели оскорбить, унизить, захуесосить, закибербулить и пр. Это просто один большой локальный прикол.\nПравда?",
        "ios_text" : "\nsince 2023",
        "Window_mode" : "Режим экрана Remdi 8",
        "Fullscreen" : "Во весь экран",
        "Window" : "В окне",
        "Skip" : "Пропускать",
        "Skip_all" : "Весь пиздёж",
        "Skip_seen" : "Что уже видел",
        "Volume" : "Громкость",
        "Music_lower" : "Хардбасс",
        "Sound" : "Отрыжки",
        "Ambience" : "Шептуны",
        "Text_speed" : "Скорость пиздежа",
        "Font" : "Размер базара",
        "Normal_font" : "Обычный",
        "Big_font" : "Сделать больше",

}

init python:
    def force_quit():
        renpy.quit()

screen quit:



    modal True tag menu

    add get_image("bergensanitari.webp")

    text translation_new["Quit_confirm"] style "settings_link" size 60 text_align 0.5 xalign 0.5 yalign 0.33 color "#FFFFFF" antialias True kerning 2

    textbutton translation_new["Yes"] text_size 70 style "log_button" text_style "settings_link" xalign 0.21 yalign 0.55 text_color "#FFFFFF" text_hover_color "#FF0000" action Quit(confirm=False)
    textbutton translation_new["No"] text_size 70 style "log_button" text_style "settings_link" xalign 0.75 yalign 0.55 text_color "#FFFFFF" text_hover_color "#FF0000" action Return()

label _compat_confirm_quit:
    $ renpy.call_screen('quit')

init python:
    _game_menu_screen = "game_menu_selector"
screen game_menu_selector:

    modal True tag menu


    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    add get_image("ebanoemenu/ingame_menu.png") xalign 0.5 yalign 0.5
    imagemap:

        auto get_image("ebanoemenu/ingame_menu_%s.png") xalign 0.5 yalign 0.5
        hotspot (0, 43, 660, 65) focus_mask None clicked MainMenu()
        hotspot (0, 89, 660, 65) focus_mask None clicked ShowMenu('save')
        hotspot (0, 160, 660, 65) focus_mask None clicked ShowMenu('load')
        hotspot (0, 221, 660, 65) focus_mask None clicked ShowMenu('help')
        hotspot (0, 273, 660, 65) focus_mask None clicked (ShowMenu('preferences'), Hide('game_menu_selector'))
        hotspot (0, 343, 660, 65) focus_mask None clicked ShowMenu('quit')

screen save:



    modal True tag menu

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["settings"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('preferences')
        textbutton translation_new["LOAD"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('load')
        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.png") yalign 0.65
            text " "+translation_new["SAVE"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.png") yalign 0.65
        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        textbutton translation_new["Save_game"] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_save_callback, selected_slot), FileSave(selected_slot))
        textbutton "{size=-12}{b}x{/b} {/size}"+translation_new["Delete"] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton translation_new["Auto"] text_size 25 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_size 25 right_padding 25 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):

                fixed:
                    add FileScreenshot(i) xpos 7 ypos 7

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "save_load_button"
                        has fixed
                        text ( "%s." % i + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "file_picker_text" xpos 10 ypos 10



init python:
    _load_prompt = "load"
screen load:



    modal True tag menu

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["settings"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('preferences')
        textbutton translation_new["SAVE"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('save')
        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.png") yalign 0.65
            text " "+translation_new["LOAD"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.png") yalign 0.65
        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()
        textbutton translation_new["Load_game"] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.5 action (FunctionCallback(on_load_callback,selected_slot), FileLoad(selected_slot))
        textbutton "{size=-12}{b}x{/b} {/size}"+translation_new["Delete"] style "log_button" text_style "settings_link" yalign 0.92 xalign 0.97 action FileDelete(selected_slot)

        vbox xalign 0.023 yalign 0.5:
            grid 1 10:
                for i in range(0, 10):
                    if i == 0:
                        textbutton translation_new["Auto"] text_size 25 style "log_button" text_style "settings_link" action (FilePage("auto"), SetVariable("selected_slot", False))
                    else:
                        textbutton str(i) text_size 25 right_padding 25 style "log_button" text_style "settings_link" action (FilePage(i), SetVariable("selected_slot", False))

        grid 4 3 xpos 0.13 ypos 0.2 xmaximum 0.81 ymaximum 0.65:
            transpose False
            xfill True
            yfill True
            for i in range(1, 13):

                fixed:
                    add FileScreenshot(i) xpos 7 ypos 7

                    button:
                        action SetVariable("selected_slot", i)
                        xfill False
                        yfill False
                        style "save_load_button"
                        has fixed
                        text ( "%s." % i + FileTime(i, format=' %d.%m.%y, %H:%M', empty=" "+translation_new["Empty_slot"]) + "\n" +FileSaveName(i)) style "file_picker_text" xpos 10 ypos 10

screen infa:

    modal True tag menu

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.png") yalign 0.65
            text " "+translation_new["INFO"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.png") yalign 0.65

        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        grid 1 3 xpos 0.05 ypos 0.2 xmaximum 1150:
            text translation_new["info_text"] style "finger"
            text translation_new["android_text"] style "finger"
            text translation_new["ios_text"] style "finger"

screen preferences:



    modal True tag menu

    $ bar_null = Frame(get_image("ebanoemenu/bar_null.png"),36,36)
    $ bar_full = Frame(get_image("ebanoemenu/bar_full.png"),36,36)

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["SAVE"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('save')
        textbutton translation_new["LOAD"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('load')
        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.png") yalign 0.65
            text " "+translation_new["settings"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.png") yalign 0.65
        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        side "c b r":
            area (0.25, 0.23, 0.51, 0.71)
            viewport id "preferences":
                mousewheel True
                draggable True
                scrollbars None

                has grid 1 13 xfill True spacing 15
                text translation_new["Window_mode"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.fullscreen:
                            add get_image("ebanoemenu/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Fullscreen"] style "log_button" text_style "settings_text" action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add get_image("ebanoemenu/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Window"] style "log_button" text_style "settings_text" action Preference("display", "window")



                text translation_new["Skip"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add get_image("ebanoemenu/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Skip_all"] style "log_button" text_style "settings_text" action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add get_image("ebanoemenu/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Skip_seen"] style "log_button" text_style "settings_text" action Preference("skip", "seen")


                text translation_new["Volume"] style "settings_header" xalign 0.5

                grid 2 1 xfill True:
                    textbutton translation_new["Music_lower"] style "log_button" text_style "settings_text" action Play("sound", "source/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("music volume") left_bar bar_full right_bar bar_null thumb "source/ebanoemenu/htumb.png" hover_thumb "source/ebanoemenu/htumb.png" xmaximum 0.8 ymaximum 3 xpos -0.35

                grid 2 1 xfill True:
                    textbutton translation_new["Sound"] style "log_button" text_style "settings_text" action Play("sound", "source/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("sound volume") left_bar bar_full right_bar bar_null thumb "source/ebanoemenu/htumb.png" hover_thumb "source/ebanoemenu/htumb.png" xmaximum 0.8 ymaximum 3 xpos -0.35

                grid 2 1 xfill True:
                    textbutton translation_new["Ambience"] style "log_button" text_style "settings_text" action Play("sound", "source/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("voice volume") left_bar bar_full right_bar bar_null thumb "source/ebanoemenu/htumb.png" hover_thumb "source/ebanoemenu/htumb.png" xmaximum 0.8 ymaximum 3 xpos -0.35

                text translation_new["Text_speed"] style "settings_header" xalign 0.5
                bar value Preference("text speed") left_bar bar_full right_bar bar_null thumb "source/ebanoemenu/htumb.png" hover_thumb "source/ebanoemenu/htumb.png" xalign 0.5 xmaximum 0.8 ymaximum 3

                text translation_new["Font"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.bazarbig == True:
                            add get_image("ebanoemenu/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Normal_font"] style "log_button" text_style "settings_text" action [SetField(persistent,'bazarbig', False)]

                    hbox xalign 0.5:
                        if not persistent.bazarbig == False:
                            add get_image("ebanoemenu/leaf.png") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Big_font"] style "log_button" text_style "settings_text" action [SetField(persistent,'bazarbig', True)]

                null

            bar value XScrollValue("preferences") left_bar "source/none.png" right_bar "source/none.png" thumb "source/none.png" hover_thumb "source/none.png"
            vbar value YScrollValue("preferences") bottom_bar "source/none.png" top_bar "source/none.png" thumb "source/ebanoemenu/vthumb.png" thumb_offset -12
