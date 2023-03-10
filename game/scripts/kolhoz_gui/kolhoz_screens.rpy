#Skitetsky Remaster GUI
#by @b3rg3n
#(C) Skeet Dynasty 2023

init offset = -1

#Defines
init python:
    renpy.music.register_channel("test_one", "sfx", False)
    renpy.music.register_channel("test_two", "sfx", False)
    renpy.music.register_channel("test_three", "sfx", False)
    renpy.music.register_channel("test_four", "sfx", False)
    renpy.music.register_channel("test_five", "sfx", False)
    renpy.music.register_channel("test_six", "sfx", False)
    renpy.music.register_channel("test_seven", "sfx", False)

    main_font = "source/fonts/3.otf"
    header_font = "source/fonts/3.otf"
    link_font = "source/fonts/3.otf"
    info_font = "source/fonts/2.ttf"
    splash_font = "source/fonts/3.otf"

#Styles Text
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
    style.save_load_button.background = get_image("gui/save_load/thumbnail_idle.webp")
    style.save_load_button.hover_background = get_image("gui/save_load/thumbnail_hover.webp")
    style.save_load_button.selected_background = get_image("gui/save_load/thumbnail_selected.webp")
    style.save_load_button.selected_hover_background = get_image("gui/save_load/thumbnail_selected.webp")
    style.save_load_button.selected_idle_background = get_image("gui/save_load/thumbnail_selected.webp")

    style.blank_button = Style(style.button)
    style.blank_button.background = "source/none.webp"
    style.blank_button.hover_background = "source/none.webp"
    style.blank_button.selected_background = "source/none.webp"
    style.blank_button.selected_hover_background = "source/none.webp"
    style.blank_button.selected_idle_background = "source/none.webp"

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

    style.log_button_text_edit = Style(style.log_button_text)
    style.log_button_text_edit.size = 50


#Menu Links Buttons
init:
    style gitbut is button:
        background "source/ebanoemenu/github.webp"
        hover_background "source/ebanoemenu/github_hover.webp"
        selected_background "source/ebanoemenu/github_hover.webp"
        selected_hover_background "source/ebanoemenu/github_hover.webp"
        selected_idle_background "source/ebanoemenu/github_hover.webp"
    style tgbut is button:
        background "source/ebanoemenu/tg.webp"
        hover_background "source/ebanoemenu/tg_hover.webp"
        selected_background "source/ebanoemenu/tg_hover.webp"
        selected_hover_background "source/ebanoemenu/tg_hover.webp"
        selected_idle_background "source/ebanoemenu/tg_hover.webp"
    style gitbut1 is button:
        background "source/ebanoemenu/github1.webp"
        hover_background "source/ebanoemenu/github1_hover.webp"
        selected_background "source/ebanoemenu/github1_hover.webp"
        selected_hover_background "source/ebanoemenu/github1_hover.webp"
        selected_idle_background "source/ebanoemenu/github1_hover.webp"
    style tgbut1 is button:
        background "source/ebanoemenu/tg1.webp"
        hover_background "source/ebanoemenu/tg1_hover.webp"
        selected_background "source/ebanoemenu/tg1_hover.webp"
        selected_hover_background "source/ebanoemenu/tg1_hover.webp"
        selected_idle_background "source/ebanoemenu/tg1_hover.webp"

#Screens - Main Menu
init python:
    _main_menu_screen = "main_menu"
screen pizda_polnaya:

    modal True tag menu

    imagemap:
        auto "source/ebanoemenu/menushka1_%s.webp"
        hotspot (40,212,227,51) clicked Start() hovered Play("test_one", "source/sfx/ebanko1.ogg")
        hotspot (50,280,206,46) clicked ShowMenu('load') hovered Play("test_two", "source/sfx/pizda1.ogg")
        hotspot (63,342,183,44) clicked ShowMenu('preferences') hovered Play("test_three", "source/sfx/ahuel1.ogg")
        hotspot (99,404,105,42) clicked ShowMenu('infa') hovered Play("test_five", "source/sfx/deti1.ogg")
        hotspot (69,462,169,46) clicked ShowMenu('quit') hovered Play("test_four", "source/sfx/gb1.ogg")

    button style "gitbut1" pos (0.93,0.01) action OpenURL("http://github.com/b3rg3n") hovered Play("test_six", "source/sfx/wapdomik1.ogg")
    button style "tgbut1" pos (0.93,0.15) action OpenURL("http://t.me/b3rg3n") hovered Play("test_seven", "source/sfx/tgskt1.ogg")

