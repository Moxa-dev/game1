# Основной скрипт игры
# Путь в IT - Визуальная новелла
# Автор: Moxa-dev
# Дата: 2025-03-19

# Импорт необходимых модулей
init python:
    import random
    import datetime

# Определение изображений
image bg classroom = "images/backgrounds/classroom.jpg"
image bg office = "images/backgrounds/office.jpg"
image bg conference_hall = "images/backgrounds/conference_hall.jpg"
image bg laboratory = "images/backgrounds/laboratory.jpg"

# Начало игры
label start:
    # Инициализация начальных значений
    $ player_name = renpy.input("Как вас зовут?", length=32)
    $ current_chapter = 1
    $ карьерный_путь = None
    
    scene bg classroom
    with fade
    
    "Добро пожаловать в мир IT! Здесь начинается ваш путь к успешной карьере."
    
    show prof normal at center
    PROF "Здравствуйте, [player_name]! Я буду вашим наставником в этом путешествии."
    
    menu:
        PROF "С чего хотите начать свой путь?"
        
        "Изучить основы программирования":
            $ карьерный_путь = "software"
            jump начало_программирования
        
        "Погрузиться в анализ данных":
            $ карьерный_путь = "data"
            jump начало_аналитики
        
        "Узнать о кибербезопасности":
            $ карьерный_путь = "security"
            jump начало_безопасности

    return

# Главы игры
label начало_программирования:
    $ технические_навыки += 1
    $ unlock_achievement("first_steps")
    
    PROF "Отличный выбор! Программирование - это основа современных технологий."
    
    call дополнительное_обучение
    
    return

label начало_аналитики:
    $ знания += 1
    $ unlock_achievement("first_steps")
    
    PROF "Аналитика данных - перспективное направление!"
    
    call дополнительное_обучение
    
    return

label начало_безопасности:
    $ технические_навыки += 1
    $ unlock_achievement("first_steps")
    
    PROF "Кибербезопасность становится всё более важной в современном мире."
    
    call дополнительное_обучение
    
    return