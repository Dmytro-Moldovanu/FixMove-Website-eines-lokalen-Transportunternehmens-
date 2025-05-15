"""
Контроллер для обработки основных маршрутов приложения
"""
from flask import Blueprint, render_template

# Создаем Blueprint для основных маршрутов
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    """
    Обработчик для главной страницы
    
    Returns:
        str: Отрендеренный HTML-шаблон главной страницы
    """
    return render_template('index.html') 