screen main_menu:

    modal True tag menu

    imagemap:
        auto "source/ebanoemenu/menushka_%s.webp"
        hotspot (40,212,227,51) clicked Start() hovered Play("test_one", "source/sfx/ebanko.ogg")
        hotspot (50,280,206,46) clicked ShowMenu('load') hovered Play("test_two", "source/sfx/prosnulsa2.ogg")
        hotspot (63,342,183,44) clicked ShowMenu('preferences') hovered Play("test_three", "source/sfx/ahuel.ogg")
        hotspot (99,404,105,42) clicked ShowMenu('infa') hovered Play("test_five", "source/sfx/deti.ogg")
        hotspot (69,462,169,46) clicked ShowMenu('quit') hovered Play("test_four", "source/sfx/gb.ogg")

    button style "gitbut" pos (0.93,0.01) action OpenURL("http://github.com/b3rg3n") hovered Play("test_six", "source/sfx/wapdomik.ogg")
    button style "tgbut" pos (0.93,0.15) action OpenURL("http://t.me/b3rg3n") hovered Play("test_seven", "source/sfx/tgskt.ogg")

#Screens - Out
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

#Screens - InGame Menu
init python:
    _game_menu_screen = "game_menu_selector"
screen game_menu_selector:

    modal True tag menu

    button style "blank_button" xpos 0 ypos 0 xfill True yfill True action Return()

    add get_image("ebanoemenu/ingame_menu.webp") xalign 0.5 yalign 0.5
    imagemap:

        auto get_image("ebanoemenu/ingame_menu_%s.webp") xalign 0.5 yalign 0.5
        hotspot (0, 43, 660, 65) focus_mask None clicked MainMenu()
        hotspot (0, 89, 660, 65) focus_mask None clicked ShowMenu('save')
        hotspot (0, 160, 660, 65) focus_mask None clicked ShowMenu('load')
        hotspot (0, 221, 660, 65) focus_mask None clicked ShowMenu('help')
        hotspot (0, 273, 660, 65) focus_mask None clicked (ShowMenu('preferences'), Hide('game_menu_selector'))
        hotspot (0, 343, 660, 65) focus_mask None clicked ShowMenu('quit')

#Save & Load Slots Position
init -100 python:

    store.selected_slot = "_"
    persistent._file_page = 1

#Load Shit
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

#Save Image Position
    config.thumbnail_width = 211
    config.thumbnail_height = 117

    style.file_picker_ss_window.xpos = 0
    style.file_picker_ss_window.ypos = 0

