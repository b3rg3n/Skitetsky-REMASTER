# Skitetsky Remaster Easy Character Registration
# by @b3rg3n
# (C) Skeet Dynasty 2023

init python:

    def reg_char(id, name, who_color, what_color = "#fff", pref = "", suf = ""):
        global Character
        gl = globals()
        
        gl[id] = Character( name, color=who_color, what_color=what_color, drop_shadow = [ (2, 2) ], drop_shadow_color = "#000", what_drop_shadow = [ (2, 2) ], what_drop_shadow_color = "#000", what_prefix=pref, what_suffix=suf )

    reg_char("th", '', "#18FFEB", pref="~", suf="~")
    reg_char("th1", ' ', "#dd9933", "#42AAFF", pref="~", suf="~")
    reg_char("th2", ' ', "#dd9933", "#FF5252", pref="~", suf="~")
    reg_char("th3", ' ', "#dd9933", "#FF8000", pref="~", suf="~")
    reg_char("th4", ' ', "#dd9933", "#008080", pref="~", suf="~")
    reg_char("skt", 'Дима Скит', "#008080")
    reg_char("dobby", 'Доберман', "#77dd77")
    reg_char("cld", 'ColdFSociety', "#00008b")
    reg_char("lxrd", 'deadlylxrd', "#ffffff")
    reg_char("lxrd1", 'Клон Вади', "#ffff00")
    reg_char("mrz", 'В. Морозко', "#ffffff")
    reg_char("lxrd2", 'К. Морозко', "#ffff00")
    reg_char("brg", 'BERGEN', "#ff0000")
    reg_char("nn", 'iNeoony', "#ff9baa")
    reg_char("barmn", 'Бармен', "#ff0000")
    reg_char("vsn", 'Вишневский', "#c8ffc8")
    reg_char("dmn", 'Диман', "#d2691e")
    reg_char("shg", 'Шепiд', "#ff4500")
    reg_char("strlk", 'Стрелок', "#77dd77")
    reg_char("razrab", 'Разраб', "#800000")
    reg_char("lis", '???', "#c8ffc8")
    reg_char("avlm", 'Авелайм', "#808000")
    reg_char("melles", 'Melles1991', "#ffff00")
    reg_char("vchn", 'Вечный', "#ff0000")
    reg_char("rmzn", 'Рамазанчик', "#ffff00")
    reg_char("galenin", 'Илюша', "#ffd700")
    reg_char("bergen1", 'Семпай', "#ffff00")
    reg_char("shv", 'Швiлли', "#c8ffc8")
    reg_char("vas", 'Василиса', "#FF8000")
    reg_char("par1", 'Парниша', "#bb8282")
    reg_char("par2", 'Парниша', "#c2b466")
    reg_char("par3", 'Парниша', "#a48f5d")
    reg_char("rcn", 'Ракун', "#ffff00")
    reg_char("oguzok", 'Огузок', "#c2b466")
    reg_char("zih1", '???', "#c2b466")
    reg_char("zih", 'Зихао', "#c2b466")
    reg_char("him", 'Химори', "#FFC0CB")
    reg_char("foma", 'Фома', "#c2b466")
    reg_char("mt", 'Мент', "#bb8282")
    reg_char("mt1", 'Мент', "#c2b466")
    reg_char("ivt1", 'Иветта', "#ff0000", "#ff0000")
    reg_char("golosone", 'Голоса', "#008000", "#008000")
    reg_char("golostwo", 'Голоса', "#77dd77", "#77dd77")
    reg_char("golosthree", 'Голоса', "#00fa9a", "#00fa9a")


init:

    define nvlivt = Character (u'Иветта:', kind=nvl, color = "#ff0000", what_color="FFFFFF",)
    define nvlvas = Character (u'Василиса:', kind=nvl, color = "#FF8000", what_color="FFFFFF",)
    define nvllxrd = Character (u'Вадим:', kind=nvl, color = "#ffffff", what_color="FFFFFF",)
    define nvlbazar = Character (u' ', kind=nvl, color = "#dd9933", what_color="FFFFFF",)
    define nvlskt = Character (u'Скит:', kind=nvl, color = "#008080", what_color="FFFFFF",)
    define nvltn = Character (u'Тунец:', kind=nvl, color = "#c8ffc8", what_color="FFFFFF",)
    define nvlstr = Character (u'Стрелок:', kind=nvl, color = "#ff0000", what_color="FFFFFF",)
    define nvlshv = Character (u'Саня:', kind=nvl, color = "#c8ffc8", what_color="FFFFFF",)
    define nvlvhcn = Character (u'Вечный:', kind=nvl, color = "#ff0000", what_color="FFFFFF",)
    define nvlcld = Character (u'Колд:', kind=nvl, color = "#00008b", what_color="FFFFFF",)