# Skitetsky Remaster Mods Engine
# by @deadlylxrd
# (C) Skeet Dynasty 2023

python early:
    mods = {}

init python:
   style.settings_link_edit = Style(style.settings_link)
   style.settings_link_edit.size = 30

screen mods():
    modal True tag menu

    $ bar_null = Frame(get_image("ebanoemenu/bar_null.webp"),36,36)
    $ bar_full = Frame(get_image("ebanoemenu/bar_full.webp"),36,36)

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:
        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["Mods"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.webp") yalign 0.65
        textbutton translation_new["Back"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.015 yalign 0.92 
            action [Hide("mods"), ShowMenu("preferences")]

        vbox:
            xalign -0.3
            yalign 0.2
            for lbl, name in sorted(mods.items()):
                textbutton name:
                    style "log_button"
                    text_style "settings_link_edit"
                    xpos 500 ypos 50
                    action Start(lbl)