# Определение экранов интерфейса
# Путь в IT - Визуальная новелла

################################################################################
# Главное меню
################################################################################
screen main_menu():
    tag menu
    
    add gui.main_menu_background
    
    vbox:
        style_prefix "main_menu"
        xalign 0.5
        yalign 0.5
        spacing 20
        
        text "[config.name!t]":
            style "main_menu_title"
        
        textbutton _("Новая игра") action Start()
        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Достижения") action ShowMenu("achievements")
        textbutton _("Об игре") action ShowMenu("about")
        textbutton _("Выход") action Quit(confirm=True)

################################################################################
# Игровой интерфейс
################################################################################
screen game_menu(title, scroll=None):
    style_prefix "game_menu"
    
    frame:
        style "game_menu_outer_frame"
        
        hbox:
            frame:
                style "game_menu_navigation_frame"
                
                vbox:
                    style_prefix "navigation"
                    spacing gui.navigation_spacing
                    
                    textbutton _("Вернуться") action Return()
                    textbutton _("Настройки") action ShowMenu("preferences")
                    textbutton _("Сохранить") action ShowMenu("save")
                    textbutton _("Загрузить") action ShowMenu("load")
                    textbutton _("Главное меню") action MainMenu()
                    textbutton _("Выход") action Quit(confirm=True)
            
            frame:
                style "game_menu_content_frame"
                
                if scroll == "viewport":
                    viewport:
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        
                        side_yfill True
                        
                        vbox:
                            transclude
                
                else:
                    transclude

################################################################################
# Экран достижений
################################################################################
screen achievements():
    tag menu
    use game_menu(_("Достижения"), scroll="viewport"):
        style_prefix "achievements"
        
        vbox:
            spacing 10
            
            text _("Ваши достижения"):
                style "achievements_label"
            
            grid 2 8:
                spacing 20
                for achievement in achievements_list.values():
                    frame:
                        xsize 400
                        ysize 100
                        
                        vbox:
                            spacing 5
                            text achievement.name style "achievement_name"
                            text achievement.description style "achievement_description"
                            text ("✓" if achievement.unlocked else "✗") style "achievement_status"

################################################################################
# Стили
################################################################################
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

style main_menu_vbox:
    xalign 0.5
    xmaximum 1200
    spacing gui.navigation_spacing

style main_menu_text:
    xalign 0.5
    layout "subtitle"
    text_align 0.5
    color gui.accent_color

style main_menu_title:
    size gui.title_text_size
    color gui.title_text_color

style achievement_name:
    size 24
    color "#ffffff"

style achievement_description:
    size 16
    color "#cccccc"

style achievement_status:
    size 20
    color "#00ff00"