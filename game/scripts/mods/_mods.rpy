# Skitetsky Remaster Mods Engine
# by @deadlylxrd
# (C) Skeet Dynasty 2023

python early:
    mods = {}

init -999 python:
    
    import os

    def create_mods_directory():

        android_package = "ru.bergen.skeetremaster"


        if renpy.variant("mobile"):
            path = "/storage/emulated/0/Android/data/"+android_package+"/files/game/"

            if not os.path.exists(path):
                os.makedirs(path)

            else:
                pass

        else:
            pass
        


init python:
   style.settings_link_edit = Style(style.settings_link)
   style.settings_link_edit.size = 30



screen mods():

    modal True tag menu



    $ bar_null = Frame(get_image("ebanoemenu/bar_null.webp"),36,36)
    $ bar_full = Frame(get_image("ebanoemenu/bar_full.webp"),36,36)

    window background get_image("zatemnenie.webp") xmaximum 1280 ymaximum 720:

        hbox xalign 0.5 yalign 0.08:
            add get_image("ebanoemenu/star.webp") yalign 0.65
            text " "+translation_new["Mods"]+" " style "settings_link" yalign 0.5 color "#ffffff"
            add get_image("ebanoemenu/star.webp") yalign 0.65
        textbutton translation_new["Back"]:
            style "log_button"
            text_style "settings_link"
            xalign 0.015 yalign 0.92 
            action [Hide("mods"), ShowMenu("preferences")]



        if mods:

            side "c b r":
                area (0.27, 0.24, 0.47, 0.70)
                viewport id "mods":
                    draggable True
                    mousewheel True
                    scrollbars None
                    yinitial 0.0


                    has grid 1 len(mods)

                    for lbl, name in sorted(mods.items()):
                        textbutton name:
                            style "log_button" 
                            text_style "settings_link_edit" 
                            xpos 170 ypos 30
                            action Start(lbl)




                bar value XScrollValue("mods") left_bar "source/none.webp" right_bar "source/none.webp" thumb "source/none.webp" hover_thumb "source/none.webp"
                vbar value YScrollValue("mods") bottom_bar "source/none.webp" top_bar "source/none.webp" thumb "source/ebanoemenu/vthumb.webp" thumb_offset -12