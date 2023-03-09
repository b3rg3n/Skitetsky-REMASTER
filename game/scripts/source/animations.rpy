init:

    define ed_flash_red = Fade(1, 0, 1, color="#e11")
    define ed_alpha_diss_fast = Dissolve(0.5, alpha=True)
    define flash = Fade(.25, 0, .75, color="#fff")
    define dissolve2 = Dissolve(2.0)
    define dspr = Dissolve(.2)
    define ed_earth_draw = ImageDissolve("source/ed_earth_draw.webp", 3.0)
    define ed_lap = ImageDissolve("source/ed_lap.webp", 2.0)
    define ed_night_dis = ImageDissolve("source/ed_night_dis.webp", 5.0)
    define poplil_pacan = ImageDissolve("source/wow_blya.webp", 6.66)
    define dis = Dissolve(0.5, alpha=True)
    define flash2 = Fade(2, 2, 2, color="#fff")
    define flash_red = Fade(1, 0, 1, color="#e11")
    define flash_red2 = Fade(2, 2, 2, color="#e11")
    define flash_fast = Fade(0.25, 0, 0.75, color="#fff")
    define flash_fast2 = Fade(0.05, 0, 0.35, color="#fff")
    define flash_fast_red = Fade(0.25, 0, 0.75, color="#ff0000")
    define flash_fast_red2 = Fade(0.05, 0, 0.75, color="#ff0000")
    define fade3 = Fade(1.5, 0, 1.5)
    define fade2 = Fade(1, 0, 1)
    define hell_dissolve = Dissolve(50)
    define dissolve3 = Dissolve(3)
    define dissolve4 = Dissolve(4)
    define dissolve_fast = Dissolve(0.5)
    define dissolve_long = Dissolve(100)
    define dspr = Dissolve(.2)
    define dissolve4 = Dissolve(4)
    define awrain = ImageDissolve("source/awrain.webp", 1.5, 60, reverse=False)
    define awrain2 = ImageDissolve("source/awrain.webp", 4.5, 80, reverse=False)
    define awrain3 = ImageDissolve("source/awrain.webp", 0.5, 30, reverse=False)
    define awwhole = ImageDissolve("source/awwhole.webp", 4.5, 60, reverse=False)
    define awbhole = ImageDissolve("source/awbhole.webp", 3.5, 60, reverse=True)
    define awmad = ImageDissolve("source/awmad.webp", 3.0, 75, reverse=False)
    define awspot = ImageDissolve("source/aw_eff_spot.webp", 3.5, 60, reverse=True)
    define awspot2 = ImageDissolve("source/aw_eff_spot.webp", 3.5, 60, reverse=False)
    define awnoose = ImageDissolve("source/aw_noose.webp", 3.5, 60, reverse=True)

    image aw_afd_ky1:
        contains:
            choice:
                "aw_afd_ky1_1"
            choice:
                "aw_afd_ky1_2"
            choice:
                "aw_afd_ky1_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_afd_ky1_1"
            choice:
                "aw_afd_ky1_2"
            choice:
                "aw_afd_ky1_3"
            alpha 0.45
            pause 0.15
            repeat
        contains:
            choice:
                "aw_afd_ky1_1"
            choice:
                "aw_afd_ky1_2"
            choice:
                "aw_afd_ky1_3"
            alpha 0.45
            pause 0.15
            repeat

    image aw_afd_dth1:
        contains:
            choice:
                "aw_afd_dth1_1"
            choice:
                "aw_afd_dth1_2"
            choice:
                "aw_afd_dth1_3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_afd_dth1_1"
            choice:
                "aw_afd_dth1_2"
            choice:
                "aw_afd_dth1_3"
            alpha 0.45
            pause 0.15
            repeat
        contains:
            choice:
                "aw_afd_dth1_1"
            choice:
                "aw_afd_dth1_2"
            choice:
                "aw_afd_dth1_3"
            alpha 0.45
            pause 0.15
            repeat

    image Fight_Ddv_Dun_png:
        'source/fight_png_01_LW0607.webp' with dissolve
        pause(0.1)
        'source/fight_png_02_LW0607.webp' with dissolve
        pause(0.1)
        repeat
        

    image coldherovo:
        'source/pip.webp'
        zoom 1.0
        ease 1.0 xzoom 6.5
        ease 1.0 xzoom 13.1
        ease 1.0 xzoom 15.2
        ease 1.0 xzoom 3.2
        ease 1.0 xzoom 7.7
        ease 1.0 xzoom 14.2
        ease 1.0 xzoom 1.2
        ease 1.0 xzoom 17.45
        ease 1.0 xzoom 7.27
        ease 1.0 xzoom 8.2
        ease 1.0 xzoom 9.2
        ease 1.0 xzoom 1.0
        repeat

    image anim pizda_ot_skita:
        'int_bus_night' with poplil_pacan
        pause 8
        "int_bus_black" with poplil_pacan
        pause 8
        repeat

    image rageone:
        "et_rage1" with dissolve
        pause .6
        "et_rage2" with dissolve
        pause .6
        repeat

    image ragetwo:
        "et_rage1" with dissolve
        pause .6
        "et_rage2" with dissolve
        pause .6
        "et_rage3" with dissolve
        pause .6
        repeat

    image ragethree:
        "et_rage1" with dissolve
        pause .3
        "et_rage2" with dissolve
        pause .3
        "et_rage3" with dissolve
        pause .3
        "et_rage4" with dissolve
        pause .3
        repeat


    image unblink:
        contains:
            "source/blink_up.webp"
            xalign 0 yalign 0
            ease 1.5 pos (0,-1080)
        contains:
            "source/blink_down.webp"
            xalign 0 yalign 0
            ease 1.5 pos (0,1080)

    image blink:
        contains:
            "source/blink_up.webp"
            pos (0,-1080)
            ease 1.5 xalign 0 yalign 0
        contains:
            "source/blink_down.webp"
            pos (0,1080)
            ease 1.5 xalign 0 yalign 0

    image normalno_ebanulo:
        'source/babah1.webp' with dissolve
        pause(0.1)
        'source/babah2.webp' with dissolve
        pause(0.1)
        'source/babah3.webp' with dissolve
        pause(0.1)
        'source/babah4.webp' with dissolve
        pause(0.1)
        'source/babah5.webp' with dissolve
        pause(0.1)
        'source/babah6.webp' with dissolve
        pause(0.1)
        
    image bg aw_club_f:
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            pause 0.15
            repeat
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            alpha 0.25
            pause 0.15
            repeat
        contains:
            choice:
                "aw_club_f1"
            choice:
                "aw_club_f2"
            choice:
                "aw_club_f3"
            alpha 0.25
            pause 0.15
            repeat

    image anim br_smoke:
        contains:
            'source/br_smoke_1.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.5)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'source/br_smoke_2.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.6)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'source/br_smoke_3.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.7)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'source/br_smoke_4.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.8)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0
        contains:
            'source/br_smoke_5.webp'
            xalign 0.5 yalign 0.5 ypos 0.9 alpha 0.0 zoom 1.0
            pause (0.9)
            linear 0.75 ypos 0.8 zoom 0.9 alpha 1.0
            linear 0.75 ypos 0.7 zoom 0.96 alpha 0.0

    image eth_base_pixel:
        "eth_pixel"
        xanchor 0.5 yanchor 0.5 rotate 0

    image eth_move_pixels:
        "eth_base_pixel"
        parallel:
            choice:
                xpos 0 ypos 0.2
            choice:
                xpos 0.1 ypos 0.1
            choice:
                xpos 0.2 ypos 0.0
            choice:
                xpos 0.3 ypos -0.1
            choice:
                xpos 0.4 ypos -0.2
            choice:
                xpos 0.5 ypos -0.1
            choice:
                xpos 0.6 ypos 0
            choice:
                xpos 0.7 ypos 0.1
            choice:
                xpos 0.8 ypos 0.2
            choice:
                xpos 0.9 ypos 0.1
            choice:
                xpos 1.0 ypos 0.0
        parallel:
            choice:
                easeout 10 xpos 0.1
            choice:
                easeout 10 xpos 0.2
            choice:
                easeout 10 xpos 0.3
            choice:
                easeout 10 xpos 0.5
            choice:
                easeout 10 xpos 0.7
            choice:
                easeout 10 xpos 0.8
            choice:
                easeout 10 xpos 0.9
        parallel:
            choice:
                linear 7 ypos 1.1
            choice:
                linear 8 ypos 1.1
            choice:
                linear 9 ypos 1.1
            choice:
                linear 10 ypos 1.1
            choice:
                linear 10 ypos 1.1
        repeat
    image eth_pixels:
        contains:
            "eth_move_pixels"
        contains:
            pause 0.25
            "eth_move_pixels"
        contains:
            pause 0.5
            "eth_move_pixels"
        contains:
            pause 0.75
            "eth_move_pixels"
        contains:
            pause 1.0
            "eth_move_pixels"
        contains:
            pause 1.25
            "eth_move_pixels"
        contains:
            pause 1.5
            "eth_move_pixels"
        contains:
            pause 1.75
            "eth_move_pixels"
        contains:
            pause 2.0
            "eth_move_pixels"
        contains:
            pause 2.25
            "eth_move_pixels"
        contains:
            pause 2.5
            "eth_move_pixels"
        contains:
            pause 2.75
            "eth_move_pixels"
        contains:
            pause 3.0
            "eth_move_pixels"
        contains:
            pause 3.25
            "eth_move_pixels"
        contains:
            pause 3.5
            "eth_move_pixels"
        contains:
            pause 3.75
            "eth_move_pixels"
        contains:
            pause 4.0
            "eth_move_pixels"
        contains:
            pause 4.25
            "eth_move_pixels"
        contains:
            pause 4.5
            "eth_move_pixels"
        contains:
            pause 4.75
            "eth_move_pixels"
        contains:
            pause 5.0
            "eth_move_pixels"
        contains:
            pause 5.25
            "eth_move_pixels"
        contains:
            pause 5.5
            "eth_move_pixels"
        contains:
            pause 5.75
            "eth_move_pixels"
        contains:
            pause 6.0
            "eth_move_pixels"
        contains:
            pause 6.25
            "eth_move_pixels"
        contains:
            pause 6.5
            "eth_move_pixels"
        contains:
            pause 6.75
            "eth_move_pixels"
        contains:
            pause 6.0
            "eth_move_pixels"
        contains:
            pause 6.25
            "eth_move_pixels"
        contains:
            pause 6.5
            "eth_move_pixels"
        contains:
            pause 6.75
            "eth_move_pixels"
        contains:
            pause 6.0
            "eth_move_pixels"
        contains:
            pause 7.25
            "eth_move_pixels"
        contains:
            pause 7.5
            "eth_move_pixels"
        contains:
            pause 7.75
            "eth_move_pixels"
        contains:
            pause 7.0
            "eth_move_pixels"
        contains:
            pause 7.25
            "eth_move_pixels"
        contains:
            pause 7.5
            "eth_move_pixels"
        contains:
            pause 7.75
            "eth_move_pixels"
        contains:
            pause 8.0
            "eth_move_pixels"
        contains:
            pause 8.25
            "eth_move_pixels"
        contains:
            pause 8.5
            "eth_move_pixels"
        contains:
            pause 8.75
            "eth_move_pixels"
        contains:
            pause 9.0
            "eth_move_pixels"
        contains:
            pause 9.25
            "eth_move_pixels"
        contains:
            pause 9.5
            "eth_move_pixels"
        contains:
            pause 9.75
            "eth_move_pixels"

    image overlay aw_memory_back_1:
        contains:
            parallel:
                choice:
                    "source/aw_o_1.webp"
                choice:
                    "source/aw_o_2.webp"
                choice:
                    "source/aw_o_3.webp"
                choice:
                    "source/aw_o_4.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat



    image overlay aw_memory_back_2:
        contains:
            parallel:
                choice:
                    "source/a_1.webp"
                choice:
                    "source/a_2.webp"
                choice:
                    "source/a_3.webp"
            xanchor 0.5 yanchor 0.5 xpos 0.5 ypos 0.5
            parallel:
                parallel:
                    choice:
                        xzoom 1.0
                    choice:
                        xzoom -1.0
                parallel:
                    choice:
                        yzoom 1.0
                    choice:
                        yzoom -1.0
            alpha 0.5
            pause 0.02
            repeat

    image doshd:
        contains:
            "source/rain.webp"
            xpos 0.5 ypos -1.0
        contains:
            "source/rain.webp"
            xpos -0.5 ypos -1.0
        contains:
            "source/rain.webp"
            xpos 0.5 ypos 0.0
        contains:
            "source/rain.webp"
            xpos -0.5 ypos 0.0
        contains:
            "source/rain.webp"
            xpos 0.5 ypos 1.0
        contains:
            "source/rain.webp"
            xpos -0.5 ypos 1.0
        contains:
            "source/rain.webp"
            xpos 0.5 ypos 2.0
        contains:
            "source/rain.webp"
            xpos -0.5 ypos 2.0
        block:
            yanchor 1.0
            linear 0.3 yanchor 0.0
            repeat



    image lepestki:
        choice:
            "source/lep_1.webp"
        choice:
            "source/lep_2.webp"
        choice:
            "source/lep_3.webp"
        choice:
            "source/lep_4.webp"
        choice:
            "source/lep_5.webp"
        xanchor 0.5 yanchor 0.5 rotate 0
        parallel:
            choice:
                rotate 0
                linear 5 rotate 360
                repeat
            choice:
                rotate 0
                linear 7 rotate -360
                repeat
            choice:
                rotate 0
                linear 9 rotate 360
                repeat
            choice:
                rotate 0
                linear 11 rotate -360
                repeat
            choice:
                rotate 0
                linear 13 rotate 360
                repeat
            choice:
                rotate 0
                linear 15 rotate -360
                repeat

    image ftf_moving_lepestki:
        "lepestki"
        parallel:
            choice:
                xpos -0.1 ypos 0.2
            choice:
                xpos -0.1 ypos 0.1
            choice:
                xpos -0.1 ypos 0.0
            choice:
                xpos 0.0 ypos -0.1
            choice:
                xpos 0.0 ypos -0.2
            choice:
                xpos 0.1 ypos -0.1
            choice:
                xpos 0.1 ypos -0.2
            choice:
                xpos 0.2 ypos -0.1
            choice:
                xpos 0.2 ypos -0.2
            choice:
                xpos 0.3 ypos -0.1
            choice:
                xpos 0.3 ypos -0.2
        parallel:
            choice:
                easeout 10 xpos 0.5
            choice:
                easeout 10 xpos 0.6
            choice:
                easeout 10 xpos 0.7
            choice:
                easeout 10 xpos 0.8
            choice:
                easeout 10 xpos 0.9
            choice:
                easeout 10 xpos 1.0
            choice:
                easeout 10 xpos 1.1
        parallel:
            choice:
                linear 7 ypos 1.1
            choice:
                linear 8 ypos 1.1
            choice:
                linear 9 ypos 1.1
            choice:
                linear 10 ypos 1.1
            choice:
                linear 10 ypos 1.1
        repeat

    image lepestki_krutyatsa:
        contains:
            "ftf_moving_lepestki"
        contains:
            pause 0.5
            "ftf_moving_lepestki"
        contains:
            pause 1.0
            "ftf_moving_lepestki"
        contains:
            pause 1.5
            "ftf_moving_lepestki"
        contains:
            pause 2.0
            "ftf_moving_lepestki"
        contains:
            pause 2.5
            "ftf_moving_lepestki"
        contains:
            pause 3.0
            "ftf_moving_lepestki"
        contains:
            pause 3.5
            "ftf_moving_lepestki"
        contains:
            pause 4.0
            "ftf_moving_lepestki"
        contains:
            pause 4.5
            "ftf_moving_lepestki"
        contains:
            pause 5.0
            "ftf_moving_lepestki"
        contains:
            pause 5.5
            "ftf_moving_lepestki"
        contains:
            pause 6.0
            "ftf_moving_lepestki"
        contains:
            pause 6.5
            "ftf_moving_lepestki"
        contains:
            pause 7.0
            "ftf_moving_lepestki"
        contains:
            pause 7.5
            "ftf_moving_lepestki"
        contains:
            pause 8.0
            "ftf_moving_lepestki"
        contains:
            pause 8.5
            "ftf_moving_lepestki"
        contains:
            pause 9.0
            "ftf_moving_lepestki"
        contains:
            pause 9.5
            "ftf_moving_lepestki"

    image tripsMVWWW777:
        'source/trip1MVWWW777.webp' with dissolve
        pause (0.5)
        'source/trip2MVWWW777.webp' with dissolve
        pause (0.5)
        'source/trip3MVWWW777.webp' with dissolve
        pause (0.5)
        repeat

    image menu_art_sheped:
        subpixel True
        "source/ebanoemenu/sheped.webp"
        xcenter 750
        ycenter 385
        zoom 0.58
        menu_art_move(0.58, 750, 0.58)

    image menu_art_skit:
        subpixel True
        "source/ebanoemenu/skit1.webp"
        xcenter 600
        ycenter 465
        zoom 0.60
        menu_art_move(0.54, 600, 0.60)

    image menu_art_osemenitel:
        subpixel True
        "source/ebanoemenu/osemenitel3000.webp"
        xcenter 450
        ycenter 465
        zoom 0.60
        menu_art_move(0.54, 600, 0.60)

    image menu_art_vladislave:
        subpixel True
        "source/ebanoemenu/vladick1.webp"
        xcenter 900
        ycenter 525
        zoom 0.58
        menu_art_move(0.58, 750, 0.58)


    image menu_art_kost:
        subpixel True
        "source/ebanoemenu/avelime.webp"
        xcenter 750
        ycenter 585
        zoom 0.58
        menu_art_move(0.58, 750, 0.58)

    image menu_art_semenyak:
        subpixel True
        "source/ebanoemenu/spit.webp"
        xcenter 510
        ycenter 500
        zoom 0.68
        menu_art_move(0.68, 510, 0.68)

    image menu_art_vladick:
        subpixel True
        "source/ebanoemenu/kazahsuka.webp"
        xcenter 1080
        ycenter 640
        zoom 1.00
        menu_art_move(1.00, 1000, 1.00)

    image menu_art_china:
        subpixel True
        "source/ebanoemenu/huesoskostya.webp"
        xcenter 1080
        ycenter 180
        zoom 1.00
        menu_art_move(1.00, 1000, 1.00)

    image menu_art_bergen:
        subpixel True
        "source/ebanoemenu/bergensprite.webp"
        xcenter 975
        ycenter 335
        zoom 0.60
        menu_art_move(0.54, 600, 0.60)
