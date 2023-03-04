init -1000 python:

    import os.path

    def get_image(file):
        return "source/%s" % file

init -1199 python:
    from os import path
    mod_prefix = False
    if mod_prefix:
        mod_prefix = '_' + mod_prefix
    else:
        mod_prefix = ''
    modID = 'source/'

    for file in renpy.list_files():
        if modID in file:
            file_name = path.splitext(path.basename(file))[0] + mod_prefix
            if file.endswith((".wav", ".mp2", ".mp3", ".ogg", ".opus")):
                globals()[file_name] = file


init -1001 python:
    
    renpy.music.register_channel("sound", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)
    renpy.music.register_channel("sound_loop", "voice", True)
    renpy.music.register_channel("sound_loop2", "voice", True)
    renpy.music.register_channel("sound_loop3", "voice", True)
    renpy.music.register_channel("ambience", "voice", True)
    
    def volume(vol, chnl):
        renpy.music.set_volume(vol, channel=chnl)
    
    def stop_music():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience", "music"):
            renpy.music.stop(channel=chnl)

    def stop_sound():
        for chnl in ("sound", "sound2", "sound3", "sound_loop", "sound_loop2", "sound_loop3", "ambience"):
            renpy.sound.stop(channel=chnl)


init:

###LABELS BLYA
    default persistent.bazarbig = False
    default persistent.zastavka_skip = False

    $ poroshok_zauzal = False
    $ pomacal_stvoli = False
    $ popil_malisha = False
    $ vsem_pizda = False

    $ menushka_akt0 = False
    $ menushka_akt1 = False
    $ menushka_akt2 = False
    $ menushka_akt3 = False
    $ menushka_akt4 = False
    $ menushka_akt5 = False
    $ menushka_akt6 = False
    $ menushka_akt7 = False
    $ menushka_akt8 = False
    $ menushka_akt9 = False
    $ menushka_akt10 = False
    $ menushka_dlc1 = False
    $ menushka_dlc2 = False
    $ menushka_dlc3 = False
###VIDEOSOS
    image menushka = Movie(fps=24, size = (1280, 720), play="source/menushka.webm")
    image burnint = Movie(play="source/burnint.ogv")
    image roofburn = Movie(play="source/roofburn.ogv")
    image squareanim = Movie(play="source/Everlasting Evening - (Wallpaper Engine).ogv")
    image bunkerson = Movie(play="source/bunker.ogv")
    image menushka1 = Movie(fps=24, size = (1280, 720), play="source/menushka1.ogv")
###

