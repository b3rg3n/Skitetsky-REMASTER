init:
    $ mods ["test_mod"] = u"Тестовый мод"
    image black = "#000"

label test_mod:
    play music goloederevo fadein 3
    scene squareanim with flash
    show skitpio at center
    with dissolve
    window show
    skt "Привет!"
    window hide
    scene bg ext_path2_day with fade
    show skitpio at center
    with dissolve
    window show
    skt "Это тестовый мод."
    brg "Это всё?"
    skt "Да."
    "На этом всё."
    window hide
    stop music fadeout 2
    scene black with fade3
    pause 0.5
    return

