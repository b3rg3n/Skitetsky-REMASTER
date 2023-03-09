# Skitetsky Remaster Splash & Menu Changer
# by @b3rg3n
# (C) Skeet Dynasty 2023

label main_menu:
    stop sound fadeout 3
    stop music fadeout 3
    window hide
    if persistent.menushka_akt0 is True:
        play music splin fadein 2
        scene bergenokno
        show redpart
        show bergenokno1
        with Fade(1.5, 1, 2)
        call screen main_menu
    if persistent.menushka_akt1 is True:
        play music lisnak fadein 2
        scene nvnight
        show redpart
        with Fade(1.5, 1, 2)
        show skitpio:
            default subpixel True 
            parallel:
                Null(450.0, 720.0)
                'skitpio'
            parallel:
                pos (-2.0, 1.0) 
                linear 0.60 pos (0.35, 1.0) 
        show bergensvd:
            default subpixel True 
            parallel:
                Null(726.0, 754.0)
                'bergensvd'
            parallel:
                xpos 2.0 
                linear 0.60 xpos 0.94 
        show deadlylxrd:
            default subpixel True 
            parallel:
                Null(500.0, 842.0)
                'deadlylxrd'
            parallel:
                xpos 0.5 
                linear 0.60 xpos 0.65 
            parallel:
                ypos -2.0 
                linear 0.61 ypos 1.0 
        show kazahspr:
            default subpixel True xpos 0.8 
            parallel:
                Null(600.0, 720.0)
                'kazahspr'
            parallel:
                ypos 2.0 
                linear 0.61 xpos 0.8 ypos 1.0 
        with Pause(0.71)
        show skitpio:
            pos (0.35, 1.0) 
        show bergensvd:
            xpos 0.94 
        show deadlylxrd:
            pos (0.65, 1.0) 
        show kazahspr:
            pos (0.8, 1.0) 
        call screen main_menu
    if persistent.menushka_akt2 is True:
        play music burnitdown fadein 2
        scene et_road_dark
        show redpart
        with Fade(1.5, 1, 2)
        show menu_art_china
        show menu_art_sheped
        show menu_art_bergen
        show menu_art_kost
        show menu_art_vladislave
        show menu_art_skit
        show menu_art_vladick
        show menu_art_semenyak
        call screen main_menu
    if persistent.menushka_akt3 is True:
        play music fcent fadein 2
        scene laba
        show ogonek
        with Fade(1.5, 1, 2)
        show deadlylxrd:
            default subpixel True 
            parallel:
                Null(500.0, 842.0)
                'deadlylxrd'
            parallel:
                xpos 2.0 
                linear 0.60 xpos 0.85 
        show kazahspr:
            default subpixel True 
            parallel:
                Null(600.0, 720.0)
                'kazahspr'
            parallel:
                pos (-0.5, 1.0) 
                linear 0.60 pos (0.45, 1.0) 
        show lordsprclon3:
            default subpixel True xpos 0.7
            parallel:
                Null(498.0, 841.0)
                'lordsprclon3'
                0.10
                'lordsprclon3'
            parallel:
                ypos -2.0 
                linear 0.60 xpos 0.7 ypos 1.0
        show coldspr1:
            default subpixel True xpos 0.6 
            parallel:
                Null(600.0, 720.0)
                'coldspr1'
                0.59
                'coldspr1'
            parallel:
                ypos 2.0 
                linear 0.60 xpos 0.6 ypos 1.0 
        with Pause(1.69)
        show deadlylxrd:
            xpos 0.85 
        show kazahspr:
            pos (0.45, 1.0) 
        show lordsprclon3:
            pos (0.7, 1.0) 
        show coldspr1:
            pos (0.6, 1.0) 
        call screen main_menu
    if persistent.menushka_akt4 is True:
        play music jailbreak fadein 2
        scene bar100
        show ogonek
        with Fade(1.5, 1, 2)
        show vasilisa:
            default subpixel True 
            parallel:
                Null(640.0, 640.0)
                'vasilisa'
            parallel:
                ypos 2.0 
                linear 0.60 ypos 1.0 
        show bergennorm:
            default subpixel True 
            parallel:
                Null(508.0, 733.0)
                'bergennorm'
            parallel:
                xpos 1.75 
                linear 0.60 xpos 0.9 
        with Pause(0.70)
        show vasilisa:
            ypos 1.0 
        show bergennorm:
            xpos 0.87 
        call screen main_menu
    else:
        play music pizdec fadein 2
        scene menushka
        show overlaymenushki
        show versiya
        with Fade(1.5, 1, 2)
        call screen main_menu


