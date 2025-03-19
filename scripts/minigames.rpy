# Система мини-игр
# Last Updated: 2025-03-19 01:03:21
# Author: Moxa-dev

init python:
    class TechnicalChallenge:
        def __init__(self, name, description, difficulty, questions):
            self.name = name
            self.description = description
            self.difficulty = difficulty  # 1-5
            self.questions = questions
            self.score = 0
            self.max_score = len(questions)
        
        def calculate_reward(self):
            """Вычисляет награду за прохождение теста"""
            base_reward = self.difficulty * 10
            accuracy = (self.score / self.max_score)
            return int(base_reward * accuracy)

# Технические тесты
define TECHNICAL_TESTS = {
    "algorithms": TechnicalChallenge(
        "Алгоритмы и структуры данных",
        "Проверьте свои знания алгоритмов",
        3,
        [
            {
                "question": "Какая сложность быстрой сортировки в среднем случае?",
                "options": ["O(n)", "O(n log n)", "O(n^2)", "O(1)"],
                "correct": 1,
                "explanation": "Быстрая сортировка имеет сложность O(n log n) в среднем случае."
            },
            {
                "question": "Что такое хеш-коллизия?",
                "options": [
                    "Ошибка в коде",
                    "Одинаковый хеш для разных данных",
                    "Потеря данных",
                    "Переполнение памяти"
                ],
                "correct": 1,
                "explanation": "Хеш-коллизия происходит, когда разные данные дают одинаковый хеш."
            }
        ]
    ),
    
    "databases": TechnicalChallenge(
        "Базы данных",
        "Тест по работе с базами данных",
        2,
        [
            {
                "question": "Что такое индекс в БД?",
                "options": [
                    "Номер записи",
                    "Структура для ускорения поиска",
                    "Тип данных",
                    "Имя таблицы"
                ],
                "correct": 1,
                "explanation": "Индекс - это структура данных, ускоряющая поиск записей."
            }
        ]
    )
}

# Coding Challenge
init python:
    class CodingChallenge:
        def __init__(self, name, description, initial_code, solution, tests):
            self.name = name
            self.description = description
            self.initial_code = initial_code
            self.solution = solution
            self.tests = tests
        
        def check_solution(self, user_code):
            """Проверяет решение пользователя"""
            try:
                # Здесь логика проверки кода
                pass
            except Exception as e:
                return False, str(e)

# Примеры задач
define CODING_CHALLENGES = {
    "fibonacci": CodingChallenge(
        "Числа Фибоначчи",
        "Напишите функцию для вычисления N-го числа Фибоначчи",
        "def fibonacci(n):\n    # Ваш код здесь\n    pass",
        "def fibonacci(n):\n    if n <= 1: return n\n    return fibonacci(n-1) + fibonacci(n-2)",
        [
            {"input": 0, "expected": 0},
            {"input": 1, "expected": 1},
            {"input": 5, "expected": 5}
        ]
    )
}

# Практические задания
define PRACTICAL_TASKS = {
    "api_design": {
        "name": "Проектирование API",
        "description": "Спроектируйте REST API для блог-платформы",
        "requirements": [
            "Эндпоинты для CRUD операций с постами",
            "Аутентификация пользователей",
            "Обработка комментариев"
        ],
        "difficulty": 3,
        "time_limit": 30  # минут
    }
}