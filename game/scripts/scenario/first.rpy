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
    show screen change_say_box_blya
    scene nmallblur with ed_night_dis
    play ambience rain_out fadein 5
    scene nmall
    show doshd
    with dissolve2
    "Куда наваливаем?"
    show zatemnenie with dissolve2
    menu:
        "Пролог" if True:
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump carter0
        "The Carter One: Постигая основы безумия" if True:
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump carter1
        "The Carter Two: Планапокалипсис" if True:
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump carter2
        "The Carter Three: iNeoony's Revenge" if True:
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump carter3
        "The Carter Four: Rotten Diary" if True:
            stop ambience fadeout 5
            scene nmallblur
            hide nmall
            hide doshd
            with dissolve2
            jump carter4
