init python:
    import math
    class FireGlowDot(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "source/firedrop.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("ogonek", FireGlowDot().sm)

init python:

    class MndMenuCh(object):

        def __init__(self):

            self.sm = SpriteManager(update=self.update)

            self.glows = [ ]
            self.rd = "source/chast1.png"

            d = Transform(self.rd, zoom=0.25)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(20, 40))

            d = Transform(self.rd, zoom=0.5)
            for i in range(0, 50):
                self.add(d, renpy.random.randint(45, 60))

        def add(self, d, speed):
            s = self.sm.create(d)

            start = renpy.random.randint(0, 1080)
            s.x = renpy.random.randint(0, 1920)

            self.glows.append((s, start, speed))

        def update(self, st):
            for s, start, speed in self.glows:
                s.y = (start - speed/2 * st) % 1080 - 20
                s.x = s.x + math.sin(s.y/speed*2)

            return 0
    renpy.image("redpart", MndMenuCh().sm)


init:

    transform ed_bus_move:
        choice:
            ease 0.02 pos (0.001, 0.001)
            ease 0.02 pos (0, 0)
        choice:
            ease 0.02 pos (-0.001, 0.001)
            ease 0.02 pos (0, 0)
        choice:
            ease 0.02 pos (0.001, 0.001)
            ease 0.02 pos (0, 0.001)
        choice:
            ease 0.02 pos (-0.001, 0.001)
            ease 0.02 pos (0, 0.001)
        repeat

    transform aw_dance_2:
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.6 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease 0.6 xpos 0.5 ypos 0.49
            ease 0.6 xpos 0.48 ypos 0.51
            ease 0.6 xpos 0.5 ypos 0.49
            ease 0.6 xpos 0.52 ypos 0.51
            repeat

    transform aw_master_tryas:
        xalign 0.5 yalign 0.5
        parallel:
            ease 0.25 zoom 1.1
            ease 0.5 zoom 1.0
        parallel:
            ease 0.25 rotate -1.5
            ease 0.25 rotate 1.0
            ease 0.25 rotate 0.0

    transform aw_drinkscreens:
        xalign 0.5 yalign 0.5
        parallel:
            ease 2.0 xpos 0.505
            ease 2.0 xpos 0.4975
            ease 2.0 xpos 0.5025
            ease 2.0 xpos 0.495
            repeat
        parallel:
            ease 1.9 ypos 0.505
            ease 1.9 ypos 0.495
            ease 1.9 ypos 0.5025
            ease 1.9 ypos 0.4975
            repeat
        parallel:
            ease 2.25 rotate -0.75
            ease 2.25 rotate -0.25
            ease 2.25 rotate -0.5
            ease 2.25 rotate 0.5
            ease 2.25 rotate 0.0
            ease 2.25 rotate 0.25
            ease 2.25 rotate 0.7
            repeat
        parallel:
            ease 2.15 zoom 1.01
            ease 2.15 zoom 1.03
            ease 2.15 zoom 1.02
            ease 2.15 zoom 1.05
            ease 2.15 zoom 1.04
            ease 2.15 zoom 1.02
            ease 2.15 zoom 1.03
            ease 2.15 zoom 1.01
            ease 2.15 zoom 1.02
            repeat

    transform ed_get_achievement:
        pos(0.2, 0.8)
        anchor(0.5, 0.5)
        zoom 0.0
        ease 1.5 zoom 1.05
        ease 0.25 zoom 0.95
        ease 0.25 zoom 1.0
        pause 4.0
        ease 0.5 pos(-0.8, 0.85)
        ease 0.5 pos(-1.0, 0.85) alpha 0.0

    transform menu_art_move(z, x, z2):
        subpixel True
        yoffset 0 + (1200 * z)
        xoffset (740 - x) * z * 0.5
        zoom z2 * 0.75
        time 0.0
        parallel:
            ease 1.75 yoffset 0
        parallel:
            pause 0.75
            ease 1.5 zoom z2 xoffset 0

    transform ed_running_fast:
        truecenter
        zoom 1.25
        parallel:
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.25 rotate -0.75
            ease 0.25 zoom 1.30 rotate 0.75
            ease 0.20 zoom 1.35 rotate -0.75
            repeat
        parallel:
            ease 0.25 xpos 0.495
            ease 0.20 xpos 0.505
            repeat
        parallel:
            ease 0.25 ypos 0.495
            ease 0.30 ypos 0.505
            repeat

    transform spizdil:
        anchor (0.5, 0.5)
        ypos -0.3
        xpos 0.5
        linear 3.0 ypos 0.5

    transform beg:
        parallel:
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            ease 0.2 zoom 1.04 xpos 0.5 ypos 0.49
        parallel:
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.48 ypos 0.51
            ease 0.2 xpos 0.5 ypos 0.49
            ease 0.2 xpos 0.52 ypos 0.51
            repeat

    transform beg_end:
        ease 0.2 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5

    transform aw_heartattack(img):
        #contains:
        #    img
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 1.10
            repeat
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 0.90
            repeat
        contains:
            "blood"
            alpha 0.0
            block:
                ease 0.25 alpha 1.0
                ease 0.75 alpha 0.75
                repeat
    python:
        def Aw_HeartAttack(img):
            renpy.show(img, tag="bg2", at_list=[aw_heartattack(img)])

    transform aw_alko(img):
        #contains:
        #    img
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 1.10
            repeat
        contains:
            img
            alpha 0.0 zoom 1.0 xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                ease 0.25 alpha 0.25
                ease 0.5 alpha 0.0
            parallel:
                ease 0.75 zoom 0.90
            repeat

    python:
        def Aw_Alko(img):
            renpy.show(img, tag="bg2", at_list=[aw_alko(img)])

    transform mnd_chapter_anim:
        block:
            parallel:
                parallel:
                    choice:
                        xanchor 0.2
                    choice:
                        xanchor 0.3
                    choice:
                        xanchor 0.4
                    choice:
                        xanchor 0.5
                    choice:
                        xanchor 0.6
                    choice:
                        xanchor 0.7
                    choice:
                        xanchor 0.8
                parallel:
                    choice:
                        yanchor 0.2
                    choice:
                        yanchor 0.3
                    choice:
                        yanchor 0.4
                    choice:
                        yanchor 0.5
                    choice:
                        yanchor 0.6
                    choice:
                        yanchor 0.7
                    choice:
                        yanchor 0.8
            parallel:
                choice:
                    rotate -2
                choice:
                    rotate -1
                choice:
                    rotate 0
                choice:
                    rotate 1
                choice:
                    rotate 2
            parallel:
                choice:
                    alpha 1.0
                choice:
                    alpha 0.9
                choice:
                    alpha 0.8
                choice:
                    alpha 0.7
                choice:
                    alpha 0.6
                choice:
                    alpha 0.5
                choice:
                    alpha 0.4
            pause 0.02
            repeat 20
        block:
            parallel:
                parallel:
                    choice:
                        xanchor 0.498
                    choice:
                        xanchor 0.5
                    choice:
                        xanchor 0.502
                parallel:
                    choice:
                        yanchor 0.498
                    choice:
                        yanchor 0.5
                    choice:
                        yanchor 0.502
            parallel:
                choice:
                    rotate -0.2
                choice:
                    rotate -0.1
                choice:
                    rotate 0
                choice:
                    rotate 0.1
                choice:
                    rotate 0.2
            parallel:
                choice:
                    alpha 1.0
                choice:
                    alpha 0.9
                choice:
                    alpha 0.8
            pause 0.02
            repeat

    python:
        style.mnd_chapter_text.font = "source/Surfbars.otf"
        style.mnd_chapter_text.xalign = 0.5
        style.mnd_chapter_text.yalign = 0.5
        style.mnd_chapter_text.size = 100    #modded: style.mnd_chapter_text.size = 150
        style.mnd_chapter_text.color = "#ffffff"

        def MND_Chapter(name, time=3):
            renpy.show_screen("mnd_chapter", name)
            renpy.pause(time-0.4, hard=True)
            renpy.hide("mnd_chapter", layer="screens")
            renpy.show_screen("mnd_chapter", name)
            renpy.pause(0.4, hard=True)
            renpy.hide("mnd_chapter", layer="screens")

screen mnd_chapter(name):
    text name:
        style "mnd_chapter_text"
        at mnd_chapter_anim