label splashscreen:

    python:
        
        if not persistent.set_volumes:
            
            persistent.set_volumes = True

            _preferences.volumes['music'] = .65
            _preferences.volumes['sfx'] = 1.0
            _preferences.volumes['voice'] = .65
    jump splashblya
#    if persistent.zastavka_skip is True:
#        jump splashcreen3
#    else:
#        jump spashcreen1

label spashcreen1:
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    play music mosh1 fadein 3
    $ renpy.pause(1.5, hard=True)
    scene diskbg with dissolve4
    $ renpy.pause(1, hard=True)
    show sktwarn2 with awrain
    $ renpy.pause(8, hard=True)
    call screen skitsoglasenblya with dissolve2
    return

label splashscreen2:
    show sktwarn1
    hide sktwarn2
    with awrain2
    $ renpy.pause(8, hard=True)
    stop music fadeout 6
    scene black with dissolve4
    $ renpy.pause(1, hard=True)
    $ renpy.movie_cutscene('source/videosos/skrimer.webm')
    play sound zaelo
    $ renpy.pause(2, hard=True)
    play sound ornulseblanov
    $ renpy.pause(5, hard=True)
    $ persistent.zastavka_skip = True
    jump splashcreen3

label splashblya:
    play music kotik fadein 2
    scene disknew
    show redpart
    with Fade(1.5, 1, 2)
    $ renpy.pause (1.0, hard=True)
    show text "{font=[splash_font]}{color=#FFFFFF}{size=47}Запрещено для детей. {/size}{size=30}*смеётся*{/size}\n{size=47}BERGEN не хотел никого оскорбить.\n{/size}{size=30}Правда?{/font}{/color}{/size}" with dissolve2:
        anchor (0.5, 0.5)
        xalign 0.5
        yalign 0.5
    $ renpy.pause (1.1, hard=True)
    show gui load_icon_br at br_rotate(1.0, 0.7, 0.5, 1.0) with dspr
    $ renpy.pause (6.66, hard=True)
    hide text with dissolve2
    $ renpy.pause (1.1, hard=True)
    show text "{font=[splash_font]}{color=#FFFFFF}{size=47}В игре имеется нецензурная лексика.{/font}{/color}{/size}" with dissolve2:
        anchor (0.5, 0.5)
        xalign 0.5
        yalign 0.5
    $ renpy.pause (6.66, hard=True)
    hide text with dissolve2
    $ renpy.pause (1.1, hard=True)
    show text "{font=[splash_font]}{color=#FFFFFF}{size=47}Настоятельно рекомендуется играть в наушниках.{/size}\n{size=30}Всё для лучшего погружения.{/font}{/color}{/size}" with dissolve2:
        anchor (0.5, 0.5)
        xalign 0.5
        yalign 0.5
    $ renpy.pause (6.66, hard=True)
    hide text with dissolve2
    $ renpy.pause (1.1, hard=True)
    show text "{font=[splash_font]}{color=#FFFFFF}{size=47}Приятного проходения.{/size}{/font}{/color}" with dissolve2:
        anchor (0.5, 0.5)
        xalign 0.5
        yalign 0.5
    $ renpy.pause (6.66, hard=True)
    hide text with dissolve2
    $ renpy.pause (1.1, hard=True)
    stop music fadeout 3
    scene black with dissolve2
    $ renpy.pause (1.1, hard=True)
    return

label splashcreen3:
    $ renpy.movie_cutscene('source/videosos/zastavkaremaster.webm')
    return

screen skitsoglasenblya:
    tag aw_r1 
    modal True
    imagemap:
        ground "source/aw_warn_h_n.webp" 
        hover "source/aw_warn_h_y.webp" 
        alpha True
        hotspot (0, 612, 229, 108) action Quit(confirm=not main_menu)
        hotspot (871, 635, 409, 87) clicked[Jump("splashscreen2")]
