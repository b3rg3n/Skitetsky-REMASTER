label start:
    $ persistent.zastavka_skip = True
    if persistent.menushka_akt1 is True:
        play sound maloletka1
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
    jump first_scenario