# Система достижений
# Last Updated: 2025-03-19 01:03:21
# Author: Moxa-dev

init python:
    class Achievement:
        def __init__(self, id, name, description, requirement, icon, secret=False):
            self.id = id
            self.name = name
            self.description = description
            self.requirement = requirement
            self.icon = icon
            self.secret = secret
            self.unlocked = False
            self.unlock_date = None
        
        def unlock(self):
            if not self.unlocked:
                self.unlocked = True
                self.unlock_date = datetime.datetime.now()
                renpy.notify(f"Достижение разблокировано: {self.name}")
                # Сохраняем в статистику
                persistent.unlocked_achievements[self.id] = True

# Список всех достижений
default persistent.unlocked_achievements = {}

# Технические достижения
define TECH_ACHIEVEMENTS = {
    "first_code": Achievement(
        "first_code",
        "Первая строка кода",
        "Напишите свою первую программу",
        "Завершить первый урок программирования",
        "images/gui/achievements/first_code.png"
    ),
    "bug_hunter": Achievement(
        "bug_hunter",
        "Охотник за багами",
        "Найдите и исправьте 5 багов",
        "Исправить 5 ошибок в коде",
        "images/gui/achievements/bug_hunter.png"
    ),
    "code_master": Achievement(
        "code_master",
        "Мастер кода",
        "Достигните высокого уровня в программировании",
        "Набрать 50 очков технических навыков",
        "images/gui/achievements/code_master.png",
        secret=True
    )
}

# Карьерные достижения
define CAREER_ACHIEVEMENTS = {
    "first_job": Achievement(
        "first_job",
        "Первая работа",
        "Получите свою первую работу в IT",
        "Пройти собеседование и получить оффер",
        "images/gui/achievements/first_job.png"
    ),
    "team_lead": Achievement(
        "team_lead",
        "Командный лидер",
        "Станьте лидером команды",
        "Возглавить проектную команду",
        "images/gui/achievements/team_lead.png",
        secret=True
    )
}

# Социальные достижения
define SOCIAL_ACHIEVEMENTS = {
    "networker": Achievement(
        "networker",
        "Нетворкер",
        "Установите 10 профессиональных контактов",
        "Познакомиться с 10 IT-специалистами",
        "images/gui/achievements/networker.png"
    ),
    "mentor": Achievement(
        "mentor",
        "Ментор",
        "Станьте наставником для других",
        "Помочь трём начинающим разработчикам",
        "images/gui/achievements/mentor.png",
        secret=True
    )
}

# Образовательные достижения
define EDUCATION_ACHIEVEMENTS = {
    "quick_learner": Achievement(
        "quick_learner",
        "Быстрый ученик",
        "Освойте новую технологию за короткий срок",
        "Изучить технологию менее чем за неделю",
        "images/gui/achievements/quick_learner.png"
    ),
    "polyglot": Achievement(
        "polyglot",
        "Полиглот",
        "Изучите 5 языков программирования",
        "Освоить 5 разных языков программирования",
        "images/gui/achievements/polyglot.png"
    )
}

# Функции для работы с достижениями
init python:
    def check_achievements():
        """Проверяет условия получения достижений"""
        # Технические достижения
        if технические_навыки >= 50:
            TECH_ACHIEVEMENTS["code_master"].unlock()
        
        # Карьерные достижения
        if current_position == "team_lead":
            CAREER_ACHIEVEMENTS["team_lead"].unlock()
        
        # Социальные достижения
        if len(professional_contacts) >= 10:
            SOCIAL_ACHIEVEMENTS["networker"].unlock()
        
        # Образовательные достижения
        if len(known_languages) >= 5:
            EDUCATION_ACHIEVEMENTS["polyglot"].unlock()

    def get_achievement_progress(achievement_id):
        """Возвращает прогресс достижения в процентах"""
        # Здесь логика подсчёта прогресса для каждого достижения
        pass