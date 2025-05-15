"""
Инициализация Flask приложения
"""
from flask import Flask
from app.config import Config
import os

def create_app(config_class=Config):
    """
    Фабричный метод для создания приложения Flask
    """
    # Теперь используем внутренние папки app
    app = Flask(__name__)
                
    app.config.from_object(config_class)
    
    # Создаем папку для загрузок, если она не существует
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Регистрация маршрутов из контроллеров
    from app.controllers.main_controller import main_bp
    from app.controllers.form_controller import form_bp
    
    app.register_blueprint(main_bp)
    app.register_blueprint(form_bp)
    
    return app 