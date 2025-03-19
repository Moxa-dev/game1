# Сюжетные ветки
# Last Updated: 2025-03-19 01:03:21
# Author: Moxa-dev

# Карьерные пути
define CAREER_PATHS = {
    "software": {
        "name": "Разработка ПО",
        "description": "Путь разработчика программного обеспечения",
        "required_skills": ["programming", "algorithms", "databases"],
        "possible_positions": [
            "Junior Developer",
            "Middle Developer",
            "Senior Developer",
            "Team Lead",
            "Technical Architect"
        ]
    },
    "data": {
        "name": "Анализ данных",
        "description": "Путь специалиста по данным",
        "required_skills": ["statistics", "python", "machine_learning"],
        "possible_positions": [
            "Data Analyst",
            "Data Scientist",
            "ML Engineer",
            "Data Architect"
        ]
    },
    "security": {
        "name": "Кибербезопасность",
        "description": "Путь специалиста по безопасности",
        "required_skills": ["networking", "cryptography", "security_tools"],
        "possible_positions": [
            "Security Analyst",
            "Penetration Tester",
            "Security Engineer",
            "CISO"
        ]
    }
}

# Сюжетные метки для разных путей
label software_development_path:
    scene bg office
    with fade
    
    show mentor at left
    MENTOR "Вы выбрали путь разработчика. Давайте начнем с основ."
    
    menu:
        "Выберите специализацию:"
        
        "Frontend-разработка":
            $ specialization = "frontend"
            jump frontend_path
        
        "Backend-разработка":
            $ specialization = "backend"
            jump backend_path
        
        "Full-stack разработка":
            $ specialization = "fullstack"
            jump fullstack_path
    
    return

label data_science_path:
    scene bg laboratory
    with fade
    
    show mentor at left
    MENTOR "Аналитика данных требует сильной математической подготовки."
    
    menu:
        "С чего начнем?"
        
        "Статистика и анализ":
            $ specialization = "analysis"
            jump data_analysis_path
        
        "Машинное обучение":
            $ specialization = "ml"
            jump machine_learning_path
        
        "Большие данные":
            $ specialization = "bigdata"
            jump big_data_path
    
    return

label security_path:
    scene bg office
    with fade
    
    show mentor at left
    MENTOR "Безопасность - это ответственность и постоянное обучение."
    
    menu:
        "Выберите направление:"
        
        "Защита информации":
            $ specialization = "infosec"
            jump information_security_path
        
        "Тестирование на проникновение":
            $ specialization = "pentest"
            jump penetration_testing_path
        
        "Безопасность приложений":
            $ specialization = "appsec"
            jump application_security_path
    
    return