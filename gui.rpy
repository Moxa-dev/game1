# Настройки графического интерфейса
# Путь в IT - Визуальная новелла

################################################################################
# Цвета
################################################################################
init python:
    gui.accent_color = "#0066cc"
    gui.idle_color = "#888888"
    gui.hover_color = "#0099ff"
    gui.selected_color = "#ffffff"
    
    gui.insensitive_color = "#8888887f"
    gui.interface_text_color = "#ffffff"
    gui.text_color = "#ffffff"
    gui.link_color = "#0066cc"
    gui.hover_link_color = "#0099ff"
    
    gui.title_text_color = "#ffffff"
    gui.error_color = "#ff0000"

################################################################################
# Шрифты и размеры текста
################################################################################
define gui.text_font = "fonts/MainFont-Regular.ttf"
define gui.name_text_font = "fonts/MainFont-Bold.ttf"
define gui.interface_text_font = "fonts/MainFont-Regular.ttf"

define gui.text_size = 22
define gui.name_text_size = 28
define gui.interface_text_size = 22
define gui.label_text_size = 24
define gui.notify_text_size = 16
define gui.title_text_size = 50

################################################################################
# Размеры интерфейса
################################################################################
define gui.dialogue_width = 600
define gui.dialogue_text_xalign = 0.0

define gui.namebox_width = 168
define gui.namebox_height = 39
define gui.name_xalign = 0.0
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

################################################################################
# Кнопки
################################################################################
define gui.button_width = 300
define gui.button_height = 42

define gui.button_borders = Borders(4, 4, 4, 4)
define gui.button_tile = False
define gui.button_text_font = gui.interface_text_font
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

################################################################################
# Полосы прокрутки
################################################################################
define gui.scrollbar_size = 12
define gui.scrollbar_color = "#c8c8c8"
define gui.scroll_speed = 50

define gui.slider_size = 25
define gui.slider_tile = False
define gui.slider_borders = Borders(4, 4, 4, 4)
define gui.slider_thumb = "gui/slider/horizontal_[prefix_]thumb.png"