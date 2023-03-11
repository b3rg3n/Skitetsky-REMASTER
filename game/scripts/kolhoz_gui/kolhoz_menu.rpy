# Skitetsky Remaster Splash & Menu
# by @b3rg3n
# (C) Skeet Dynasty 2023

label main_menu:
    stop sound fadeout 3
    stop music fadeout 3
    window hide
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
    if persistent.zastavka_skip is True:
        return
    else:
        jump spashcreen1

label spashcreen1:
    scene black with dissolve2
    $ renpy.pause(1, hard=True)
    play music ctd fadein 2
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
