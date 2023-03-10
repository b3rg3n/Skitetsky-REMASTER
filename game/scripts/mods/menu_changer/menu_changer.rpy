init:
    $ mods ["menu_changer"] = u"Выбор фона меню"

label menu_changer:
    play sound maloletka
    if persistent.menushka_akt1 is True:
        scene menushitfade1:
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
    else:
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
    menu:
        "Оригинал":
            $ persistent.menushka_akt0 = False
            $ persistent.menushka_akt1 = False
            $ persistent.menushka_akt2 = False
            $ persistent.menushka_akt3 = False
            $ persistent.menushka_akt4 = False
            $ persistent.menushka_akt5 = False
            $ persistent.menushka_akt6 = False
            $ persistent.menushka_akt7 = False
            $ persistent.menushka_akt8 = False
            $ persistent.menushka_akt9 = False
            $ persistent.menushka_akt10 = False
            $ persistent.menushka_dlc1 = False
            $ persistent.menushka_dlc2 = False
            $ persistent.menushka_dlc3 = False
            return
        "Поломанное":
            $ persistent.menushka_akt0 = False
            $ persistent.menushka_akt1 = True
            $ persistent.menushka_akt2 = False
            $ persistent.menushka_akt3 = False
            $ persistent.menushka_akt4 = False
            $ persistent.menushka_akt5 = False
            $ persistent.menushka_akt6 = False
            $ persistent.menushka_akt7 = False
            $ persistent.menushka_akt8 = False
            $ persistent.menushka_akt9 = False
            $ persistent.menushka_akt10 = False
            $ persistent.menushka_dlc1 = False
            $ persistent.menushka_dlc2 = False
            $ persistent.menushka_dlc3 = False
            return