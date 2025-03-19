# Конфигурация игры
# Путь в IT - Визуальная новелла

define config.name = _("Путь в IT")
define config.version = "1.0.0"

# Базовые настройки
define gui.show_name = True
define config.window_icon = "gui/window_icon.png"
define config.window_title = _("Путь в IT - Визуальная новелла")

# Настройки окна
define config.window_width = 1280
define config.window_height = 720
define config.default_fullscreen = False

# Настройки сохранения
define config.has_autosave = True
define config.autosave_frequency = 200
define config.autosave_slots = 5
define config.save_directory = "tech_path_novel_ru"

# Настройки аудио
define config.has_sound = True
define config.has_music = True
define config.has_voice = False
define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7

# Настройки переходов
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.main_game_transition = dissolve

# Настройки быстрого меню
define config.quick_menu = True
define quick_menu = True