init:
    style gitbut1 is button:
        background "source/ebanoemenu/github1.webp"
        hover_background "source/ebanoemenu/github1_hover.webp"
        selected_background "source/ebanoemenu/github1_hover.webp"
        selected_hover_background "source/ebanoemenu/github1_hover.webp"
        selected_idle_background "source/ebanoemenu/github1_hover.webp"
    style tgbut1 is button:
        background "source/ebanoemenu/tg1.webp"
        hover_background "source/ebanoemenu/tg1_hover.webp"
        selected_background "source/ebanoemenu/tg1_hover.webp"
        selected_hover_background "source/ebanoemenu/tg1_hover.webp"
        selected_idle_background "source/ebanoemenu/tg1_hover.webp"

screen pizda_polnaya:

    modal True tag menu

    imagemap:
        auto "source/ebanoemenu/menushka1_%s.webp"
        hotspot (53,155,189,23) clicked Start() hovered Play("test_one", "source/sfx/ebanko1.ogg")
        hotspot (53,223,155,24) clicked Start() hovered Play("test_two", "source/sfx/pizda1.ogg")
        hotspot (53,294,135,21) clicked Start() hovered Play("test_three", "source/sfx/ahuel1.ogg")
        hotspot (53,363,68,22) clicked Start() hovered Play("test_five", "source/sfx/deti1.ogg")
        hotspot (53,432,119,22) clicked Start() hovered Play("test_four", "source/sfx/gb1.ogg")

    button style "gitbut1" pos (0.93,0.01) action OpenURL("http://github.com/b3rg3n") hovered Play("test_six", "source/sfx/wapdomik1.ogg")
    button style "tgbut1" pos (0.93,0.15) action OpenURL("http://t.me/b3rg3n") hovered Play("test_seven", "source/sfx/tgskt1.ogg")
