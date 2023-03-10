#Skitetsky Remaster Options
#by @b3rg3n & @deadlylxrd
#(C) Skeet Dynasty 2023

define config.name = _("Skitetsky REMASTER")
define gui.show_name = False
define config.version = "1.0"

define gui.about = _p("""
Хуле тут говорить?

Это ремастер самой успешной вн от бергенчика.

{a=https://www.t.me/bergenhub}Канал{/a} разработчика в тг.

{a=https://www.t.me/b3rg3n}Написать{/a} разработчику в тг.

Слова выше - кликабельные.

У тебя ещё остались вопросы?
""")

define build.name = "SkitetskyREMASTER"
define config.has_sound = True
define config.has_music = True
define config.has_voice = True
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.after_load_transition = dissolve
define config.end_game_transition = dissolve
define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)
define config.window = "auto"
default preferences.text_cps = 100
default preferences.afm_time = 15
define config.save_directory = "SkitetskyREMASTER-1665656175"
define config.window_icon = "gui/window_icon.png"

init python:

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.jpeg', 'archive')
    build.classify('game/**.ogv', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.wav', 'archive')
    build.classify('game/**.ttf', 'archive')
    build.classify('game/**.otf', 'archive')
    build.classify('game/**.webm', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/tl/**', 'archive')
    build.classify('game/cache/**', 'archive')
    build.classify('game/**.rpyc', 'archive')
    build.classify('game/**.rpy', 'archive')

    build.documentation('*.html')
    build.documentation('*.txt')

define config.variants = ["phone", "tablet", "touch", "ios", None]

define config.gestures = { "n" : "game_menu",
                           "w" : "help",
                           "e" : "toggle_skip",
                           "s" : "hide_windows"}
init -1700 python:
    _game_menu_screen = "save"

init -999:
    $ create_mods_directory()