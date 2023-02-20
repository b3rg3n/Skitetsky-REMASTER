init -2 python:

    renpy.display.screen.screens[("say_old", None)] = renpy.display.screen.screens[("say", None)]

screen say_big(who, what):
    style_prefix "say"

    imagebutton:
        auto "source/dialogue_box/big/backward_%s.png"
        xpos 25
        ypos 583
        action Rollback()
    add "source/dialogue_box/big/dialogue_box_large.png":
        xpos 116
        ypos 544
    imagebutton:
        auto "source/dialogue_box/big/hide_%s.png"
        xpos 1005
        ypos 556
        action HideInterface()
    imagebutton:
        auto "source/dialogue_box/big/save_%s.png"
        xpos 1045
        ypos 556
        action ShowMenu('save')
    imagebutton:
        auto "source/dialogue_box/big/menu_%s.png"
        xpos 1084
        ypos 556
        action ShowMenu('preferences')
    imagebutton:
        auto "source/dialogue_box/big/load_%s.png"
        xpos 1122
        ypos 556
        action ShowMenu('load')
    if not config.skipping:
        imagebutton:
            auto "source/dialogue_box/big/forward_%s.png"
            xpos 1179
            ypos 583
            action Skip()
    else:
        imagebutton:
            auto "source/dialogue_box/big/fast_forward_%s.png"
            xpos 1179
            ypos 583
            action Skip()
    text what:
        id "what"
        xpos 129
        ypos 576
        xmaximum 1027
        size 27
        line_spacing 1
    if who:
        text who:
            id "who"
            xpos 129
            ypos 562
            size 27
            line_spacing 1


screen change_say_box_blya:
    if (persistent.bazarbig):
        $ renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("say_big", None)]
    else:
        $ renpy.display.screen.screens[("say", None)] = renpy.display.screen.screens[("say_old", None)]