###NAMES
    define skt = Character(u'Дима Скит', color="#008080")
    define dobby = Character(u'Доберман', color="#77dd77")
    define th = Character (u' ', color = "#dd9933")
    define cld = Character(u'ColdFSociety', color="#00008b")
    define lxrd = Character(u'deadlylxrd', color="#ffffff")
    define lxrd1 = Character(u'Клон Вади', color="#ffff00")
    define mrz = Character(u'В. Морозко', color="#ffffff")
    define lxrd2 = Character(u'К. Морозко', color="#ffff00")
    define brg = Character(u'BERGEN', color="#ff0000")
    define nn = Character(u'iNeoony', color="#ff9baa")
    define golosone = Character(u'Голоса', color="#008000", what_color="008000",)
    define golostwo = Character(u'Голоса', color="#77dd77", what_color="77dd77",)
    define golosthree = Character(u'Голоса', color="#00fa9a", what_color="00fa9a",)
    define barmn = Character(u'Бармен', color="#ff0000")
    define vsn = Character(u'Вишневский', color="#c8ffc8")
    define th1 = Character (u' ', color = "#dd9933", what_color="#42AAFF")
    define th2 = Character (u' ', color = "#dd9933", what_color="#FF5252")
    define th3 = Character (u' ', color = "#dd9933", what_outlines=[ (1, "#FF8000") ])
    define th4 = Character (u' ', color = "#dd9933", what_outlines=[ (1, "#008080") ])
    define dmn = Character(u'Диман', color="#d2691e")
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
    define shg = Character(u'Шепiд', color="#ff4500")
    define strlk = Character(u'Стрелок', color="#77dd77")
    define razrab = Character(u'Разраб', color="#800000")
    define huiznaet = Character(u'???', color="#c8ffc8")
    define lis = Character(u'???', color="#c8ffc8")
    define avlm = Character(u'Авелайм', color="#808000")
    define melles = Character(u'Melles1991', color="#ffff00")
    define vchn = Character(u'Вечный', color="#ff0000")
    define rmzn = Character(u'Рамазанчик', color="#ffff00")
    define galenin = Character(u'Илюша', color="#ffd700")
    define ineony = Character('iNeoony', color="#c8ffc8")
    define bergen1 = Character('Семпай', color="#ffff00")
    define shv = Character('Швiлли', color="#c8ffc8")
    define vas = Character('Василиса', color="#FF8000")
    define rcn = Character(u'Ракун', color="#ffff00")
    define aw_mj1 = Character(u'Мужчина', color="#bb8282")
    define aw_mj2 = Character(u'Мужчина', color="#c2b466")
    define aw_mj3 = Character(u'Мужчина', color="#a48f5d")
    define par1 = Character(u'Парниша', color="#bb8282")
    define par2 = Character(u'Парниша', color="#c2b466")
    define par3 = Character(u'Парниша', color="#a48f5d")
    define ivt = Character('Василиса', color="#FF8000")
    define ivt1 = Character('Иветта', color="#ff0000", what_color="ff0000",)
    define oguzok = Character(u'Огузок', color="#c2b466")
    define zih1 = Character(u'???', color="#c2b466")
    define zih = Character(u'Зихао', color="#c2b466")
    define him = Character(u'Химори', color="#FFC0CB")
    define foma = Character(u'Фома', color="#c2b466")
    define mt = Character(u'Мент', color="#bb8282")
    define mt1 = Character(u'Мент', color="#c2b466")
###

###DISSOLVES
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
    $ flash2 = Fade(2, 2, 2, color="#fff")
    $ flash_red = Fade(1, 0, 1, color="#e11")
    $ flash_red2 = Fade(2, 2, 2, color="#e11")
    $ flash_fast = Fade(0.25, 0, 0.75, color="#fff")
    $ flash_fast2 = Fade(0.05, 0, 0.35, color="#fff")
    $ flash_fast_red = Fade(0.25, 0, 0.75, color="#ff0000")
    $ flash_fast_red2 = Fade(0.05, 0, 0.75, color="#ff0000")
    $ fade3 = Fade(1.5, 0, 1.5)
    $ fade2 = Fade(1, 0, 1)
    $ hell_dissolve = Dissolve(50)
    $ dissolve3 = Dissolve(3)
    $ dissolve4 = Dissolve(4)
    $ dissolve_fast = Dissolve(0.5)
    $ dissolve_long = Dissolve(100)
    $ dspr = Dissolve(.2)
    $ dissolve4 = Dissolve(4)
    $ awrain = ImageDissolve("source/awrain.webp", 1.5, 60, reverse=False)
    $ awrain2 = ImageDissolve("source/awrain.webp", 4.5, 80, reverse=False)
    $ awrain3 = ImageDissolve("source/awrain.webp", 0.5, 30, reverse=False)
    $ awwhole = ImageDissolve("source/awwhole.webp", 4.5, 60, reverse=False)
    $ awbhole = ImageDissolve("source/awbhole.webp", 3.5, 60, reverse=True)
    $ awmad = ImageDissolve("source/awmad.webp", 3.0, 75, reverse=False)
    $ awspot = ImageDissolve("source/aw_eff_spot.webp", 3.5, 60, reverse=True)
    $ awspot2 = ImageDissolve("source/aw_eff_spot.webp", 3.5, 60, reverse=False)
    $ awnoose = ImageDissolve("source/aw_noose.webp", 3.5, 60, reverse=True)
