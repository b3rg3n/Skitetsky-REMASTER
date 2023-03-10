label start:
    $ persistent.zastavka_skip = True
    play sound maloletka
    if persistent.menushka_akt0 is True:
        scene menushitfade0:
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
    elif persistent.menushka_akt1 is True:
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
    elif persistent.menushka_akt2 is True:
        scene menushitfade2:
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
    elif persistent.menushka_akt3 is True:
        scene menushitfade3:
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
    elif persistent.menushka_akt4 is True:
        scene menushitfade4:
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
    jump first_scenario