#Screens - Save
screen save:

    modal True tag menu

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["settings"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('preferences')
        textbutton translation_new["LOAD"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('load')
        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["SAVE"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.webp") yalign 0.65
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


#Screens - Load
init python:
    _load_prompt = "load"
screen load:

    modal True tag menu

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["settings"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('preferences')
        textbutton translation_new["SAVE"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('save')
        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["LOAD"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.webp") yalign 0.65
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

#Screens - About
screen infa:

    modal True tag menu

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["INFO"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.webp") yalign 0.65

        textbutton translation_new["Back"] style "log_button" text_style "settings_link" xalign 0.015 yalign 0.92 action Return()

        grid 1 3 xpos 0.05 ypos 0.2 xmaximum 1150:
            text translation_new["info_text"] style "finger"
            text translation_new["android_text"] style "finger"
            text translation_new["ios_text"] style "finger"

#Screens - Settings
screen preferences:

    modal True tag menu

    $ bar_null = Frame(get_image("ebanoemenu/bar_null.webp"),36,36)
    $ bar_full = Frame(get_image("ebanoemenu/bar_full.webp"),36,36)

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        textbutton translation_new["SAVE"] style "log_button" text_style "settings_link" xalign 0.02 yalign 0.08 action ShowMenu('save')
        textbutton translation_new["LOAD"] style "log_button" text_style "settings_link" xalign 0.98 yalign 0.08 action ShowMenu('load')
        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["settings"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.webp") yalign 0.65
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
                            add get_image("ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Fullscreen"] style "log_button" text_style "settings_text" action Preference("display", "fullscreen")

                    hbox xalign 0.5:
                        if not _preferences.fullscreen:
                            add get_image("ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Window"] style "log_button" text_style "settings_text" action Preference("display", "window")



                text translation_new["Skip"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:

                    hbox xalign 0.5:
                        if _preferences.skip_unseen:
                            add get_image("ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Skip_all"] style "log_button" text_style "settings_text" action Preference("skip", "all")

                    hbox xalign 0.5:
                        if not _preferences.skip_unseen:
                            add get_image("ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Skip_seen"] style "log_button" text_style "settings_text" action Preference("skip", "seen")


                text translation_new["Volume"] style "settings_header" xalign 0.5

                grid 2 1 xfill True:
                    textbutton translation_new["Music_lower"] style "log_button" text_style "settings_text" action Play("sound", "source/sfx/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("music volume") left_bar bar_full right_bar bar_null thumb "source/ebanoemenu/htumb.webp" hover_thumb "source/ebanoemenu/htumb.webp" xmaximum 0.8 ymaximum 3 xpos -0.35

                grid 2 1 xfill True:
                    textbutton translation_new["Sound"] style "log_button" text_style "settings_text" action Play("sound", "source/sfx/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("sound volume") left_bar bar_full right_bar bar_null thumb "source/ebanoemenu/htumb.webp" hover_thumb "source/ebanoemenu/htumb.webp" xmaximum 0.8 ymaximum 3 xpos -0.35

                grid 2 1 xfill True:
                    textbutton translation_new["Ambience"] style "log_button" text_style "settings_text" action Play("sound", "source/sfx/ebanko.ogg") xpos 0.1 ypos -0.2
                    bar value Preference("voice volume") left_bar bar_full right_bar bar_null thumb "source/ebanoemenu/htumb.webp" hover_thumb "source/ebanoemenu/htumb.webp" xmaximum 0.8 ymaximum 3 xpos -0.35

                text translation_new["Text_speed"] style "settings_header" xalign 0.5
                bar value Preference("text speed") left_bar bar_full right_bar bar_null thumb "source/ebanoemenu/htumb.webp" hover_thumb "source/ebanoemenu/htumb.webp" xalign 0.5 xmaximum 0.8 ymaximum 3

                text translation_new["Font"] style "settings_header" xalign 0.5
                grid 2 1 xfill True:
                    hbox xalign 0.5:
                        if persistent.bazarbig == True:
                            add get_image("ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Normal_font"] style "log_button" text_style "settings_text" action [SetField(persistent,'bazarbig', False)]

                    hbox xalign 0.5:
                        if not persistent.bazarbig == False:
                            add get_image("ebanoemenu/leaf.webp") ypos 0.12
                        else:
                            null width 22
                        textbutton translation_new["Big_font"] style "log_button" text_style "settings_text" action [SetField(persistent,'bazarbig', True)]

                textbutton translation_new["Mods"]:
                    style "log_button"
                    text_style "log_button_text_edit" 
                    xalign 0.5 
                    action [Hide("preferences"), ShowMenu("mods")]

            bar value XScrollValue("preferences") left_bar "source/none.webp" right_bar "source/none.webp" thumb "source/none.webp" hover_thumb "source/none.webp"
            vbar value YScrollValue("preferences") bottom_bar "source/none.webp" top_bar "source/none.webp" thumb "source/ebanoemenu/vthumb.webp" thumb_offset -12

#Screens - Choice
screen choice(items):
    style_prefix "choice"

    modal True
    frame background Frame('source/ec_nightmare.webp', 0, 0) xfill True yalign 0.5 bottom_padding 33 top_padding 33:
        $ l = len(items)
        grid 1 l:
            xalign 0.5
            for caption, action, chosen in items:
                if action and caption:
                    button:
                        background None
                        action action
                        text caption font 'source/fonts/BloggerSans.ttf' size 23 hover_size 25 at ec_tr_choice
                        xalign 0.5


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 270
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")

#Screens - Notify
screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


#Screens - History
screen help():

    tag menu

    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("Тут нихуя нет.")

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }

style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    text_align gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    text_align gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5

#Mobile Shit
style pref_vbox:
    variant "medium"
    xsize 450

screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0




style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 600

#Screens - Confirm
screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Базару 0") action yes_action
                textbutton _("В пизду") action no_action

    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")

#Screens - Input
screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


#Screens - Skip Indicator
screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 6

            text _("Перематываю")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "DejaVuSans.ttf"

#Styles Name
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

#Styles RenPy Ofiginal
style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

#Kolhoz Ebaniy
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
        "Mods" : "Моды",

}

#Rudiment Ebuchiy Suka
screen quick_menu():

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Назад") action Rollback()
            textbutton _("История") action ShowMenu('history')
            textbutton _("Пропуск") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Авто") action Preference("auto-forward", "toggle")
            textbutton _("Запомнить") action ShowMenu('save')
            textbutton _("Крутилки") action ShowMenu('preferences')


init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Узнать правду") action Start()

        else:

            textbutton _("История") action ShowMenu("history")

            textbutton _("Запомнить") action ShowMenu("save")

        textbutton _("Вспомнить") action ShowMenu("load")

        textbutton _("Крутилки") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Завершить повтор") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Главное меню") action MainMenu()

        textbutton _("Об игре") action ShowMenu("about")

        textbutton _("Съебаться") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

screen main_menublya():

    tag menu

    add gui.main_menu_background

    frame:
        style "main_menu_frame"

    use navigation

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")

screen game_menu(title, scroll=None, yinitial=0.0):

    style_prefix "game_menu"

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:

            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude

    use navigation

    textbutton _("Вернуться"):
        style "return_button"

        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 30
    top_padding 120

    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_viewport:
    xsize 920

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 10

style game_menu_label:
    xpos 50
    ysize 120

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -30
