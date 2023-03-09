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
    jump scenariogovna

label scenariogovna:
    show screen change_say_box_blya
    scene nmallblur with ed_night_dis
    play ambience rain_out fadein 5
    scene nmall
    show doshd
    with dissolve2
    "Куда наваливаем?"
    show zatemnenie with dissolve2
    menu:
        "The Carter Zero: Исток":
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
#        "The Carter Five: Doppelganger":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktfive
#        "The Carter Six: Взломать Скитецкого":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktsix
#        "The Carter Seven: Frozen Zone":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktseven
#        "The Carter Eight: Eclipse":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktseven
#        "The Carter Nine: After Midnight":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump akteight
#        "The Carter Ten: Exodus":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump aktnine
#        "The Carter DLC: История одного неудачника":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump dlc1
#        "The Carter DLC: After 4PDA":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump dlc2
#        "The Carter DLC: JoZef - навсегда?":
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump dlc3