###

###IMAGES
    image sl_zombie_sprite_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite2_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite3_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite4_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite5_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite6_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite7_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite8_LW0607 = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sl_zombie_sprite9_LW0607  = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image hitmarkermlg_LW0607 = "source/hitmarkermlg_LW0607.webp"
    image sl_blkg_LW0607 = "source/sl_blkg_LW0607.webp"
    image dark_LW0607 = "source/dark_LW0607.webp"
    image blood_LW0607 = "source/blood_LW0607.webp"
    image comedysheped = "source/comedysheped.webp"
    image sheped = im.MatrixColor("source/sheped.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image strelok = im.MatrixColor("source/strelok.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image skeetgrustinka = "source/skeetgrustinka.webp"
    image nmall = Image("source/nmall.webp")
    image nmallblur = Image("source/nmall1.webp")
    image traphata = Image("source/traphata.webp")
    image domext = Image("source/2.webp")
    image domint = Image("source/dom1.webp")
    image domintnight = Image("source/dom11.webp")
    image pc = Image("source/pc.webp")
    image propusk = Image("source/propusk.webp")
    image nmallint = Image("source/nmallint.webp")
    image krisa = Image("source/doberman.webp")
    image grena = Image("source/grena.webp")
    image babah = Image("source/babah.webp")
    image novomall = Image("source/mall.webp")
    image deadlylxrd = im.MatrixColor("source/lordspr.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image bergen = im.MatrixColor("source/bergensprite.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image ineony = im.MatrixColor("source/kazahsuka.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image kohnyashvilli = Image("source/kuhshv.webp")
    image kuhnyanight = Image("source/kuhnyanight.webp")
    image kuhnya = Image("source/kuhnya.webp")
    image zaborskit = Image("source/zaborskit.webp")
    image zaborskit1 = Image("source/zaborskit1.webp")
    image zaborskit2 = Image("source/zaborskit2.webp")
    image zaborskit3 = Image("source/zaborskit4.webp")
    image skittolkan = Image("source/skittolkan.webp")
    image skittolkan1 = Image("source/skittolkan1.webp")
    image skittolkan2 = Image("source/skittolkan2.webp")
    image skitupalvtolkan = Image("source/skitupalvtolkan.webp")
    image vannaya = Image("source/vannaya.webp")
    image dristun = Image("source/dristun.webp")
    image morozovcover = Image("source/morozovcover.webp")
    image menushitfade = Image("source/menushitfade.webp")
    image menushitfade0 = Image("source/menushitfade0.png")
    image menushitfade1 = Image("source/menushitfade1.png")
    image menushitfade2 = Image("source/menushitfade2.png")
    image menushitfade3 = Image("source/menushitfade3.png")
    image menushitfade4 = Image("source/menushitfade4.png")
    image menushitfade5 = Image("source/menushitfade5.png")
    image menushitfade6 = Image("source/menushitfade6.png")
    image menushitfade7 = Image("source/menushitfade7.png")
    image menushitfade8 = Image("source/menushitfade8.png")
    image menushitfade9 = Image("source/menushitfade9.png")
    image menushitfade10 = Image("source/menushitfade10.png")
    image menushitfadedlc1 = Image("source/menushitfadedcl1.png")
    image menushitfadedlc2 = Image("source/menushitfadedlc2.png")
    image menushitfadedlc3 = Image("source/menushitfadedlc3.png")
    image overlaymenushki = Image("source/overlaymenushki.webp")
    image novoshahtinsk = Image("source/1.webp")
    image hataneonydisk = Image("source/hataneonydisk.webp")
    image m1 = Image("source/m1.webp")
    image m2 = Image("source/m2.webp")
    image m3 = Image("source/m3.webp")
    image m4 = Image("source/m4.webp")
    image m5 = Image("source/m5.webp")
    image lordspr1 = im.MatrixColor("source/lordspr1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image lordspr2 = im.MatrixColor("source/lordspr2.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image lordspr3 = im.MatrixColor("source/lordspr3.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image bomba = Image("source/bomba.webp")
    image dobermann = im.MatrixColor("source/dobermann.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image bergensvd = im.MatrixColor("source/bergensvd.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image dobermann1 = im.MatrixColor("source/dobermann1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image dobermann2 = im.MatrixColor("source/dobermann2.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image dobermann3 = im.MatrixColor("source/dobermann3.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image zvukdisk = Image("source/zvukdisk.webp")
    image barman = im.MatrixColor("source/barman.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image bar = Image("source/bar.webp")
    image bergennorm = im.MatrixColor("source/bergennorm.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image basketbol = Image("source/basketbol.webp")
    image avtobusgorit = Image("source/ed_bus_burn.webp")
    image vorotampizda = Image("source/ed_gate_ruined.webp")
    image anim blink_down = "source/blink_down.webp"
    image anim blink_up = "source/blink_up.webp"
    image int_bus = Image("source/int_bus.webp")
    image ext_bus = Image("source/ext_bus.webp")
    image bg ext_bus = Image("source/ext_bus.webp")
    image bg int_catacombs_living1 = Image("source/int_catacombs.webp")
    image bg int_catacombs = Image("source/int_catacombs.webp")
    image bg int_catacombs_hole = Image("source/int_catacombs_hole.webp")
    image bg int_mine = Image("source/int_mine.webp")
    image bg int_mine_room = Image("source/int_mine_room.webp")
    image bg int_mine_coalface = Image("source/int_mine_coalface.webp")
    image bg int_mine_crossroad = Image("source/int_mine_crossroad.webp")
    image bg int_mine_door = Image("source/int_mine_door.webp")
    image bg int_mine_exit_night_light = Image("source/int_mine_exit_night_light.webp")
    image bg int_mine_exit_night_light_ramazan = Image("source/int_mine_exit_night_light_ramazan.webp")
    image bg int_mine_halt = Image("source/int_mine_halt.webp")
    image bg int_musclub_day = Image("source/int_musclub_day.webp")
    image bg int_old_building_night = Image("source/int_old_building_night.webp")
    image bg ext_old_building_sunset = Image("source/ext_old_building_sunset_red_7dl_AMS_XX072020.webp")
    image bg int_clubs_male2_dildo = Image("source/int_clubs_male2_dildo.webp")
    image bg int_clubs_male_day_baza = Image("source/int_clubs_male_day_baza.webp")
    image bg ext_path2_day_posral = Image("source/ext_path2_day_posral.webp")
    image bg ext_path_day = Image("source/ext_path_day.webp")
    image bg ext_path2_day = Image("source/ext_path2_day.webp")
    image bg ext_camp_entrance_day = Image("source/ext_camp_entrance_day.webp")
    image bg ext_road_day = Image("source/ext_road_day.webp")
    image bg ext_clubs_day = Image("source/ext_clubs_day.webp")
    image bg ext_square_night = Image("source/ext_square_night.webp")
    image bg ext_clubs_night = Image("source/ext_clubs_night.webp")
    image bg ext_no_bus_night = Image("source/ext_no_bus_night.webp")
    image bg ext_bus_night = Image("source/ext_bus_night.webp")
    image bg ext_path_night = Image("source/ext_path_night.webp")
    image bg goscar = Image("source/Gosling_and_car_AMS_XX072020.webp")
    image sheped_grust = im.MatrixColor("source/sheped_pechalka.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image pistolpm = im.MatrixColor("source/pmbich.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image pistolpm1 = im.MatrixColor("source/pmbich1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image pistolpm11 = im.MatrixColor("source/pmbich11.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image blazer = im.MatrixColor("source/blazer.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image pahom = im.MatrixColor("source/pahom.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image pahom1 = im.MatrixColor("source/pahom1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image pahom2 = im.MatrixColor("source/pahom2.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image pahom3 = im.MatrixColor("source/pahom3.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image bg ext_old_building_night_moonlight = Image("source/ext_old_building_night_moonlight.webp")
    image avelimespr = im.MatrixColor("source/avelime.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image bg ext_playground_day = Image("source/ext_playground_day.webp")
    image bg ext_playground_night = Image("source/ext_playground_night.webp")
    image bg ext_path_sunset = Image("source/ext_path_sunset.webp")
    image smska = im.MatrixColor("source/smska.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image skitscary = Image("source/ed_sem_face_burn.webp")
    image et_rage1 = "source/et_rage1.webp"
    image et_rage2 = "source/et_rage2.webp"
    image et_rage3 = "source/et_rage3.webp"
    image et_rage4 = "source/et_rage4.webp"
    image zatemnenie = Image("source/zatemnenie.webp")
    image eth_pixel = "source/pixel.webp"
    image blood = "source/blood.webp"
    image versiya = "gui/overlay/versiya.webp"
    image int_bus_black = Image("source/int_bus_black.webp")
    image int_bus_night = Image("source/int_bus_night.webp")
    image skitpio = im.MatrixColor("source/skit1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image skitpio1 = ConditionSwitch(
    "persistent.sprite_time=='sunset'",im.MatrixColor( im.Composite((450,720), (0,0), "source/skit1111.webp"), im.matrix.tint(0.94, 0.82, 1.0) ), 
    "persistent.sprite_time=='night'",im.MatrixColor( im.Composite((450,720), (0,0), "source/skit1111.webp"), im.matrix.tint(0.63, 0.78, 0.82) ), 
    True,im.Composite((450,720), (0,0), "source/skit1111.webp") )
    image sovenok = Image("source/et_camp_enter_dark.webp")
    image sovenokblur = Image("source/et_camp_enter_dark1.webp")
    image sketmon = Image("source/sketmon.webp")
    image ext_bus_night = Image("source/ext_bus_night.webp")
    image slzombar = im.MatrixColor("source/sl_zombie_sprite_LW0607.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image slzombar1 = im.MatrixColor("source/sl_zombie_sprite.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image us_dead = im.MatrixColor("source/us_dead.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image nebo = Image("source/nebo.webp")
    image nebo1 = Image("source/nebo1.webp")
    image nebo2 = Image("source/nebo2.webp")
    image coldspr = im.MatrixColor("source/pip.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image coldspr1 = im.MatrixColor("source/pip1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image coldsprnight = im.MatrixColor("source/pip11.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image ext_road_night = Image("source/ext_road_night.webp")
    image act1komnata = "source/act1komnata.webp"
    image act1ciga1 = "source/akt1ciga1.webp"
    image akt1ciga2 = "source/akt1ciga2.webp"
    image akt1ciga3 = "source/akt1ciga3.webp"
    image akt1ciga4 = "source/akt1ciga4.webp"
    image akt1ciga5 = "source/akt1ciga5.webp"
    image act1ciga6 = "source/akt1ciga6.webp"
    image act1ciga7 = "source/akt1ciga7.webp"
    image avtoreblansuka = "source/bergensprite.webp"
    image avtoreblansuka1 = "source/bergensprite1.webp"
    image vishel1 = "source/vishel1.webp"
    image vishel2 = "source/vishel2.webp"
    image vishel3 = "source/vishel3.webp"
    image vishel4 = "source/vishel4.webp"
    image vishel5 = "source/vishel5.webp"
    image vishel6 = "source/vishel6.webp"
    image vishel7 = "source/vishel7.webp"
    image vishel8 = "source/vishel8.webp"
    image vishel9 = "source/vishel9.webp"
    image liazik99 = "source/liazik99.webp"
    image melles_spr = "source/melles_spr.webp"
    image dimanspr = "source/diman.webp"
    image dlxrd = "source/lordspr.webp"
    image rmznspr = "source/ramazanshluha.webp"
    image rmznspr1 = "source/ramazanshluha1.webp"
    image ramazan = "source/ramazanchik.webp"
    image porrigeshv = "source/porrige.webp"
    image shstvol1 = im.MatrixColor("source/Crysis_191.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image shstvol11 = im.MatrixColor("source/Crysis_1911.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image SVD_wovystr_LW0607 = "source/SVD_wovystr_LW0607.webp"
    image SVD_svystrel_LW0607 = "source/SVD_svystrel_LW0607.webp"
    image volga = im.MatrixColor("source/volga.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image buhaem = "source/buhaem.webp"
    image coldbuhaet = "source/coldbuhaet.webp"
    image dlya_ebalaMVWWW777 = "source/dlya_ebalaMVWWW777.webp"
    image dlya_ebalaleftMVWWW777 = "source/dlya_ebalaleftMVWWW777.webp"
    image hernya_kakaya_toMVWWW777 = "source/hernya_kakaya_toMVWWW777.webp"
    image trip1MVWWW777 = "source/trip1MVWWW777.webp"
    image trip2MVWWW777 = "source/trip2MVWWW777.webp"
    image trip3MVWWW777 = "source/trip3MVWWW777.webp"
    image skit1 = Image("source/skit11.webp")
    image skit2 = Image("source/skit2.webp")
    image skit3 = Image("source/skit3.webp")
    image nvnight = Image("source/nvnight.webp")
    image ineony = Image("source/ineony.webp")
    image ineony1 = Image("source/ineony1.webp")
    image bergenbook = Image("source/bergenbook.webp")
    image anim_transition_1 = Image("source/anim_transition_1.webp")
    image anim_transition_2 = Image("source/anim_transition_2.webp")
    image anim_transition_3 = Image("source/anim_transition_3.webp")
    image laba = Image("source/laba.webp")
    image lordsprclon1 = im.MatrixColor("source/lordsprclon1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image lordsprclon2 = im.MatrixColor("source/lordsprclon2.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image lordsprclon3 = im.MatrixColor("source/lordsprclon3.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image lordsprclon4 = im.MatrixColor("source/lordsprclon4.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image skitserun = Image("source/skitserun.webp")
    image skitserun1 = Image("source/skitserun1.webp")
    image vladik-serun2 = Image("source/vladik-serun2.webp")
    image tusa = Image("source/tusa.webp")
    image bergdomint1 = Image("source/bergdomint1.webp")
    image vlados2 = im.MatrixColor("source/vlados2.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image vasilisa = im.MatrixColor("source/vasilisa.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image vasilisanight = im.MatrixColor("source/vasilisanight.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image bar1 = Image("source/bar1.webp")
    image komnata_seksa = Image("source/komnata_seksa.webp")
    image tusaposle = Image("source/tusaposle.webp")
    image labaext = Image("source/labaext.webp")
    image train = Image("source/train.webp")
    image train1 = Image("source/train1.webp")
    image train2 = Image("source/train2.webp")
    image train3 = Image("source/train3.webp")
    image tolkanmall = Image("source/tolkanmall.webp")
    image novomallblya = Image("source/novomallblya.webp")
    image kulak_LW0607 = "source/kulak_LW0607.webp"
    image kulak2_LW0607 = "source/kulak2_LW0607.webp"
    image dlya_ebala_LW0607 = "source/dlya_ebala_LW0607.webp"
    image dlya_ebalaleft_LW0607 = "source/dlya_ebalaleft_LW0607.webp"
    image bg aw_private_ms_1 = "source/aw_private_ms_1.webp"
    image bg aw_private_ms_2 = "source/aw_private_ms_2.webp"
    image bg aw_private_ms_3 = "source/aw_private_ms_3.webp"
    image bg aw_private_ms_4 = "source/aw_private_ms_4.webp"
    image bg aw_private_ms_end = "source/aw_private_ms_end.webp"
    image bg aw_private_r_1 = "source/aw_private_r_1.webp"
    image bg aw_private_r_2 = "source/aw_private_r_2.webp"
    image aw_club_f3 = "source/aw_club_f3.webp"
    image aw_club_f2 = "source/aw_club_f2.webp"
    image aw_club_f1 = "source/aw_club_f1.webp"
    image aw_axe_zam = "source/aw_axe_zam.webp"
    image marat1 = im.MatrixColor("source/marat1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sergo1 = im.MatrixColor("source/sergo1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sanya1 = im.MatrixColor("source/sanya1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image marat11 = im.MatrixColor("source/marat11.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sergo11 = im.MatrixColor("source/sergo11.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sanya11 = im.MatrixColor("source/sanya11.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image marat12 = im.MatrixColor("source/marat12.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sergo12 = im.MatrixColor("source/sergo12.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sanya12 = im.MatrixColor("source/sanya12.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image marat13 = im.MatrixColor("source/marat13.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sergo13 = im.MatrixColor("source/sergo13.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image sanya13 = im.MatrixColor("source/sanya13.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image scena_leto = "source/scena_leto.webp"
    image scena_leto1 = "source/scena_leto1.webp"
    image pizdavsem2 = im.MatrixColor("source/pizdavsem2.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image pizdavsem = im.MatrixColor("source/pizdavsem1.webp", im.matrix.tint(0.94, 0.82, 1.0))
    image corridor = "source/corridor.webp"
    image zihao = "source/zihao.webp"
    image diskbg = "source/diskbg.webp"
    image sktwarn1 = "source/sktwarn1.webp"
    image sktwarn2 = "source/sktwarn2.webp"
    image diary = "source/diary.webp"
    image nightdvor = "source/nightdvor.webp"
    image tank = ("source/tank.webp")
    image padik = ("source/padik.webp")
    image morozko = ("source/morozko.webp")
    image ddoser = ("source/ddoser.png")
    image kreslo = ("source/kreslo.png")
    image kk = ("source/kamera_kazaha.webp")
    image kazahspr = im.MatrixColor("source/kazah.png", im.matrix.tint(0.94, 0.82, 1.0))
    image harchok = im.MatrixColor("source/harchok.png", im.matrix.tint(0.94, 0.82, 1.0))
    image vent = ("source/mnd_vent_1.png")
    image portal = ("source/portal.png")
    image zagruzka = ("source/zagruzka.png")
    image nport = ("source/nport.webp")
    image ment = im.MatrixColor("source/ment.png", im.matrix.tint(0.94, 0.82, 1.0))
    image ment1 = im.MatrixColor("source/ment1.png", im.matrix.tint(0.94, 0.82, 1.0))
    image bar100 = ("source/bar100.jpg")
    image aw_afd_dth1_1 = "source/aw_afd_dth1_1.png"
    image aw_afd_dth1_2 = "source/aw_afd_dth1_2.png"
    image aw_afd_dth1_3 = "source/aw_afd_dth1_3.png"
    image aw_afd_ky1_1 = "source/aw_afd_ky1_1.png"
    image aw_afd_ky1_2 = "source/aw_afd_ky1_2.png"
    image aw_afd_ky1_3 = "source/aw_afd_ky1_3.png"
    image himori = ("source/himori.png")
    image bg aw_f_cor_1 = "source/aw_f_cor_1.png"
    image ubratpotomblya = "source/ebanoemenu/menushka_hover.png"
    image bergenokno = "source/bergenokno.webp"
    image bergenokno1 = "source/bergenokno1.webp"
    image et_road_dark = "source/et_road_dark.webp"
    image bg int_liaz = "source/int_liaz.webp"
    image int_liaz1 = "source/int_liaz1.webp"
    image ivettaspr = im.MatrixColor("source/ivettaspr.png", im.matrix.tint(0.94, 0.82, 1.0))
    image skitpiohit = im.MatrixColor("source/skitpiohit.png", im.matrix.tint(0.94, 0.82, 1.0))
###

###ANIMATIONS
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
